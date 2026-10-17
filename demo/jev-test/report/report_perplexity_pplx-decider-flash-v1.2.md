# Report - perplexity/pplx-decider-flash-v1.2

Email valutate: 300  (errori di chiamata: 0)
**Accuratezza globale: 93.3%**
- email facili: 232 -> 95.7%
- email difficili: 68 -> 85.3%

## Precision / recall / F1 per classe

classe                  supp    prec     rec      f1
personale                 43 100.0% 100.0% 100.0%
professionale             32  75.6%  96.9%  84.9%
spam                      27  79.4% 100.0%  88.5%
pubblicita                39 100.0% 100.0% 100.0%
newsletter                37 100.0% 100.0% 100.0%
proposta_commerciale      37  97.4% 100.0%  98.7%
phishing                  41 100.0%  53.7%  69.8%
notifica_automatica       44  95.7% 100.0%  97.8%
macro F1                                      92.5%

## Matrice di confusione (righe = attesa, colonne = predetta)

                        person  profes    spam  pubbli  newsle  propos  phishi  notifi
personale                   43       0       0       0       0       0       0       0
professionale                0      31       0       0       0       1       0       0
spam                         0       0      27       0       0       0       0       0
pubblicita                   0       0       0      39       0       0       0       0
newsletter                   0       0       0       0      37       0       0       0
proposta_commerciale         0       0       0       0       0      37       0       0
phishing                     0      10       7       0       0       0      22       2
notifica_automatica          0       0       0       0       0       0       0      44

## Calibrazione: accuratezza per fascia di confidenza

confidenza         n  accuratezza
0.00-0.50          8        50.0%
0.50-0.70          7        85.7%
0.70-0.90         60        81.7%
0.90-0.97        102        96.1%
0.97-1.00        123       100.0%
Se si accettano solo risposte con confidenza >= 0.8: copertura 93.3%, accuratezza 95.7%
Se si accettano solo risposte con confidenza >= 0.9: copertura 75.0%, accuratezza 98.2%

## Latenza e costo

Latenza per richiesta: mediana 0.28s, p95 0.44s
Costo totale: $0.0014 su 300 richieste ($0.000005/email)
Token in ingresso totali: 135263

## Errori (20)

- phishing -> professionale: 10
- phishing -> spam: 7
- phishing -> notifica_automatica: 2
- professionale -> proposta_commerciale: 1

Esempi (i più sicuri di sé, quindi i più interessanti):

- #209 atteso=phishing predetto=professionale conf=0.94 [difficile] | Re: Fattura 1420
- #113 atteso=phishing predetto=professionale conf=0.93 [difficile] | Re: Fattura 3369
- #118 atteso=phishing predetto=professionale conf=0.93 [difficile] | Cambio coordinate bancarie
- #168 atteso=phishing predetto=spam conf=0.91 | Ho accesso alla tua webcam
- #248 atteso=phishing predetto=spam conf=0.9 | Ho accesso alla tua webcam
- #120 atteso=phishing predetto=professionale conf=0.89 [difficile] | Re: Fattura 3848
- #68 atteso=phishing predetto=spam conf=0.87 | Ho accesso alla tua webcam
- #158 atteso=phishing predetto=professionale conf=0.86 | Fattura 924 scaduta - vedi allegato
- #19 atteso=phishing predetto=professionale conf=0.85 | Fattura 2916 scaduta - vedi allegato
- #274 atteso=phishing predetto=professionale conf=0.84 | Fattura 1968 scaduta - vedi allegato
- #66 atteso=phishing predetto=professionale conf=0.83 | Fattura 7086 scaduta - vedi allegato
- #251 atteso=phishing predetto=professionale conf=0.81 | Fattura 7128 scaduta - vedi allegato
