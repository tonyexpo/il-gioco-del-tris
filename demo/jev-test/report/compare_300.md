# Confronto modelli

Email in comune a tutti i modelli: **300** (per modello: microsoft-decision-1 300, gpt-6-luna-decisions 300, gpt-6-luna r=medium 300, pplx-decider-flash-v1.2 300, jev-1.14 300)
Intervallo di confidenza: Wilson al 95%. Con pochi campioni gli intervalli si sovrappongono quasi sempre: differenze di una o due email non sono significative.

## 1. Riepilogo

| modello                 | corrette | acc.  | IC 95%      | facili | difficili | F1 macro | lat. mediana | lat. p95 | costo/1000 | err. chiamata |
|-------------------------|----------|-------|-------------|--------|-----------|----------|--------------|----------|------------|---------------|
| gpt-6-luna-decisions    | 293/300  | 97.7% | 95.3%-98.9% | 98.3%  | 95.6%     | 97.5%    | 0.37s        | 0.63s    | $0.063     | 0             |
| gpt-6-luna r=medium     | 290/300  | 96.7% | 94.0%-98.2% | 97.4%  | 94.1%     | 96.4%    | 2.39s        | 3.50s    | $0.078     | 0             |
| jev-1.14                | 290/300  | 96.7% | 94.0%-98.2% | 97.4%  | 94.1%     | 96.3%    | 0.32s        | 0.47s    | $0.032     | 0             |
| microsoft-decision-1    | 284/300  | 94.7% | 91.5%-96.7% | 97.0%  | 86.8%     | 94.4%    | 0.41s        | 0.88s    | $0.016     | 0             |
| pplx-decider-flash-v1.2 | 280/300  | 93.3% | 89.9%-95.6% | 95.7%  | 85.3%     | 92.5%    | 0.28s        | 0.44s    | $0.005     | 0             |

## 2. Recall per classe (quante email di quella classe vengono riconosciute)

| classe               | n  | microsoft-decision-1 | gpt-6-luna-decisions | gpt-6-luna r=medium | pplx-decider-flash-v1.2 | jev-1.14 |
|----------------------|----|----------------------|----------------------|---------------------|-------------------------|----------|
| personale            | 43 | 100.0%               | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| professionale        | 32 | 96.9%                | 96.9%                | 93.8%               | 96.9%                   | 87.5%    |
| spam                 | 27 | 100.0%               | 96.3%                | 88.9%               | 100.0%                  | 96.3%    |
| pubblicita           | 39 | 92.3%                | 97.4%                | 97.4%               | 100.0%                  | 97.4%    |
| newsletter           | 37 | 100.0%               | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| proposta_commerciale | 37 | 100.0%               | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| phishing             | 41 | 80.5%                | 92.7%                | 92.7%               | 53.7%                   | 90.2%    |
| notifica_automatica  | 44 | 90.9%                | 97.7%                | 97.7%               | 100.0%                  | 100.0%   |

## 3. Sicurezza sul phishing (41 email di phishing nel campione)

| modello                 | riconosciuti | scambiati per spam | scambiati per posta legittima (grave) | falsi allarmi (non phishing -> phishing) |
|-------------------------|--------------|--------------------|---------------------------------------|------------------------------------------|
| microsoft-decision-1    | 33/41        | 3                  | 5                                     | 0                                        |
| gpt-6-luna-decisions    | 38/41        | 3                  | 0                                     | 2                                        |
| gpt-6-luna r=medium     | 38/41        | 3                  | 0                                     | 5                                        |
| pplx-decider-flash-v1.2 | 22/41        | 7                  | 12                                    | 0                                        |
| jev-1.14                | 37/41        | 3                  | 1                                     | 1                                        |

## 4. Affidabilità della confidenza

| modello                 | conf. media se giusto | conf. media se sbaglia | copertura conf>=0.9 | acc. con conf>=0.9 |
|-------------------------|-----------------------|------------------------|---------------------|--------------------|
| microsoft-decision-1    | 0.97                  | 0.66                   | 88.0%               | 99.2%              |
| gpt-6-luna-decisions    | 0.99                  | 0.78                   | 95.3%               | 99.0%              |
| pplx-decider-flash-v1.2 | 0.93                  | 0.77                   | 75.0%               | 98.2%              |
| jev-1.14                | 0.97                  | 0.76                   | 90.0%               | 97.8%              |

Un buon modello ha confidenza alta quando ha ragione e bassa quando sbaglia: così si può mandare a revisione manuale ciò che è sotto soglia. I modelli LLM via chat non restituiscono confidenza e restano fuori.

## 5. Email controverse

- email su cui i modelli danno risposte diverse: **31** su 300
- email sbagliate da tutti i modelli: **4** (probabili etichette ambigue: da rivedere a mano)

Legenda: `ok` = risposta corretta, altrimenti la categoria sbagliata data dal modello; H = email difficile.

### Sbagliate da tutti

| id  |   | atteso        | oggetto                         | microsoft-decision-1 | gpt-6-luna-decisions | gpt-6-luna r=medium  | pplx-decider-flash-v1.2 | jev-1.14             |
|-----|---|---------------|---------------------------------|----------------------|----------------------|----------------------|-------------------------|----------------------|
| 21  | H | professionale | Informazioni sui vostri servizi | proposta_commerciale | proposta_commerciale | proposta_commerciale | proposta_commerciale    | proposta_commerciale |
| 68  |   | phishing      | Ho accesso alla tua webcam      | spam                 | spam                 | spam                 | spam                    | spam                 |
| 168 |   | phishing      | Ho accesso alla tua webcam      | spam                 | spam                 | spam                 | spam                    | spam                 |
| 248 |   | phishing      | Ho accesso alla tua webcam      | spam                 | spam                 | spam                 | spam                    | spam                 |

### Disaccordo tra modelli

| id  |   | atteso              | oggetto                                     | microsoft-decision-1 | gpt-6-luna-decisions | gpt-6-luna r=medium  | pplx-decider-flash-v1.2 | jev-1.14             |
|-----|---|---------------------|---------------------------------------------|----------------------|----------------------|----------------------|-------------------------|----------------------|
| 7   |   | phishing            | Documento in attesa della tua firma         | ok                   | ok                   | ok                   | notifica_automatica     | ok                   |
| 14  | H | spam                | Re: Re: tua richiesta                       | ok                   | phishing             | phishing             | ok                      | phishing             |
| 19  |   | phishing            | Fattura 2916 scaduta - vedi allegato        | ok                   | ok                   | ok                   | professionale           | ok                   |
| 23  | H | phishing            | Favore urgente                              | professionale        | ok                   | ok                   | professionale           | ok                   |
| 59  |   | spam                | Urgent business proposal                    | ok                   | ok                   | phishing             | ok                      | ok                   |
| 66  |   | phishing            | Fattura 7086 scaduta - vedi allegato        | ok                   | ok                   | ok                   | professionale           | ok                   |
| 80  | H | notifica_automatica | Invito: Sync Orion - mercoledì 10:00        | professionale        | ok                   | ok                   | ok                      | ok                   |
| 95  |   | pubblicita          | Fibra a 10 euro al mese per sempre          | spam                 | ok                   | ok                   | ok                      | ok                   |
| 113 | H | phishing            | Re: Fattura 3369                            | professionale        | ok                   | ok                   | professionale           | ok                   |
| 116 | H | phishing            | Opportunità per il tuo profilo              | ok                   | ok                   | ok                   | spam                    | ok                   |
| 118 | H | phishing            | Cambio coordinate bancarie                  | professionale        | ok                   | ok                   | professionale           | professionale        |
| 120 | H | phishing            | Re: Fattura 3848                            | professionale        | ok                   | ok                   | professionale           | ok                   |
| 127 |   | notifica_automatica | Fattura 3155 disponibile                    | professionale        | ok                   | ok                   | ok                      | ok                   |
| 150 | H | spam                | ciao                                        | ok                   | ok                   | phishing             | ok                      | ok                   |
| 158 |   | phishing            | Fattura 924 scaduta - vedi allegato         | ok                   | ok                   | ok                   | professionale           | ok                   |
| 185 |   | notifica_automatica | Avviso di scadenza rata condominiale        | ok                   | phishing             | phishing             | ok                      | ok                   |
| 190 |   | phishing            | Consegna fallita: conferma il tuo indirizzo | ok                   | ok                   | ok                   | notifica_automatica     | ok                   |
| 202 | H | notifica_automatica | Invito: Sync Atlas - mercoledì 10:00        | professionale        | ok                   | ok                   | ok                      | ok                   |
| 209 | H | phishing            | Re: Fattura 1420                            | professionale        | ok                   | ok                   | professionale           | ok                   |
| 227 |   | pubblicita          | Fibra a 60 euro al mese per sempre          | spam                 | ok                   | ok                   | ok                      | ok                   |
| 237 | H | phishing            | Opportunità per il tuo profilo              | ok                   | ok                   | ok                   | spam                    | ok                   |
| 242 | H | phishing            | Opportunità per il tuo profilo              | ok                   | ok                   | ok                   | spam                    | ok                   |
| 251 |   | phishing            | Fattura 7128 scaduta - vedi allegato        | ok                   | ok                   | ok                   | professionale           | ok                   |
| 256 | H | pubblicita          | I tuoi punti stanno per scadere             | ok                   | spam                 | phishing             | ok                      | spam                 |
| 273 | H | notifica_automatica | Invito: Sync Delta - lunedì 17:00           | professionale        | ok                   | ok                   | ok                      | ok                   |
| 274 |   | phishing            | Fattura 1968 scaduta - vedi allegato        | ok                   | ok                   | ok                   | professionale           | ok                   |
| 285 |   | professionale       | Re: Preventivo progetto Mercurio            | ok                   | ok                   | ok                   | ok                      | proposta_commerciale |
| 286 |   | professionale       | Re: Preventivo progetto Mercurio            | ok                   | ok                   | proposta_commerciale | ok                      | proposta_commerciale |
| 290 | H | phishing            | Opportunità per il tuo profilo              | ok                   | ok                   | ok                   | spam                    | ok                   |
| 292 |   | pubblicita          | Volo per Roma da 40 euro                    | spam                 | ok                   | ok                   | ok                      | ok                   |
| 299 |   | professionale       | Re: Preventivo progetto Delta               | ok                   | ok                   | ok                   | ok                      | proposta_commerciale |


## 6. Classifiche

### Più veloci (latenza mediana per richiesta)

| # | modello                 | lat. mediana | vs il più veloce | lat. p95 | accuratezza |
|---|-------------------------|--------------|------------------|----------|-------------|
| 1 | pplx-decider-flash-v1.2 | 0.28s        | 1.0x             | 0.44s    | 93.3%       |
| 2 | jev-1.14                | 0.32s        | 1.1x             | 0.47s    | 96.7%       |
| 3 | gpt-6-luna-decisions    | 0.37s        | 1.3x             | 0.63s    | 97.7%       |
| 4 | microsoft-decision-1    | 0.41s        | 1.5x             | 0.88s    | 94.7%       |
| 5 | gpt-6-luna r=medium     | 2.39s        | 8.4x             | 3.50s    | 96.7%       |

### Meno costosi (costo per 1000 email)

| # | modello                 | costo / 1000 email | vs il più economico | costo / 1000 risposte corrette | accuratezza |
|---|-------------------------|--------------------|---------------------|--------------------------------|-------------|
| 1 | pplx-decider-flash-v1.2 | $0.005             | 1.0x                | $0.005                         | 93.3%       |
| 2 | microsoft-decision-1    | $0.016             | 3.6x                | $0.017                         | 94.7%       |
| 3 | jev-1.14                | $0.032             | 7.1x                | $0.033                         | 96.7%       |
| 4 | gpt-6-luna-decisions    | $0.063             | 13.9x               | $0.064                         | 97.7%       |
| 5 | gpt-6-luna r=medium     | $0.078             | 17.3x               | $0.081                         | 96.7%       |

Latenza e costo sono quelli misurati da OpenRouter in questa esecuzione e possono variare con rete, carico e tariffe. Il costo dell'LLM include anche i token di output e di reasoning, quelli dei modelli decisionali solo l'input.

### Migliori per risoluzione (email classificate correttamente)

| # | modello                 | corrette | accuratezza | IC 95%      | email difficili | phishing riconosciuti |
|---|-------------------------|----------|-------------|-------------|-----------------|-----------------------|
| 1 | gpt-6-luna-decisions    | 293/300  | 97.7%       | 95.3%-98.9% | 65/68 (95.6%)   | 38/41 (92.7%)         |
| 2 | gpt-6-luna r=medium     | 290/300  | 96.7%       | 94.0%-98.2% | 64/68 (94.1%)   | 38/41 (92.7%)         |
| 2 | jev-1.14                | 290/300  | 96.7%       | 94.0%-98.2% | 64/68 (94.1%)   | 37/41 (90.2%)         |
| 4 | microsoft-decision-1    | 284/300  | 94.7%       | 91.5%-96.7% | 59/68 (86.8%)   | 33/41 (80.5%)         |
| 5 | pplx-decider-flash-v1.2 | 280/300  | 93.3%       | 89.9%-95.6% | 58/68 (85.3%)   | 22/41 (53.7%)         |

A pari accuratezza la posizione è la stessa. Se gli intervalli di confidenza si sovrappongono, la differenza tra due modelli non è statisticamente significativa.
