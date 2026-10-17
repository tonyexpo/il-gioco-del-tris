# Report - typesafe/jev-1.14

Email valutate: 300  (errori di chiamata: 0)
**Accuratezza globale: 96.7%**
- email facili: 232 -> 97.4%
- email difficili: 68 -> 94.1%

## Precision / recall / F1 per classe

classe                  supp    prec     rec      f1
personale                 43 100.0% 100.0% 100.0%
professionale             32  96.6%  87.5%  91.8%
spam                      27  86.7%  96.3%  91.2%
pubblicita                39 100.0%  97.4%  98.7%
newsletter                37 100.0% 100.0% 100.0%
proposta_commerciale      37  90.2% 100.0%  94.9%
phishing                  41  97.4%  90.2%  93.7%
notifica_automatica       44 100.0% 100.0% 100.0%
macro F1                                      96.3%

## Matrice di confusione (righe = attesa, colonne = predetta)

                        person  profes    spam  pubbli  newsle  propos  phishi  notifi
personale                   43       0       0       0       0       0       0       0
professionale                0      28       0       0       0       4       0       0
spam                         0       0      26       0       0       0       1       0
pubblicita                   0       0       1      38       0       0       0       0
newsletter                   0       0       0       0      37       0       0       0
proposta_commerciale         0       0       0       0       0      37       0       0
phishing                     0       1       3       0       0       0      37       0
notifica_automatica          0       0       0       0       0       0       0      44

## Calibrazione: accuratezza per fascia di confidenza

confidenza         n  accuratezza
0.00-0.50          2         0.0%
0.50-0.70          4        75.0%
0.70-0.90         24        95.8%
0.90-0.97         28        78.6%
0.97-1.00        242       100.0%
Se si accettano solo risposte con confidenza >= 0.8: copertura 95.0%, accuratezza 97.9%
Se si accettano solo risposte con confidenza >= 0.9: copertura 90.0%, accuratezza 97.8%

## Latenza e costo

Latenza per richiesta: mediana 0.32s, p95 0.47s
Costo totale: $0.0096 su 300 richieste ($0.000032/email)
Token in ingresso totali: 228991

## Errori (10)

- professionale -> proposta_commerciale: 4
- phishing -> spam: 3
- spam -> phishing: 1
- phishing -> professionale: 1
- pubblicita -> spam: 1

Esempi (i più sicuri di sé, quindi i più interessanti):

- #168 atteso=phishing predetto=spam conf=0.92 | Ho accesso alla tua webcam
- #286 atteso=professionale predetto=proposta_commerciale conf=0.92 | Re: Preventivo progetto Mercurio
- #68 atteso=phishing predetto=spam conf=0.91 | Ho accesso alla tua webcam
- #285 atteso=professionale predetto=proposta_commerciale conf=0.91 | Re: Preventivo progetto Mercurio
- #299 atteso=professionale predetto=proposta_commerciale conf=0.91 | Re: Preventivo progetto Delta
- #248 atteso=phishing predetto=spam conf=0.9 | Ho accesso alla tua webcam
- #21 atteso=professionale predetto=proposta_commerciale conf=0.7 [difficile] | Informazioni sui vostri servizi
- #118 atteso=phishing predetto=professionale conf=0.63 [difficile] | Cambio coordinate bancarie
- #14 atteso=spam predetto=phishing conf=0.47 [difficile] | Re: Re: tua richiesta
- #256 atteso=pubblicita predetto=spam conf=0.35 [difficile] | I tuoi punti stanno per scadere
