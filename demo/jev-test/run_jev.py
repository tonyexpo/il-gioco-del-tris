#!/usr/bin/env python3
"""Classifica le email di emails.jsonl con Jev via OpenRouter (Decisions API) e produce un report.

Una richiesta per email, con due domande nella stessa chiamata:
  - categoria  (choice, 8 classi)  -> usata per l'accuratezza
  - urgente    (noul, sì/no)       -> solo dimostrativa

Uso:
  set OPENROUTER_API_KEY=sk-or-...
  python run_jev.py --limit 20            # prova veloce
  python run_jev.py                       # tutte le email
  python run_jev.py --report-only         # rigenera il report da results.jsonl

Solo libreria standard. I risultati sono incrementali: se interrompi, rilancia e riparte da dove era.
"""
import argparse
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "https://openrouter.ai/api/alpha/decisions"
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "typesafe/jev-1.14"

# Setup predefinito per modello. I modelli non elencati usano la Decisions API.
# Per testare Luna LLM con un altro reasoning cambia "reasoning" qui (none | low | medium | high)
# oppure passa --reasoning da riga di comando, che ha la precedenza.
MODEL_DEFAULTS = {
    "openai/gpt-6-luna": {"api": "chat", "reasoning": "medium"},
}

CRITERIA = {
    "personale": "Messaggio tra amici o familiari, di tono privato e informale, senza finalità lavorative o commerciali.",
    "professionale": "Comunicazione di lavoro tra colleghi, clienti o fornitori già in relazione: riunioni, progetti, fatture, ferie, colloqui.",
    "spam": "Posta indesiderata, truffe grossolane o messaggi di massa senza alcuna legittimità (lotterie, eredità, farmaci, guadagni facili).",
    "pubblicita": "Promozione di prodotti o servizi di un negozio o brand: sconti, saldi, codici promo, carrelli abbandonati.",
    "newsletter": "Pubblicazione periodica a cui l'utente si è iscritto: articoli, notizie, aggiornamenti editoriali o di prodotto.",
    "proposta_commerciale": "Offerta B2B seria e mirata di un'azienda o di un commerciale: collaborazioni, preventivi, partnership, servizi.",
    "phishing": "Tentativo di furto di credenziali, dati o denaro fingendosi banca, ente, azienda o superiore.",
    "notifica_automatica": "Messaggio generato automaticamente da un sistema: conferme d'ordine, ricevute, codici OTP, promemoria, avvisi.",
}
QUESTIONS = {
    "categoria": {
        "type": "choice",
        "instructions": "In quale categoria rientra questa email?",
        "criteria": CRITERIA,
    },
    "urgente": {
        "type": "noul",
        "instructions": "Il destinatario deve agire o rispondere con urgenza a questa email?",
    },
}
LABELS = list(CRITERIA)


def render(e):
    return f"Da: {e['from']}\nOggetto: {e['subject']}\n\n{e['body']}"


def call(api_key, model, email):
    return post_json(URL, {"model": model, "state": render(email), "questions": QUESTIONS}, api_key)


CHAT_SYSTEM = (
    "Sei un classificatore di email. Assegna all'email esattamente una di queste categorie:\n"
    + "\n".join(f"- {k}: {v}" for k, v in CRITERIA.items())
    + "\n\nIndica inoltre se il destinatario deve agire o rispondere con urgenza. Rispondi solo con il JSON richiesto."
)
CHAT_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "classificazione_email",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {"categoria": {"type": "string", "enum": LABELS}, "urgente": {"type": "boolean"}},
            "required": ["categoria", "urgente"],
            "additionalProperties": False,
        },
    },
}


def call_chat(api_key, model, email, reasoning=None):
    body = {"model": model, "temperature": 0, "response_format": CHAT_SCHEMA, "usage": {"include": True},
            "messages": [{"role": "system", "content": CHAT_SYSTEM}, {"role": "user", "content": render(email)}]}
    if reasoning:
        body["reasoning"] = {"effort": reasoning}
    return post_json(CHAT_URL, body, api_key)


def post_json(url, body, api_key, retries=5):
    payload = json.dumps(body).encode()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json",
               "User-Agent": "jev-email-demo/1.0", "X-Title": "Jev email demo"}
    for attempt in range(retries):
        t0 = time.time()
        try:
            req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read()), time.time() - t0
        except urllib.error.HTTPError as ex:
            body = ex.read().decode(errors="replace")[:500]
            if ex.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(2 ** attempt + 0.5)
                continue
            raise RuntimeError(f"HTTP {ex.code}: {body}")
        except (urllib.error.URLError, TimeoutError):
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("retries esauriti")


def parse(resp):
    """Estrae (etichetta, confidenza, probabilità, urgente_p) in modo tollerante sul formato."""
    ans = resp.get("answers", resp)
    c = ans.get("categoria") or {}
    probs = c.get("probabilities") or c.get("probs")
    label = c.get("choice") or c.get("answer") or c.get("label")
    if label is None and isinstance(probs, dict) and probs:
        label = max(probs, key=probs.get)
    u = ans.get("urgente") or {}
    urg = u.get("probability", u.get("probabilityYes", u.get("yes", u.get("p"))))
    return label, c.get("confidence"), probs, urg


def parse_chat(resp):
    """Stesso contratto di parse(), per i modelli LLM: niente probabilità né confidenza."""
    text = resp["choices"][0]["message"].get("content") or ""
    text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    d = json.loads(text)
    label = d.get("categoria")
    if label not in LABELS:
        raise ValueError(f"categoria fuori elenco: {label!r}")
    return label, None, None, 1.0 if d.get("urgente") else 0.0


def cost_of(resp):
    u = resp.get("usage") or {}
    return u.get("cost") if isinstance(u.get("cost"), (int, float)) else None


def out_tokens_of(resp):
    u = resp.get("usage") or {}
    reasoning = (u.get("completion_tokens_details") or {}).get("reasoning_tokens") or 0
    return u.get("completion_tokens") or u.get("outputTokens") or 0, reasoning


def tokens_of(resp):
    u = resp.get("usage") or {}
    return u.get("inputTokens") or u.get("prompt_tokens") or u.get("input_tokens") or 0


def load_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def run(args):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        sys.exit("Imposta OPENROUTER_API_KEY (PowerShell: $env:OPENROUTER_API_KEY='sk-or-...')")
    emails = load_jsonl(args.emails)
    if not emails:
        sys.exit(f"{args.emails} non trovato: lancia prima generate_emails.py")
    emails = emails[args.offset:args.offset + args.limit] if args.limit else emails[args.offset:]
    done = {r["id"] for r in load_jsonl(args.results) if "error" not in r}
    todo = [e for e in emails if e["id"] not in done]
    print(f"{len(emails)} email, {len(done)} già fatte, {len(todo)} da classificare con {args.model}")

    if args.api == "chat":
        caller, parser = (lambda k, m, e: call_chat(k, m, e, args.reasoning)), parse_chat
    else:
        caller, parser = call, parse
    lock, counter = threading.Lock(), {"n": 0, "bad": 0, "raw_saved": False}
    out = open(args.results, "a", encoding="utf-8")

    def work(e):
        try:
            resp, dt = caller(key, args.model, e)
            with lock:
                if not counter["raw_saved"]:
                    with open(f"raw_first_response_{args.model.replace('/', '_')}.json", "w", encoding="utf-8") as f:
                        json.dump(resp, f, indent=2, ensure_ascii=False)
                    counter["raw_saved"] = True
            label, conf, probs, urg = parser(resp)
            rec = {"id": e["id"], "expected": e["label"], "hard": e["hard"], "predicted": label,
                   "confidence": conf, "probabilities": probs, "urgent_p": urg,
                   "latency": round(dt, 3), "cost": cost_of(resp), "input_tokens": tokens_of(resp)}
            rec["output_tokens"], rec["reasoning_tokens"] = out_tokens_of(resp)
            if label is None:
                rec["error"] = "risposta non interpretabile (vedi raw_first_response_<modello>.json)"
                rec["raw"] = resp
        except Exception as ex:
            rec = {"id": e["id"], "expected": e["label"], "hard": e["hard"], "error": str(ex)}
        with lock:
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()
            counter["n"] += 1
            counter["bad"] += "error" in rec
            if counter["n"] % 25 == 0 or counter["n"] == len(todo):
                print(f"  {counter['n']}/{len(todo)} (errori: {counter['bad']})", flush=True)
        return rec

    # la prima richiesta da sola: se il formato/auth è sbagliato ci fermiamo subito
    if todo:
        first = work(todo[0])
        if "error" in first:
            sys.exit(f"Prima richiesta fallita: {first['error']}")
        with ThreadPoolExecutor(args.workers) as pool:
            futs = [pool.submit(work, e) for e in todo[1:]]
            for f in as_completed(futs):
                pass
    out.close()


# --------------------------------------------------------------------------- report
def pct(x):
    return f"{100 * x:5.1f}%"


def report(args):
    emails = {e["id"]: e for e in load_jsonl(args.emails)}
    rows = {}
    for r in load_jsonl(args.results):  # l'ultimo record per id vince
        rows[r["id"]] = r
    ok = [r for r in rows.values() if "error" not in r]
    err = len(rows) - len(ok)
    if not ok:
        sys.exit("Nessun risultato valido in " + args.results)

    L = []
    p = L.append
    n = len(ok)
    acc = sum(r["predicted"] == r["expected"] for r in ok) / n
    p(f"# Report - {args.title}\n")
    p(f"Email valutate: {n}  (errori di chiamata: {err})")
    p(f"**Accuratezza globale: {pct(acc).strip()}**")
    for name, sel in (("facili", False), ("difficili", True)):
        sub = [r for r in ok if r["hard"] == sel]
        if sub:
            p(f"- email {name}: {len(sub)} -> {pct(sum(r['predicted'] == r['expected'] for r in sub) / len(sub)).strip()}")

    p("\n## Precision / recall / F1 per classe\n")
    p(f"{'classe':22s} {'supp':>5s} {'prec':>7s} {'rec':>7s} {'f1':>7s}")
    f1s = []
    for lab in LABELS:
        tp = sum(r["predicted"] == lab and r["expected"] == lab for r in ok)
        pred = sum(r["predicted"] == lab for r in ok)
        sup = sum(r["expected"] == lab for r in ok)
        pr = tp / pred if pred else 0
        rc = tp / sup if sup else 0
        f1 = 2 * pr * rc / (pr + rc) if pr + rc else 0
        f1s.append(f1)
        p(f"{lab:22s} {sup:5d} {pct(pr)} {pct(rc)} {pct(f1)}")
    p(f"{'macro F1':22s} {'':5s} {'':7s} {'':7s} {pct(sum(f1s) / len(f1s))}")

    p("\n## Matrice di confusione (righe = attesa, colonne = predetta)\n")
    short = {l: l[:6] for l in LABELS}
    p(f"{'':22s}" + "".join(f"{short[l]:>8s}" for l in LABELS))
    for a in LABELS:
        cells = Counter(r["predicted"] for r in ok if r["expected"] == a)
        p(f"{a:22s}" + "".join(f"{cells.get(b, 0):8d}" for b in LABELS))

    confs = [(r["confidence"], r["predicted"] == r["expected"]) for r in ok if isinstance(r.get("confidence"), (int, float))]
    if confs:
        p("\n## Calibrazione: accuratezza per fascia di confidenza\n")
        p(f"{'confidenza':14s} {'n':>5s} {'accuratezza':>12s}")
        for lo, hi in ((0, .5), (.5, .7), (.7, .9), (.9, .97), (.97, 1.01)):
            sub = [c for c in confs if lo <= c[0] < hi]
            if sub:
                p(f"{lo:.2f}-{min(hi, 1):.2f}      {len(sub):5d} {pct(sum(c[1] for c in sub) / len(sub)):>12s}")
        for thr in (0.8, 0.9):
            sub = [c for c in confs if c[0] >= thr]
            if sub:
                p(f"Se si accettano solo risposte con confidenza >= {thr}: copertura {pct(len(sub) / len(confs)).strip()}, "
                  f"accuratezza {pct(sum(c[1] for c in sub) / len(sub)).strip()}")

    lat = sorted(r["latency"] for r in ok if r.get("latency"))
    costs = [r["cost"] for r in ok if isinstance(r.get("cost"), (int, float))]
    toks = sum(r.get("input_tokens") or 0 for r in ok)
    p("\n## Latenza e costo\n")
    if lat:
        p(f"Latenza per richiesta: mediana {lat[len(lat) // 2]:.2f}s, p95 {lat[int(len(lat) * .95) - 1]:.2f}s")
    if costs:
        p(f"Costo totale: ${sum(costs):.4f} su {len(costs)} richieste (${sum(costs) / len(costs):.6f}/email)")
    if toks:
        p(f"Token in ingresso totali: {toks}")
    outs, reas = sum(r.get("output_tokens") or 0 for r in ok), sum(r.get("reasoning_tokens") or 0 for r in ok)
    if outs:
        p(f"Token in uscita totali: {outs} (di cui reasoning: {reas})")

    wrong = [r for r in ok if r["predicted"] != r["expected"]]
    p(f"\n## Errori ({len(wrong)})\n")
    pairs = Counter((r["expected"], r["predicted"]) for r in wrong)
    for (a, b), c in pairs.most_common(8):
        p(f"- {a} -> {b}: {c}")
    p("\nEsempi (i più sicuri di sé, quindi i più interessanti):\n")
    wrong.sort(key=lambda r: -(r.get("confidence") or 0))
    for r in wrong[:12]:
        e = emails.get(r["id"], {})
        conf = r.get("confidence")
        p(f"- #{r['id']} atteso={r['expected']} predetto={r['predicted']} conf={conf if conf is None else round(conf, 2)}"
          f"{' [difficile]' if r['hard'] else ''} | {e.get('subject', '')[:70]}")

    text = "\n".join(L)
    print(text)
    os.makedirs(os.path.dirname(args.report) or ".", exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"\n(report salvato in {args.report})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--emails", default="emails.jsonl")
    ap.add_argument("--results", help="default: results_<modello>.jsonl")
    ap.add_argument("--report", help="default: report/report_<modello>.md")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--api", choices=["decisions", "chat"],
                    help="decisions = modelli decisionali; chat = LLM via chat completions con output strutturato "
                         "(default: da MODEL_DEFAULTS, altrimenti decisions)")
    ap.add_argument("--reasoning", choices=["none", "low", "medium", "high"],
                    help="solo con --api chat: livello di reasoning (default: da MODEL_DEFAULTS)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0, help="quante email classificare (0 = tutte quelle rimaste)")
    ap.add_argument("--offset", type=int, default=0,
                    help="salta le prime N email (es. --offset 100 --limit 200 = email 101-300)")
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args()
    cfg = MODEL_DEFAULTS.get(a.model, {})
    a.api = a.api or cfg.get("api", "decisions")
    a.reasoning = (a.reasoning or cfg.get("reasoning")) if a.api == "chat" else None
    slug =a.model.replace("/", "_") + (f"__reasoning-{a.reasoning}" if a.reasoning else "")
    a.title = a.model + (f" (reasoning={a.reasoning})" if a.reasoning else "")
    a.results = a.results or f"results_{slug}.jsonl"
    a.report = a.report or os.path.join("report", f"report_{slug}.md")
    if not a.report_only:
        run(a)
    report(a)
