# egg-inspection-demo

Demo: ispezione di uova (pulizia e integrità) a partire da una foto, con 4
modelli via OpenRouter — due modelli **decisionali** (Jev 1.14, GPT-6 Luna
Decisions, tramite la Decisions API) e due **LLM generativi** di raffronto
(GPT-6 Luna, GPT-6.1 Sol, tramite Chat Completions). Programma Node senza
dipendenze (ESM, Node 20+).

Architettura, formato comune tra i due endpoint e regola di decisione:
[`docs/architettura.md`](docs/architettura.md).

Come lanciarla (chiave OpenRouter, download delle foto, opzioni, dove
trovare i report): [`docs/utilizzo.md`](docs/utilizzo.md).

Report già generati: [`docs/reports/`](docs/reports/).

## Nota sulla cartella `_pics`

Il dataset di foto (`_pics/`, ~200 immagini da Figshare, Wikimedia Commons
e Hugging Face, con `manifest.json`) **non è incluso in questo repository**
— va rigenerato in locale con `npm run pics` (vedi
[`docs/utilizzo.md`](docs/utilizzo.md)). Di conseguenza le miniature nei
report in `docs/reports/` non si vedono su GitHub: i link sono relativi a
`_pics/`, assente qui di proposito.
