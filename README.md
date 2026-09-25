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

## Licenza

Distribuito con licenza [Apache 2.0](LICENSE).
