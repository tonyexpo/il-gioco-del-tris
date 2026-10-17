# Confronto modelli

Email in comune a tutti i modelli: **100** (per modello: microsoft-decision-1 100, gpt-6-luna-decisions 100, gpt-6-luna r=medium 100, pplx-decider-flash-v1.2 100, jev-1.14 100)
Intervallo di confidenza: Wilson al 95%. Con pochi campioni gli intervalli si sovrappongono quasi sempre: differenze di una o due email non sono significative.

## 1. Riepilogo

| modello                 | corrette | acc.  | IC 95%      | facili | difficili | F1 macro | lat. mediana | lat. p95 | costo/1000 | err. chiamata |
|-------------------------|----------|-------|-------------|--------|-----------|----------|--------------|----------|------------|---------------|
| gpt-6-luna-decisions    | 97/100   | 97.0% | 91.5%-99.0% | 98.8%  | 88.2%     | 97.0%    | 0.36s        | 0.75s    | $0.063     | 0             |
| jev-1.14                | 97/100   | 97.0% | 91.5%-99.0% | 98.8%  | 88.2%     | 97.0%    | 0.33s        | 0.55s    | $0.032     | 0             |
| gpt-6-luna r=medium     | 96/100   | 96.0% | 90.2%-98.4% | 97.6%  | 88.2%     | 96.0%    | 2.31s        | 3.27s    | $0.076     | 0             |
| microsoft-decision-1    | 95/100   | 95.0% | 88.8%-97.8% | 97.6%  | 82.4%     | 95.0%    | 0.43s        | 0.94s    | $0.016     | 0             |
| pplx-decider-flash-v1.2 | 94/100   | 94.0% | 87.5%-97.2% | 95.2%  | 88.2%     | 93.9%    | 0.31s        | 0.49s    | $0.005     | 0             |

## 2. Recall per classe (quante email di quella classe vengono riconosciute)

| classe               | n  | microsoft-decision-1 | gpt-6-luna-decisions | gpt-6-luna r=medium | pplx-decider-flash-v1.2 | jev-1.14 |
|----------------------|----|----------------------|----------------------|---------------------|-------------------------|----------|
| personale            | 11 | 100.0%               | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| professionale        | 13 | 92.3%                | 92.3%                | 92.3%               | 92.3%                   | 92.3%    |
| spam                 | 11 | 100.0%               | 90.9%                | 81.8%               | 100.0%                  | 90.9%    |
| pubblicita           | 10 | 90.0%                | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| newsletter           | 12 | 100.0%               | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| proposta_commerciale | 17 | 100.0%               | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |
| phishing             | 13 | 84.6%                | 92.3%                | 92.3%               | 61.5%                   | 92.3%    |
| notifica_automatica  | 13 | 92.3%                | 100.0%               | 100.0%              | 100.0%                  | 100.0%   |

## 3. Sicurezza sul phishing (13 email di phishing nel campione)

| modello                 | riconosciuti | scambiati per spam | scambiati per posta legittima (grave) | falsi allarmi (non phishing -> phishing) |
|-------------------------|--------------|--------------------|---------------------------------------|------------------------------------------|
| microsoft-decision-1    | 11/13        | 1                  | 1                                     | 0                                        |
| gpt-6-luna-decisions    | 12/13        | 1                  | 0                                     | 1                                        |
| gpt-6-luna r=medium     | 12/13        | 1                  | 0                                     | 2                                        |
| pplx-decider-flash-v1.2 | 8/13         | 1                  | 4                                     | 0                                        |
| jev-1.14                | 12/13        | 1                  | 0                                     | 1                                        |

## 4. Affidabilità della confidenza

| modello                 | conf. media se giusto | conf. media se sbaglia | copertura conf>=0.9 | acc. con conf>=0.9 |
|-------------------------|-----------------------|------------------------|---------------------|--------------------|
| microsoft-decision-1    | 0.98                  | 0.69                   | 91.0%               | 98.9%              |
| gpt-6-luna-decisions    | 1.00                  | 0.89                   | 99.0%               | 98.0%              |
| pplx-decider-flash-v1.2 | 0.93                  | 0.76                   | 75.0%               | 100.0%             |
| jev-1.14                | 0.98                  | 0.69                   | 92.0%               | 98.9%              |

Un buon modello ha confidenza alta quando ha ragione e bassa quando sbaglia: così si può mandare a revisione manuale ciò che è sotto soglia. I modelli LLM via chat non restituiscono confidenza e restano fuori.

## 5. Email controverse

- email su cui i modelli danno risposte diverse: **8** su 100
- email sbagliate da tutti i modelli: **2** (probabili etichette ambigue: da rivedere a mano)

Legenda: `ok` = risposta corretta, altrimenti la categoria sbagliata data dal modello; H = email difficile.

### Sbagliate da tutti

| id |   | atteso        | oggetto                         | microsoft-decision-1 | gpt-6-luna-decisions | gpt-6-luna r=medium  | pplx-decider-flash-v1.2 | jev-1.14             |
|----|---|---------------|---------------------------------|----------------------|----------------------|----------------------|-------------------------|----------------------|
| 21 | H | professionale | Informazioni sui vostri servizi | proposta_commerciale | proposta_commerciale | proposta_commerciale | proposta_commerciale    | proposta_commerciale |
| 68 |   | phishing      | Ho accesso alla tua webcam      | spam                 | spam                 | spam                 | spam                    | spam                 |

### Disaccordo tra modelli

| id |   | atteso              | oggetto                              | microsoft-decision-1 | gpt-6-luna-decisions | gpt-6-luna r=medium | pplx-decider-flash-v1.2 | jev-1.14 |
|----|---|---------------------|--------------------------------------|----------------------|----------------------|---------------------|-------------------------|----------|
| 7  |   | phishing            | Documento in attesa della tua firma  | ok                   | ok                   | ok                  | notifica_automatica     | ok       |
| 14 | H | spam                | Re: Re: tua richiesta                | ok                   | phishing             | phishing            | ok                      | phishing |
| 19 |   | phishing            | Fattura 2916 scaduta - vedi allegato | ok                   | ok                   | ok                  | professionale           | ok       |
| 23 | H | phishing            | Favore urgente                       | professionale        | ok                   | ok                  | professionale           | ok       |
| 59 |   | spam                | Urgent business proposal             | ok                   | ok                   | phishing            | ok                      | ok       |
| 66 |   | phishing            | Fattura 7086 scaduta - vedi allegato | ok                   | ok                   | ok                  | professionale           | ok       |
| 80 | H | notifica_automatica | Invito: Sync Orion - mercoledì 10:00 | professionale        | ok                   | ok                  | ok                      | ok       |
| 95 |   | pubblicita          | Fibra a 10 euro al mese per sempre   | spam                 | ok                   | ok                  | ok                      | ok       |

