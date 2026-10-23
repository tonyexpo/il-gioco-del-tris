# Il gioco del tris — demo multi-modello

> ⚠️ **Nota sui binari inclusi.** Sì, in questa repo trovi anche `bin/`, `obj/`
> e altri artefatti già compilati per ogni progetto. Non è la prassi comune su
> GitHub, ma qui è una scelta deliberata: questi progetti sono la base di
> codice mostrata nei video, e devono restare eseguibili e identici a quanto
> visto on-screen anche per chi non ha voglia (o modo) di ricompilare tutto da
> zero. Meglio un repo "sporco" ma garantito funzionante, che uno pulito ma
> non testabile.

> 📁 **Cerchi un modello specifico?** Ogni cartella in `src/` corrisponde a un
> modello diverso: consulta la tabella [Abbinamento cartella → modello](#abbinamento-cartella--modello)
> qui sotto per trovare quella giusta.

Questa repository raccoglie il codice prodotto durante una serie di video per il
mio canale YouTube, in formato orizzontale, in cui uso lo **stesso identico
prompt** per far sviluppare da modelli AI diversi — quasi sempre modelli
**locali**, raramente un servizio SaaS — la stessa piccola applicazione
desktop: il gioco del tris (tic-tac-toe).

Ogni cartella dentro `src/` corrisponde a una registrazione/modello diverso:
è l'output ottenuto in quella specifica live, così com'è uscito dal modello.

## Ambiente di test

- **Modelli locali:** eseguiti sempre tramite **LM Studio**.
- **Orchestrazione agentica/multi-agentica:** sempre **Goose**, con
  un'eccezione nei test con modelli piccoli, dove per semplificare l'accesso
  ai tool si sono provate strade diverse — finora entrambe poco produttive e
  non adottate come norma per il resto della serie:
  - `tictactoe11`, `tictactoe11-b`, `tictactoe12` → **Cline (CLI)**
  - `tictactoe11-c` → **OpenCode CLI**

## Il prompt

Il prompt usato è sempre lo stesso, per garantire un confronto equo tra i
vari modelli:

> Sei uno sviluppatore senior. Sviluppa in WPF un gioco del tris (tic-tac-toe)
> seguendo il pattern MVVM. L'UX è a discrezione ma deve restare semplice. La
> logica del PC è randomica. Il giocatore umano è sempre X, il PC è sempre O.
> È presente un pulsante di reset in basso. Cliccando su uno dei 9 pulsanti
> della griglia la partita parte.

## Perché questa repo è "diversa" dal solito

Lo scopo di questa repository **non è distribuire codice sorgente pulito da
ricompilare**, ma fornire l'accesso esatto a quanto avvenuto sul PC durante
ogni live registrata. Per questo, di proposito:

- **Non è presente alcun `.gitignore`**: cartelle di build come `bin/`,
  `obj/`, `.vs/` sono incluse così come generate durante la registrazione.
- **Eventuali refusi nei nomi di cartelle/file vengono mantenuti**, non
  corretti (es. `toctactoe2` invece di `tictactoe2`), perché riflettono
  esattamente ciò che è stato scritto/generato durante la live.

In altre parole: quello che scarichi è garantito identico a quello mostrato
nel video, senza alcuna "pulizia" successiva che potrebbe introdurre
differenze rispetto a quanto visto on-screen.

## Struttura

```
src/
  tictactoe1/   → output della live/modello 1
  toctactoe2/   → output della live/modello 2
  tictactoe3/   → output della live/modello 3
  tictactoe4/   → output della live/modello 4
  tictactoe5/   → output della live/modello 5
  tictactoe6/   → output della live/modello 6
  tictactoe7/   → output della live/modello 7
  tictactoe8/   → output della live/modello 8
  tictactoe9/   → output della live/modello 9
  tictactoe10/  → output della live/modello 10
  tictactoe-slm1/ → confronto multi-modello SLM, orchestrato da GPT-6-Sol
  tictactoe11/  → output della live/modello 11 (JS vanilla, single-page)
  tictactoe11-b/ → variante/secondo tentativo dello stesso modello (JS vanilla, single-page)
  tictactoe11-c/ → terzo tentativo dello stesso modello, via OpenCode CLI (JS vanilla, single-page)
  tictactoe12/  → output della live/modello 12 (JS vanilla, single-page)
  tictactoe13/  → confronto multi-modello, tris 3D stile Minecraft (JS vanilla + three.js)
  tictactoe14/  → confronto quantizzazioni Qwen-3.8-27B (IQ3 vs Q8_0), JS vanilla
  tictactoe15/  → output della live/modello 15 (tris 3D neon, JS vanilla + three.js)
  tictactoe16/  → output della live/modello 16 (tris 3D neon, JS vanilla + three.js)
  tictactoe17/  → output della live/modello 17 (tris 3D neon, JS vanilla + three.js)
  tictactoe18/  → tentativo fallito/modello 18 (nessun gioco prodotto, vedi nota)
  tictactoe19/  → batch di test con LFM2.5-24B q6_k_xl (vedi nota)
  tictactoe20/  → tentativo fallito/modello 20 (nessun gioco prodotto, vedi nota)
```

## Abbinamento cartella → modello

| Cartella      | Modello                                      |
|---------------|-----------------------------------------------|
| `tictactoe1`  | gemma-4-e2b                                    |
| `toctactoe2`  | gemma-4-e4b                                    |
| `tictactoe3`  | gemma-4-12B-it Q4                              |
| `tictactoe4`  | gpt-5.6-luna                                   |
| `tictactoe5`  | qwen-3.8-27B Q3 (ud-unslothdynamic)            |
| `tictactoe6`  | qwen-3.8-27B Q2 (ud)                           |
| `tictactoe7`  | GPT-6-Astra                                    |
| `tictactoe8`  | Fable-5.1                                      |
| `tictactoe9`  | Bonsai 27B (basato su Qwen 3.6) — orchestrato da GPT-5.6-Sol in Goose |
| `tictactoe10` | Qwen-3.8-27B IQ3 ([ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)) — orchestrato da GPT-5.6-Sol in scenario multi-agentico |
| `tictactoe11` | Spark-X2.5-1.7B — implementazione in JavaScript vanilla, single-page (modello piccolo) |
| `tictactoe11-b` | Spark-X2.5-1.7B — variante/secondo tentativo, JavaScript vanilla, single-page |
| `tictactoe11-c` | Spark-X2.5-1.7B — terzo tentativo, JavaScript vanilla, single-page, via **OpenCode CLI** |
| `tictactoe12` | qwen-3.5-4b — implementazione in JavaScript vanilla, single-page (modello piccolo) |
| `tictactoe15` | DeepSeek V4.1 Flash (max) — tris 3D neon stile Subway Surfers (JS vanilla + three.js) |
| `tictactoe16` | Claude Opus 5.5 (high) — tris 3D neon stile Subway Surfers (JS vanilla + three.js) |
| `tictactoe17` | Mistral Large 4 (appena rilasciato) — tris 3D neon stile Subway Surfers (JS vanilla + three.js) |
| `tictactoe18` | Qwen 3.8 27B IQ1 (Unsloth) — tentativo fallito, nessun gioco prodotto |
| `tictactoe19` | LFM2.5-24B (q6_k_xl) — batch di test multipli (hello world, tris JS vanilla, QA, sito Valsesia), vedi nota |
| `tictactoe20` | Nvidia Nemotron 3.5 Bolt 74B-A9B IQ2_M (Unsloth) — tentativo fallito, nessun gioco prodotto |

## tictactoe-slm1 — confronto multi-modello SLM (orchestrato da GPT-6-Sol)

A differenza delle altre cartelle, `tictactoe-slm1/` non è l'output di un
singolo modello: è un confronto tra più **SLM** (small language model) sullo
stesso set di nove task standardizzati, orchestrato da **GPT-6-Sol** tramite
un prompt multi-agentico incluso nella cartella stessa
(`PROMPT-PROSEGUIMENTO-MODELLI.txt`).

Sotto-struttura:

```
tictactoe-slm1/
  artefatti-comuni/                → asset condivisi tra i test (immagini, audio,
                                      dataset, protocollo QA, piano di test)
  PROMPT-PROSEGUIMENTO-MODELLI.txt → prompt multi-agentico con orchestratore
  REPORT-FINALE-COMPARATIVO.md     → report di confronto tra i modelli
  <nome-modello>/
    01-tris-web/                   → tris in HTML/JS
    02-tris-wpf/                   → tris in WPF (stesso task delle altre cartelle del repo)
    03-tesina-milano/
    04-tesina-obama/
    05-copy-milano/
    06-traduzione-marketing/
    07-multimodale/
    08-documenti/
    09-vendite/
    REPORT-QA.md                  → verifica qualità per il singolo modello
```

Modelli SLM testati in questo batch:

- `gemma-4-e2b`
- `granite-4.2-3b`
- `lfm2.5-2.6b`
- `minicpm5-2b`
- `ministral-3-3b`
- `qwen3.5-4b`

## tictactoe13 — tris 3D stile Minecraft (confronto multi-modello)

Come `tictactoe-slm1/`, anche `tictactoe13/` non è l'output di un singolo
modello: raccoglie il confronto tra più modelli sullo stesso prompt, stavolta
con un twist grafico — tris in JavaScript vanilla (con three.js via CDN
come opzione), ambientato in uno stile 3D ispirato a Minecraft.

Il prompt usato (`prompt_tris.txt`, incluso nella cartella):

> Sviluppa un gioco del tris in javascript vanilla + eventualmente three.js
> (cdn), single page in tris.html, giocatore sempre X, PC sempre O, logica e
> UX a discrezione, stile minecraft 3D, genera un po di mondo attorno che
> sia bello da guardare, effetti sonori sintetizzati.

Sotto-struttura:

```
tictactoe13/
  prompt_tris.txt      → prompt usato per tris.html (vedi sopra)
  <nome-modello>/
    tris.html           → il task richiesto dal prompt
    snake.html           → secondo task (snake), incluso così com'è prodotto
```

Modelli testati in questo batch:

- `glm-53-flash` — GLM-5.3-Flash
- `qwen-38-flash` — Qwen-3.8-Flash
- `sonnet-55` — Claude Sonnet 5.5

## tictactoe14 — confronto quantizzazioni (Qwen-3.8-27B)

Come le altre cartelle multi-modello, `tictactoe14/` confronta non modelli
diversi ma due **quantizzazioni** dello stesso modello, **Qwen-3.8-27B**, sullo
stesso prompt: `IQ3` contro `Q8_0` (molto meno aggressiva, più vicina alla
precisione originale).

Il prompt usato (`prompt.txt`, incluso nella cartella):

> Sviluppa un gioco del tris in javascript, vanilla, single page in
> tris.html, giocatore umano sempre X, PC sempre O, logica e UX a piacere,
> aggiungi dei suoni sintetizzati.

Sotto-struttura:

```
tictactoe14/
  prompt.txt              → prompt usato (vedi sopra)
  qwen-3.8-27b-iq3/
    tris.html              → output alla quantizzazione IQ3
  qwen-3.8-27b-q8_0/
    tris.html              → output alla quantizzazione Q8_0
```

## tictactoe15 / tictactoe16 / tictactoe17 — tris 3D neon stile Subway Surfers

A differenza di `tictactoe13`/`tictactoe14`, qui `tictactoe15`, `tictactoe16`
e `tictactoe17` sono cartelle singole (un modello ciascuna), non container
multi-modello — ma condividono lo stesso prompt, incluso in ciascuna come
`prompt.txt`:

> Ciao, sviluppa un gioco del tris con grafica 3D neon ispirata a Subway
> Surfers, giocatore sempre X, pc sempre O, UX e logica a tua discrezione,
> sviluppalo nel file tris3d.html (single page) usando javascript vanilla ed
> eventualmente three.js (da cdn), aggiungi suoni sintetizzati.

Tutte e tre le cartelle includono anche un `snake3d.html` bonus, come già
visto in `tictactoe13`.

## tictactoe18 — tentativo fallito

A differenza di tutte le altre cartelle, `tictactoe18/` non contiene un gioco:
**Qwen 3.8 27B IQ1 (Unsloth)** è entrato in loop continuo e non ha mai
prodotto un tris funzionante, né con il prompt 3D neon né tornando al
prompt base in JS vanilla usato per i tentativi precedenti. Provato sia con
**Cline (CLI)** che con **OpenCode CLI**, stesso risultato. L'unico file
rimasto, `test.html`, è uno stub diagnostico ("Ciao, mondo!") usato solo per
verificare che il tool di scrittura funzionasse — non è un tentativo di
gioco. Conservato così com'è, per la stessa filosofia "copia fedele" del
resto del repo: anche un fallimento totale fa parte della registrazione.

## tictactoe19 — batch di test con LFM2.5-24B (q6_k_xl)

A differenza delle altre cartelle "singolo modello", `tictactoe19/` non
raccoglie un solo task ma una sessione di test più ampia con lo stesso
modello, **LFM2.5-24B** alla quantizzazione **q6_k_xl**, usata anche per
indagare alcuni problemi di esecuzione dei tool (shell/ambiente) emersi
durante le live:

```
tictactoe19/
  helloworld.html               → file di prova minimo, verifica scrittura file
  tris.html / tris.css / tris.js → tris in JS vanilla, multi-file
  valsesia.html                  → sito one-page "Valsesia/SP299" (vedi prompt dedicato)
  qa-20261023T082749Z.md         → verifica QA su tris.html/css/js
  qa-20261023T090220Z.md         → nuova verifica QA sui file aggiornati di tris
  qa-20261023T091717Z.md         → verifica QA su valsesia.html
```

Il prompt strutturato usato per `valsesia.html` è conservato in
[`prompt/prompt-sito-premium-valsesia-sp299.md`](prompt/prompt-sito-premium-valsesia-sp299.md)
— prima voce di una cartella `prompt/` dedicata ai prompt di test salvati
come file, per riutilizzarli più comodamente nei batch successivi. Gli
altri task della cartella (hello world, tris) sono partiti da richieste
conversazionali brevi, non salvate come file di prompt separato.

## tictactoe20 — tentativo fallito

Come `tictactoe18/`, anche `tictactoe20/` non contiene un gioco funzionante:
**Nvidia Nemotron 3.5 Bolt 74B-A9B IQ2_M (Unsloth)** si è bloccato e non è
mai riuscito a concludere lo sviluppo. `tris.html` è rimasto nello stato in
cui il modello l'ha lasciato: contiene testo di ragionamento e token di
tool-calling (`<tool_call>`, `<function=...>`) iniettati direttamente
nell'output del file, invece del codice del gioco. Conservato così com'è,
stessa filosofia "copia fedele" del resto del repo. `helloworld.html` resta
come stub diagnostico iniziale, non un tentativo di gioco.

## Altre demo

Non tutto qui dentro è tris: in [`demo/`](demo/) finiscono demo estemporanee
per il canale che non giustificano una repo a parte.

| Cartella | Di cosa si tratta |
|---|---|
| [`demo/jev-test/`](demo/jev-test/docs/architettura-demo.md) | Modelli decisionali vs LLM generativo per classificare email (OpenRouter) |

## Licenza

Distribuito con licenza [Apache 2.0](LICENSE).
