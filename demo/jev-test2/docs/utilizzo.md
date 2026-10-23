# Procedura di utilizzo della demo

## Requisiti

- Windows con PowerShell 5.1 (serve solo per scaricare le foto) e Node.js 20 o superiore.
- Una chiave OpenRouter in una variabile d'ambiente.
- Connessione a internet, e credito OpenRouter: la demo completa costa meno di un dollaro secondo i prezzi per token (i costi reali sono nei report).

## 1. Chiave OpenRouter

La demo cerca la chiave, in quest'ordine, in `OPENROUTER_API_KEY`, `OPEN_ROUTER_KEY`, `OPEN_ROUTER`. Per impostarla in modo permanente (vale per i terminali aperti dopo):

```powershell
[Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY', '<la tua chiave>', 'User')
```

Per impostarla solo nel terminale corrente:

```powershell
$env:OPENROUTER_API_KEY = '<la tua chiave>'
```

Controlla di essere nel terminale giusto, senza stampare la chiave:

```powershell
[bool]$env:OPENROUTER_API_KEY
```

Deve rispondere `True`. Se avvii la demo da un programma già aperto prima di impostare la variabile (editor, Claude Code), riavvialo: le variabili si leggono all'avvio.

## 2. Foto

Le 200 foto sono già in `_pics`. Per rigenerarle da zero (scarica circa 700 MB in `_dl`, una cartella temporanea che si può cancellare):

```powershell
npm run pics
```

## 3. Prima esecuzione: una decina di foto

```powershell
npm run demo -- --limit 10
```

Analizza le prime 10 foto dell'ordine alternato (5 bianche e 5 di altre tonalità) con tutti e quattro i modelli. A schermo compare una riga per foto:

```
[  3/10] figshare_IMG_20220818_154808.jpg   pulito 0.97 | crepato 0.91 -> SCARTA (crepato)  0.41s
```

Alla fine di ogni modello viene scritto il suo report, poi il confronto.

## 4. Esecuzione completa

```powershell
npm run demo
```

Le foto già analizzate nella prima esecuzione non vengono richieste di nuovo: sono in `results/<modello>.jsonl`. Le foto che avevano dato errore vengono ritentate.

## Opzioni

| Opzione | Effetto |
| --- | --- |
| `--limit N` | Analizza solo le prime N foto dell'ordine alternato |
| `--models jev,luna-decisions,luna,sol` | Sceglie i modelli (nomi: `jev`, `luna-decisions`, `luna`, `sol`). Il confronto include solo i modelli scelti, quindi per il confronto completo lancia tutti e quattro: i risultati già salvati non vengono richiesti di nuovo |
| `--concurrency N` | Richieste in parallelo per modello (predefinito 4) |
| `--fresh` | Ignora i risultati salvati e riparte da zero |
| `--mock` | Prova senza chiave né rete: risultati inventati, scritti in `results/mock`, non in `docs` |

Esempio, solo Jev e il raffronto LLM: `npm run demo -- --models jev,luna --limit 20`.

## Dove trovi i risultati

| File | Contenuto |
| --- | --- |
| `docs/reports/report-typesafe_jev-1.14.md` | Report di Jev 1.14 |
| `docs/reports/report-openai_gpt-6-luna-decisions.md` | Report di GPT-6 Luna Decisions |
| `docs/reports/report-openai_gpt-6-luna.md` | Report di GPT-6 Luna (LLM) |
| `docs/reports/report-openai_gpt-6.1-sol.md` | Report di GPT-6.1 Sol (LLM). Costa circa 19 volte Luna per foto: la demo completa su 200 foto costa circa $1,45 solo per Sol |
| `docs/reports/report-comparison.md` | Confronto: conteggi, latenza, costi, accordo tra modelli |
| `results/*.jsonl` | Dati grezzi, una riga per foto |

Ogni report di modello contiene riepilogo (accettate, scartate, motivi), esito per tipo di scena, confronto con le crepe note, tempi e costi, regole usate, dataset di origine con gli URL originali, tabella foto per foto e, in fondo, un blocco richiudibile per ogni foto con miniatura, origine, licenza, probabilità di tutte le opzioni, decisione, costo e motivazione.

Il confronto (`report-comparison.md`) mette i modelli affiancati: tabella di metriche, esiti per scena, crepe note riconosciute, accordo tra modelli e foto su cui decidono in modo diverso, più una sezione su GPT-6.1 Sol come secondo parere (accordo con ciascun modello, voto di maggioranza, foto in cui diverge da solo).

Per vedere le miniature quando i report sono su GitHub, cartella `_pics` e `docs` devono stare nello stesso repository: i link sono relativi.

I report si sovrascrivono a ogni esecuzione. Per conservarne uno, copialo prima di rilanciare.

## Provare la demo senza chiave

```powershell
npm run demo:mock -- --limit 10
```

Utile per controllare l'installazione e il formato dei report. I numeri sono simulati e il report lo dichiara in testa.

## Test

```powershell
npm test
```

## Se qualcosa non va

| Sintomo | Causa probabile |
| --- | --- |
| `Chiave OpenRouter non trovata` | La variabile non è visibile in questo terminale: vedi il punto 1 |
| `HTTP 401` | Chiave errata o revocata |
| `HTTP 402` | Credito OpenRouter esaurito |
| `HTTP 400` su Jev, immagine rifiutata | L'immagine è fuori dai limiti (lato tra 256 e 1568 px); rigenera `_pics` con `npm run pics` |
| `HTTP 404` o `400` su un modello | L'ID del modello è cambiato: correggilo in `src/config.mjs` |
| `HTTP 429` | Troppe richieste: riduci con `--concurrency 2`; la demo ritenta da sola 3 volte |
| La demo si ferma dopo 5 errori consecutivi | Guarda il messaggio d'errore stampato; i risultati già ottenuti restano salvati |
