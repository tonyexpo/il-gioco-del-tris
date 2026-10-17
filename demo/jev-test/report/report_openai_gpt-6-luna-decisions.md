# Report - openai/gpt-6-luna-decisions

Email valutate: 300  (errori di chiamata: 0)
**Accuratezza globale: 97.7%**
- email facili: 232 -> 98.3%
- email difficili: 68 -> 95.6%

## Precision / recall / F1 per classe

classe                  supp    prec     rec      f1
personale                 43 100.0% 100.0% 100.0%
professionale             32 100.0%  96.9%  98.4%
spam                      27  86.7%  96.3%  91.2%
pubblicita                39 100.0%  97.4%  98.7%
newsletter                37 100.0% 100.0% 100.0%
proposta_commerciale      37  97.4% 100.0%  98.7%
phishing                  41  95.0%  92.7%  93.8%
notifica_automatica       44 100.0%  97.7%  98.9%
macro F1                                      97.5%

## Matrice di confusione (righe = attesa, colonne = predetta)

                        person  profes    spam  pubbli  newsle  propos  phishi  notifi
personale                   43       0       0       0       0       0       0       0
professionale                0      31       0       0       0       1       0       0
spam                         0       0      26       0       0       0       1       0
pubblicita                   0       0       1      38       0       0       0       0
newsletter                   0       0       0       0      37       0       0       0
proposta_commerciale         0       0       0       0       0      37       0       0
phishing                     0       0       3       0       0       0      38       0
notifica_automatica          0       0       0       0       0       0       1      43

## Calibrazione: accuratezza per fascia di confidenza

confidenza         n  accuratezza
0.00-0.50          1         0.0%
0.50-0.70          2        50.0%
0.70-0.90         11        81.8%
0.90-0.97         13        84.6%
0.97-1.00        273        99.6%
Se si accettano solo risposte con confidenza >= 0.8: copertura 98.0%, accuratezza 98.6%
Se si accettano solo risposte con confidenza >= 0.9: copertura 95.3%, accuratezza 99.0%

## Latenza e costo

Latenza per richiesta: mediana 0.37s, p95 0.63s
Costo totale: $0.0188 su 300 richieste ($0.000063/email)
Token in ingresso totali: 187593

## Errori (7)

- phishing -> spam: 3
- spam -> phishing: 1
- professionale -> proposta_commerciale: 1
- notifica_automatica -> phishing: 1
- pubblicita -> spam: 1

Esempi (i più sicuri di sé, quindi i più interessanti):

- #21 atteso=professionale predetto=proposta_commerciale conf=0.98 [difficile] | Informazioni sui vostri servizi
- #68 atteso=phishing predetto=spam conf=0.94 | Ho accesso alla tua webcam
- #248 atteso=phishing predetto=spam conf=0.93 | Ho accesso alla tua webcam
- #168 atteso=phishing predetto=spam conf=0.85 | Ho accesso alla tua webcam
- #14 atteso=spam predetto=phishing conf=0.74 [difficile] | Re: Re: tua richiesta
- #256 atteso=pubblicita predetto=spam conf=0.59 [difficile] | I tuoi punti stanno per scadere
- #185 atteso=notifica_automatica predetto=phishing conf=0.43 | Avviso di scadenza rata condominiale
