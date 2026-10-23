# Rapporto di analisi uova: GPT-6.1 Sol (LLM, raffronto)

- **Modello richiesto**: `openai/gpt-6.1-sol`
- **Modello servito**: `openai/gpt-6.1-sol`
- **Interfaccia**: OpenRouter Chat Completions con output JSON strutturato (modello generativo, senza probabilità)
- **Data analisi**: 23 ottobre 2026 alle ore 17:37
- **Foto analizzate**: 200 su 200

## Riepilogo

| Esito | Foto | Quota |
| --- | ---: | ---: |
| Accettate (grado A, pulite e integre) | 36 | 18.0% |
| Accettate (grado B, lievemente sporche) | 54 | 27.0% |
| **Scartate** (rotte, crepate o sporche) | 107 | 53.5% |
| Non valutabili (uovo non rilevato) | 3 | 1.5% |

Motivi di scarto (una foto può averne più d'uno): crepato 99, rotto 6, sporco 7, uovo non rilevato 3.

| Pulizia | Foto |  | Integrità | Foto |
| --- | ---: | --- | --- | ---: |
| pulito | 82 |  | integro | 92 |
| lievemente sporco | 111 |  | crepato | 99 |
| sporco | 7 |  | rotto | 9 |

### Per tipo di scena

| Scena | Foto | Accettate | Scartate | Non valutabili |
| --- | ---: | ---: | ---: | ---: |
| uovo singolo | 100 | 18 | 82 | 0 |
| poche uova | 49 | 36 | 10 | 3 |
| cartone con più uova | 51 | 36 | 15 | 0 |

### Confronto con la verità nota

Solo le foto Figshare hanno una verità annotata a mano (crepe). Le altre foto non hanno etichette, quindi per pulizia e per le foto Commons/Hugging Face non esiste una misura di accuratezza.

- Uova crepate note: **82 su 100** riconosciute come crepate o rotte (82.0%).
- Le crepe di questo dataset sono sottili e le foto sono ridotte a 1568 px: è una prova difficile, non rappresentativa delle rotture evidenti.

### Tempi e costi

| Metrica | Valore |
| --- | ---: |
| Latenza media | 6.95 s |
| Latenza p50 | 5.96 s |
| Latenza p95 | 13.15 s |
| Token in ingresso | 506290 |
| Token in uscita | 18497 |
| Costo totale (da `usage.cost`) | $1.4504 |
| Costo per 1000 foto | $7.2520 |

## Come è stata fatta l'analisi

Contesto dato al modello: "Foto di controllo qualità di uova di gallina. Se nella foto ci sono più uova, valuta l'uovo in condizioni peggiori. Valuta solo quello che vedi nel guscio."

Pulizia del guscio:

- `clean` (pulito): Guscio pulito: nessuna sporcizia, feci, sangue o macchie visibili (minuscoli puntini o timbri di stampa sono ammessi).
- `slightly_dirty` (lievemente sporco): Guscio lievemente sporco: poche macchie, residui o aloni che coprono una piccola parte della superficie.
- `dirty` (sporco): Guscio sporco: feci, sangue, fango, tuorlo o macchie evidenti su una parte significativa della superficie.

Integrità del guscio:

- `intact` (integro): Guscio integro: nessuna crepa, frattura, ammaccatura o perdita di contenuto visibile.
- `cracked` (crepato): Guscio crepato: è visibile una crepa o una frattura (anche sottile) ma il guscio è ancora in un pezzo.
- `broken` (rotto): Guscio rotto: pezzi mancanti, guscio sfondato o contenuto che fuoriesce.

Regola di decisione, identica per tutti i modelli:

- scartata se l'integrità non è `intact` oppure la pulizia è `dirty`;
- grado A se pulita e integra, grado B se lievemente sporca e integra;
- non valutabile se la probabilità di "uovo visibile" è sotto 0.5.

Se la foto mostra un cartone, il modello valuta l'uovo in condizioni peggiori: un solo uovo difettoso fa scartare l'intera foto.

## Composizione del campione analizzato

100 foto di uova bianche, 49 foto di uova marroni (varie tonalità), 51 foto di uova bianche e marroni.
Le foto sono state analizzate alternando uova bianche e uova di altre tonalità (ordine mescolato con seed fisso).

## Dataset di origine delle foto

| Dataset | Autori | Licenza | Foto nella demo | URL originali |
| --- | --- | --- | ---: | --- |
| Dataset for real-time crack detection on chicken eggs (split test) | Bhavya Botta, Ashis Kumar Datta | CC BY 4.0 | 100 | [pagina](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) · [DOI](https://doi.org/10.6084/m9.figshare.21568425.v1) · [file](https://ndownloader.figshare.com/files/38230539) |
| Wikimedia Commons: Category:Brown chicken eggs, Category:Chicken eggs, Category:Cracked eggs | Vari (autore e licenza per file nel manifest) | CC0 / CC BY / CC BY-SA / pubblico dominio (per file) | 49 | [pagina](https://commons.wikimedia.org/wiki/Category:Brown_chicken_eggs) |
| Egg-Detection (white-egg / brown-egg) | afshin-dini | MIT | 51 | [pagina](https://huggingface.co/datasets/afshin-dini/Egg-Detection) · [file](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/) |

- **figshare_test**: Uova di gallina bianche singole con crepe sottili, annotazioni VOC (classi egg, crack).
- **wikimedia_commons**: Selezione manuale di 49 foto: uova marroni di varie tonalitÃ  e alcune con crepe, rotture, sangue o piume. Non annotate.
- **hf_egg_detection**: Cartoni con piÃ¹ uova bianche e marroni. afshin-dini/Egg-Instance-Segmentation contiene le stesse immagini.

## Dettaglio per foto

| # | Foto | Scena | Pulizia | Integrità | Decisione | Latenza | Motivazione del modello |
| ---: | --- | --- | --- | --- | --- | ---: | --- |
| 1 | [figshare_IMG_20220818_154808.jpg](../../_pics/figshare_IMG_20220818_154808.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.59 s | Guscio integro con poche piccole macchie scure localizzate sul lato sinistro, senza crepe visibili.; verità: cracked |
| 2 | [commons_04.jpg](../../_pics/commons_04.jpg) | poche uova | pulito | integro | accetta (A) | 5.70 s | I gusci appaiono puliti e integri, senza sporcizia significativa, crepe o perdite di contenuto visibili. |
| 3 | [figshare_IMG_20220818_154045.jpg](../../_pics/figshare_IMG_20220818_154045.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.01 s | Piccole macchie e residui sul guscio; crepa sottile visibile sul lato sinistro, senza perdita di contenuto.; verità: cracked |
| 4 | [commons_03.jpg](../../_pics/commons_03.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 6.14 s | L'uovo in primo piano a destra presenta una sottile crepa nella parte superiore; non si osserva sporcizia evidente. |
| 5 | [figshare_IMG_20220818_155841.jpg](../../_pics/figshare_IMG_20220818_155841.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.13 s | Guscio pulito con crepe ramificate ben visibili, senza pezzi mancanti né fuoriuscita di contenuto.; verità: cracked |
| 6 | [hf_sample47.jpg](../../_pics/hf_sample47.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 6.74 s | L’uovo marrone a destra, penultimo in basso, presenta una crepa visibile; il guscio appare pulito. |
| 7 | [figshare_IMG_20220818_155248.jpg](../../_pics/figshare_IMG_20220818_155248.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.33 s | Piccole macchie brunastre localizzate sul lato destro; guscio integro, senza crepe o perdite visibili.; verità: cracked |
| 8 | [commons_30.jpg](../../_pics/commons_30.jpg) | poche uova | pulito | integro | accetta (A) | 4.48 s | Tutte le uova presentano gusci puliti e integri, senza sporcizia, crepe o perdite visibili. |
| 9 | [figshare_IMG_20220818_155341.jpg](../../_pics/figshare_IMG_20220818_155341.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.41 s | Piccole macchie e residui sul lato destro del guscio, senza crepe o rotture visibili.; verità: cracked |
| 10 | [commons_15.jpg](../../_pics/commons_15.jpg) | poche uova | pulito | integro | accetta (A) | 4.04 s | Guscio pulito e uniforme, senza sporcizia, crepe o fratture visibili. |
| 11 | [figshare_IMG_20220818_153759.jpg](../../_pics/figshare_IMG_20220818_153759.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 6.14 s | Guscio con poche piccole macchie e lievi aloni localizzati; nessuna crepa o rottura visibile.; verità: cracked |
| 12 | [hf_sample7.jpg](../../_pics/hf_sample7.jpg) | cartone con più uova | pulito | integro | accetta (A) | 9.79 s | I gusci visibili sono puliti, con soli timbri di stampa, senza crepe, rotture o perdite evidenti. |
| 13 | [figshare_IMG_20220818_160114.jpg](../../_pics/figshare_IMG_20220818_160114.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.84 s | Guscio pulito con una crepa sottile visibile nella parte centrale inferiore, senza perdita di contenuto.; verità: cracked |
| 14 | [commons_36.jpg](../../_pics/commons_36.jpg) | poche uova | pulito | integro | accetta (A) | 3.92 s | Guscio pulito e integro, con soli timbri di stampa e nessuna crepa visibile. |
| 15 | [figshare_IMG_20220818_155859.jpg](../../_pics/figshare_IMG_20220818_155859.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.52 s | Piccolo alone brunastro sul guscio e crepe visibili nella parte inferiore, senza pezzi mancanti né fuoriuscite.; verità: cracked |
| 16 | [hf_sample3.jpg](../../_pics/hf_sample3.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.06 s | L’uovo centrale presenta una piccola macchia giallastra sul guscio, senza crepe o rotture visibili. |
| 17 | [figshare_IMG_20220818_155422.jpg](../../_pics/figshare_IMG_20220818_155422.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.69 s | Piccole macchie brunastre sul lato sinistro e crepe ramificate nella zona centrale del guscio, senza perdite visibili.; verità: cracked |
| 18 | [commons_25.jpg](../../_pics/commons_25.jpg) | poche uova | pulito | integro | accetta (A) | 5.00 s | Guscio pulito con minuscoli puntini naturali, senza sporcizia, crepe o rotture visibili. |
| 19 | [figshare_IMG_20220818_154854.jpg](../../_pics/figshare_IMG_20220818_154854.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.79 s | Residui localizzati nella parte inferiore del guscio e una crepa sottile visibile, senza pezzi mancanti.; verità: cracked |
| 20 | [hf_sample30.jpg](../../_pics/hf_sample30.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.76 s | L’uovo marrone in basso presenta alcune macchie chiare e piccoli segni superficiali, senza crepe visibili. |
| 21 | [figshare_IMG_20220818_154019.jpg](../../_pics/figshare_IMG_20220818_154019.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.82 s | Guscio integro con poche piccole macchie e lievi residui localizzati; nessuna crepa visibile.; verità: cracked |
| 22 | [hf_sample9.jpg](../../_pics/hf_sample9.jpg) | cartone con più uova | pulito | integro | accetta (A) | 7.23 s | I gusci visibili sono puliti, con soli timbri di stampa, senza crepe, rotture o perdite evidenti. |
| 23 | [figshare_IMG_20220818_154949.jpg](../../_pics/figshare_IMG_20220818_154949.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.98 s | Piccoli residui e aloni sul lato sinistro; crepa evidente sul lato destro, senza perdita di contenuto.; verità: cracked |
| 24 | [commons_18.jpg](../../_pics/commons_18.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.89 s | Alcune uova presentano piccoli aloni e residui superficiali; non si vedono crepe o rotture. |
| 25 | [figshare_IMG_20220818_155415.jpg](../../_pics/figshare_IMG_20220818_155415.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.06 s | Piccole macchie brunastre sul guscio e crepe ramificate visibili nella zona centrale, senza perdita di contenuto.; verità: cracked |
| 26 | [commons_23.jpg](../../_pics/commons_23.jpg) | poche uova | pulito | integro | accetta (A) | 8.05 s | Gusci puliti, con piccoli puntini naturali e senza crepe, rotture o perdite visibili. |
| 27 | [figshare_IMG_20220818_155457.jpg](../../_pics/figshare_IMG_20220818_155457.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.75 s | Guscio con una crepa visibile sul lato sinistro e piccole macchie brunastre nella parte inferiore.; verità: cracked |
| 28 | [hf_sample8.jpg](../../_pics/hf_sample8.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.50 s | I gusci visibili sono puliti e integri, senza crepe o perdite; presenti soltanto timbri e minuscoli puntini. |
| 29 | [figshare_IMG_20220818_154636.jpg](../../_pics/figshare_IMG_20220818_154636.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.71 s | Piccoli residui giallastri sulla parte inferiore del guscio; nessuna crepa o rottura visibile.; verità: cracked |
| 30 | [hf_sample20.jpg](../../_pics/hf_sample20.jpg) | cartone con più uova | pulito | integro | accetta (A) | 6.62 s | I gusci appaiono puliti e integri, senza crepe o residui visibili; presenti solo timbri e minuscoli puntini. |
| 31 | [figshare_IMG_20220818_154528.jpg](../../_pics/figshare_IMG_20220818_154528.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.79 s | Guscio pulito con minuscoli puntini ammessi; visibile una crepa sottile e irregolare, senza perdita di contenuto.; verità: cracked |
| 32 | [hf_sample34.jpg](../../_pics/hf_sample34.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 8.37 s | L’uovo bianco centrale a destra presenta una sottile crepa e lievi segni grigiastri sul guscio. |
| 33 | [figshare_IMG_20220818_160007.jpg](../../_pics/figshare_IMG_20220818_160007.jpg) | uovo singolo | sporco | rotto | **scarta**: rotto, sporco | 6.98 s | Sporcizia evidente su una parte significativa del guscio, con zona sfondata e crepe circostanti.; verità: cracked |
| 34 | [commons_27.jpg](../../_pics/commons_27.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 6.06 s | L'uovo in primo piano a sinistra presenta alcune macchie scure localizzate; non si vedono crepe o rotture. |
| 35 | [figshare_IMG_20220818_154535.jpg](../../_pics/figshare_IMG_20220818_154535.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 8.06 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa sulla superficie, senza perdita di contenuto.; verità: cracked |
| 36 | [hf_sample13.jpg](../../_pics/hf_sample13.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.79 s | I gusci visibili sono puliti e integri, senza crepe o rotture; presenti solo timbri e minuscoli puntini. |
| 37 | [figshare_IMG_20220818_155015.jpg](../../_pics/figshare_IMG_20220818_155015.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 9.72 s | Visibile una crepa sul lato sinistro del guscio e poche piccole macchie brunastre sul lato destro.; verità: cracked |
| 38 | [hf_sample46.jpg](../../_pics/hf_sample46.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 9.32 s | L’uovo marrone in basso a destra presenta un piccolo segno scuro sul guscio, senza crepe visibili. |
| 39 | [figshare_IMG_20220818_155401.jpg](../../_pics/figshare_IMG_20220818_155401.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.57 s | Piccole macchie brunastre e residui localizzati sul guscio, senza crepe o rotture visibili.; verità: cracked |
| 40 | [commons_34.jpg](../../_pics/commons_34.jpg) | poche uova | pulito | integro | accetta (A) | 3.93 s | Guscio pulito, senza macchie o residui visibili; nessuna crepa, frattura o perdita di contenuto. |
| 41 | [figshare_IMG_20220818_155709.jpg](../../_pics/figshare_IMG_20220818_155709.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.80 s | Guscio pulito con una crepa sottile visibile sul lato destro, senza pezzi mancanti o fuoriuscite.; verità: cracked |
| 42 | [commons_32.jpg](../../_pics/commons_32.jpg) | poche uova | pulito | integro | accetta (A) | 5.16 s | Guscio pulito con minuscoli puntini naturali, senza crepe, fratture o perdite visibili. |
| 43 | [figshare_IMG_20220818_155137.jpg](../../_pics/figshare_IMG_20220818_155137.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.64 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa sulla superficie centrale, senza perdita di contenuto.; verità: cracked |
| 44 | [commons_42.jpg](../../_pics/commons_42.jpg) | poche uova | sporco | integro | **scarta**: sporco | 4.82 s | Il guscio presenta un'estesa copertura di sangue; non sono visibili crepe o rotture. |
| 45 | [figshare_IMG_20220818_155511.jpg](../../_pics/figshare_IMG_20220818_155511.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.92 s | Visibile una sottile crepa sul lato destro del guscio e pochi piccoli residui brunastri.; verità: cracked |
| 46 | [commons_16.jpg](../../_pics/commons_16.jpg) | poche uova | pulito | integro | accetta (A) | 4.38 s | Guscio pulito con minuscoli puntini naturali, senza sporcizia, crepe o rotture visibili. |
| 47 | [figshare_IMG_20220818_154136.jpg](../../_pics/figshare_IMG_20220818_154136.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.91 s | Piccole macchie sul guscio e una sottile crepa visibile nella parte inferiore sinistra, senza fuoriuscita di contenuto.; verità: cracked |
| 48 | [commons_19.jpg](../../_pics/commons_19.jpg) | poche uova | pulito | integro | accetta (A) | 5.11 s | I gusci visibili sono puliti, con minuscoli puntini naturali e senza crepe, fratture o perdite evidenti. |
| 49 | [figshare_IMG_20220818_154759.jpg](../../_pics/figshare_IMG_20220818_154759.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 8.49 s | Piccoli residui scuri localizzati e una sottile crepa visibile nella parte centrale inferiore del guscio.; verità: cracked |
| 50 | [commons_47.jpg](../../_pics/commons_47.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.25 s | Una piccola piuma aderisce al guscio; non sono visibili crepe, fratture o perdite di contenuto. |
| 51 | [figshare_IMG_20220818_155540.jpg](../../_pics/figshare_IMG_20220818_155540.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 7.03 s | Guscio pulito con minuscoli puntini; evidente crepa ramificata, senza pezzi mancanti né fuoriuscita di contenuto.; verità: cracked |
| 52 | [hf_sample17.jpg](../../_pics/hf_sample17.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.17 s | L’uovo in basso a sinistra presenta piccoli residui e aloni sul guscio, senza crepe visibili. |
| 53 | [figshare_IMG_20220818_154226.jpg](../../_pics/figshare_IMG_20220818_154226.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.12 s | Visibile una sottile crepa sul guscio, con poche piccole macchie e residui superficiali.; verità: cracked |
| 54 | [hf_sample33.jpg](../../_pics/hf_sample33.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 6.35 s | L’uovo bianco nella seconda fila a destra presenta una sottile crepa visibile, senza sporco evidente. |
| 55 | [figshare_IMG_20220818_155846.jpg](../../_pics/figshare_IMG_20220818_155846.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 3.91 s | Guscio pulito con crepe evidenti nella parte superiore e centrale, senza pezzi mancanti né fuoriuscite.; verità: cracked |
| 56 | [commons_11.jpg](../../_pics/commons_11.jpg) | poche uova | pulito | integro | accetta (A) | 4.78 s | Guscio pulito e uniforme, senza sporcizia, crepe, fratture o perdite di contenuto visibili. |
| 57 | [figshare_IMG_20220818_153842.jpg](../../_pics/figshare_IMG_20220818_153842.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.59 s | Guscio integro, con poche piccole macchie e residui brunastri sulla superficie.; verità: cracked |
| 58 | [commons_48.jpg](../../_pics/commons_48.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 6.23 s | Una piccola piuma aderisce al guscio; non sono visibili crepe, fratture o perdite di contenuto. |
| 59 | [figshare_IMG_20220818_160129.jpg](../../_pics/figshare_IMG_20220818_160129.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 7.20 s | Guscio pulito, con una sottile crepa visibile nella parte inferiore destra, senza perdita di contenuto.; verità: cracked |
| 60 | [hf_sample2.jpg](../../_pics/hf_sample2.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 8.63 s | L'uovo nella terza fila a destra presenta piccoli residui marroni sul guscio, senza crepe visibili. |
| 61 | [figshare_IMG_20220818_155851.jpg](../../_pics/figshare_IMG_20220818_155851.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.78 s | Guscio pulito, con una sottile crepa visibile nella parte superiore centrale, senza perdita di contenuto.; verità: cracked |
| 62 | [hf_sample29.jpg](../../_pics/hf_sample29.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 7.55 s | L'uovo marrone in basso a destra presenta un piccolo residuo chiaro sul guscio; non sono visibili crepe. |
| 63 | [figshare_IMG_20220818_154436.jpg](../../_pics/figshare_IMG_20220818_154436.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 3.90 s | Guscio pulito con una sottile crepa visibile nella parte superiore, senza fuoriuscita di contenuto.; verità: cracked |
| 64 | [hf_sample37.jpg](../../_pics/hf_sample37.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 8.02 s | Il secondo uovo da sinistra nella fila superiore presenta una crepa visibile nella parte inferiore del guscio, altrimenti pulito. |
| 65 | [figshare_IMG_20220818_154051.jpg](../../_pics/figshare_IMG_20220818_154051.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.54 s | Piccole macchie e residui sul guscio; visibile una crepa sottile e ramificata, senza perdita di contenuto.; verità: cracked |
| 66 | [hf_sample40.jpg](../../_pics/hf_sample40.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 13.65 s | L’uovo nella seconda fila a destra presenta una sottile crepa sul guscio e piccole macchie superficiali. |
| 67 | [figshare_IMG_20220818_155910.jpg](../../_pics/figshare_IMG_20220818_155910.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.15 s | Guscio pulito con una lunga crepa visibile; nessun pezzo mancante o fuoriuscita di contenuto.; verità: cracked |
| 68 | [hf_sample41.jpg](../../_pics/hf_sample41.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 13.38 s | L'uovo a destra nella quarta fila presenta una sottile frattura sul bordo superiore sinistro; guscio pulito. |
| 69 | [figshare_IMG_20220818_154057.jpg](../../_pics/figshare_IMG_20220818_154057.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.77 s | Guscio con poche macchie e residui superficiali; evidente crepa orizzontale, senza perdita di contenuto.; verità: cracked |
| 70 | [hf_sample43.jpg](../../_pics/hf_sample43.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 7.79 s | L'uovo bianco nella seconda fila a sinistra presenta crepe visibili sul lato destro, senza sporcizia evidente. |
| 71 | [figshare_IMG_20220818_154444.jpg](../../_pics/figshare_IMG_20220818_154444.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.38 s | Piccoli aloni e residui sul guscio; crepe ramificate visibili nella parte inferiore, senza perdita di contenuto.; verità: cracked |
| 72 | [commons_20.jpg](../../_pics/commons_20.jpg) | poche uova | pulito | integro | accetta (A) | 13.15 s | Gusci puliti con soli minuscoli puntini; nessuna crepa, frattura o perdita di contenuto visibile. |
| 73 | [figshare_IMG_20220818_155948.jpg](../../_pics/figshare_IMG_20220818_155948.jpg) | uovo singolo | sporco | rotto | **scarta**: rotto, sporco | 9.13 s | Guscio sfondato con porzione mancante, lunga frattura e macchie di sporco diffuse su una parte significativa della superficie.; verità: cracked |
| 74 | [hf_sample11.jpg](../../_pics/hf_sample11.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.47 s | I gusci visibili sono puliti e integri, senza crepe o rotture; presenti solo timbri e minuscoli puntini. |
| 75 | [figshare_IMG_20220818_155606.jpg](../../_pics/figshare_IMG_20220818_155606.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.17 s | Visibili fratture ramificate nella zona centrale del guscio e poche piccole macchie brunastre sulla superficie.; verità: cracked |
| 76 | [commons_49.jpg](../../_pics/commons_49.jpg) | poche uova | lievemente sporco | rotto | **scarta**: rotto | 12.26 s | Guscio sfondato nella parte inferiore, con frammenti sollevati e residui localizzati attorno alla rottura. |
| 77 | [figshare_IMG_20220818_154914.jpg](../../_pics/figshare_IMG_20220818_154914.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.57 s | Residui e macchie localizzati sul guscio; crepe sottili visibili nella zona centrale, senza perdita di contenuto.; verità: cracked |
| 78 | [hf_sample22.jpg](../../_pics/hf_sample22.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.32 s | L'uovo centrale presenta un piccolo residuo brunastro sul guscio; non sono visibili crepe o rotture. |
| 79 | [figshare_IMG_20220818_155240.jpg](../../_pics/figshare_IMG_20220818_155240.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.09 s | Piccole macchie brunastre sul lato destro e una sottile crepa diagonale nella zona centrale del guscio.; verità: cracked |
| 80 | [commons_06.jpg](../../_pics/commons_06.jpg) | poche uova | pulito | integro | accetta (A) | 11.99 s | Entrambe le uova hanno gusci puliti e integri, senza sporco, crepe o rotture visibili. |
| 81 | [figshare_IMG_20220818_160039.jpg](../../_pics/figshare_IMG_20220818_160039.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.04 s | Guscio con poche piccole macchie e fratture ramificate visibili nella zona centrale, senza fuoriuscita di contenuto.; verità: cracked |
| 82 | [hf_sample42.jpg](../../_pics/hf_sample42.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 13.78 s | L’uovo in basso a sinistra presenta una sottile crepa sul lato destro; non si osserva sporcizia evidente. |
| 83 | [figshare_IMG_20220818_154715.jpg](../../_pics/figshare_IMG_20220818_154715.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 15.25 s | Poche piccole macchie sul guscio e crepe visibili nella zona centrale inferiore, senza pezzi mancanti.; verità: cracked |
| 84 | [hf_sample12.jpg](../../_pics/hf_sample12.jpg) | cartone con più uova | pulito | integro | accetta (A) | 3.88 s | I gusci visibili sono puliti e integri, senza crepe o residui evidenti; presenti solo timbri e minuscoli puntini. |
| 85 | [figshare_IMG_20220818_154238.jpg](../../_pics/figshare_IMG_20220818_154238.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.44 s | Piccole macchie brunastre e lievi aloni su porzioni limitate del guscio; nessuna crepa o rottura visibile.; verità: cracked |
| 86 | [hf_sample16.jpg](../../_pics/hf_sample16.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.86 s | L'uovo in basso presenta un piccolo alone sul guscio vicino al timbro; non sono visibili crepe o rotture. |
| 87 | [figshare_IMG_20220818_154413.jpg](../../_pics/figshare_IMG_20220818_154413.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.12 s | Guscio pulito con crepe ramificate visibili nella zona centrale, senza pezzi mancanti né fuoriuscite di contenuto.; verità: cracked |
| 88 | [commons_14.jpg](../../_pics/commons_14.jpg) | poche uova | pulito | integro | accetta (A) | 11.20 s | Entrambi i gusci sono integri e puliti, con solo minuscoli puntini e nessuna crepa visibile. |
| 89 | [figshare_IMG_20220818_155559.jpg](../../_pics/figshare_IMG_20220818_155559.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 17.16 s | Guscio con crepe ramificate visibili e poche piccole macchie giallastre; nessuna perdita di contenuto.; verità: cracked |
| 90 | [hf_sample1.jpg](../../_pics/hf_sample1.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.68 s | L'uovo nella terza fila a destra presenta piccole macchie marroni sul guscio, senza crepe visibili. |
| 91 | [figshare_IMG_20220818_155517.jpg](../../_pics/figshare_IMG_20220818_155517.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 16.26 s | Piccole macchie giallastre sul guscio e una sottile crepa visibile nella parte centrale inferiore, senza fuoriuscite.; verità: cracked |
| 92 | [hf_sample5.jpg](../../_pics/hf_sample5.jpg) | cartone con più uova | pulito | integro | accetta (A) | 11.81 s | I gusci visibili sono puliti e integri, senza sporco né crepe; presente solo un timbro consentito. |
| 93 | [figshare_IMG_20220818_154429.jpg](../../_pics/figshare_IMG_20220818_154429.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.35 s | Guscio pulito con crepe visibili nella zona centrale, senza pezzi mancanti né fuoriuscite di contenuto.; verità: cracked |
| 94 | [commons_13.jpg](../../_pics/commons_13.jpg) | poche uova | pulito | integro | accetta (A) | 14.14 s | Entrambe le uova presentano gusci puliti e integri, senza sporco, crepe o rotture visibili. |
| 95 | [figshare_IMG_20220818_160049.jpg](../../_pics/figshare_IMG_20220818_160049.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.99 s | Piccole macchie giallastre sul guscio e crepe visibili nella zona centrale inferiore, senza fuoriuscita di contenuto.; verità: cracked |
| 96 | [commons_17.jpg](../../_pics/commons_17.jpg) | poche uova | pulito | integro | accetta (A) | 5.51 s | I gusci appaiono puliti, con soli minuscoli puntini naturali, senza crepe, fratture o perdite visibili. |
| 97 | [figshare_IMG_20220818_155353.jpg](../../_pics/figshare_IMG_20220818_155353.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 11.23 s | Piccole macchie brunastre e residui localizzati sul guscio; nessuna crepa o rottura visibile.; verità: cracked |
| 98 | [hf_sample35.jpg](../../_pics/hf_sample35.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 13.68 s | L'uovo bianco superiore presenta una sottile crepa sul lato inferiore sinistro; non si osserva sporcizia significativa. |
| 99 | [figshare_IMG_20220818_154557.jpg](../../_pics/figshare_IMG_20220818_154557.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.69 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa irregolare sul lato sinistro, senza perdita di contenuto.; verità: cracked |
| 100 | [hf_sample27.jpg](../../_pics/hf_sample27.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 11.11 s | L'uovo in basso a sinistra presenta un piccolo residuo biancastro sul guscio; non sono visibili crepe. |
| 101 | [figshare_IMG_20220818_153953.jpg](../../_pics/figshare_IMG_20220818_153953.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.01 s | Guscio integro con pochi piccoli residui e macchie brunastre localizzate, senza crepe visibili.; verità: cracked |
| 102 | [hf_sample14.jpg](../../_pics/hf_sample14.jpg) | cartone con più uova | pulito | integro | accetta (A) | 8.31 s | I gusci visibili sono puliti e integri, senza crepe o residui; presenti soltanto timbri e minuscoli puntini. |
| 103 | [figshare_IMG_20220818_160014.jpg](../../_pics/figshare_IMG_20220818_160014.jpg) | uovo singolo | sporco | rotto | **scarta**: rotto, sporco | 12.41 s | Macchie e residui diffusi sul guscio; zona sfondata nella parte superiore con una crepa che si estende lateralmente.; verità: cracked |
| 104 | [hf_sample19.jpg](../../_pics/hf_sample19.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.87 s | L'uovo superiore presenta piccoli aloni e residui sul guscio; non sono visibili crepe o rotture. |
| 105 | [figshare_IMG_20220818_154113.jpg](../../_pics/figshare_IMG_20220818_154113.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.10 s | Crepa sottile visibile nella parte superiore destra del guscio; piccoli residui e aloni sul lato sinistro.; verità: cracked |
| 106 | [hf_sample18.jpg](../../_pics/hf_sample18.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 9.44 s | L’uovo in alto a sinistra presenta piccoli residui sul guscio vicino al timbro; non sono visibili crepe. |
| 107 | [figshare_IMG_20220818_160123.jpg](../../_pics/figshare_IMG_20220818_160123.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.63 s | Crepa sottile ben visibile al centro del guscio, con piccoli residui localizzati; nessuna perdita di contenuto.; verità: cracked |
| 108 | [hf_sample26.jpg](../../_pics/hf_sample26.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.78 s | Piccole macchie e residui localizzati sul guscio; nessuna crepa o perdita di contenuto visibile. |
| 109 | [figshare_IMG_20220818_155430.jpg](../../_pics/figshare_IMG_20220818_155430.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.88 s | Crepe ramificate visibili al centro del guscio e piccole macchie brunastre sul lato destro, senza fuoriuscita di contenuto.; verità: cracked |
| 110 | [hf_sample32.jpg](../../_pics/hf_sample32.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.22 s | L’uovo in basso a destra presenta piccoli residui e macchie superficiali; non sono visibili crepe o rotture. |
| 111 | [figshare_IMG_20220818_154419.jpg](../../_pics/figshare_IMG_20220818_154419.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 8.15 s | Guscio pulito con crepe ramificate visibili nella zona centrale inferiore, senza pezzi mancanti né fuoriuscite.; verità: cracked |
| 112 | [hf_sample25.jpg](../../_pics/hf_sample25.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 8.93 s | Piccoli residui e macchie localizzate su alcuni gusci; nessuna crepa o rottura visibile. |
| 113 | [figshare_IMG_20220818_160028.jpg](../../_pics/figshare_IMG_20220818_160028.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.31 s | Guscio con crepe ramificate evidenti e poche piccole macchie superficiali, senza perdita visibile di contenuto.; verità: cracked |
| 114 | [commons_01.jpg](../../_pics/commons_01.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 7.34 s | Guscio integro, con un piccolo residuo brunastro visibile sopra il timbro. |
| 115 | [figshare_IMG_20220818_160055.jpg](../../_pics/figshare_IMG_20220818_160055.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.56 s | Guscio con crepe sottili ramificate e pochi piccoli residui giallastri; nessuna perdita di contenuto visibile.; verità: cracked |
| 116 | [hf_sample10.jpg](../../_pics/hf_sample10.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.14 s | I gusci visibili sono puliti e integri, senza crepe o residui; presenti soltanto timbri di stampa. |
| 117 | [figshare_IMG_20220818_155905.jpg](../../_pics/figshare_IMG_20220818_155905.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.05 s | Guscio pulito con una crepa ramificata evidente, senza pezzi mancanti né fuoriuscita di contenuto.; verità: cracked |
| 118 | [commons_39.jpg](../../_pics/commons_39.jpg) | poche uova | lievemente sporco | crepato | **scarta**: crepato | 7.85 s | Visibile una sottile crepa sull’uovo a destra; presenti piccole macchie su alcuni gusci. |
| 119 | [figshare_IMG_20220818_154319.jpg](../../_pics/figshare_IMG_20220818_154319.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.17 s | Guscio pulito con minuscoli puntini ammessi; visibile una lunga crepa sottile, senza perdita di contenuto.; verità: cracked |
| 120 | [commons_37.jpg](../../_pics/commons_37.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 4.45 s | Visibili alcune macchie arancioni su piccole porzioni dei gusci, senza crepe o rotture evidenti. |
| 121 | [figshare_IMG_20220818_160044.jpg](../../_pics/figshare_IMG_20220818_160044.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.38 s | Guscio con fratture ramificate evidenti nella zona centrale e poche piccole macchie brunastre nella parte inferiore.; verità: cracked |
| 122 | [hf_sample24.jpg](../../_pics/hf_sample24.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.39 s | Piccoli residui chiari sul guscio dell’uovo centrale superiore; nessuna crepa o fuoriuscita visibile. |
| 123 | [figshare_IMG_20220818_155030.jpg](../../_pics/figshare_IMG_20220818_155030.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 6.97 s | Pochi piccoli aloni e residui sul guscio, soprattutto a destra; nessuna crepa o perdita visibile.; verità: cracked |
| 124 | [hf_sample31.jpg](../../_pics/hf_sample31.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.74 s | L’uovo marrone in basso presenta piccole macchie e residui superficiali; non sono visibili crepe o rotture. |
| 125 | [figshare_IMG_20220818_155717.jpg](../../_pics/figshare_IMG_20220818_155717.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.42 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa nella parte inferiore destra.; verità: cracked |
| 126 | [hf_sample48.jpg](../../_pics/hf_sample48.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 5.78 s | L’uovo marrone a destra, penultimo dal basso, presenta una crepa visibile; il guscio è pulito e senza perdite. |
| 127 | [figshare_IMG_20220818_154752.jpg](../../_pics/figshare_IMG_20220818_154752.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.32 s | Piccole macchie scure localizzate e una sottile crepa visibile nella zona centrale sinistra del guscio.; verità: cracked |
| 128 | [hf_sample23.jpg](../../_pics/hf_sample23.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.99 s | L'uovo in alto a destra presenta piccole macchie scure sul guscio, senza crepe o rotture visibili. |
| 129 | [figshare_IMG_20220818_155804.jpg](../../_pics/figshare_IMG_20220818_155804.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 7.62 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa sul lato sinistro, senza perdita di contenuto.; verità: cracked |
| 130 | [commons_10.jpg](../../_pics/commons_10.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.30 s | L'uovo a sinistra presenta una piccola macchia biancastra sul guscio; non si vedono crepe o rotture. |
| 131 | [figshare_IMG_20220818_155611.jpg](../../_pics/figshare_IMG_20220818_155611.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.84 s | Crepe ramificate visibili sul guscio, senza perdita di contenuto; piccole macchie brunastre nella parte inferiore.; verità: cracked |
| 132 | [hf_sample38.jpg](../../_pics/hf_sample38.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.25 s | L’uovo in basso a destra presenta piccoli residui e macchie sul guscio, senza crepe visibili. |
| 133 | [figshare_IMG_20220818_155724.jpg](../../_pics/figshare_IMG_20220818_155724.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 7.74 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa sul lato destro.; verità: cracked |
| 134 | [commons_46.jpg](../../_pics/commons_46.jpg) | poche uova | pulito | rotto | non valutabile | 4.09 s | Visibile solo un guscio sfondato e frammentato, senza sporcizia evidente; nessun uovo intero. |
| 135 | [figshare_IMG_20220818_154818.jpg](../../_pics/figshare_IMG_20220818_154818.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.46 s | Piccole macchie brunastre localizzate sul guscio, senza crepe, fratture o perdite visibili.; verità: cracked |
| 136 | [hf_sample39.jpg](../../_pics/hf_sample39.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.67 s | L’uovo in basso a destra presenta piccoli residui e macchie sul guscio, senza crepe visibili. |
| 137 | [figshare_IMG_20220818_154103.jpg](../../_pics/figshare_IMG_20220818_154103.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.52 s | Guscio con poche piccole macchie brunastre e una lunga frattura visibile, senza perdita di contenuto.; verità: cracked |
| 138 | [hf_sample50.jpg](../../_pics/hf_sample50.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 10.98 s | L’uovo a sinistra nella seconda fila presenta una sottile crepa e piccoli residui superficiali. |
| 139 | [figshare_IMG_20220818_155617.jpg](../../_pics/figshare_IMG_20220818_155617.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.54 s | Piccole macchie brunastre sul guscio e crepe ramificate visibili nella zona centrale inferiore, senza perdita di contenuto.; verità: cracked |
| 140 | [commons_45.jpg](../../_pics/commons_45.jpg) | poche uova | pulito | rotto | **scarta**: rotto | 4.94 s | È presente un uovo intero, ma i gusci in primo piano sono rotti, con ampie parti mancanti e senza sporcizia. |
| 141 | [figshare_IMG_20220818_154959.jpg](../../_pics/figshare_IMG_20220818_154959.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.33 s | Crepa evidente sulla parte centrale del guscio, con piccole macchie brunastre sul lato destro.; verità: cracked |
| 142 | [commons_26.jpg](../../_pics/commons_26.jpg) | poche uova | pulito | integro | accetta (A) | 10.37 s | Gusci integri e puliti, con minuscoli puntini superficiali; nessuna crepa o perdita di contenuto visibile. |
| 143 | [figshare_IMG_20220818_153857.jpg](../../_pics/figshare_IMG_20220818_153857.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.26 s | Poche piccole macchie e residui sul guscio, senza crepe o rotture visibili.; verità: cracked |
| 144 | [commons_43.jpg](../../_pics/commons_43.jpg) | poche uova | pulito | rotto | non valutabile | 7.62 s | Visibili solo frammenti di guscio senza sporcizia evidente; uovo rotto con contenuto fuoriuscito. |
| 145 | [figshare_IMG_20220818_154312.jpg](../../_pics/figshare_IMG_20220818_154312.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 3.81 s | Guscio pulito con una frattura irregolare visibile nella zona centrale, senza perdita di contenuto.; verità: cracked |
| 146 | [commons_08.jpg](../../_pics/commons_08.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.96 s | Piccoli residui scuri localizzati su alcuni gusci; nessuna crepa, frattura o perdita di contenuto visibile. |
| 147 | [figshare_IMG_20220818_154335.jpg](../../_pics/figshare_IMG_20220818_154335.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.22 s | Visibile una crepa sottile nella parte superiore del guscio e lievi residui sul lato destro.; verità: cracked |
| 148 | [hf_sample15.jpg](../../_pics/hf_sample15.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.93 s | L’uovo in basso a sinistra presenta un piccolo alone beige sul guscio; non sono visibili crepe o rotture. |
| 149 | [figshare_IMG_20220818_155547.jpg](../../_pics/figshare_IMG_20220818_155547.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.94 s | Guscio con piccole macchie e una crepa ramificata evidente, senza pezzi mancanti né fuoriuscite visibili.; verità: cracked |
| 150 | [commons_12.jpg](../../_pics/commons_12.jpg) | poche uova | pulito | integro | accetta (A) | 3.74 s | Guscio pulito e uniforme, senza macchie, crepe o rotture visibili. |
| 151 | [figshare_IMG_20220818_155047.jpg](../../_pics/figshare_IMG_20220818_155047.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.10 s | Visibile una crepa sul lato sinistro del guscio e poche piccole macchie superficiali; nessuna fuoriuscita di contenuto.; verità: cracked |
| 152 | [commons_31.jpg](../../_pics/commons_31.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.54 s | L'uovo posteriore destro presenta alcune macchie scure localizzate; non sono visibili crepe o rotture. |
| 153 | [figshare_IMG_20220818_155700.jpg](../../_pics/figshare_IMG_20220818_155700.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.06 s | Visibili una sottile crepa sul lato destro e piccoli residui giallastri sulla superficie del guscio.; verità: cracked |
| 154 | [hf_sample44.jpg](../../_pics/hf_sample44.jpg) | cartone con più uova | sporco | integro | **scarta**: sporco | 7.46 s | L’uovo nella terza fila a sinistra presenta ampie macchie grigiastre sul guscio, senza crepe evidenti. |
| 155 | [figshare_IMG_20220818_154613.jpg](../../_pics/figshare_IMG_20220818_154613.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.28 s | Guscio pulito con minuscoli puntini ammessi; visibile una crepa irregolare sulla superficie, senza perdita di contenuto.; verità: cracked |
| 156 | [commons_38.jpg](../../_pics/commons_38.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.14 s | Guscio integro con pochi piccoli aloni e macchie superficiali; nessuna crepa visibile. |
| 157 | [figshare_IMG_20220818_155436.jpg](../../_pics/figshare_IMG_20220818_155436.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.95 s | Crepe visibili nella zona centrale del guscio e piccole macchie brunastre sul lato destro, senza fuoriuscite di contenuto.; verità: cracked |
| 158 | [commons_05.jpg](../../_pics/commons_05.jpg) | poche uova | pulito | integro | accetta (A) | 4.90 s | Guscio pulito con minuscoli puntini naturali, senza sporco, crepe o fratture visibili. |
| 159 | [figshare_IMG_20220818_154407.jpg](../../_pics/figshare_IMG_20220818_154407.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.85 s | Guscio con numerose crepe centrali e lievi tracce di sporco localizzate, senza perdita visibile di contenuto.; verità: cracked |
| 160 | [hf_sample49.jpg](../../_pics/hf_sample49.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 4.95 s | L’uovo a destra nella penultima fila presenta una crepa visibile, senza pezzi mancanti né sporcizia evidente. |
| 161 | [figshare_IMG_20220818_155148.jpg](../../_pics/figshare_IMG_20220818_155148.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.97 s | Visibile una sottile crepa nella parte superiore sinistra del guscio e poche piccole macchie brunastre.; verità: cracked |
| 162 | [hf_sample28.jpg](../../_pics/hf_sample28.jpg) | cartone con più uova | pulito | integro | accetta (A) | 7.95 s | Gusci puliti, con soli minuscoli puntini e un timbro; nessuna crepa, frattura o perdita visibile. |
| 163 | [figshare_IMG_20220818_155959.jpg](../../_pics/figshare_IMG_20220818_155959.jpg) | uovo singolo | sporco | crepato | **scarta**: crepato, sporco | 8.17 s | Macchie e residui evidenti sulla parte superiore del guscio, con crepe visibili e ramificate.; verità: cracked |
| 164 | [hf_sample4.jpg](../../_pics/hf_sample4.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.37 s | L’uovo centrale a destra presenta piccoli residui marroni sul guscio, senza crepe o rotture visibili. |
| 165 | [figshare_IMG_20220818_155744.jpg](../../_pics/figshare_IMG_20220818_155744.jpg) | uovo singolo | pulito | integro | accetta (A) | 3.48 s | Guscio pulito, senza macchie evidenti, crepe o perdite di contenuto visibili.; verità: cracked |
| 166 | [hf_sample36.jpg](../../_pics/hf_sample36.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 8.04 s | L’uovo bianco nella fila inferiore, secondo da destra, presenta una crepa visibile nella parte superiore del guscio. |
| 167 | [figshare_IMG_20220818_154731.jpg](../../_pics/figshare_IMG_20220818_154731.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 8.69 s | Guscio con crepe visibili e poche piccole macchie brunastre, senza pezzi mancanti né fuoriuscite.; verità: cracked |
| 168 | [commons_09.jpg](../../_pics/commons_09.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 8.07 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa nella parte superiore centrale. |
| 169 | [figshare_IMG_20220818_154544.jpg](../../_pics/figshare_IMG_20220818_154544.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 8.48 s | Poche piccole macchie sul guscio e una crepa sinuosa visibile nella parte inferiore, senza fuoriuscite.; verità: cracked |
| 170 | [hf_sample51.jpg](../../_pics/hf_sample51.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 9.68 s | L’uovo marrone nella fila superiore, quarto da sinistra, presenta una crepa curva visibile nella parte alta del guscio. |
| 171 | [figshare_IMG_20220818_154218.jpg](../../_pics/figshare_IMG_20220818_154218.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 11.10 s | Guscio con poche piccole macchie e una sottile crepa verticale visibile nella zona centrale.; verità: cracked |
| 172 | [commons_21.jpg](../../_pics/commons_21.jpg) | poche uova | pulito | integro | accetta (A) | 11.74 s | Gusci puliti, con piccoli puntini e timbri ammessi; nessuna crepa, rottura o perdita di contenuto visibile. |
| 173 | [figshare_IMG_20220818_160033.jpg](../../_pics/figshare_IMG_20220818_160033.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.64 s | Guscio con crepe ramificate visibili e poche piccole macchie superficiali, senza perdita di contenuto.; verità: cracked |
| 174 | [hf_sample6.jpg](../../_pics/hf_sample6.jpg) | cartone con più uova | pulito | integro | accetta (A) | 4.99 s | I gusci visibili sono puliti e integri, senza crepe o residui; presenti soltanto timbri di stampa ammessi. |
| 175 | [figshare_IMG_20220818_155523.jpg](../../_pics/figshare_IMG_20220818_155523.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 9.65 s | Piccole macchie e residui chiari localizzati sul guscio; nessuna crepa o rottura visibile.; verità: cracked |
| 176 | [commons_02.jpg](../../_pics/commons_02.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 12.58 s | L'uovo marrone presenta poche piccole macchie scure sul guscio, senza crepe o rotture visibili. |
| 177 | [figshare_IMG_20220818_154011.jpg](../../_pics/figshare_IMG_20220818_154011.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.23 s | Guscio integro con poche piccole macchie e lievi residui localizzati; nessuna crepa visibile.; verità: cracked |
| 178 | [commons_28.jpg](../../_pics/commons_28.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 10.88 s | L’uovo bianco presenta piccoli aloni e residui superficiali; non sono visibili crepe o rotture. |
| 179 | [figshare_IMG_20220818_154708.jpg](../../_pics/figshare_IMG_20220818_154708.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.02 s | Guscio con poche piccole macchie e una crepa evidente nella zona centrale, senza perdita di contenuto.; verità: cracked |
| 180 | [commons_33.jpg](../../_pics/commons_33.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 4.76 s | L'uovo centrale presenta una lunga crepa trasversale, senza pezzi mancanti o fuoriuscite; guscio privo di sporcizia evidente. |
| 181 | [figshare_IMG_20220818_155812.jpg](../../_pics/figshare_IMG_20220818_155812.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.61 s | Guscio integro con poche piccole macchie e lievi aloni; nessuna crepa o perdita visibile.; verità: cracked |
| 182 | [commons_35.jpg](../../_pics/commons_35.jpg) | poche uova | pulito | integro | accetta (A) | 12.21 s | Guscio pulito con timbro di stampa, senza crepe, rotture o residui visibili. |
| 183 | [figshare_IMG_20220818_155915.jpg](../../_pics/figshare_IMG_20220818_155915.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 11.51 s | Guscio pulito con una crepa sottile visibile nella parte inferiore, senza perdita di contenuto.; verità: cracked |
| 184 | [commons_07.jpg](../../_pics/commons_07.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 18.04 s | L’uovo bianco presenta piccoli aloni grigiastri sul guscio; non si vedono crepe né rotture. |
| 185 | [figshare_IMG_20220818_153638.jpg](../../_pics/figshare_IMG_20220818_153638.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.04 s | Piccoli residui e aloni sul guscio; sottile crepa orizzontale visibile nella zona centrale destra.; verità: cracked |
| 186 | [commons_29.jpg](../../_pics/commons_29.jpg) | poche uova | pulito | integro | accetta (A) | 4.19 s | Guscio visibile pulito, senza macchie, crepe o rotture evidenti. |
| 187 | [figshare_IMG_20220818_155503.jpg](../../_pics/figshare_IMG_20220818_155503.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 12.12 s | Crepa sottile visibile sul guscio, ancora in un pezzo; piccoli residui e macchie nella parte inferiore.; verità: cracked |
| 188 | [hf_sample45.jpg](../../_pics/hf_sample45.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 11.94 s | Piccoli residui chiari su alcuni gusci; non si osservano crepe, rotture o fuoriuscite di contenuto. |
| 189 | [figshare_IMG_20220818_154847.jpg](../../_pics/figshare_IMG_20220818_154847.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 8.89 s | Piccoli residui e macchie localizzati sulla superficie; visibile una crepa sottile, senza pezzi mancanti o fuoriuscite.; verità: cracked |
| 190 | [hf_sample21.jpg](../../_pics/hf_sample21.jpg) | cartone con più uova | pulito | integro | accetta (A) | 4.92 s | I gusci visibili sono puliti e integri, senza crepe o residui; presenti solo timbri di stampa. |
| 191 | [figshare_IMG_20220818_154328.jpg](../../_pics/figshare_IMG_20220818_154328.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 11.43 s | Guscio pulito con minuscoli puntini; visibile una sottile crepa orizzontale nella parte inferiore, senza fuoriuscite.; verità: cracked |
| 192 | [commons_22.jpg](../../_pics/commons_22.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 4.59 s | L'uovo a sinistra presenta poche macchie e residui nella parte inferiore; non sono visibili crepe o rotture. |
| 193 | [figshare_IMG_20220818_154724.jpg](../../_pics/figshare_IMG_20220818_154724.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.96 s | Visibile una frattura estesa del guscio, senza perdita di contenuto, e piccole macchie brunastre localizzate.; verità: cracked |
| 194 | [commons_44.jpg](../../_pics/commons_44.jpg) | poche uova | pulito | rotto | non valutabile | 5.88 s | Nessun uovo intero: guscio frammentato con ampie parti mancanti e contenuto fuoriuscito; nessuna sporcizia evidente sul guscio. |
| 195 | [figshare_IMG_20220818_155132.jpg](../../_pics/figshare_IMG_20220818_155132.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 11.47 s | Guscio pulito con minuscoli puntini e una crepa ramificata visibile nella parte inferiore, senza fuoriuscite.; verità: cracked |
| 196 | [commons_40.jpg](../../_pics/commons_40.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 10.75 s | Guscio pulito con ampie crepe ramificate, senza pezzi mancanti né fuoriuscite visibili. |
| 197 | [figshare_IMG_20220818_154905.jpg](../../_pics/figshare_IMG_20220818_154905.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 10.73 s | Piccoli residui e macchie localizzate sul guscio; visibile una crepa nella zona centrale, senza fuoriuscita di contenuto.; verità: cracked |
| 198 | [commons_41.jpg](../../_pics/commons_41.jpg) | poche uova | sporco | rotto | **scarta**: rotto, sporco | 11.50 s | L’uovo anteriore presenta guscio sfondato e residui di contenuto sulla superficie. |
| 199 | [figshare_IMG_20220818_154943.jpg](../../_pics/figshare_IMG_20220818_154943.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 10.83 s | Guscio con piccoli residui e macchie localizzate; evidente frattura nella zona centrale, senza perdita visibile di contenuto.; verità: cracked |
| 200 | [commons_24.jpg](../../_pics/commons_24.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 5.88 s | Guscio pulito, con una sottile crepa visibile nella parte centrale inferiore, senza fuoriuscita di contenuto. |

## Dettaglio completo per foto

Un blocco per foto analizzata, nello stesso ordine della tabella sopra: clicca sul titolo per aprirlo. L'origine di tutte le 200 foto del campione è anche in `_pics/manifest.json`. Il modello è generativo: non fornisce probabilità, ma una breve motivazione.

<details>
<summary><b>1. figshare_IMG_20220818_154808.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154808.jpg" alt="figshare_IMG_20220818_154808.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154808.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.59 s · token 2572 in / 58 out · costo $0.007008
- **Motivazione del modello**: Guscio integro con poche piccole macchie scure localizzate sul lato sinistro, senza crepe visibili.

</details>

<details>
<summary><b>2. commons_04.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_04.jpg" alt="commons_04.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:AraucanaEgg_vs_Brown_White.jpg](https://commons.wikimedia.org/wiki/File:AraucanaEgg_vs_Brown_White.jpg)
- **Licenza**: Public domain · **Autore**: Gmoose1
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1549x1550
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.70 s · token 3278 in / 85 out · costo $0.009043
- **Motivazione del modello**: I gusci appaiono puliti e integri, senza sporcizia significativa, crepe o perdite di contenuto visibili.

</details>

<details>
<summary><b>3. figshare_IMG_20220818_154045.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154045.jpg" alt="figshare_IMG_20220818_154045.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154045.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.01 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Piccole macchie e residui sul guscio; crepa sottile visibile sul lato sinistro, senza perdita di contenuto.

</details>

<details>
<summary><b>4. commons_03.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_03.jpg" alt="commons_03.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_3145g.jpg](https://commons.wikimedia.org/wiki/File:Eggs_3145g.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: StaraBlazkova
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1000x669
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.14 s · token 1203 in / 140 out · costo $0.004406
- **Motivazione del modello**: L'uovo in primo piano a destra presenta una sottile crepa nella parte superiore; non si osserva sporcizia evidente.

</details>

<details>
<summary><b>5. figshare_IMG_20220818_155841.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155841.jpg" alt="figshare_IMG_20220818_155841.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155841.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.13 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Guscio pulito con crepe ramificate ben visibili, senza pezzi mancanti né fuoriuscita di contenuto.

</details>

<details>
<summary><b>6. hf_sample47.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample47.jpg" alt="hf_sample47.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample47.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample47.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.74 s · token 2572 in / 103 out · costo $0.007458
- **Motivazione del modello**: L’uovo marrone a destra, penultimo in basso, presenta una crepa visibile; il guscio appare pulito.

</details>

<details>
<summary><b>7. figshare_IMG_20220818_155248.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155248.jpg" alt="figshare_IMG_20220818_155248.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155248.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.33 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Piccole macchie brunastre localizzate sul lato destro; guscio integro, senza crepe o perdite visibili.

</details>

<details>
<summary><b>8. commons_30.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_30.jpg" alt="commons_30.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_(8501854880).jpg](https://commons.wikimedia.org/wiki/File:Eggs_(8501854880).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: liz west from Boxborough, MA, USA
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1181
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.48 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Tutte le uova presentano gusci puliti e integri, senza sporcizia, crepe o perdite visibili.

</details>

<details>
<summary><b>9. figshare_IMG_20220818_155341.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155341.jpg" alt="figshare_IMG_20220818_155341.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155341.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.41 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Piccole macchie e residui sul lato destro del guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>10. commons_15.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_15.jpg" alt="commons_15.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Oeuf_de_poule.jpg](https://commons.wikimedia.org/wiki/File:Oeuf_de_poule.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Jeangagnon
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1198x1432
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.04 s · token 2449 in / 51 out · costo $0.006631
- **Motivazione del modello**: Guscio pulito e uniforme, senza sporcizia, crepe o fratture visibili.

</details>

<details>
<summary><b>11. figshare_IMG_20220818_153759.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153759.jpg" alt="figshare_IMG_20220818_153759.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153759.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.14 s · token 2572 in / 114 out · costo $0.007568
- **Motivazione del modello**: Guscio con poche piccole macchie e lievi aloni localizzati; nessuna crepa o rottura visibile.

</details>

<details>
<summary><b>12. hf_sample7.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample7.jpg" alt="hf_sample7.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample7.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample7.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.79 s · token 2572 in / 251 out · costo $0.008939
- **Motivazione del modello**: I gusci visibili sono puliti, con soli timbri di stampa, senza crepe, rotture o perdite evidenti.

</details>

<details>
<summary><b>13. figshare_IMG_20220818_160114.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160114.jpg" alt="figshare_IMG_20220818_160114.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160114.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.84 s · token 2572 in / 54 out · costo $0.006968
- **Motivazione del modello**: Guscio pulito con una crepa sottile visibile nella parte centrale inferiore, senza perdita di contenuto.

</details>

<details>
<summary><b>14. commons_36.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_36.jpg" alt="commons_36.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:FreeRangeEgg.jpg](https://commons.wikimedia.org/wiki/File:FreeRangeEgg.jpg)
- **Licenza**: CC BY-SA 3.0
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1000x825
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.92 s · token 1395 in / 53 out · costo $0.004016
- **Motivazione del modello**: Guscio pulito e integro, con soli timbri di stampa e nessuna crepa visibile.

</details>

<details>
<summary><b>15. figshare_IMG_20220818_155859.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155859.jpg" alt="figshare_IMG_20220818_155859.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155859.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.52 s · token 2572 in / 101 out · costo $0.007438
- **Motivazione del modello**: Piccolo alone brunastro sul guscio e crepe visibili nella parte inferiore, senza pezzi mancanti né fuoriuscite.

</details>

<details>
<summary><b>16. hf_sample3.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample3.jpg" alt="hf_sample3.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample3.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample3.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.06 s · token 2572 in / 92 out · costo $0.007348
- **Motivazione del modello**: L’uovo centrale presenta una piccola macchia giallastra sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>17. figshare_IMG_20220818_155422.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155422.jpg" alt="figshare_IMG_20220818_155422.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155422.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.69 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Piccole macchie brunastre sul lato sinistro e crepe ramificate nella zona centrale del guscio, senza perdite visibili.

</details>

<details>
<summary><b>18. commons_25.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_25.jpg" alt="commons_25.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:First_egg_(7680068562).jpg](https://commons.wikimedia.org/wiki/File:First_egg_(7680068562).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: normanack
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1549x1549
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.00 s · token 3278 in / 56 out · costo $0.008754
- **Motivazione del modello**: Guscio pulito con minuscoli puntini naturali, senza sporcizia, crepe o rotture visibili.

</details>

<details>
<summary><b>19. figshare_IMG_20220818_154854.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154854.jpg" alt="figshare_IMG_20220818_154854.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154854.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.79 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Residui localizzati nella parte inferiore del guscio e una crepa sottile visibile, senza pezzi mancanti.

</details>

<details>
<summary><b>20. hf_sample30.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample30.jpg" alt="hf_sample30.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample30.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample30.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.76 s · token 2572 in / 86 out · costo $0.007288
- **Motivazione del modello**: L’uovo marrone in basso presenta alcune macchie chiare e piccoli segni superficiali, senza crepe visibili.

</details>

<details>
<summary><b>21. figshare_IMG_20220818_154019.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154019.jpg" alt="figshare_IMG_20220818_154019.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154019.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.82 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Guscio integro con poche piccole macchie e lievi residui localizzati; nessuna crepa visibile.

</details>

<details>
<summary><b>22. hf_sample9.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample9.jpg" alt="hf_sample9.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample9.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample9.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.23 s · token 2572 in / 157 out · costo $0.007999
- **Motivazione del modello**: I gusci visibili sono puliti, con soli timbri di stampa, senza crepe, rotture o perdite evidenti.

</details>

<details>
<summary><b>23. figshare_IMG_20220818_154949.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154949.jpg" alt="figshare_IMG_20220818_154949.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154949.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.98 s · token 2572 in / 95 out · costo $0.007378
- **Motivazione del modello**: Piccoli residui e aloni sul lato sinistro; crepa evidente sul lato destro, senza perdita di contenuto.

</details>

<details>
<summary><b>24. commons_18.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_18.jpg" alt="commons_18.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Spiral_of_Brown_Eggs.jpg](https://commons.wikimedia.org/wiki/File:Spiral_of_Brown_Eggs.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Krugglesuvu
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1273x1554
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.89 s · token 2749 in / 131 out · costo $0.008181
- **Motivazione del modello**: Alcune uova presentano piccoli aloni e residui superficiali; non si vedono crepe o rotture.

</details>

<details>
<summary><b>25. figshare_IMG_20220818_155415.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155415.jpg" alt="figshare_IMG_20220818_155415.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155415.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.06 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Piccole macchie brunastre sul guscio e crepe ramificate visibili nella zona centrale, senza perdita di contenuto.

</details>

<details>
<summary><b>26. commons_23.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_23.jpg" alt="commons_23.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_(7177637421).jpg](https://commons.wikimedia.org/wiki/File:Eggs_(7177637421).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: James Bowe
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.05 s · token 2572 in / 190 out · costo $0.008329
- **Motivazione del modello**: Gusci puliti, con piccoli puntini naturali e senza crepe, rotture o perdite visibili.

</details>

<details>
<summary><b>27. figshare_IMG_20220818_155457.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155457.jpg" alt="figshare_IMG_20220818_155457.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155457.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.75 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: Guscio con una crepa visibile sul lato sinistro e piccole macchie brunastre nella parte inferiore.

</details>

<details>
<summary><b>28. hf_sample8.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample8.jpg" alt="hf_sample8.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample8.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample8.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.50 s · token 2572 in / 101 out · costo $0.007438
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o perdite; presenti soltanto timbri e minuscoli puntini.

</details>

<details>
<summary><b>29. figshare_IMG_20220818_154636.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154636.jpg" alt="figshare_IMG_20220818_154636.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154636.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.71 s · token 2572 in / 90 out · costo $0.007328
- **Motivazione del modello**: Piccoli residui giallastri sulla parte inferiore del guscio; nessuna crepa o rottura visibile.

</details>

<details>
<summary><b>30. hf_sample20.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample20.jpg" alt="hf_sample20.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample20.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample20.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.62 s · token 2572 in / 80 out · costo $0.007228
- **Motivazione del modello**: I gusci appaiono puliti e integri, senza crepe o residui visibili; presenti solo timbri e minuscoli puntini.

</details>

<details>
<summary><b>31. figshare_IMG_20220818_154528.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154528.jpg" alt="figshare_IMG_20220818_154528.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154528.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.79 s · token 2572 in / 60 out · costo $0.007029
- **Motivazione del modello**: Guscio pulito con minuscoli puntini ammessi; visibile una crepa sottile e irregolare, senza perdita di contenuto.

</details>

<details>
<summary><b>32. hf_sample34.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample34.jpg" alt="hf_sample34.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample34.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample34.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.37 s · token 2572 in / 164 out · costo $0.008068
- **Motivazione del modello**: L’uovo bianco centrale a destra presenta una sottile crepa e lievi segni grigiastri sul guscio.

</details>

<details>
<summary><b>33. figshare_IMG_20220818_160007.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_160007.jpg" alt="figshare_IMG_20220818_160007.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160007.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto, sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.98 s · token 2572 in / 79 out · costo $0.007219
- **Motivazione del modello**: Sporcizia evidente su una parte significativa del guscio, con zona sfondata e crepe circostanti.

</details>

<details>
<summary><b>34. commons_27.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_27.jpg" alt="commons_27.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Spotted_Brown_Chicken_Eggs_(5719609727).jpg](https://commons.wikimedia.org/wiki/File:Spotted_Brown_Chicken_Eggs_(5719609727).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: spiralmushroom
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1043
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.06 s · token 2337 in / 91 out · costo $0.006751
- **Motivazione del modello**: L'uovo in primo piano a sinistra presenta alcune macchie scure localizzate; non si vedono crepe o rotture.

</details>

<details>
<summary><b>35. figshare_IMG_20220818_154535.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154535.jpg" alt="figshare_IMG_20220818_154535.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154535.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.06 s · token 2572 in / 120 out · costo $0.007628
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa sulla superficie, senza perdita di contenuto.

</details>

<details>
<summary><b>36. hf_sample13.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample13.jpg" alt="hf_sample13.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample13.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample13.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.79 s · token 2572 in / 83 out · costo $0.007259
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o rotture; presenti solo timbri e minuscoli puntini.

</details>

<details>
<summary><b>37. figshare_IMG_20220818_155015.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155015.jpg" alt="figshare_IMG_20220818_155015.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155015.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.72 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Visibile una crepa sul lato sinistro del guscio e poche piccole macchie brunastre sul lato destro.

</details>

<details>
<summary><b>38. hf_sample46.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample46.jpg" alt="hf_sample46.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample46.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample46.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.32 s · token 2572 in / 124 out · costo $0.007668
- **Motivazione del modello**: L’uovo marrone in basso a destra presenta un piccolo segno scuro sul guscio, senza crepe visibili.

</details>

<details>
<summary><b>39. figshare_IMG_20220818_155401.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155401.jpg" alt="figshare_IMG_20220818_155401.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155401.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.57 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Piccole macchie brunastre e residui localizzati sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>40. commons_34.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_34.jpg" alt="commons_34.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_on_Table.jpg](https://commons.wikimedia.org/wiki/File:Egg_on_Table.jpg)
- **Licenza**: CC BY-SA 2.0 · **Autore**: Eric Petruno
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.93 s · token 2337 in / 58 out · costo $0.006421
- **Motivazione del modello**: Guscio pulito, senza macchie o residui visibili; nessuna crepa, frattura o perdita di contenuto.

</details>

<details>
<summary><b>41. figshare_IMG_20220818_155709.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155709.jpg" alt="figshare_IMG_20220818_155709.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155709.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.80 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Guscio pulito con una crepa sottile visibile sul lato destro, senza pezzi mancanti o fuoriuscite.

</details>

<details>
<summary><b>42. commons_32.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_32.jpg" alt="commons_32.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Tiny_treasure,_first_egg_(7680059460).jpg](https://commons.wikimedia.org/wiki/File:Tiny_treasure,_first_egg_(7680059460).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: normanack
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.16 s · token 2572 in / 55 out · costo $0.006979
- **Motivazione del modello**: Guscio pulito con minuscoli puntini naturali, senza crepe, fratture o perdite visibili.

</details>

<details>
<summary><b>43. figshare_IMG_20220818_155137.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155137.jpg" alt="figshare_IMG_20220818_155137.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155137.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.64 s · token 2572 in / 122 out · costo $0.007648
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa sulla superficie centrale, senza perdita di contenuto.

</details>

<details>
<summary><b>44. commons_42.jpg</b> · scarta: sporco</summary>

<img src="../../_pics/commons_42.jpg" alt="commons_42.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Bloody-egg.jpg](https://commons.wikimedia.org/wiki/File:Bloody-egg.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Maqi
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 600x902
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: scarta: sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.82 s · token 1058 in / 79 out · costo $0.003433
- **Motivazione del modello**: Il guscio presenta un'estesa copertura di sangue; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>45. figshare_IMG_20220818_155511.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155511.jpg" alt="figshare_IMG_20220818_155511.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155511.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.92 s · token 2572 in / 105 out · costo $0.007478
- **Motivazione del modello**: Visibile una sottile crepa sul lato destro del guscio e pochi piccoli residui brunastri.

</details>

<details>
<summary><b>46. commons_16.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_16.jpg" alt="commons_16.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_upright.jpg](https://commons.wikimedia.org/wiki/File:Egg_upright.jpg)
- **Licenza**: Public domain · **Autore**: Paolo Neo
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1491
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.38 s · token 3160 in / 56 out · costo $0.008459
- **Motivazione del modello**: Guscio pulito con minuscoli puntini naturali, senza sporcizia, crepe o rotture visibili.

</details>

<details>
<summary><b>47. figshare_IMG_20220818_154136.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154136.jpg" alt="figshare_IMG_20220818_154136.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154136.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.91 s · token 2572 in / 116 out · costo $0.007588
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa visibile nella parte inferiore sinistra, senza fuoriuscita di contenuto.

</details>

<details>
<summary><b>48. commons_19.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_19.jpg" alt="commons_19.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Fresh_Eggs_(Unsplash_fBturNUtd8).jpg](https://commons.wikimedia.org/wiki/File:Fresh_Eggs_(Unsplash_fBturNUtd8).jpg)
- **Licenza**: CC0 · **Autore**: Brina Blum brina_blum
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.11 s · token 2337 in / 59 out · costo $0.006431
- **Motivazione del modello**: I gusci visibili sono puliti, con minuscoli puntini naturali e senza crepe, fratture o perdite evidenti.

</details>

<details>
<summary><b>49. figshare_IMG_20220818_154759.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154759.jpg" alt="figshare_IMG_20220818_154759.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154759.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.49 s · token 2572 in / 180 out · costo $0.008228
- **Motivazione del modello**: Piccoli residui scuri localizzati e una sottile crepa visibile nella parte centrale inferiore del guscio.

</details>

<details>
<summary><b>50. commons_47.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_47.jpg" alt="commons_47.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B4-001.jpg](https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B4-001.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: OhWeh
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.25 s · token 2572 in / 133 out · costo $0.007758
- **Motivazione del modello**: Una piccola piuma aderisce al guscio; non sono visibili crepe, fratture o perdite di contenuto.

</details>

<details>
<summary><b>51. figshare_IMG_20220818_155540.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155540.jpg" alt="figshare_IMG_20220818_155540.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155540.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.03 s · token 2572 in / 94 out · costo $0.007369
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; evidente crepa ramificata, senza pezzi mancanti né fuoriuscita di contenuto.

</details>

<details>
<summary><b>52. hf_sample17.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample17.jpg" alt="hf_sample17.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample17.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample17.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.17 s · token 2572 in / 87 out · costo $0.007299
- **Motivazione del modello**: L’uovo in basso a sinistra presenta piccoli residui e aloni sul guscio, senza crepe visibili.

</details>

<details>
<summary><b>53. figshare_IMG_20220818_154226.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154226.jpg" alt="figshare_IMG_20220818_154226.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154226.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.12 s · token 2572 in / 101 out · costo $0.007438
- **Motivazione del modello**: Visibile una sottile crepa sul guscio, con poche piccole macchie e residui superficiali.

</details>

<details>
<summary><b>54. hf_sample33.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample33.jpg" alt="hf_sample33.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample33.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample33.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.35 s · token 2572 in / 129 out · costo $0.007718
- **Motivazione del modello**: L’uovo bianco nella seconda fila a destra presenta una sottile crepa visibile, senza sporco evidente.

</details>

<details>
<summary><b>55. figshare_IMG_20220818_155846.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155846.jpg" alt="figshare_IMG_20220818_155846.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155846.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.91 s · token 2572 in / 55 out · costo $0.006979
- **Motivazione del modello**: Guscio pulito con crepe evidenti nella parte superiore e centrale, senza pezzi mancanti né fuoriuscite.

</details>

<details>
<summary><b>56. commons_11.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_11.jpg" alt="commons_11.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_on_white_background.jpg](https://commons.wikimedia.org/wiki/File:Egg_on_white_background.jpg)
- **Licenza**: Public domain · **Autore**: Paolo Neo
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.78 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Guscio pulito e uniforme, senza sporcizia, crepe, fratture o perdite di contenuto visibili.

</details>

<details>
<summary><b>57. figshare_IMG_20220818_153842.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153842.jpg" alt="figshare_IMG_20220818_153842.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153842.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.59 s · token 2572 in / 84 out · costo $0.007268
- **Motivazione del modello**: Guscio integro, con poche piccole macchie e residui brunastri sulla superficie.

</details>

<details>
<summary><b>58. commons_48.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_48.jpg" alt="commons_48.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B16-001.jpg](https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B16-001.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: OhWeh
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.23 s · token 2572 in / 85 out · costo $0.007279
- **Motivazione del modello**: Una piccola piuma aderisce al guscio; non sono visibili crepe, fratture o perdite di contenuto.

</details>

<details>
<summary><b>59. figshare_IMG_20220818_160129.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160129.jpg" alt="figshare_IMG_20220818_160129.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160129.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.20 s · token 2572 in / 91 out · costo $0.007339
- **Motivazione del modello**: Guscio pulito, con una sottile crepa visibile nella parte inferiore destra, senza perdita di contenuto.

</details>

<details>
<summary><b>60. hf_sample2.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample2.jpg" alt="hf_sample2.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample2.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample2.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.63 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: L'uovo nella terza fila a destra presenta piccoli residui marroni sul guscio, senza crepe visibili.

</details>

<details>
<summary><b>61. figshare_IMG_20220818_155851.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155851.jpg" alt="figshare_IMG_20220818_155851.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155851.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.78 s · token 2572 in / 86 out · costo $0.007288
- **Motivazione del modello**: Guscio pulito, con una sottile crepa visibile nella parte superiore centrale, senza perdita di contenuto.

</details>

<details>
<summary><b>62. hf_sample29.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample29.jpg" alt="hf_sample29.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample29.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample29.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.55 s · token 2572 in / 103 out · costo $0.007458
- **Motivazione del modello**: L'uovo marrone in basso a destra presenta un piccolo residuo chiaro sul guscio; non sono visibili crepe.

</details>

<details>
<summary><b>63. figshare_IMG_20220818_154436.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154436.jpg" alt="figshare_IMG_20220818_154436.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154436.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.90 s · token 2572 in / 54 out · costo $0.006968
- **Motivazione del modello**: Guscio pulito con una sottile crepa visibile nella parte superiore, senza fuoriuscita di contenuto.

</details>

<details>
<summary><b>64. hf_sample37.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample37.jpg" alt="hf_sample37.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample37.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample37.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.02 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: Il secondo uovo da sinistra nella fila superiore presenta una crepa visibile nella parte inferiore del guscio, altrimenti pulito.

</details>

<details>
<summary><b>65. figshare_IMG_20220818_154051.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154051.jpg" alt="figshare_IMG_20220818_154051.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154051.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.54 s · token 2572 in / 88 out · costo $0.007308
- **Motivazione del modello**: Piccole macchie e residui sul guscio; visibile una crepa sottile e ramificata, senza perdita di contenuto.

</details>

<details>
<summary><b>66. hf_sample40.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample40.jpg" alt="hf_sample40.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample40.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample40.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 13.65 s · token 2572 in / 200 out · costo $0.008429
- **Motivazione del modello**: L’uovo nella seconda fila a destra presenta una sottile crepa sul guscio e piccole macchie superficiali.

</details>

<details>
<summary><b>67. figshare_IMG_20220818_155910.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155910.jpg" alt="figshare_IMG_20220818_155910.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155910.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.15 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Guscio pulito con una lunga crepa visibile; nessun pezzo mancante o fuoriuscita di contenuto.

</details>

<details>
<summary><b>68. hf_sample41.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample41.jpg" alt="hf_sample41.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample41.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample41.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 13.38 s · token 2572 in / 195 out · costo $0.008379
- **Motivazione del modello**: L'uovo a destra nella quarta fila presenta una sottile frattura sul bordo superiore sinistro; guscio pulito.

</details>

<details>
<summary><b>69. figshare_IMG_20220818_154057.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154057.jpg" alt="figshare_IMG_20220818_154057.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154057.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.77 s · token 2572 in / 58 out · costo $0.007008
- **Motivazione del modello**: Guscio con poche macchie e residui superficiali; evidente crepa orizzontale, senza perdita di contenuto.

</details>

<details>
<summary><b>70. hf_sample43.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample43.jpg" alt="hf_sample43.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample43.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample43.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.79 s · token 2572 in / 156 out · costo $0.007989
- **Motivazione del modello**: L'uovo bianco nella seconda fila a sinistra presenta crepe visibili sul lato destro, senza sporcizia evidente.

</details>

<details>
<summary><b>71. figshare_IMG_20220818_154444.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154444.jpg" alt="figshare_IMG_20220818_154444.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154444.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.38 s · token 2572 in / 86 out · costo $0.007288
- **Motivazione del modello**: Piccoli aloni e residui sul guscio; crepe ramificate visibili nella parte inferiore, senza perdita di contenuto.

</details>

<details>
<summary><b>72. commons_20.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_20.jpg" alt="commons_20.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Different_colored_chicken_eggs-01ASD.jpg](https://commons.wikimedia.org/wiki/File:Different_colored_chicken_eggs-01ASD.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Asurnipal
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1567x1532
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 13.15 s · token 3219 in / 83 out · costo $0.008876
- **Motivazione del modello**: Gusci puliti con soli minuscoli puntini; nessuna crepa, frattura o perdita di contenuto visibile.

</details>

<details>
<summary><b>73. figshare_IMG_20220818_155948.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_155948.jpg" alt="figshare_IMG_20220818_155948.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155948.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto, sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.13 s · token 2572 in / 80 out · costo $0.007228
- **Motivazione del modello**: Guscio sfondato con porzione mancante, lunga frattura e macchie di sporco diffuse su una parte significativa della superficie.

</details>

<details>
<summary><b>74. hf_sample11.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample11.jpg" alt="hf_sample11.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample11.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample11.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.47 s · token 2572 in / 92 out · costo $0.007348
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o rotture; presenti solo timbri e minuscoli puntini.

</details>

<details>
<summary><b>75. figshare_IMG_20220818_155606.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155606.jpg" alt="figshare_IMG_20220818_155606.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155606.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.17 s · token 2572 in / 136 out · costo $0.007789
- **Motivazione del modello**: Visibili fratture ramificate nella zona centrale del guscio e poche piccole macchie brunastre sulla superficie.

</details>

<details>
<summary><b>76. commons_49.jpg</b> · scarta: rotto</summary>

<img src="../../_pics/commons_49.jpg" alt="commons_49.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Strange_brown_egg.jpg](https://commons.wikimedia.org/wiki/File:Strange_brown_egg.jpg)
- **Licenza**: CC0 · **Autore**: Smallman12q
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1401
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 12.26 s · token 2984 in / 100 out · costo $0.008459
- **Motivazione del modello**: Guscio sfondato nella parte inferiore, con frammenti sollevati e residui localizzati attorno alla rottura.

</details>

<details>
<summary><b>77. figshare_IMG_20220818_154914.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154914.jpg" alt="figshare_IMG_20220818_154914.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154914.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.57 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Residui e macchie localizzati sul guscio; crepe sottili visibili nella zona centrale, senza perdita di contenuto.

</details>

<details>
<summary><b>78. hf_sample22.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample22.jpg" alt="hf_sample22.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample22.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample22.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.32 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: L'uovo centrale presenta un piccolo residuo brunastro sul guscio; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>79. figshare_IMG_20220818_155240.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155240.jpg" alt="figshare_IMG_20220818_155240.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155240.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.09 s · token 2572 in / 88 out · costo $0.007308
- **Motivazione del modello**: Piccole macchie brunastre sul lato destro e una sottile crepa diagonale nella zona centrale del guscio.

</details>

<details>
<summary><b>80. commons_06.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_06.jpg" alt="commons_06.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Brown_chicken_eggs.jpg](https://commons.wikimedia.org/wiki/File:Brown_chicken_eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Piasoft
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1041
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.99 s · token 2337 in / 56 out · costo $0.006401
- **Motivazione del modello**: Entrambe le uova hanno gusci puliti e integri, senza sporco, crepe o rotture visibili.

</details>

<details>
<summary><b>81. figshare_IMG_20220818_160039.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160039.jpg" alt="figshare_IMG_20220818_160039.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160039.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.04 s · token 2572 in / 87 out · costo $0.007299
- **Motivazione del modello**: Guscio con poche piccole macchie e fratture ramificate visibili nella zona centrale, senza fuoriuscita di contenuto.

</details>

<details>
<summary><b>82. hf_sample42.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample42.jpg" alt="hf_sample42.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample42.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample42.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 13.78 s · token 2572 in / 131 out · costo $0.007738
- **Motivazione del modello**: L’uovo in basso a sinistra presenta una sottile crepa sul lato destro; non si osserva sporcizia evidente.

</details>

<details>
<summary><b>83. figshare_IMG_20220818_154715.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154715.jpg" alt="figshare_IMG_20220818_154715.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154715.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 15.25 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Poche piccole macchie sul guscio e crepe visibili nella zona centrale inferiore, senza pezzi mancanti.

</details>

<details>
<summary><b>84. hf_sample12.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample12.jpg" alt="hf_sample12.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample12.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample12.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.88 s · token 2572 in / 85 out · costo $0.007279
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o residui evidenti; presenti solo timbri e minuscoli puntini.

</details>

<details>
<summary><b>85. figshare_IMG_20220818_154238.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154238.jpg" alt="figshare_IMG_20220818_154238.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154238.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.44 s · token 2572 in / 95 out · costo $0.007378
- **Motivazione del modello**: Piccole macchie brunastre e lievi aloni su porzioni limitate del guscio; nessuna crepa o rottura visibile.

</details>

<details>
<summary><b>86. hf_sample16.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample16.jpg" alt="hf_sample16.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample16.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample16.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.86 s · token 2572 in / 117 out · costo $0.007599
- **Motivazione del modello**: L'uovo in basso presenta un piccolo alone sul guscio vicino al timbro; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>87. figshare_IMG_20220818_154413.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154413.jpg" alt="figshare_IMG_20220818_154413.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154413.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.12 s · token 2572 in / 92 out · costo $0.007348
- **Motivazione del modello**: Guscio pulito con crepe ramificate visibili nella zona centrale, senza pezzi mancanti né fuoriuscite di contenuto.

</details>

<details>
<summary><b>88. commons_14.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_14.jpg" alt="commons_14.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Deux_oeufs_bruns.jpg](https://commons.wikimedia.org/wiki/File:Deux_oeufs_bruns.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Jeangagnon
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.20 s · token 2572 in / 98 out · costo $0.007409
- **Motivazione del modello**: Entrambi i gusci sono integri e puliti, con solo minuscoli puntini e nessuna crepa visibile.

</details>

<details>
<summary><b>89. figshare_IMG_20220818_155559.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155559.jpg" alt="figshare_IMG_20220818_155559.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155559.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 17.16 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Guscio con crepe ramificate visibili e poche piccole macchie giallastre; nessuna perdita di contenuto.

</details>

<details>
<summary><b>90. hf_sample1.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample1.jpg" alt="hf_sample1.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample1.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample1.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.68 s · token 2572 in / 130 out · costo $0.007729
- **Motivazione del modello**: L'uovo nella terza fila a destra presenta piccole macchie marroni sul guscio, senza crepe visibili.

</details>

<details>
<summary><b>91. figshare_IMG_20220818_155517.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155517.jpg" alt="figshare_IMG_20220818_155517.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155517.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 16.26 s · token 2572 in / 87 out · costo $0.007299
- **Motivazione del modello**: Piccole macchie giallastre sul guscio e una sottile crepa visibile nella parte centrale inferiore, senza fuoriuscite.

</details>

<details>
<summary><b>92. hf_sample5.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample5.jpg" alt="hf_sample5.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample5.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample5.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.81 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza sporco né crepe; presente solo un timbro consentito.

</details>

<details>
<summary><b>93. figshare_IMG_20220818_154429.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154429.jpg" alt="figshare_IMG_20220818_154429.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154429.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.35 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Guscio pulito con crepe visibili nella zona centrale, senza pezzi mancanti né fuoriuscite di contenuto.

</details>

<details>
<summary><b>94. commons_13.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_13.jpg" alt="commons_13.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:2_eggs.JPG](https://commons.wikimedia.org/wiki/File:2_eggs.JPG)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Hannahdownes
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 14.14 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Entrambe le uova presentano gusci puliti e integri, senza sporco, crepe o rotture visibili.

</details>

<details>
<summary><b>95. figshare_IMG_20220818_160049.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160049.jpg" alt="figshare_IMG_20220818_160049.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160049.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.99 s · token 2572 in / 96 out · costo $0.007389
- **Motivazione del modello**: Piccole macchie giallastre sul guscio e crepe visibili nella zona centrale inferiore, senza fuoriuscita di contenuto.

</details>

<details>
<summary><b>96. commons_17.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_17.jpg" alt="commons_17.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Three_chicken_eggs.jpg](https://commons.wikimedia.org/wiki/File:Three_chicken_eggs.jpg)
- **Licenza**: CC0 · **Autore**: www.Pixel.la Free Stock Photos
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.51 s · token 2337 in / 60 out · costo $0.006441
- **Motivazione del modello**: I gusci appaiono puliti, con soli minuscoli puntini naturali, senza crepe, fratture o perdite visibili.

</details>

<details>
<summary><b>97. figshare_IMG_20220818_155353.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155353.jpg" alt="figshare_IMG_20220818_155353.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155353.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.23 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: Piccole macchie brunastre e residui localizzati sul guscio; nessuna crepa o rottura visibile.

</details>

<details>
<summary><b>98. hf_sample35.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample35.jpg" alt="hf_sample35.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample35.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample35.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 13.68 s · token 2572 in / 155 out · costo $0.007978
- **Motivazione del modello**: L'uovo bianco superiore presenta una sottile crepa sul lato inferiore sinistro; non si osserva sporcizia significativa.

</details>

<details>
<summary><b>99. figshare_IMG_20220818_154557.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154557.jpg" alt="figshare_IMG_20220818_154557.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154557.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.69 s · token 2572 in / 101 out · costo $0.007438
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa irregolare sul lato sinistro, senza perdita di contenuto.

</details>

<details>
<summary><b>100. hf_sample27.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample27.jpg" alt="hf_sample27.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample27.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample27.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.11 s · token 2572 in / 143 out · costo $0.007858
- **Motivazione del modello**: L'uovo in basso a sinistra presenta un piccolo residuo biancastro sul guscio; non sono visibili crepe.

</details>

<details>
<summary><b>101. figshare_IMG_20220818_153953.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153953.jpg" alt="figshare_IMG_20220818_153953.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153953.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.01 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Guscio integro con pochi piccoli residui e macchie brunastre localizzate, senza crepe visibili.

</details>

<details>
<summary><b>102. hf_sample14.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample14.jpg" alt="hf_sample14.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample14.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample14.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.31 s · token 2572 in / 60 out · costo $0.007029
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o residui; presenti soltanto timbri e minuscoli puntini.

</details>

<details>
<summary><b>103. figshare_IMG_20220818_160014.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_160014.jpg" alt="figshare_IMG_20220818_160014.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160014.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto, sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 12.41 s · token 2572 in / 155 out · costo $0.007978
- **Motivazione del modello**: Macchie e residui diffusi sul guscio; zona sfondata nella parte superiore con una crepa che si estende lateralmente.

</details>

<details>
<summary><b>104. hf_sample19.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample19.jpg" alt="hf_sample19.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample19.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample19.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.87 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: L'uovo superiore presenta piccoli aloni e residui sul guscio; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>105. figshare_IMG_20220818_154113.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154113.jpg" alt="figshare_IMG_20220818_154113.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154113.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.10 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Crepa sottile visibile nella parte superiore destra del guscio; piccoli residui e aloni sul lato sinistro.

</details>

<details>
<summary><b>106. hf_sample18.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample18.jpg" alt="hf_sample18.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample18.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample18.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.44 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: L’uovo in alto a sinistra presenta piccoli residui sul guscio vicino al timbro; non sono visibili crepe.

</details>

<details>
<summary><b>107. figshare_IMG_20220818_160123.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160123.jpg" alt="figshare_IMG_20220818_160123.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160123.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.63 s · token 2572 in / 79 out · costo $0.007219
- **Motivazione del modello**: Crepa sottile ben visibile al centro del guscio, con piccoli residui localizzati; nessuna perdita di contenuto.

</details>

<details>
<summary><b>108. hf_sample26.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample26.jpg" alt="hf_sample26.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample26.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample26.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.78 s · token 2572 in / 93 out · costo $0.007358
- **Motivazione del modello**: Piccole macchie e residui localizzati sul guscio; nessuna crepa o perdita di contenuto visibile.

</details>

<details>
<summary><b>109. figshare_IMG_20220818_155430.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155430.jpg" alt="figshare_IMG_20220818_155430.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155430.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.88 s · token 2572 in / 88 out · costo $0.007308
- **Motivazione del modello**: Crepe ramificate visibili al centro del guscio e piccole macchie brunastre sul lato destro, senza fuoriuscita di contenuto.

</details>

<details>
<summary><b>110. hf_sample32.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample32.jpg" alt="hf_sample32.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample32.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample32.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.22 s · token 2572 in / 86 out · costo $0.007288
- **Motivazione del modello**: L’uovo in basso a destra presenta piccoli residui e macchie superficiali; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>111. figshare_IMG_20220818_154419.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154419.jpg" alt="figshare_IMG_20220818_154419.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154419.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.15 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Guscio pulito con crepe ramificate visibili nella zona centrale inferiore, senza pezzi mancanti né fuoriuscite.

</details>

<details>
<summary><b>112. hf_sample25.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample25.jpg" alt="hf_sample25.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample25.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample25.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.93 s · token 2572 in / 108 out · costo $0.007509
- **Motivazione del modello**: Piccoli residui e macchie localizzate su alcuni gusci; nessuna crepa o rottura visibile.

</details>

<details>
<summary><b>113. figshare_IMG_20220818_160028.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160028.jpg" alt="figshare_IMG_20220818_160028.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160028.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.31 s · token 2572 in / 118 out · costo $0.007608
- **Motivazione del modello**: Guscio con crepe ramificate evidenti e poche piccole macchie superficiali, senza perdita visibile di contenuto.

</details>

<details>
<summary><b>114. commons_01.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_01.jpg" alt="commons_01.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Brown_egg.jpg](https://commons.wikimedia.org/wiki/File:Brown_egg.jpg)
- **Licenza**: CC BY-SA 1.0 · **Autore**: George Shuklin
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1088
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.34 s · token 2396 in / 81 out · costo $0.006798
- **Motivazione del modello**: Guscio integro, con un piccolo residuo brunastro visibile sopra il timbro.

</details>

<details>
<summary><b>115. figshare_IMG_20220818_160055.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160055.jpg" alt="figshare_IMG_20220818_160055.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160055.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.56 s · token 2572 in / 80 out · costo $0.007228
- **Motivazione del modello**: Guscio con crepe sottili ramificate e pochi piccoli residui giallastri; nessuna perdita di contenuto visibile.

</details>

<details>
<summary><b>116. hf_sample10.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample10.jpg" alt="hf_sample10.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample10.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample10.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.14 s · token 2572 in / 90 out · costo $0.007328
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o residui; presenti soltanto timbri di stampa.

</details>

<details>
<summary><b>117. figshare_IMG_20220818_155905.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155905.jpg" alt="figshare_IMG_20220818_155905.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155905.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.05 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: Guscio pulito con una crepa ramificata evidente, senza pezzi mancanti né fuoriuscita di contenuto.

</details>

<details>
<summary><b>118. commons_39.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_39.jpg" alt="commons_39.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huehnereier_2989.jpg](https://commons.wikimedia.org/wiki/File:Huehnereier_2989.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: Rüdiger Wölk       This photo was taken by Rüdiger Wölk.  Please credit this photo Rüdiger Wölk, Münster.    View all photos (large page) of Rüdiger Wölk  I would also appreciate an email to rudiger.wolk@gmail.com with details of use. Für Hinweise auf Veröffentlichungen (rudiger.wolk@gmail.com) oder Belegexemplare bin ich Ihnen dankbar.
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.85 s · token 2337 in / 199 out · costo $0.007831
- **Motivazione del modello**: Visibile una sottile crepa sull’uovo a destra; presenti piccole macchie su alcuni gusci.

</details>

<details>
<summary><b>119. figshare_IMG_20220818_154319.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154319.jpg" alt="figshare_IMG_20220818_154319.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154319.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.17 s · token 2572 in / 75 out · costo $0.007178
- **Motivazione del modello**: Guscio pulito con minuscoli puntini ammessi; visibile una lunga crepa sottile, senza perdita di contenuto.

</details>

<details>
<summary><b>120. commons_37.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_37.jpg" alt="commons_37.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown.JPG](https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown.JPG)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Lanntaron
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.45 s · token 2572 in / 58 out · costo $0.007008
- **Motivazione del modello**: Visibili alcune macchie arancioni su piccole porzioni dei gusci, senza crepe o rotture evidenti.

</details>

<details>
<summary><b>121. figshare_IMG_20220818_160044.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160044.jpg" alt="figshare_IMG_20220818_160044.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160044.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.38 s · token 2572 in / 92 out · costo $0.007348
- **Motivazione del modello**: Guscio con fratture ramificate evidenti nella zona centrale e poche piccole macchie brunastre nella parte inferiore.

</details>

<details>
<summary><b>122. hf_sample24.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample24.jpg" alt="hf_sample24.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample24.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample24.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.39 s · token 2572 in / 113 out · costo $0.007559
- **Motivazione del modello**: Piccoli residui chiari sul guscio dell’uovo centrale superiore; nessuna crepa o fuoriuscita visibile.

</details>

<details>
<summary><b>123. figshare_IMG_20220818_155030.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155030.jpg" alt="figshare_IMG_20220818_155030.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155030.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.97 s · token 2572 in / 127 out · costo $0.007698
- **Motivazione del modello**: Pochi piccoli aloni e residui sul guscio, soprattutto a destra; nessuna crepa o perdita visibile.

</details>

<details>
<summary><b>124. hf_sample31.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample31.jpg" alt="hf_sample31.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample31.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample31.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.74 s · token 2572 in / 116 out · costo $0.007588
- **Motivazione del modello**: L’uovo marrone in basso presenta piccole macchie e residui superficiali; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>125. figshare_IMG_20220818_155717.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155717.jpg" alt="figshare_IMG_20220818_155717.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155717.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.42 s · token 2572 in / 100 out · costo $0.007429
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa nella parte inferiore destra.

</details>

<details>
<summary><b>126. hf_sample48.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample48.jpg" alt="hf_sample48.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample48.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample48.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.78 s · token 2572 in / 99 out · costo $0.007418
- **Motivazione del modello**: L’uovo marrone a destra, penultimo dal basso, presenta una crepa visibile; il guscio è pulito e senza perdite.

</details>

<details>
<summary><b>127. figshare_IMG_20220818_154752.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154752.jpg" alt="figshare_IMG_20220818_154752.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154752.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.32 s · token 2572 in / 88 out · costo $0.007308
- **Motivazione del modello**: Piccole macchie scure localizzate e una sottile crepa visibile nella zona centrale sinistra del guscio.

</details>

<details>
<summary><b>128. hf_sample23.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample23.jpg" alt="hf_sample23.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample23.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample23.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.99 s · token 2572 in / 106 out · costo $0.007489
- **Motivazione del modello**: L'uovo in alto a destra presenta piccole macchie scure sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>129. figshare_IMG_20220818_155804.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155804.jpg" alt="figshare_IMG_20220818_155804.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155804.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.62 s · token 2572 in / 85 out · costo $0.007279
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa sul lato sinistro, senza perdita di contenuto.

</details>

<details>
<summary><b>130. commons_10.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_10.jpg" alt="commons_10.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown_(6).JPG](https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown_(6).JPG)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Lanntaron
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.30 s · token 2572 in / 91 out · costo $0.007339
- **Motivazione del modello**: L'uovo a sinistra presenta una piccola macchia biancastra sul guscio; non si vedono crepe o rotture.

</details>

<details>
<summary><b>131. figshare_IMG_20220818_155611.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155611.jpg" alt="figshare_IMG_20220818_155611.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155611.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.84 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: Crepe ramificate visibili sul guscio, senza perdita di contenuto; piccole macchie brunastre nella parte inferiore.

</details>

<details>
<summary><b>132. hf_sample38.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample38.jpg" alt="hf_sample38.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample38.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample38.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.25 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: L’uovo in basso a destra presenta piccoli residui e macchie sul guscio, senza crepe visibili.

</details>

<details>
<summary><b>133. figshare_IMG_20220818_155724.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155724.jpg" alt="figshare_IMG_20220818_155724.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155724.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.74 s · token 2572 in / 124 out · costo $0.007668
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa sul lato destro.

</details>

<details>
<summary><b>134. commons_46.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_46.jpg" alt="commons_46.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Cracked_(85516059).jpeg](https://commons.wikimedia.org/wiki/File:Cracked_(85516059).jpeg)
- **Licenza**: CC BY 3.0 · **Autore**: Cyd Haselton
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1041
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: rotto (`broken`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.09 s · token 2337 in / 95 out · costo $0.006791
- **Motivazione del modello**: Visibile solo un guscio sfondato e frammentato, senza sporcizia evidente; nessun uovo intero.

</details>

<details>
<summary><b>135. figshare_IMG_20220818_154818.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154818.jpg" alt="figshare_IMG_20220818_154818.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154818.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.46 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Piccole macchie brunastre localizzate sul guscio, senza crepe, fratture o perdite visibili.

</details>

<details>
<summary><b>136. hf_sample39.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample39.jpg" alt="hf_sample39.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample39.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample39.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.67 s · token 2572 in / 71 out · costo $0.007138
- **Motivazione del modello**: L’uovo in basso a destra presenta piccoli residui e macchie sul guscio, senza crepe visibili.

</details>

<details>
<summary><b>137. figshare_IMG_20220818_154103.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154103.jpg" alt="figshare_IMG_20220818_154103.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154103.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.52 s · token 2572 in / 87 out · costo $0.007299
- **Motivazione del modello**: Guscio con poche piccole macchie brunastre e una lunga frattura visibile, senza perdita di contenuto.

</details>

<details>
<summary><b>138. hf_sample50.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample50.jpg" alt="hf_sample50.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample50.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample50.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 10.98 s · token 2572 in / 269 out · costo $0.009118
- **Motivazione del modello**: L’uovo a sinistra nella seconda fila presenta una sottile crepa e piccoli residui superficiali.

</details>

<details>
<summary><b>139. figshare_IMG_20220818_155617.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155617.jpg" alt="figshare_IMG_20220818_155617.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155617.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.54 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Piccole macchie brunastre sul guscio e crepe ramificate visibili nella zona centrale inferiore, senza perdita di contenuto.

</details>

<details>
<summary><b>140. commons_45.jpg</b> · scarta: rotto</summary>

<img src="../../_pics/commons_45.jpg" alt="commons_45.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggshell_001.jpg](https://commons.wikimedia.org/wiki/File:Eggshell_001.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: H. Zell
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.94 s · token 2572 in / 80 out · costo $0.007228
- **Motivazione del modello**: È presente un uovo intero, ma i gusci in primo piano sono rotti, con ampie parti mancanti e senza sporcizia.

</details>

<details>
<summary><b>141. figshare_IMG_20220818_154959.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154959.jpg" alt="figshare_IMG_20220818_154959.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154959.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.33 s · token 2572 in / 53 out · costo $0.006959
- **Motivazione del modello**: Crepa evidente sulla parte centrale del guscio, con piccole macchie brunastre sul lato destro.

</details>

<details>
<summary><b>142. commons_26.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_26.jpg" alt="commons_26.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Just_lying_there_being_pretty_(4301382316).jpg](https://commons.wikimedia.org/wiki/File:Just_lying_there_being_pretty_(4301382316).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: storebukkebruse
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 10.37 s · token 2572 in / 132 out · costo $0.007749
- **Motivazione del modello**: Gusci integri e puliti, con minuscoli puntini superficiali; nessuna crepa o perdita di contenuto visibile.

</details>

<details>
<summary><b>143. figshare_IMG_20220818_153857.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153857.jpg" alt="figshare_IMG_20220818_153857.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153857.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.26 s · token 2572 in / 54 out · costo $0.006968
- **Motivazione del modello**: Poche piccole macchie e residui sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>144. commons_43.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_43.jpg" alt="commons_43.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Broken_egg_orange.jpg](https://commons.wikimedia.org/wiki/File:Broken_egg_orange.jpg)
- **Licenza**: CC BY 3.0 · **Autore**: Goldmund100
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1490
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: rotto (`broken`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.62 s · token 3160 in / 110 out · costo $0.008998
- **Motivazione del modello**: Visibili solo frammenti di guscio senza sporcizia evidente; uovo rotto con contenuto fuoriuscito.

</details>

<details>
<summary><b>145. figshare_IMG_20220818_154312.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154312.jpg" alt="figshare_IMG_20220818_154312.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154312.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.81 s · token 2572 in / 78 out · costo $0.007208
- **Motivazione del modello**: Guscio pulito con una frattura irregolare visibile nella zona centrale, senza perdita di contenuto.

</details>

<details>
<summary><b>146. commons_08.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_08.jpg" alt="commons_08.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Giriraja_eggs.jpg](https://commons.wikimedia.org/wiki/File:Giriraja_eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Netha Hussain
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.96 s · token 2572 in / 99 out · costo $0.007418
- **Motivazione del modello**: Piccoli residui scuri localizzati su alcuni gusci; nessuna crepa, frattura o perdita di contenuto visibile.

</details>

<details>
<summary><b>147. figshare_IMG_20220818_154335.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154335.jpg" alt="figshare_IMG_20220818_154335.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154335.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.22 s · token 2572 in / 54 out · costo $0.006968
- **Motivazione del modello**: Visibile una crepa sottile nella parte superiore del guscio e lievi residui sul lato destro.

</details>

<details>
<summary><b>148. hf_sample15.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample15.jpg" alt="hf_sample15.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample15.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample15.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.93 s · token 2572 in / 93 out · costo $0.007358
- **Motivazione del modello**: L’uovo in basso a sinistra presenta un piccolo alone beige sul guscio; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>149. figshare_IMG_20220818_155547.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155547.jpg" alt="figshare_IMG_20220818_155547.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155547.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.94 s · token 2572 in / 78 out · costo $0.007208
- **Motivazione del modello**: Guscio con piccole macchie e una crepa ramificata evidente, senza pezzi mancanti né fuoriuscite visibili.

</details>

<details>
<summary><b>150. commons_12.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_12.jpg" alt="commons_12.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_egg.jpg](https://commons.wikimedia.org/wiki/File:Chicken_egg.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Javier8aflores
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1200x900
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.74 s · token 1719 in / 50 out · costo $0.004796
- **Motivazione del modello**: Guscio pulito e uniforme, senza macchie, crepe o rotture visibili.

</details>

<details>
<summary><b>151. figshare_IMG_20220818_155047.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155047.jpg" alt="figshare_IMG_20220818_155047.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155047.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.10 s · token 2572 in / 120 out · costo $0.007628
- **Motivazione del modello**: Visibile una crepa sul lato sinistro del guscio e poche piccole macchie superficiali; nessuna fuoriuscita di contenuto.

</details>

<details>
<summary><b>152. commons_31.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_31.jpg" alt="commons_31.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_-_Home_Grown_(or_laid)_(7147848749).jpg](https://commons.wikimedia.org/wiki/File:Eggs_-_Home_Grown_(or_laid)_(7147848749).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: craigles75
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.54 s · token 2337 in / 85 out · costo $0.006691
- **Motivazione del modello**: L'uovo posteriore destro presenta alcune macchie scure localizzate; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>153. figshare_IMG_20220818_155700.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155700.jpg" alt="figshare_IMG_20220818_155700.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155700.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.06 s · token 2572 in / 79 out · costo $0.007219
- **Motivazione del modello**: Visibili una sottile crepa sul lato destro e piccoli residui giallastri sulla superficie del guscio.

</details>

<details>
<summary><b>154. hf_sample44.jpg</b> · scarta: sporco</summary>

<img src="../../_pics/hf_sample44.jpg" alt="hf_sample44.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample44.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample44.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: scarta: sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.46 s · token 2572 in / 190 out · costo $0.008329
- **Motivazione del modello**: L’uovo nella terza fila a sinistra presenta ampie macchie grigiastre sul guscio, senza crepe evidenti.

</details>

<details>
<summary><b>155. figshare_IMG_20220818_154613.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154613.jpg" alt="figshare_IMG_20220818_154613.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154613.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.28 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: Guscio pulito con minuscoli puntini ammessi; visibile una crepa irregolare sulla superficie, senza perdita di contenuto.

</details>

<details>
<summary><b>156. commons_38.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_38.jpg" alt="commons_38.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Ei01.jpg](https://commons.wikimedia.org/wiki/File:Ei01.jpg)
- **Licenza**: Public domain · **Autore**: No machine-readable author provided. Acf assumed (based on copyright claims).
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 955x858
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.14 s · token 1369 in / 77 out · costo $0.004191
- **Motivazione del modello**: Guscio integro con pochi piccoli aloni e macchie superficiali; nessuna crepa visibile.

</details>

<details>
<summary><b>157. figshare_IMG_20220818_155436.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155436.jpg" alt="figshare_IMG_20220818_155436.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155436.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.95 s · token 2572 in / 61 out · costo $0.007038
- **Motivazione del modello**: Crepe visibili nella zona centrale del guscio e piccole macchie brunastre sul lato destro, senza fuoriuscite di contenuto.

</details>

<details>
<summary><b>158. commons_05.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_05.jpg" alt="commons_05.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_egg_2009-06-04.jpg](https://commons.wikimedia.org/wiki/File:Chicken_egg_2009-06-04.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Sun Ladder
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1120x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.90 s · token 2455 in / 55 out · costo $0.006686
- **Motivazione del modello**: Guscio pulito con minuscoli puntini naturali, senza sporco, crepe o fratture visibili.

</details>

<details>
<summary><b>159. figshare_IMG_20220818_154407.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154407.jpg" alt="figshare_IMG_20220818_154407.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154407.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.85 s · token 2572 in / 105 out · costo $0.007478
- **Motivazione del modello**: Guscio con numerose crepe centrali e lievi tracce di sporco localizzate, senza perdita visibile di contenuto.

</details>

<details>
<summary><b>160. hf_sample49.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample49.jpg" alt="hf_sample49.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample49.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample49.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.95 s · token 2572 in / 83 out · costo $0.007259
- **Motivazione del modello**: L’uovo a destra nella penultima fila presenta una crepa visibile, senza pezzi mancanti né sporcizia evidente.

</details>

<details>
<summary><b>161. figshare_IMG_20220818_155148.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155148.jpg" alt="figshare_IMG_20220818_155148.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155148.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.97 s · token 2572 in / 97 out · costo $0.007398
- **Motivazione del modello**: Visibile una sottile crepa nella parte superiore sinistra del guscio e poche piccole macchie brunastre.

</details>

<details>
<summary><b>162. hf_sample28.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample28.jpg" alt="hf_sample28.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample28.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample28.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.95 s · token 2572 in / 128 out · costo $0.007709
- **Motivazione del modello**: Gusci puliti, con soli minuscoli puntini e un timbro; nessuna crepa, frattura o perdita visibile.

</details>

<details>
<summary><b>163. figshare_IMG_20220818_155959.jpg</b> · scarta: crepato, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_155959.jpg" alt="figshare_IMG_20220818_155959.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155959.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato, sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.17 s · token 2572 in / 86 out · costo $0.007288
- **Motivazione del modello**: Macchie e residui evidenti sulla parte superiore del guscio, con crepe visibili e ramificate.

</details>

<details>
<summary><b>164. hf_sample4.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample4.jpg" alt="hf_sample4.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample4.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample4.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 6.37 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: L’uovo centrale a destra presenta piccoli residui marroni sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>165. figshare_IMG_20220818_155744.jpg</b> · accetta (A)</summary>

<img src="../../_pics/figshare_IMG_20220818_155744.jpg" alt="figshare_IMG_20220818_155744.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155744.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 3.48 s · token 2572 in / 52 out · costo $0.006948
- **Motivazione del modello**: Guscio pulito, senza macchie evidenti, crepe o perdite di contenuto visibili.

</details>

<details>
<summary><b>166. hf_sample36.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample36.jpg" alt="hf_sample36.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample36.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample36.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.04 s · token 2572 in / 90 out · costo $0.007328
- **Motivazione del modello**: L’uovo bianco nella fila inferiore, secondo da destra, presenta una crepa visibile nella parte superiore del guscio.

</details>

<details>
<summary><b>167. figshare_IMG_20220818_154731.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154731.jpg" alt="figshare_IMG_20220818_154731.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154731.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.69 s · token 2572 in / 58 out · costo $0.007008
- **Motivazione del modello**: Guscio con crepe visibili e poche piccole macchie brunastre, senza pezzi mancanti né fuoriuscite.

</details>

<details>
<summary><b>168. commons_09.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_09.jpg" alt="commons_09.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Toj%C3%A1s.jpg](https://commons.wikimedia.org/wiki/File:Toj%C3%A1s.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Safranyl
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 962x1088
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.07 s · token 1661 in / 203 out · costo $0.006181
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa nella parte superiore centrale.

</details>

<details>
<summary><b>169. figshare_IMG_20220818_154544.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154544.jpg" alt="figshare_IMG_20220818_154544.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154544.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.48 s · token 2572 in / 97 out · costo $0.007398
- **Motivazione del modello**: Poche piccole macchie sul guscio e una crepa sinuosa visibile nella parte inferiore, senza fuoriuscite.

</details>

<details>
<summary><b>170. hf_sample51.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample51.jpg" alt="hf_sample51.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample51.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample51.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.68 s · token 2572 in / 176 out · costo $0.008188
- **Motivazione del modello**: L’uovo marrone nella fila superiore, quarto da sinistra, presenta una crepa curva visibile nella parte alta del guscio.

</details>

<details>
<summary><b>171. figshare_IMG_20220818_154218.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154218.jpg" alt="figshare_IMG_20220818_154218.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154218.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.10 s · token 2572 in / 98 out · costo $0.007409
- **Motivazione del modello**: Guscio con poche piccole macchie e una sottile crepa verticale visibile nella zona centrale.

</details>

<details>
<summary><b>172. commons_21.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_21.jpg" alt="commons_21.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Six_eggs_views_from_the_top_on_a_white_background.jpg](https://commons.wikimedia.org/wiki/File:Six_eggs_views_from_the_top_on_a_white_background.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: TudorTulok
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1244
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.74 s · token 2690 in / 135 out · costo $0.008074
- **Motivazione del modello**: Gusci puliti, con piccoli puntini e timbri ammessi; nessuna crepa, rottura o perdita di contenuto visibile.

</details>

<details>
<summary><b>173. figshare_IMG_20220818_160033.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160033.jpg" alt="figshare_IMG_20220818_160033.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160033.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.64 s · token 2572 in / 78 out · costo $0.007208
- **Motivazione del modello**: Guscio con crepe ramificate visibili e poche piccole macchie superficiali, senza perdita di contenuto.

</details>

<details>
<summary><b>174. hf_sample6.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample6.jpg" alt="hf_sample6.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample6.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample6.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.99 s · token 2572 in / 59 out · costo $0.007019
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o residui; presenti soltanto timbri di stampa ammessi.

</details>

<details>
<summary><b>175. figshare_IMG_20220818_155523.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155523.jpg" alt="figshare_IMG_20220818_155523.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155523.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 9.65 s · token 2572 in / 102 out · costo $0.007449
- **Motivazione del modello**: Piccole macchie e residui chiari localizzati sul guscio; nessuna crepa o rottura visibile.

</details>

<details>
<summary><b>176. commons_02.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_02.jpg" alt="commons_02.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_green_brown_on_end.jpg](https://commons.wikimedia.org/wiki/File:Eggs_green_brown_on_end.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Hustvedt
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1019
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 12.58 s · token 2278 in / 93 out · costo $0.006624
- **Motivazione del modello**: L'uovo marrone presenta poche piccole macchie scure sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>177. figshare_IMG_20220818_154011.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154011.jpg" alt="figshare_IMG_20220818_154011.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154011.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.23 s · token 2572 in / 57 out · costo $0.006999
- **Motivazione del modello**: Guscio integro con poche piccole macchie e lievi residui localizzati; nessuna crepa visibile.

</details>

<details>
<summary><b>178. commons_28.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_28.jpg" alt="commons_28.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_eggs_21.jpg](https://commons.wikimedia.org/wiki/File:Chicken_eggs_21.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: BogTar201213
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1172
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 10.88 s · token 2572 in / 85 out · costo $0.007279
- **Motivazione del modello**: L’uovo bianco presenta piccoli aloni e residui superficiali; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>179. figshare_IMG_20220818_154708.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154708.jpg" alt="figshare_IMG_20220818_154708.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154708.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.02 s · token 2572 in / 85 out · costo $0.007279
- **Motivazione del modello**: Guscio con poche piccole macchie e una crepa evidente nella zona centrale, senza perdita di contenuto.

</details>

<details>
<summary><b>180. commons_33.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_33.jpg" alt="commons_33.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flickr_-_cyclonebill_-_%C3%86g_(1).jpg](https://commons.wikimedia.org/wiki/File:Flickr_-_cyclonebill_-_%C3%86g_(1).jpg)
- **Licenza**: CC BY-SA 2.0 · **Autore**: cyclonebill
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.76 s · token 2572 in / 62 out · costo $0.007049
- **Motivazione del modello**: L'uovo centrale presenta una lunga crepa trasversale, senza pezzi mancanti o fuoriuscite; guscio privo di sporcizia evidente.

</details>

<details>
<summary><b>181. figshare_IMG_20220818_155812.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155812.jpg" alt="figshare_IMG_20220818_155812.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155812.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.61 s · token 2572 in / 98 out · costo $0.007409
- **Motivazione del modello**: Guscio integro con poche piccole macchie e lievi aloni; nessuna crepa o perdita visibile.

</details>

<details>
<summary><b>182. commons_35.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_35.jpg" alt="commons_35.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:MonstereiXXXL.jpg](https://commons.wikimedia.org/wiki/File:MonstereiXXXL.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: -jkb-
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 12.21 s · token 2572 in / 79 out · costo $0.007219
- **Motivazione del modello**: Guscio pulito con timbro di stampa, senza crepe, rotture o residui visibili.

</details>

<details>
<summary><b>183. figshare_IMG_20220818_155915.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155915.jpg" alt="figshare_IMG_20220818_155915.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155915.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.51 s · token 2572 in / 81 out · costo $0.007239
- **Motivazione del modello**: Guscio pulito con una crepa sottile visibile nella parte inferiore, senza perdita di contenuto.

</details>

<details>
<summary><b>184. commons_07.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_07.jpg" alt="commons_07.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_colours.jpg](https://commons.wikimedia.org/wiki/File:Egg_colours.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Timothy Titus
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x922
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 18.04 s · token 2102 in / 140 out · costo $0.006653
- **Motivazione del modello**: L’uovo bianco presenta piccoli aloni grigiastri sul guscio; non si vedono crepe né rotture.

</details>

<details>
<summary><b>185. figshare_IMG_20220818_153638.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_153638.jpg" alt="figshare_IMG_20220818_153638.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153638.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 7.04 s · token 2572 in / 133 out · costo $0.007758
- **Motivazione del modello**: Piccoli residui e aloni sul guscio; sottile crepa orizzontale visibile nella zona centrale destra.

</details>

<details>
<summary><b>186. commons_29.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_29.jpg" alt="commons_29.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Braunes_H%C3%BChnerei.JPG](https://commons.wikimedia.org/wiki/File:Braunes_H%C3%BChnerei.JPG)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Fiver, der Hellseher
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.19 s · token 2572 in / 50 out · costo $0.006928
- **Motivazione del modello**: Guscio visibile pulito, senza macchie, crepe o rotture evidenti.

</details>

<details>
<summary><b>187. figshare_IMG_20220818_155503.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155503.jpg" alt="figshare_IMG_20220818_155503.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155503.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 12.12 s · token 2572 in / 58 out · costo $0.007008
- **Motivazione del modello**: Crepa sottile visibile sul guscio, ancora in un pezzo; piccoli residui e macchie nella parte inferiore.

</details>

<details>
<summary><b>188. hf_sample45.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample45.jpg" alt="hf_sample45.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample45.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample45.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.94 s · token 2572 in / 135 out · costo $0.007778
- **Motivazione del modello**: Piccoli residui chiari su alcuni gusci; non si osservano crepe, rotture o fuoriuscite di contenuto.

</details>

<details>
<summary><b>189. figshare_IMG_20220818_154847.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154847.jpg" alt="figshare_IMG_20220818_154847.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154847.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 8.89 s · token 2572 in / 90 out · costo $0.007328
- **Motivazione del modello**: Piccoli residui e macchie localizzati sulla superficie; visibile una crepa sottile, senza pezzi mancanti o fuoriuscite.

</details>

<details>
<summary><b>190. hf_sample21.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample21.jpg" alt="hf_sample21.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample21.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample21.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.92 s · token 2572 in / 56 out · costo $0.006988
- **Motivazione del modello**: I gusci visibili sono puliti e integri, senza crepe o residui; presenti solo timbri di stampa.

</details>

<details>
<summary><b>191. figshare_IMG_20220818_154328.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154328.jpg" alt="figshare_IMG_20220818_154328.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154328.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.43 s · token 2572 in / 82 out · costo $0.007248
- **Motivazione del modello**: Guscio pulito con minuscoli puntini; visibile una sottile crepa orizzontale nella parte inferiore, senza fuoriuscite.

</details>

<details>
<summary><b>192. commons_22.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_22.jpg" alt="commons_22.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Diff%C3%A9rents_oeufs.jpg](https://commons.wikimedia.org/wiki/File:Diff%C3%A9rents_oeufs.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Tylwyth Eldar
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.59 s · token 2337 in / 86 out · costo $0.006701
- **Motivazione del modello**: L'uovo a sinistra presenta poche macchie e residui nella parte inferiore; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>193. figshare_IMG_20220818_154724.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154724.jpg" alt="figshare_IMG_20220818_154724.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154724.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 4.96 s · token 2572 in / 99 out · costo $0.007418
- **Motivazione del modello**: Visibile una frattura estesa del guscio, senza perdita di contenuto, e piccole macchie brunastre localizzate.

</details>

<details>
<summary><b>194. commons_44.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_44.jpg" alt="commons_44.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huevo_Quebrado.jpg](https://commons.wikimedia.org/wiki/File:Huevo_Quebrado.jpg)
- **Licenza**: Public domain · **Autore**: Jorge Barrios
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 965x723
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: rotto (`broken`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.88 s · token 1252 in / 105 out · costo $0.004178
- **Motivazione del modello**: Nessun uovo intero: guscio frammentato con ampie parti mancanti e contenuto fuoriuscito; nessuna sporcizia evidente sul guscio.

</details>

<details>
<summary><b>195. figshare_IMG_20220818_155132.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155132.jpg" alt="figshare_IMG_20220818_155132.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155132.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.47 s · token 2572 in / 101 out · costo $0.007438
- **Motivazione del modello**: Guscio pulito con minuscoli puntini e una crepa ramificata visibile nella parte inferiore, senza fuoriuscite.

</details>

<details>
<summary><b>196. commons_40.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_40.jpg" alt="commons_40.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huehnerei_mit_Sprung_(fcm).jpg](https://commons.wikimedia.org/wiki/File:Huehnerei_mit_Sprung_(fcm).jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Frank C. Müller
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1314
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 10.75 s · token 2866 in / 54 out · costo $0.007704
- **Motivazione del modello**: Guscio pulito con ampie crepe ramificate, senza pezzi mancanti né fuoriuscite visibili.

</details>

<details>
<summary><b>197. figshare_IMG_20220818_154905.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154905.jpg" alt="figshare_IMG_20220818_154905.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154905.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 10.73 s · token 2572 in / 90 out · costo $0.007328
- **Motivazione del modello**: Piccoli residui e macchie localizzate sul guscio; visibile una crepa nella zona centrale, senza fuoriuscita di contenuto.

</details>

<details>
<summary><b>198. commons_41.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/commons_41.jpg" alt="commons_41.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Bloody-eggs.jpg](https://commons.wikimedia.org/wiki/File:Bloody-eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Maqi
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 900x675
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto, sporco
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 11.50 s · token 1162 in / 209 out · costo $0.004993
- **Motivazione del modello**: L’uovo anteriore presenta guscio sfondato e residui di contenuto sulla superficie.

</details>

<details>
<summary><b>199. figshare_IMG_20220818_154943.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154943.jpg" alt="figshare_IMG_20220818_154943.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154943.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 10.83 s · token 2572 in / 95 out · costo $0.007378
- **Motivazione del modello**: Guscio con piccoli residui e macchie localizzate; evidente frattura nella zona centrale, senza perdita visibile di contenuto.

</details>

<details>
<summary><b>200. commons_24.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_24.jpg" alt="commons_24.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_(394351849).jpg](https://commons.wikimedia.org/wiki/File:Egg_(394351849).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: liz west from Boxborough, MA, USA
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1550x1549
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6.1-sol` · latenza 5.88 s · token 3278 in / 129 out · costo $0.009484
- **Motivazione del modello**: Guscio pulito, con una sottile crepa visibile nella parte centrale inferiore, senza fuoriuscita di contenuto.

</details>
