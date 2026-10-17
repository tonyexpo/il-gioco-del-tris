# Report - microsoft/microsoft-decision-1

Email valutate: 300  (errori di chiamata: 0)
**Accuratezza globale: 94.7%**
- email facili: 232 -> 97.0%
- email difficili: 68 -> 86.8%

## Precision / recall / F1 per classe

classe                  supp    prec     rec      f1
personale                 43 100.0% 100.0% 100.0%
professionale             32  77.5%  96.9%  86.1%
spam                      27  81.8% 100.0%  90.0%
pubblicita                39 100.0%  92.3%  96.0%
newsletter                37 100.0% 100.0% 100.0%
proposta_commerciale      37  97.4% 100.0%  98.7%
phishing                  41 100.0%  80.5%  89.2%
notifica_automatica       44 100.0%  90.9%  95.2%
macro F1                                      94.4%

## Matrice di confusione (righe = attesa, colonne = predetta)

                        person  profes    spam  pubbli  newsle  propos  phishi  notifi
personale                   43       0       0       0       0       0       0       0
professionale                0      31       0       0       0       1       0       0
spam                         0       0      27       0       0       0       0       0
pubblicita                   0       0       3      36       0       0       0       0
newsletter                   0       0       0       0      37       0       0       0
proposta_commerciale         0       0       0       0       0      37       0       0
phishing                     0       5       3       0       0       0      33       0
notifica_automatica          0       4       0       0       0       0       0      40

## Calibrazione: accuratezza per fascia di confidenza

confidenza         n  accuratezza
0.00-0.50          7        71.4%
0.50-0.70         12        33.3%
0.70-0.90         17        76.5%
0.90-0.97          8        87.5%
0.97-1.00        256        99.6%
Se si accettano solo risposte con confidenza >= 0.8: copertura 90.7%, accuratezza 98.9%
Se si accettano solo risposte con confidenza >= 0.9: copertura 88.0%, accuratezza 99.2%

## Latenza e costo

Latenza per richiesta: mediana 0.41s, p95 0.88s
Costo totale: $0.0048 su 300 richieste ($0.000016/email)
Token in ingresso totali: 115031

## Errori (16)

- phishing -> professionale: 5
- notifica_automatica -> professionale: 4
- phishing -> spam: 3
- pubblicita -> spam: 3
- professionale -> proposta_commerciale: 1

Esempi (i più sicuri di sé, quindi i più interessanti):

- #21 atteso=professionale predetto=proposta_commerciale conf=1.0 [difficile] | Informazioni sui vostri servizi
- #118 atteso=phishing predetto=professionale conf=0.97 [difficile] | Cambio coordinate bancarie
- #168 atteso=phishing predetto=spam conf=0.83 | Ho accesso alla tua webcam
- #113 atteso=phishing predetto=professionale conf=0.77 [difficile] | Re: Fattura 3369
- #120 atteso=phishing predetto=professionale conf=0.74 [difficile] | Re: Fattura 3848
- #68 atteso=phishing predetto=spam conf=0.72 | Ho accesso alla tua webcam
- #248 atteso=phishing predetto=spam conf=0.69 | Ho accesso alla tua webcam
- #95 atteso=pubblicita predetto=spam conf=0.6 | Fibra a 10 euro al mese per sempre
- #23 atteso=phishing predetto=professionale conf=0.58 [difficile] | Favore urgente
- #80 atteso=notifica_automatica predetto=professionale conf=0.53 [difficile] | Invito: Sync Orion - mercoledì 10:00
- #202 atteso=notifica_automatica predetto=professionale conf=0.53 [difficile] | Invito: Sync Atlas - mercoledì 10:00
- #273 atteso=notifica_automatica predetto=professionale conf=0.53 [difficile] | Invito: Sync Delta - lunedì 17:00
