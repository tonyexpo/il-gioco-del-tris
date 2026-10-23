# Architettura del codice

La demo è un programma Node senza dipendenze (ESM, Node 20 o superiore) che manda ogni foto a quattro modelli tramite OpenRouter, riporta le loro risposte in un **formato comune**, applica una **regola di decisione unica** e scrive i report. Questo documento spiega come sono collegate le parti. Come si lancia la demo è in [utilizzo.md](utilizzo.md).

## Visione d'insieme

```
                       ┌────────────────────────── src/demo.mjs ───────────────────────────┐
 _pics/manifest.json ─►│ ordine foto ─► per ogni modello: coda di foto + N worker           │
 _pics/*.jpg           │                                  │                                  │
                       └──────────────────────────────────┼──────────────────────────────────┘
                                                          ▼
                                              src/api.mjs  inspect(model, foto)
                                     ┌────────────────────┴─────────────────────┐
                              kind = 'decisions'                           kind = 'chat'
                       POST /api/alpha/decisions                POST /api/v1/chat/completions
                       (Jev 1.14, GPT-6 Luna Decisions)         (GPT-6 Luna)
                                     │                                          │
                              parseDecisions()                            parseChat()
                                     └────────────────────┬─────────────────────┘
                                                          ▼
                                       risultato normalizzato  (vedi "Modello intermedio")
                                                          ▼
                                       src/decision.mjs  decide()  ─►  ACCEPT / DISCARD / UNREADABLE
                                                          ▼
                                 results/<modello>.jsonl (append, una riga per foto)
                                                          ▼
                                 src/report.mjs ─► docs/reports/report-<modello>.md + report-comparison.md
```

## Moduli e dipendenze

| Modulo | Responsabilità | Dipende da |
| --- | --- | --- |
| `src/config.mjs` | Unico punto di configurazione: elenco modelli, scale di valutazione con le definizioni, contesto, soglie, nomi delle variabili per la chiave, timeout e retry | nessuno |
| `src/api.mjs` | Tutto il dialogo con OpenRouter: costruzione delle richieste, `POST` con retry, parsing delle due famiglie di risposta, conversione nel formato comune | `config` |
| `src/decision.mjs` | Funzioni pure: `decide()`, `labelProb()`, ordinamento alternato bianche/marroni con PRNG a seed fisso | `config` |
| `src/report.mjs` | Funzioni pure: `summarize()`, `buildModelReport()`, `buildComparison()`; restituiscono stringhe Markdown | `config`, `decision` |
| `src/mock.mjs` | `fetch` finto con le stesse forme di risposta di OpenRouter, per `--mock` e per i test | nessuno |
| `src/demo.mjs` | Orchestrazione: argomenti, chiave, ordine delle foto, worker concorrenti, cache su file, scrittura dei report | tutti gli altri |

`api.mjs`, `decision.mjs` e `report.mjs` non leggono variabili d'ambiente né scrivono file: lo fa solo `demo.mjs`. Per questo si provano senza rete.

## Integrazione con OpenRouter

Base URL `https://openrouter.ai/api`, autenticazione `Authorization: Bearer <chiave>`, corpo JSON. La stessa chiave serve per entrambe le superfici.

### Perché due endpoint

Jev e GPT-6 Luna Decisions sono modelli con **output "decisions"** (modalità `text+image->decisions` nel catalogo): rispondono a domande tipizzate e non generano testo, quindi non funzionano con Chat Completions. Hanno un endpoint dedicato, la **Decisions API** (`POST /api/alpha/decisions`, in alpha). GPT-6 Luna, il raffronto, è un LLM normale e usa **Chat Completions** (`POST /api/v1/chat/completions`). Nell'elenco pubblico dei modelli (`/api/v1/models`) i modelli Decisions non compaiono: si trovano con `?output_modalities=decisions`.

| Modello | ID richiesto | `kind` in `config.mjs` | Endpoint |
| --- | --- | --- | --- |
| Jev 1.14 | `typesafe/jev-1.14` | `decisions` | `/api/alpha/decisions` |
| GPT-6 Luna Decisions | `openai/gpt-6-luna-decisions` | `decisions` | `/api/alpha/decisions` |
| GPT-6 Luna | `openai/gpt-6-luna` | `chat` | `/api/v1/chat/completions` |
| GPT-6.1 Sol | `openai/gpt-6.1-sol` | `chat` | `/api/v1/chat/completions` |

`inspect()` in `api.mjs` sceglie il percorso dal campo `kind`, quindi un nuovo modello è una riga in `MODELS`.

### Decisions API: richiesta

Jev e Luna Decisions ricevono la stessa richiesta (`decisionsBody()`). La foto è una parte `image_url` con data URL base64 dentro l'array `state`; i testi sono stringhe semplici, non oggetti `{type:'text'}`. Il campo `questions` contiene tre domande:

```json
{
  "model": "typesafe/jev-1.14",
  "state": [
    "Foto di controllo qualità di uova di gallina. Se nella foto ci sono più uova, valuta l'uovo in condizioni peggiori. ...",
    { "type": "image_url", "image_url": { "url": "data:image/jpeg;base64,/9j/4AAQ..." } }
  ],
  "questions": {
    "egg_visible": { "type": "noul", "instructions": "...", "criteria": { "true": "...", "false": "..." } },
    "cleanliness": { "type": "choice", "instructions": "...", "criteria": { "clean": "...", "slightly_dirty": "...", "dirty": "..." } },
    "integrity":   { "type": "choice", "instructions": "...", "criteria": { "intact": "...", "cracked": "...", "broken": "..." } }
  }
}
```

Scelta dei tipi di domanda (i primitivi della Decisions API):

- **Choice** per pulizia e integrità: sono scale con più livelli e la risposta contiene una probabilità per ciascuno. Le definizioni dei livelli (`criteria`) vengono da `CLEANLINESS` e `INTEGRITY` in `config.mjs`.
- **Noul** (sì/no) per `egg_visible`: serve a scartare le foto senza uovo prima di fidarsi delle altre due risposte.
- **Score** (posizione su una scala ordinata) non è usato: servono etichette discrete, confrontabili con quelle che il modello LLM restituisce.
- **Box** (solo Jev 1.14, localizzazione nell'immagine) non è usato.

### Decisions API: risposta

```json
{
  "model": "typesafe/jev-1.14-20261014",
  "answers": {
    "egg_visible": { "type": "noul", "noul": 0.99 },
    "cleanliness": { "type": "choice", "choice": "slightly_dirty",
                     "probabilities": { "clean": 0.35, "slightly_dirty": 0.63, "dirty": 0.02 }, "confidence": 0.45 },
    "integrity":   { "type": "choice", "choice": "intact",
                     "probabilities": { "intact": 0.58, "cracked": 0.42, "broken": 0 }, "confidence": 0.37 }
  },
  "usage": { "input_tokens": 2449, "output_tokens": 104, "cost": 0.000102858 }
}
```

`probabilities` è la distribuzione sulle opzioni; `confidence` è un valore a parte, calcolato dal modello, e può essere molto più basso della probabilità dell'opzione scelta (qui 0,63 contro 0,45). Il codice usa i due valori in due posti diversi, vedi "Regola di decisione".

Vincoli di Jev sulle immagini, rispettati da `prepare-pics.ps1`: solo JPEG o PNG, lato tra 256 e 1568 px, massimo circa 2,4 megapixel, nessuna applicazione dell'orientamento EXIF (le foto vengono ruotate prima). Gli URL remoti non vengono scaricati dall'API, per questo le foto viaggiano come data URL.

### Chat Completions (raffronto LLM)

`chatBody()` costruisce un messaggio con il testo (contesto, definizioni di pulizia e integrità) e la stessa foto come `image_url`. La risposta è vincolata da `response_format: json_schema` con `strict: true`:

```json
{ "egg_visible": true, "cleanliness": "slightly_dirty", "integrity": "intact", "reason": "..." }
```

Lo schema impone gli stessi identificatori dei modelli Decisions (`enum` presi da `config.mjs`), quindi il confronto avviene sulle stesse etichette. Il campo `reason` (massimo 20 parole) è l'unica cosa che i modelli Decisions non hanno. Altre scelte:

- `usage: { include: true }` per avere il costo in `usage.cost`;
- `max_completion_tokens: 2000`, per non troncare un eventuale ragionamento interno;
- nessun `temperature`: il catalogo non lo elenca tra i parametri supportati da `openai/gpt-6-luna` né da `openai/gpt-6.1-sol`, quindi due esecuzioni possono differire;
- un LLM non fornisce probabilità, perciò nel formato comune quei campi sono `null`.

### Errori, retry, timeout

`post()` in `api.mjs` è l'unico punto che chiama `fetch`:

- timeout di 120 s per richiesta (`AbortSignal.timeout`);
- fino a 3 tentativi con attesa di 1 s e poi 2 s, solo per `429`, errori `5xx` ed errori di rete o timeout;
- gli altri errori HTTP (400, 401, 402, 404, 413) falliscono subito con un `ApiError` che porta `status` e il messaggio dell'API;
- la risposta di un modello che manca dei campi attesi, o che contiene un'etichetta fuori scala, diventa un `ApiError` con `status` 0.

## Modello intermedio

È il formato comune in cui i due `parse*` convertono le due famiglie di risposta. Tutto ciò che sta a valle (`decide`, `report`, cache) conosce solo questo, non l'API di partenza.

| Campo | Tipo | Da Decisions API | Da Chat Completions |
| --- | --- | --- | --- |
| `served_model` | stringa | `model` | `model` |
| `egg_visible` | 0 a 1 | `answers.egg_visible.noul` | `egg_visible` booleano, convertito in 1 o 0 |
| `cleanliness.label` | `clean`, `slightly_dirty`, `dirty` | `answers.cleanliness.choice` | `cleanliness` |
| `cleanliness.probs` | mappa o `null` | `probabilities` | `null` |
| `cleanliness.confidence` | 0 a 1 o `null` | `confidence` | `null` |
| `integrity.*` | come `cleanliness`, con `intact`, `cracked`, `broken` | `answers.integrity` | `integrity` |
| `reason` | stringa o `null` | `null` | `reason` |
| `usage` | `{input_tokens, output_tokens, cost}` | `usage.input_tokens`, `output_tokens`, `cost` | `usage.prompt_tokens`, `completion_tokens`, `cost` |

`demo.mjs` completa il record con `file`, `model`, `ok`, `latency_ms` e `decision` (il risultato di `decide()`), oppure con `ok: false` ed `error` se la chiamata è fallita. Quel record, una riga JSON per foto, è ciò che viene salvato in `results/<chiave-modello>.jsonl` e da cui si ricostruiscono i report.

## Regola di decisione

`decide(risultato)` in `decision.mjs` è una funzione pura, uguale per tutti i modelli:

1. se `egg_visible` è sotto 0,5 → `UNREADABLE`;
2. motivi di scarto: integrità diversa da `intact`; pulizia `dirty`; pulizia `slightly_dirty` solo se `acceptSlightlyDirty` è `false`;
3. almeno un motivo → `DISCARD`; altrimenti `ACCEPT` con grado `A` (pulito) o `B` (lievemente sporco).

`low_confidence` vale `true` quando il più basso tra i due `confidence` è sotto 0,6; per un LLM, che non ha `confidence`, è sempre `false`. Non cambia l'esito, serve solo a segnalare "da verificare" nel report. Il report mostra invece la **probabilità dell'etichetta scelta** (`labelProb`), non il `confidence`: per questo una riga può mostrare 0,63 ed essere comunque "da verificare".

## Orchestrazione (`demo.mjs`)

- **Ordine delle foto.** `interleaveByTone()` separa le foto con `tone: 'white'` dalle altre, mescola ciascun gruppo con un PRNG (mulberry32) a seed fisso e le alterna. È deterministico: `--limit N` prende sempre le stesse N foto, che sono la testa dell'ordine completo, quindi un run da 200 riusa le prime 10 senza ripeterle.
- **Modelli in sequenza, foto in parallelo.** Per ogni modello c'è una coda e fino a `--concurrency` worker (predefinito 4) che la consumano. I modelli girano uno dopo l'altro, così l'output a schermo resta leggibile durante una demo dal vivo.
- **Cache.** Ogni risultato viene aggiunto subito a `results/<modello>.jsonl`. All'avvio si ricaricano solo i record con `ok: true`: gli errori vengono ritentati, `--fresh` svuota il file.
- **Interruzione.** Il modello si ferma subito su 401, 402 o 403 e dopo 5 errori consecutivi; i risultati già ottenuti restano salvati, il report viene scritto sulle foto completate e il programma esce con codice 1.
- **Chiave.** `findApiKey()` cerca nell'ordine `OPENROUTER_API_KEY`, `OPEN_ROUTER_KEY`, `OPEN_ROUTER` e il valore resta in memoria nella variabile `apiKey`. Viene stampato solo il nome della variabile trovata; la chiave non entra nei record, nei report né nei log.

## Report (`report.mjs`)

`summarize(risultati, manifest)` calcola conteggi, distribuzioni, latenze (media, p50, p95), costi, token, esiti per tipo di scena e confronto con la verità nota. I builder trasformano il riepilogo in Markdown:

- `buildModelReport` produce un file per modello: riepilogo, esito per scena, confronto con la verità nota, tempi e costi, regole usate, dataset di origine, tabella foto per foto e, in coda, il **dettaglio completo** (`detailSection`). Il dettaglio è un blocco `<details>` richiudibile per foto, con miniatura, origine, licenza e autore, scena, verità nota, probabilità di tutte le opzioni e confidenza (modelli Decisions) o motivazione (LLM), decisione, modello servito, latenza, token e costo. Usa HTML semplice che GitHub renderizza.
- `buildComparison` produce il confronto: sintesi, tabella affiancata (distribuzione delle etichette, probabilità media, latenza, token, costo), esiti per tipo di scena, crepe note riconosciute da tutti, da alcuni o da nessuno, accordo tra coppie di modelli e tabella delle foto su cui i modelli decidono in modo diverso. La sintesi contiene solo affermazioni ricavate dai numeri.
- la tracciabilità dei dataset viene dal `manifest.json`; l'origine di ogni foto è nel suo blocco di dettaglio.

I link alle foto nei report sono percorsi relativi calcolati da `demo.mjs` (`picsRel`), quindi funzionano sia da `docs/reports` sia dalla cartella dei report simulati.

## Dati (`scripts/prepare-pics.ps1`)

Lo script PowerShell, indipendente dal programma Node, scarica da Figshare, Wikimedia Commons (elenco in `commons-titles.json`) e Hugging Face (revisione fissata) in `_dl`, ridimensiona a massimo 1568 px applicando l'orientamento EXIF e scrive `_pics/` con `manifest.json`. Per ogni foto il manifest riporta:

| Campo | Uso |
| --- | --- |
| `file`, `size` | nome e dimensioni dopo il ridimensionamento |
| `source`, `original`, `license`, `author` | tracciabilità, ripresa nei report |
| `scene` (`single_egg`, `few_eggs`, `carton`) | raggruppamento "per tipo di scena" |
| `tone` (`white`, `brown`, `mixed`) | alternanza dell'ordine delle foto |
| `ground_truth` (`cracked`, `intact`, `null`) | confronto con la verità nota; valorizzato solo per le foto Figshare, dalle annotazioni a mano |

## Come estendere

- **Aggiungere un modello Decisions:** una riga in `MODELS` con `kind: 'decisions'`. Il report e il confronto lo includono da soli.
- **Aggiungere un LLM:** una riga con `kind: 'chat'`, purché supporti immagini e `response_format` JSON strutturato.
- **Cambiare scale o definizioni:** `CLEANLINESS`, `INTEGRITY` e `CONTEXT` in `config.mjs`. Gli stessi testi finiscono sia nelle richieste Decisions sia nel prompt dell'LLM, quindi i modelli restano confrontabili. Cambiando gli identificatori vanno aggiornati anche `LABELS_IT` in `decision.mjs` e `decide()`.
- **Cambiare la regola di scarto:** `RULES` in `config.mjs` per le soglie, `decide()` per la logica.

## Test

`npm test` esegue 8 test con `node:test` su: regola di decisione, ordinamento alternato e deterministico, parsing delle due risposte, forma delle richieste, ordine di ricerca della chiave, percorso completo `inspect()` → `decide()` con il fetch finto e coerenza delle colonne nella tabella foto per foto del report. Non toccano la rete. Le chiamate vere sono state verificate a parte con un'esecuzione su 10 foto.

## Limiti

- **API in alpha.** La Decisions API e l'input immagine di Jev sono funzioni in fase iniziale: formato e limiti possono cambiare.
- **Verità nota parziale.** Solo le 100 foto Figshare hanno un'etichetta annotata (crepa). Per la pulizia e per le altre foto non c'è una verità di riferimento, quindi i report mostrano cosa decidono i modelli, non quanto hanno ragione.
- **Campione.** Poche foto mostrano uova davvero sporche e non ci sono uova integre con etichetta certa: i falsi allarmi non sono misurati.
- **Un'immagine per richiesta.** Nessun batching: ogni foto è una richiesta, con costo e latenza propri.
- **Modello LLM non deterministico.** Senza `temperature` le risposte possono variare tra esecuzioni.
