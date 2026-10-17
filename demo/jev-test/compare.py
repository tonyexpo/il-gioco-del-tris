#!/usr/bin/env python3
"""Confronta i risultati di più modelli (results_*.jsonl prodotti da run_jev.py) sulle stesse email.

Per un confronto equo usa solo le email classificate con successo da TUTTI i modelli confrontati
(l'intersezione). Produce compare.md con:
  1. tabella riassuntiva (accuratezza + intervallo di confidenza, F1, latenza, costo)
  2. recall per classe
  3. sicurezza sul phishing (phishing scambiati per posta legittima)
  4. affidabilità della confidenza (solo per i modelli che la restituiscono)
  5. email su cui i modelli non concordano e quelle sbagliate da tutti (etichette da rivedere)

Uso:
  python compare.py                       # tutti i results_*.jsonl nella cartella
  python compare.py --runs results_a.jsonl results_b.jsonl
  python compare.py --exclude reasoning-high reasoning-medium
"""
import argparse
import glob
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_jev import LABELS  # noqa: E402

LEGIT = {"personale", "professionale", "newsletter", "proposta_commerciale", "notifica_automatica", "pubblicita"}


def load(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def run_name(path):
    slug = os.path.basename(path)[len("results_"):-len(".jsonl")]
    slug, _, reasoning = slug.partition("__reasoning-")
    model = slug.replace("_", "/", 1)
    return model + (f" (reasoning={reasoning})" if reasoning else "")


def short(name):
    base = name.split("/", 1)[-1]
    return base.replace(" (reasoning=", " r=").rstrip(")")


def wilson(k, n, z=1.96):
    if not n:
        return 0.0, 0.0
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - m) / d, (c + m) / d


def pct(x):
    return f"{100 * x:.1f}%"


def macro_f1(rows):
    f1s = []
    for lab in LABELS:
        sup = sum(r["expected"] == lab for r in rows)
        if not sup:
            continue
        tp = sum(r["predicted"] == lab and r["expected"] == lab for r in rows)
        pred = sum(r["predicted"] == lab for r in rows)
        pr, rc = (tp / pred if pred else 0), tp / sup
        f1s.append(2 * pr * rc / (pr + rc) if pr + rc else 0)
    return sum(f1s) / len(f1s)


def table(headers, rows):
    w = [max(len(str(x)) for x in col) for col in zip(headers, *rows)]
    line = lambda r: "| " + " | ".join(str(x).ljust(n) for x, n in zip(r, w)) + " |"
    return "\n".join([line(headers), "|" + "|".join("-" * (n + 2) for n in w) + "|"] + [line(r) for r in rows])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emails", default="emails.jsonl")
    ap.add_argument("--runs", nargs="*", help="default: results_*.jsonl")
    ap.add_argument("--exclude", nargs="*", default=[], help="scarta i file il cui nome contiene una di queste stringhe")
    ap.add_argument("--out", default=os.path.join("report", "compare.md"))
    ap.add_argument("--max-rows", type=int, default=40, help="righe massime per le liste di email")
    a = ap.parse_args()

    emails = {e["id"]: e for e in load(a.emails)}
    paths = [p for p in (a.runs or sorted(glob.glob("results_*.jsonl"))) if not any(x in p for x in a.exclude)]
    if len(paths) < 2:
        sys.exit("Servono almeno due file results_*.jsonl")

    runs, call_errors = {}, {}
    for p in paths:
        by_id = {}
        for r in load(p):  # l'ultimo record per id vince
            by_id[r["id"]] = r
        name = run_name(p)
        runs[name] = {i: r for i, r in by_id.items() if "error" not in r}
        call_errors[name] = len(by_id) - len(runs[name])

    common = set.intersection(*(set(r) for r in runs.values()))
    if not common:
        sys.exit("Nessuna email in comune tra i modelli")
    ids = sorted(common)
    names = list(runs)
    shorts = [short(n) for n in names]
    if len(set(shorts)) < len(shorts):
        shorts = names
    sh = dict(zip(names, shorts))
    sel = {n: [runs[n][i] for i in ids] for n in names}

    out = []
    p = out.append
    p("# Confronto modelli\n")
    p(f"Email in comune a tutti i modelli: **{len(ids)}** (per modello: "
      + ", ".join(f"{sh[n]} {len(runs[n])}" for n in names) + ")")
    p("Intervallo di confidenza: Wilson al 95%. Con pochi campioni gli intervalli si sovrappongono quasi sempre: "
      "differenze di una o due email non sono significative.\n")

    # 1. riassuntiva
    p("## 1. Riepilogo\n")
    rows = []
    for n in names:
        rs = sel[n]
        k = sum(r["predicted"] == r["expected"] for r in rs)
        lo, hi = wilson(k, len(rs))
        easy = [r for r in rs if not r["hard"]]
        hard = [r for r in rs if r["hard"]]
        lat = sorted(r["latency"] for r in rs if r.get("latency"))
        costs = [r["cost"] for r in rs if isinstance(r.get("cost"), (int, float))]
        rows.append([sh[n], f"{k}/{len(rs)}", pct(k / len(rs)), f"{pct(lo)}-{pct(hi)}",
                     pct(sum(r['predicted'] == r['expected'] for r in easy) / len(easy)) if easy else "-",
                     pct(sum(r['predicted'] == r['expected'] for r in hard) / len(hard)) if hard else "-",
                     pct(macro_f1(rs)),
                     f"{lat[len(lat) // 2]:.2f}s" if lat else "-",
                     f"{lat[max(int(len(lat) * .95) - 1, 0)]:.2f}s" if lat else "-",
                     f"${sum(costs) / len(costs) * 1000:.3f}" if costs else "-",
                     call_errors[n]])
    rows.sort(key=lambda r: -float(r[2].rstrip("%")))
    p(table(["modello", "corrette", "acc.", "IC 95%", "facili", "difficili", "F1 macro", "lat. mediana", "lat. p95",
             "costo/1000", "err. chiamata"], rows))

    # 2. recall per classe
    p("\n## 2. Recall per classe (quante email di quella classe vengono riconosciute)\n")
    rows = []
    for lab in LABELS:
        sup = [i for i in ids if emails[i]["label"] == lab]
        if not sup:
            continue
        row = [lab, len(sup)]
        for n in names:
            row.append(pct(sum(runs[n][i]["predicted"] == lab for i in sup) / len(sup)))
        rows.append(row)
    p(table(["classe", "n"] + [sh[n] for n in names], rows))

    # 3. phishing
    ph = [i for i in ids if emails[i]["label"] == "phishing"]
    p(f"\n## 3. Sicurezza sul phishing ({len(ph)} email di phishing nel campione)\n")
    rows = []
    for n in names:
        legit = [i for i in ph if runs[n][i]["predicted"] in LEGIT]
        as_spam = [i for i in ph if runs[n][i]["predicted"] == "spam"]
        false_alarm = [i for i in ids if emails[i]["label"] != "phishing" and runs[n][i]["predicted"] == "phishing"]
        rows.append([sh[n], f"{len(ph) - len(legit) - len(as_spam)}/{len(ph)}", len(as_spam), len(legit), len(false_alarm)])
    p(table(["modello", "riconosciuti", "scambiati per spam", "scambiati per posta legittima (grave)",
             "falsi allarmi (non phishing -> phishing)"], rows))

    # 4. confidenza
    conf_models = [n for n in names if any(isinstance(r.get("confidence"), (int, float)) for r in sel[n])]
    if conf_models:
        p("\n## 4. Affidabilità della confidenza\n")
        rows = []
        for n in conf_models:
            rs = [r for r in sel[n] if isinstance(r.get("confidence"), (int, float))]
            ok = [r["confidence"] for r in rs if r["predicted"] == r["expected"]]
            bad = [r["confidence"] for r in rs if r["predicted"] != r["expected"]]
            hi = [r for r in rs if r["confidence"] >= 0.9]
            rows.append([sh[n], f"{sum(ok) / len(ok):.2f}" if ok else "-", f"{sum(bad) / len(bad):.2f}" if bad else "(nessun errore)",
                         f"{pct(len(hi) / len(rs))}", pct(sum(r['predicted'] == r['expected'] for r in hi) / len(hi)) if hi else "-"])
        p(table(["modello", "conf. media se giusto", "conf. media se sbaglia", "copertura conf>=0.9", "acc. con conf>=0.9"], rows))
        p("\nUn buon modello ha confidenza alta quando ha ragione e bassa quando sbaglia: così si può mandare a "
          "revisione manuale ciò che è sotto soglia. I modelli LLM via chat non restituiscono confidenza e restano fuori.")

    # 5. disaccordi
    def cell(n, i):
        r = runs[n][i]
        return "ok" if r["predicted"] == r["expected"] else r["predicted"]

    disagree = [i for i in ids if len({runs[n][i]["predicted"] for n in names}) > 1]
    all_wrong = [i for i in ids if all(runs[n][i]["predicted"] != runs[n][i]["expected"] for n in names)]
    p(f"\n## 5. Email controverse\n")
    p(f"- email su cui i modelli danno risposte diverse: **{len(disagree)}** su {len(ids)}")
    p(f"- email sbagliate da tutti i modelli: **{len(all_wrong)}** (probabili etichette ambigue: da rivedere a mano)\n")

    def listing(title, lst):
        if not lst:
            return
        p(f"### {title}\n")
        rows = [[i, "H" if emails[i]["hard"] else "", emails[i]["label"], emails[i]["subject"][:48]]
                + [cell(n, i) for n in names] for i in lst[:a.max_rows]]
        p(table(["id", "", "atteso", "oggetto"] + [sh[n] for n in names], rows))
        if len(lst) > a.max_rows:
            p(f"\n... altre {len(lst) - a.max_rows} (alza --max-rows)")
        p("")

    p("Legenda: `ok` = risposta corretta, altrimenti la categoria sbagliata data dal modello; H = email difficile.\n")
    listing("Sbagliate da tutti", all_wrong)
    listing("Disaccordo tra modelli", [i for i in disagree if i not in all_wrong])

    # 6. classifiche velocità e costo (in coda al report)
    stats = {}
    for n in names:
        rs = sel[n]
        lat = sorted(r["latency"] for r in rs if r.get("latency"))
        costs = [r["cost"] for r in rs if isinstance(r.get("cost"), (int, float))]
        acc = sum(r["predicted"] == r["expected"] for r in rs) / len(rs)
        cost1000 = sum(costs) / len(costs) * 1000 if costs else None
        stats[n] = {"med": lat[len(lat) // 2] if lat else None,
                    "p95": lat[max(int(len(lat) * .95) - 1, 0)] if lat else None,
                    "cost": cost1000, "acc": acc,
                    "per_correct": cost1000 / acc if cost1000 is not None and acc else None}

    p("\n## 6. Classifiche\n")
    p("### Più veloci (latenza mediana per richiesta)\n")
    fast = sorted((n for n in names if stats[n]["med"] is not None), key=lambda n: stats[n]["med"])
    if fast:
        best = stats[fast[0]]["med"]
        p(table(["#", "modello", "lat. mediana", "vs il più veloce", "lat. p95", "accuratezza"],
                [[k, sh[n], f"{stats[n]['med']:.2f}s", f"{stats[n]['med'] / best:.1f}x", f"{stats[n]['p95']:.2f}s",
                  pct(stats[n]["acc"])] for k, n in enumerate(fast, 1)]))
    p("\n### Meno costosi (costo per 1000 email)\n")
    cheap = sorted((n for n in names if stats[n]["cost"] is not None), key=lambda n: stats[n]["cost"])
    if cheap:
        best = stats[cheap[0]]["cost"]
        p(table(["#", "modello", "costo / 1000 email", "vs il più economico", "costo / 1000 risposte corrette", "accuratezza"],
                [[k, sh[n], f"${stats[n]['cost']:.3f}", f"{stats[n]['cost'] / best:.1f}x",
                  f"${stats[n]['per_correct']:.3f}", pct(stats[n]["acc"])] for k, n in enumerate(cheap, 1)]))
    p("\nLatenza e costo sono quelli misurati da OpenRouter in questa esecuzione e possono variare con rete, carico e tariffe. "
      "Il costo dell'LLM include anche i token di output e di reasoning, quelli dei modelli decisionali solo l'input.")

    p("\n### Migliori per risoluzione (email classificate correttamente)\n")
    solved = {}
    for n in names:
        rs = sel[n]
        k = sum(r["predicted"] == r["expected"] for r in rs)
        hard = [r for r in rs if r["hard"]]
        kh = sum(r["predicted"] == r["expected"] for r in hard)
        phish = [r for r in rs if r["expected"] == "phishing"]
        kp = sum(r["predicted"] == "phishing" for r in phish)
        solved[n] = (k, len(rs), kh, len(hard), kp, len(phish))
    order = sorted(names, key=lambda n: (-solved[n][0], -solved[n][2], -solved[n][4]))
    rows = []
    for n in order:
        k, tot, kh, th, kp, tp = solved[n]
        lo, hi = wilson(k, tot)
        rank = 1 + sum(solved[m][0] > k for m in names)  # a pari merito stessa posizione
        rows.append([rank, sh[n], f"{k}/{tot}", pct(k / tot), f"{pct(lo)}-{pct(hi)}",
                     f"{kh}/{th} ({pct(kh / th)})" if th else "-", f"{kp}/{tp} ({pct(kp / tp)})" if tp else "-"])
    p(table(["#", "modello", "corrette", "accuratezza", "IC 95%", "email difficili", "phishing riconosciuti"], rows))
    p("\nA pari accuratezza la posizione è la stessa. Se gli intervalli di confidenza si sovrappongono, la differenza tra due modelli non è statisticamente significativa.")

    text = "\n".join(out)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(text)
    print(f"\n(salvato in {a.out})")


if __name__ == "__main__":
    main()
