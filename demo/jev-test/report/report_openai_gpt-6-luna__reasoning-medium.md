# Report - openai/gpt-6-luna (reasoning=medium)

Email valutate: 300  (errori di chiamata: 0)
**Accuratezza globale: 96.7%**
- email facili: 232 -> 97.4%
- email difficili: 68 -> 94.1%

## Precision / recall / F1 per classe

classe                  supp    prec     rec      f1
personale                 43 100.0% 100.0% 100.0%
professionale             32 100.0%  93.8%  96.8%
spam                      27  88.9%  88.9%  88.9%
pubblicita                39 100.0%  97.4%  98.7%
newsletter                37 100.0% 100.0% 100.0%
proposta_commerciale      37  94.9% 100.0%  97.4%
phishing                  41  88.4%  92.7%  90.5%
notifica_automatica       44 100.0%  97.7%  98.9%
macro F1                                      96.4%

## Matrice di confusione (righe = attesa, colonne = predetta)

                        person  profes    spam  pubbli  newsle  propos  phishi  notifi
personale                   43       0       0       0       0       0       0       0
professionale                0      30       0       0       0       2       0       0
spam                         0       0      24       0       0       0       3       0
pubblicita                   0       0       0      38       0       0       1       0
newsletter                   0       0       0       0      37       0       0       0
proposta_commerciale         0       0       0       0       0      37       0       0
phishing                     0       0       3       0       0       0      38       0
notifica_automatica          0       0       0       0       0       0       1      43

## Latenza e costo

Latenza per richiesta: mediana 2.39s, p95 3.50s
Costo totale: $0.0234 su 300 richieste ($0.000078/email)
Token in ingresso totali: 142893
Token in uscita totali: 18158 (di cui reasoning: 11396)

## Errori (10)

- spam -> phishing: 3
- phishing -> spam: 3
- professionale -> proposta_commerciale: 2
- notifica_automatica -> phishing: 1
- pubblicita -> phishing: 1

Esempi (i più sicuri di sé, quindi i più interessanti):

- #14 atteso=spam predetto=phishing conf=None [difficile] | Re: Re: tua richiesta
- #21 atteso=professionale predetto=proposta_commerciale conf=None [difficile] | Informazioni sui vostri servizi
- #59 atteso=spam predetto=phishing conf=None | Urgent business proposal
- #68 atteso=phishing predetto=spam conf=None | Ho accesso alla tua webcam
- #150 atteso=spam predetto=phishing conf=None [difficile] | ciao
- #168 atteso=phishing predetto=spam conf=None | Ho accesso alla tua webcam
- #185 atteso=notifica_automatica predetto=phishing conf=None | Avviso di scadenza rata condominiale
- #248 atteso=phishing predetto=spam conf=None | Ho accesso alla tua webcam
- #256 atteso=pubblicita predetto=phishing conf=None [difficile] | I tuoi punti stanno per scadere
- #286 atteso=professionale predetto=proposta_commerciale conf=None | Re: Preventivo progetto Mercurio
