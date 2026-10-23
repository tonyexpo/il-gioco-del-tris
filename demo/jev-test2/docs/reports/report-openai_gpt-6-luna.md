# Rapporto di analisi uova: GPT-6 Luna (LLM, raffronto)

- **Modello richiesto**: `openai/gpt-6-luna`
- **Modello servito**: `openai/gpt-6-luna`
- **Interfaccia**: OpenRouter Chat Completions con output JSON strutturato (modello generativo, senza probabilità)
- **Data analisi**: 23 ottobre 2026 alle ore 17:37
- **Foto analizzate**: 200 su 200

## Riepilogo

| Esito | Foto | Quota |
| --- | ---: | ---: |
| Accettate (grado A, pulite e integre) | 38 | 19.0% |
| Accettate (grado B, lievemente sporche) | 57 | 28.5% |
| **Scartate** (rotte, crepate o sporche) | 101 | 50.5% |
| Non valutabili (uovo non rilevato) | 4 | 2.0% |

Motivi di scarto (una foto può averne più d'uno): crepato 92, rotto 6, sporco 7, uovo non rilevato 4.

| Pulizia | Foto |  | Integrità | Foto |
| --- | ---: | --- | --- | ---: |
| pulito | 73 |  | integro | 100 |
| lievemente sporco | 118 |  | crepato | 92 |
| sporco | 9 |  | rotto | 8 |

### Per tipo di scena

| Scena | Foto | Accettate | Scartate | Non valutabili |
| --- | ---: | ---: | ---: | ---: |
| uovo singolo | 100 | 24 | 76 | 0 |
| poche uova | 49 | 33 | 12 | 4 |
| cartone con più uova | 51 | 38 | 13 | 0 |

### Confronto con la verità nota

Solo le foto Figshare hanno una verità annotata a mano (crepe). Le altre foto non hanno etichette, quindi per pulizia e per le foto Commons/Hugging Face non esiste una misura di accuratezza.

- Uova crepate note: **76 su 100** riconosciute come crepate o rotte (76.0%).
- Le crepe di questo dataset sono sottili e le foto sono ridotte a 1568 px: è una prova difficile, non rappresentativa delle rotture evidenti.

### Tempi e costi

| Metrica | Valore |
| --- | ---: |
| Latenza media | 5.91 s |
| Latenza p50 | 5.69 s |
| Latenza p95 | 8.73 s |
| Token in ingresso | 506290 |
| Token in uscita | 27130 |
| Costo totale (da `usage.cost`) | $0.0768 |
| Costo per 1000 foto | $0.3842 |

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
| 1 | [figshare_IMG_20220818_154808.jpg](../../_pics/figshare_IMG_20220818_154808.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.64 s | Uovo intero con alcune piccole macchie scure sul guscio, senza crepe o rotture visibili.; verità: cracked |
| 2 | [commons_04.jpg](../../_pics/commons_04.jpg) | poche uova | pulito | integro | accetta (A) | 11.09 s | Tre uova visibili; gusci puliti, senza crepe o rotture evidenti. |
| 3 | [figshare_IMG_20220818_154045.jpg](../../_pics/figshare_IMG_20220818_154045.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 8.03 s | Sono visibili piccole macchie e una sottile crepa sul guscio, senza rotture né fuoriuscite.; verità: cracked |
| 4 | [commons_03.jpg](../../_pics/commons_03.jpg) | poche uova | pulito | integro | accetta (A) | 6.08 s | Le uova sono visibili; i gusci non mostrano sporco significativo né crepe o rotture. |
| 5 | [figshare_IMG_20220818_155841.jpg](../../_pics/figshare_IMG_20220818_155841.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.07 s | Uovo pulito con crepe visibili nel guscio, senza parti mancanti né fuoriuscite.; verità: cracked |
| 6 | [hf_sample47.jpg](../../_pics/hf_sample47.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 6.32 s | Le uova sono pulite; un uovo marrone presenta una crepa visibile nel guscio. |
| 7 | [figshare_IMG_20220818_155248.jpg](../../_pics/figshare_IMG_20220818_155248.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.67 s | Uovo intero con alcune macchie di sporco localizzate; non si vedono crepe né rotture.; verità: cracked |
| 8 | [commons_30.jpg](../../_pics/commons_30.jpg) | poche uova | pulito | integro | accetta (A) | 6.91 s | Quattro uova visibili; gusci puliti, senza macchie significative né crepe o rotture. |
| 9 | [figshare_IMG_20220818_155341.jpg](../../_pics/figshare_IMG_20220818_155341.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 7.28 s | Uovo intero con poche macchie marroni localizzate sul guscio; non si vedono crepe.; verità: cracked |
| 10 | [commons_15.jpg](../../_pics/commons_15.jpg) | poche uova | pulito | integro | accetta (A) | 6.35 s | Uovo intero con guscio uniforme, senza sporco evidente né crepe visibili. |
| 11 | [figshare_IMG_20220818_153759.jpg](../../_pics/figshare_IMG_20220818_153759.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 7.86 s | Guscio con pochi piccoli puntini di sporco; non si vedono crepe né rotture.; verità: cracked |
| 12 | [hf_sample7.jpg](../../_pics/hf_sample7.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.20 s | Le uova visibili hanno gusci puliti e senza crepe o rotture; i timbri sono ammessi. |
| 13 | [figshare_IMG_20220818_160114.jpg](../../_pics/figshare_IMG_20220818_160114.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 8.03 s | Uovo intero con una sottile crepa visibile e poche piccole macchie sul guscio.; verità: cracked |
| 14 | [commons_36.jpg](../../_pics/commons_36.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 6.42 s | Guscio pulito, con un sottile segno lineare visibile compatibile con una crepa. |
| 15 | [figshare_IMG_20220818_155859.jpg](../../_pics/figshare_IMG_20220818_155859.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.57 s | Uovo pulito con una crepa visibile nella parte inferiore del guscio.; verità: cracked |
| 16 | [hf_sample3.jpg](../../_pics/hf_sample3.jpg) | cartone con più uova | pulito | integro | accetta (A) | 7.63 s | Le uova visibili hanno gusci integri e puliti; i piccoli segni sembrano puntini o timbri. |
| 17 | [figshare_IMG_20220818_155422.jpg](../../_pics/figshare_IMG_20220818_155422.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.59 s | Uovo visibile con poche macchie sul guscio e una crepa sottile; il guscio è ancora intero.; verità: cracked |
| 18 | [commons_25.jpg](../../_pics/commons_25.jpg) | poche uova | pulito | integro | accetta (A) | 5.88 s | Uovo visibile con guscio pulito, senza macchie evidenti né crepe o rotture. |
| 19 | [figshare_IMG_20220818_154854.jpg](../../_pics/figshare_IMG_20220818_154854.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.72 s | Uovo con sporco localizzato nella parte inferiore e una crepa visibile sul guscio.; verità: cracked |
| 20 | [hf_sample30.jpg](../../_pics/hf_sample30.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.88 s | L’uovo marrone in basso presenta piccole macchie sul guscio; non si vedono crepe o rotture. |
| 21 | [figshare_IMG_20220818_154019.jpg](../../_pics/figshare_IMG_20220818_154019.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.64 s | Guscio con poche macchie piccole; non sono visibili crepe o rotture.; verità: cracked |
| 22 | [hf_sample9.jpg](../../_pics/hf_sample9.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 7.43 s | Le uova sono pulite; una presenta una sottile crepa visibile sul guscio. |
| 23 | [figshare_IMG_20220818_154949.jpg](../../_pics/figshare_IMG_20220818_154949.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.76 s | Piccole macchie sul guscio e una crepa visibile, senza perdita di contenuto.; verità: cracked |
| 24 | [commons_18.jpg](../../_pics/commons_18.jpg) | poche uova | pulito | integro | accetta (A) | 6.75 s | Le uova sono intere; i puntini visibili sembrano pigmentazione naturale del guscio, senza sporco evidente. |
| 25 | [figshare_IMG_20220818_155415.jpg](../../_pics/figshare_IMG_20220818_155415.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.80 s | Uovo intero visibile, con poche macchie superficiali e crepe nel guscio senza aperture.; verità: cracked |
| 26 | [commons_23.jpg](../../_pics/commons_23.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.68 s | Un guscio presenta piccoli residui e macchie sparse; non si vedono crepe o rotture. |
| 27 | [figshare_IMG_20220818_155457.jpg](../../_pics/figshare_IMG_20220818_155457.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 10.05 s | Uovo intero, con piccole macchie e irregolarità superficiali; non si distinguono crepe o rotture.; verità: cracked |
| 28 | [hf_sample8.jpg](../../_pics/hf_sample8.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 8.16 s | Un uovo presenta una sottile linea visibile sul guscio; gli altri appaiono puliti e integri. |
| 29 | [figshare_IMG_20220818_154636.jpg](../../_pics/figshare_IMG_20220818_154636.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.75 s | Guscio con poche piccole macchie; non si vedono crepe né rotture.; verità: cracked |
| 30 | [hf_sample20.jpg](../../_pics/hf_sample20.jpg) | cartone con più uova | pulito | integro | accetta (A) | 6.22 s | Le uova visibili hanno gusci puliti, senza crepe o rotture; i piccoli segni rosa sono stampe. |
| 31 | [figshare_IMG_20220818_154528.jpg](../../_pics/figshare_IMG_20220818_154528.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.83 s | Uovo con guscio quasi pulito; è visibile una sottile crepa sulla superficie.; verità: cracked |
| 32 | [hf_sample34.jpg](../../_pics/hf_sample34.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 5.93 s | Un uovo bianco presenta una sottile linea simile a una crepa; sono visibili anche piccole macchie sul guscio. |
| 33 | [figshare_IMG_20220818_160007.jpg](../../_pics/figshare_IMG_20220818_160007.jpg) | uovo singolo | sporco | rotto | **scarta**: rotto, sporco | 6.88 s | Guscio molto sporco, con macchie diffuse e una zona scheggiata con membrana esposta.; verità: cracked |
| 34 | [commons_27.jpg](../../_pics/commons_27.jpg) | poche uova | sporco | integro | **scarta**: sporco | 6.90 s | L’uovo in basso a sinistra presenta numerose macchie scure diffuse; non si vedono crepe o rotture. |
| 35 | [figshare_IMG_20220818_154535.jpg](../../_pics/figshare_IMG_20220818_154535.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.04 s | Uovo intero; guscio con pochi puntini e lievi aloni, senza crepe evidenti.; verità: cracked |
| 36 | [hf_sample13.jpg](../../_pics/hf_sample13.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 8.92 s | Le uova sono pulite; su un guscio si nota una sottile linea simile a una crepa. |
| 37 | [figshare_IMG_20220818_155015.jpg](../../_pics/figshare_IMG_20220818_155015.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.54 s | Presenti piccole macchie sul guscio e una sottile crepa visibile sul lato sinistro.; verità: cracked |
| 38 | [hf_sample46.jpg](../../_pics/hf_sample46.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.65 s | Un uovo presenta piccoli segni superficiali; non sono visibili crepe o rotture. |
| 39 | [figshare_IMG_20220818_155401.jpg](../../_pics/figshare_IMG_20220818_155401.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.96 s | Uovo intero, con piccole macchie di sporco sul guscio e nessuna crepa visibile.; verità: cracked |
| 40 | [commons_34.jpg](../../_pics/commons_34.jpg) | poche uova | pulito | integro | accetta (A) | 5.88 s | Il guscio appare pulito e integro, senza macchie significative né crepe visibili. |
| 41 | [figshare_IMG_20220818_155709.jpg](../../_pics/figshare_IMG_20220818_155709.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.75 s | Guscio pulito, con una sottile crepa visibile sul lato destro.; verità: cracked |
| 42 | [commons_32.jpg](../../_pics/commons_32.jpg) | poche uova | pulito | integro | accetta (A) | 4.14 s | Uovo visibile con guscio pulito e senza crepe o rotture. |
| 43 | [figshare_IMG_20220818_155137.jpg](../../_pics/figshare_IMG_20220818_155137.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.06 s | Si notano piccoli residui sul guscio e una sottile linea simile a una crepa.; verità: cracked |
| 44 | [commons_42.jpg](../../_pics/commons_42.jpg) | poche uova | sporco | integro | **scarta**: sporco | 3.96 s | Uovo intero con una macchia rossa estesa sul guscio; non si vedono crepe né rotture. |
| 45 | [figshare_IMG_20220818_155511.jpg](../../_pics/figshare_IMG_20220818_155511.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.73 s | Piccole macchie sul guscio e una sottile crepa diagonale visibile.; verità: cracked |
| 46 | [commons_16.jpg](../../_pics/commons_16.jpg) | poche uova | pulito | integro | accetta (A) | 4.46 s | Uovo intero con guscio pulito, senza macchie evidenti né crepe. |
| 47 | [figshare_IMG_20220818_154136.jpg](../../_pics/figshare_IMG_20220818_154136.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.44 s | Piccole macchie sul guscio e una sottile crepa visibile sul lato sinistro.; verità: cracked |
| 48 | [commons_19.jpg](../../_pics/commons_19.jpg) | poche uova | pulito | integro | accetta (A) | 5.68 s | I gusci visibili appaiono puliti e integri; i piccoli puntini sembrano pigmentazione naturale. |
| 49 | [figshare_IMG_20220818_154759.jpg](../../_pics/figshare_IMG_20220818_154759.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.82 s | Uovo intero con poche macchie localizzate sul guscio; non si notano crepe o rotture.; verità: cracked |
| 50 | [commons_47.jpg](../../_pics/commons_47.jpg) | poche uova | pulito | integro | non valutabile | 5.70 s | Non è visibile alcun uovo di gallina. |
| 51 | [figshare_IMG_20220818_155540.jpg](../../_pics/figshare_IMG_20220818_155540.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.09 s | L’uovo è intero ma presenta una crepa visibile e pochi piccoli puntini sul guscio.; verità: cracked |
| 52 | [hf_sample17.jpg](../../_pics/hf_sample17.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.87 s | Un uovo presenta una piccola macchia rosa sul guscio; non si vedono crepe né rotture. |
| 53 | [figshare_IMG_20220818_154226.jpg](../../_pics/figshare_IMG_20220818_154226.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.99 s | Uovo con poche macchie scure e una sottile crepa visibile sul guscio.; verità: cracked |
| 54 | [hf_sample33.jpg](../../_pics/hf_sample33.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 5.79 s | Un uovo presenta una sottile crepa visibile; un altro ha una piccola macchia sul guscio. |
| 55 | [figshare_IMG_20220818_155846.jpg](../../_pics/figshare_IMG_20220818_155846.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.06 s | Uovo visibile con guscio pulito e una crepa evidente, senza perdita di contenuto.; verità: cracked |
| 56 | [commons_11.jpg](../../_pics/commons_11.jpg) | poche uova | pulito | integro | accetta (A) | 5.46 s | Uovo intero con guscio uniforme, senza sporco o crepe visibili. |
| 57 | [figshare_IMG_20220818_153842.jpg](../../_pics/figshare_IMG_20220818_153842.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.59 s | Uovo intero con poche piccole macchie sul guscio; non si notano crepe o rotture.; verità: cracked |
| 58 | [commons_48.jpg](../../_pics/commons_48.jpg) | poche uova | pulito | integro | non valutabile | 6.24 s | Non è visibile alcun uovo di gallina intero. |
| 59 | [figshare_IMG_20220818_160129.jpg](../../_pics/figshare_IMG_20220818_160129.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.26 s | Il guscio appare pulito, ma presenta una sottile crepa visibile nella parte inferiore.; verità: cracked |
| 60 | [hf_sample2.jpg](../../_pics/hf_sample2.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.02 s | Un uovo presenta una piccola macchia sul guscio; non si vedono crepe o rotture. |
| 61 | [figshare_IMG_20220818_155851.jpg](../../_pics/figshare_IMG_20220818_155851.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.85 s | Piccoli puntini scuri sul guscio e una sottile crepa verticale visibile.; verità: cracked |
| 62 | [hf_sample29.jpg](../../_pics/hf_sample29.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.36 s | Le uova visibili hanno gusci puliti e senza crepe o rotture. |
| 63 | [figshare_IMG_20220818_154436.jpg](../../_pics/figshare_IMG_20220818_154436.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.58 s | Uovo pulito; è visibile una sottile crepa sulla parte superiore del guscio.; verità: cracked |
| 64 | [hf_sample37.jpg](../../_pics/hf_sample37.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 6.29 s | Un uovo presenta una sottile crepa; sul guscio di un altro si vede una macchia grigiastra. |
| 65 | [figshare_IMG_20220818_154051.jpg](../../_pics/figshare_IMG_20220818_154051.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.64 s | Guscio con poche macchioline e una sottile crepa visibile sulla superficie.; verità: cracked |
| 66 | [hf_sample40.jpg](../../_pics/hf_sample40.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.12 s | Alcuni gusci presentano piccole macchie; nessuna crepa o rottura visibile. |
| 67 | [figshare_IMG_20220818_155910.jpg](../../_pics/figshare_IMG_20220818_155910.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.17 s | Uovo pulito, con una crepa visibile sul guscio senza perdita di contenuto.; verità: cracked |
| 68 | [hf_sample41.jpg](../../_pics/hf_sample41.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.04 s | Un uovo presenta una piccola macchia rossastra; non si vedono crepe né rotture. |
| 69 | [figshare_IMG_20220818_154057.jpg](../../_pics/figshare_IMG_20220818_154057.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.35 s | Uovo visibile con poche macchie superficiali e una crepa sottile, senza rotture né fuoriuscite.; verità: cracked |
| 70 | [hf_sample43.jpg](../../_pics/hf_sample43.jpg) | cartone con più uova | lievemente sporco | crepato | **scarta**: crepato | 8.24 s | Un uovo presenta una sottile crepa; si notano anche piccoli segni isolati sul guscio. |
| 71 | [figshare_IMG_20220818_154444.jpg](../../_pics/figshare_IMG_20220818_154444.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.92 s | Uovo visibile con alcune lievi macchie e una crepa sottile sul guscio.; verità: cracked |
| 72 | [commons_20.jpg](../../_pics/commons_20.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 6.39 s | Un uovo presenta piccole macchie superficiali; tutti i gusci appaiono integri, senza crepe o rotture visibili. |
| 73 | [figshare_IMG_20220818_155948.jpg](../../_pics/figshare_IMG_20220818_155948.jpg) | uovo singolo | sporco | rotto | **scarta**: rotto, sporco | 5.65 s | Guscio con macchie diffuse e una porzione mancante; è visibile la membrana sottostante.; verità: cracked |
| 74 | [hf_sample11.jpg](../../_pics/hf_sample11.jpg) | cartone con più uova | pulito | integro | accetta (A) | 4.99 s | Le uova visibili hanno gusci puliti e integri; i timbri non indicano sporco o danni. |
| 75 | [figshare_IMG_20220818_155606.jpg](../../_pics/figshare_IMG_20220818_155606.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.93 s | Uovo visibile con alcune piccole macchie e una crepa con lembo di guscio sollevato.; verità: cracked |
| 76 | [commons_49.jpg](../../_pics/commons_49.jpg) | poche uova | sporco | rotto | **scarta**: rotto, sporco | 4.47 s | Ampia zona sporca e lesionata, con guscio sfondato e materiale esposto. |
| 77 | [figshare_IMG_20220818_154914.jpg](../../_pics/figshare_IMG_20220818_154914.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 10.24 s | Uovo con macchie di sporco localizzate e una crepa sottile visibile sul guscio.; verità: cracked |
| 78 | [hf_sample22.jpg](../../_pics/hf_sample22.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.02 s | L’uovo centrale presenta una piccola macchia; non si vedono crepe o rotture. |
| 79 | [figshare_IMG_20220818_155240.jpg](../../_pics/figshare_IMG_20220818_155240.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.57 s | Piccole macchie concentrate sul lato destro e una sottile crepa visibile al centro del guscio.; verità: cracked |
| 80 | [commons_06.jpg](../../_pics/commons_06.jpg) | poche uova | pulito | integro | accetta (A) | 5.72 s | Entrambe le uova hanno gusci integri e puliti; si vedono solo minuscoli puntini. |
| 81 | [figshare_IMG_20220818_160039.jpg](../../_pics/figshare_IMG_20220818_160039.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.43 s | Guscio con poche macchie e una crepa visibile, senza pezzi mancanti né fuoriuscite.; verità: cracked |
| 82 | [hf_sample42.jpg](../../_pics/hf_sample42.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 9.29 s | Un uovo presenta una piccola frattura sul bordo inferiore; le altre macchie sono puntini minimi. |
| 83 | [figshare_IMG_20220818_154715.jpg](../../_pics/figshare_IMG_20220818_154715.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.46 s | Uovo intero con alcune piccole macchie e una crepa visibile, senza perdita di contenuto.; verità: cracked |
| 84 | [hf_sample12.jpg](../../_pics/hf_sample12.jpg) | cartone con più uova | pulito | integro | accetta (A) | 6.86 s | Uova visibili con gusci puliti e senza crepe o rotture evidenti. |
| 85 | [figshare_IMG_20220818_154238.jpg](../../_pics/figshare_IMG_20220818_154238.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 3.62 s | Uovo intero con poche piccole macchie sul guscio; non si vedono crepe o rotture.; verità: cracked |
| 86 | [hf_sample16.jpg](../../_pics/hf_sample16.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.09 s | I gusci sono quasi puliti, ma si notano piccoli puntini; non sono visibili crepe o rotture. |
| 87 | [figshare_IMG_20220818_154413.jpg](../../_pics/figshare_IMG_20220818_154413.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.07 s | Uovo pulito, con una frattura visibile sul guscio; non si osservano pezzi mancanti né fuoriuscite.; verità: cracked |
| 88 | [commons_14.jpg](../../_pics/commons_14.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 4.98 s | L’uovo a sinistra presenta piccoli puntini; entrambi i gusci appaiono integri. |
| 89 | [figshare_IMG_20220818_155559.jpg](../../_pics/figshare_IMG_20220818_155559.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.49 s | Guscio con poche piccole macchie e una crepa visibile, senza perdita di contenuto.; verità: cracked |
| 90 | [hf_sample1.jpg](../../_pics/hf_sample1.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.80 s | Un uovo presenta piccole macchie sul guscio; non si vedono crepe né rotture. |
| 91 | [figshare_IMG_20220818_155517.jpg](../../_pics/figshare_IMG_20220818_155517.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.41 s | Piccole macchie sul guscio e una sottile crepa visibile nella parte centrale.; verità: cracked |
| 92 | [hf_sample5.jpg](../../_pics/hf_sample5.jpg) | cartone con più uova | pulito | integro | accetta (A) | 3.86 s | Le uova visibili hanno gusci puliti e senza crepe o rotture; il timbro è ammesso. |
| 93 | [figshare_IMG_20220818_154429.jpg](../../_pics/figshare_IMG_20220818_154429.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 3.46 s | Uovo pulito, con una crepa visibile sul guscio; non si vedono rotture o fuoriuscite.; verità: cracked |
| 94 | [commons_13.jpg](../../_pics/commons_13.jpg) | poche uova | pulito | integro | accetta (A) | 5.30 s | Entrambe le uova sono visibili, con gusci puliti e senza crepe o rotture. |
| 95 | [figshare_IMG_20220818_160049.jpg](../../_pics/figshare_IMG_20220818_160049.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.54 s | Piccole macchie sul guscio e una crepa visibile, senza rottura o perdita di contenuto.; verità: cracked |
| 96 | [commons_17.jpg](../../_pics/commons_17.jpg) | poche uova | pulito | integro | accetta (A) | 4.10 s | Le uova hanno gusci integri e senza sporco visibile; i piccoli puntini sembrano naturali. |
| 97 | [figshare_IMG_20220818_155353.jpg](../../_pics/figshare_IMG_20220818_155353.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.13 s | Guscio con poche macchie e puntini; non si osservano crepe o rotture.; verità: cracked |
| 98 | [hf_sample35.jpg](../../_pics/hf_sample35.jpg) | cartone con più uova | pulito | integro | accetta (A) | 9.41 s | Le uova visibili sono integre e non presentano sporco significativo. |
| 99 | [figshare_IMG_20220818_154557.jpg](../../_pics/figshare_IMG_20220818_154557.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.87 s | Guscio con pochi piccoli aloni e una sottile linea simile a una crepa sul lato sinistro.; verità: cracked |
| 100 | [hf_sample27.jpg](../../_pics/hf_sample27.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.75 s | L'uovo in basso a destra presenta una piccola macchia sul guscio; non si vedono crepe o rotture. |
| 101 | [figshare_IMG_20220818_153953.jpg](../../_pics/figshare_IMG_20220818_153953.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 6.34 s | Uovo intero con poche piccole macchie sul guscio; non si vedono crepe o rotture.; verità: cracked |
| 102 | [hf_sample14.jpg](../../_pics/hf_sample14.jpg) | cartone con più uova | pulito | integro | accetta (A) | 4.08 s | Le uova visibili hanno gusci puliti e integri; si notano solo piccoli timbri di stampa. |
| 103 | [figshare_IMG_20220818_160014.jpg](../../_pics/figshare_IMG_20220818_160014.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.64 s | Guscio con macchie di sporco localizzate e una crepa visibile, senza pezzi mancanti.; verità: cracked |
| 104 | [hf_sample19.jpg](../../_pics/hf_sample19.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 3.56 s | Un uovo presenta piccoli aloni e residui sul guscio; non si vedono crepe o rotture. |
| 105 | [figshare_IMG_20220818_154113.jpg](../../_pics/figshare_IMG_20220818_154113.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.62 s | Guscio con poche macchie e una crepa sottile visibile nella parte superiore.; verità: cracked |
| 106 | [hf_sample18.jpg](../../_pics/hf_sample18.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.01 s | Le uova visibili hanno gusci puliti e integri; i piccoli segni rosa sono timbri. |
| 107 | [figshare_IMG_20220818_160123.jpg](../../_pics/figshare_IMG_20220818_160123.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.74 s | Uovo visibile con una crepa sottile e poche piccole macchie sul guscio.; verità: cracked |
| 108 | [hf_sample26.jpg](../../_pics/hf_sample26.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.38 s | Un uovo presenta piccoli puntini e aloni sul guscio; non si vedono crepe né rotture. |
| 109 | [figshare_IMG_20220818_155430.jpg](../../_pics/figshare_IMG_20220818_155430.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.33 s | Guscio con poche macchie brune localizzate e una crepa visibile, senza perdita di contenuto.; verità: cracked |
| 110 | [hf_sample32.jpg](../../_pics/hf_sample32.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.74 s | Le uova visibili hanno gusci puliti, senza sporco significativo né crepe o rotture. |
| 111 | [figshare_IMG_20220818_154419.jpg](../../_pics/figshare_IMG_20220818_154419.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.53 s | Uovo pulito, con crepe visibili sul guscio ma senza rotture o perdita di contenuto.; verità: cracked |
| 112 | [hf_sample25.jpg](../../_pics/hf_sample25.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 5.41 s | Le uova sono integre; una presenta piccoli segni scuri visibili sul guscio. |
| 113 | [figshare_IMG_20220818_160028.jpg](../../_pics/figshare_IMG_20220818_160028.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.44 s | Guscio con piccole macchie e una crepa visibile, senza pezzi mancanti né contenuto fuoriuscito.; verità: cracked |
| 114 | [commons_01.jpg](../../_pics/commons_01.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 4.15 s | Guscio con poche piccole macchie scure; non si vedono crepe né rotture. |
| 115 | [figshare_IMG_20220818_160055.jpg](../../_pics/figshare_IMG_20220818_160055.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.97 s | Uovo visibile con poche macchie superficiali e una sottile crepa nel guscio.; verità: cracked |
| 116 | [hf_sample10.jpg](../../_pics/hf_sample10.jpg) | cartone con più uova | pulito | integro | accetta (A) | 7.47 s | Le uova visibili hanno gusci puliti, senza crepe o rotture evidenti. |
| 117 | [figshare_IMG_20220818_155905.jpg](../../_pics/figshare_IMG_20220818_155905.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.74 s | Guscio pulito, con una crepa visibile ma senza parti mancanti.; verità: cracked |
| 118 | [commons_39.jpg](../../_pics/commons_39.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.08 s | Alcuni gusci presentano piccole macchie; non si notano crepe o rotture. |
| 119 | [figshare_IMG_20220818_154319.jpg](../../_pics/figshare_IMG_20220818_154319.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.20 s | Guscio con pochi puntini di sporco e una sottile crepa visibile, senza rotture.; verità: cracked |
| 120 | [commons_37.jpg](../../_pics/commons_37.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 4.54 s | Entrambe le uova sono intere; una presenta piccole macchie marroni sul guscio. |
| 121 | [figshare_IMG_20220818_160044.jpg](../../_pics/figshare_IMG_20220818_160044.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.28 s | Uovo con alcune piccole macchie e una crepa ramificata; il guscio è ancora in un pezzo.; verità: cracked |
| 122 | [hf_sample24.jpg](../../_pics/hf_sample24.jpg) | cartone con più uova | pulito | integro | accetta (A) | 8.49 s | Le uova sono intere; si vedono solo piccoli puntini e pigmentazioni naturali, senza sporco evidente o crepe. |
| 123 | [figshare_IMG_20220818_155030.jpg](../../_pics/figshare_IMG_20220818_155030.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 4.55 s | Uovo intero con poche macchioline sul guscio; non si notano crepe né rotture.; verità: cracked |
| 124 | [hf_sample31.jpg](../../_pics/hf_sample31.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 4.72 s | L’uovo marrone in basso presenta piccoli segni sul guscio; non si vedono crepe o rotture. |
| 125 | [figshare_IMG_20220818_155717.jpg](../../_pics/figshare_IMG_20220818_155717.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 7.12 s | Uovo intero, con pochi piccoli puntini sul guscio; non si vedono crepe né rotture.; verità: cracked |
| 126 | [hf_sample48.jpg](../../_pics/hf_sample48.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 6.44 s | L’uovo marrone in basso a destra presenta una crepa visibile; gli altri gusci appaiono puliti. |
| 127 | [figshare_IMG_20220818_154752.jpg](../../_pics/figshare_IMG_20220818_154752.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.77 s | Piccole macchie sul guscio e una sottile crepa visibile.; verità: cracked |
| 128 | [hf_sample23.jpg](../../_pics/hf_sample23.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 7.05 s | Un uovo presenta piccoli segni superficiali; non si vedono crepe o rotture. |
| 129 | [figshare_IMG_20220818_155804.jpg](../../_pics/figshare_IMG_20220818_155804.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.25 s | Piccole macchie sul guscio e una sottile crepa visibile sul lato sinistro.; verità: cracked |
| 130 | [commons_10.jpg](../../_pics/commons_10.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 6.42 s | L’uovo a sinistra presenta una piccola macchia chiara; entrambi i gusci appaiono integri. |
| 131 | [figshare_IMG_20220818_155611.jpg](../../_pics/figshare_IMG_20220818_155611.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.26 s | Guscio con poche macchie nella parte inferiore e una crepa visibile, senza fuoriuscita di contenuto.; verità: cracked |
| 132 | [hf_sample38.jpg](../../_pics/hf_sample38.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.00 s | L’uovo in basso a destra presenta piccole macchie sul guscio, senza crepe o rotture visibili. |
| 133 | [figshare_IMG_20220818_155724.jpg](../../_pics/figshare_IMG_20220818_155724.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 10.02 s | Guscio con poche piccole macchie; non si notano crepe o rotture.; verità: cracked |
| 134 | [commons_46.jpg](../../_pics/commons_46.jpg) | poche uova | pulito | rotto | **scarta**: rotto | 6.69 s | Uovo visibile, con guscio sfondato e frammenti mancanti; non si notano sporcizia o macchie sul guscio. |
| 135 | [figshare_IMG_20220818_154818.jpg](../../_pics/figshare_IMG_20220818_154818.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 6.70 s | Uovo intero con poche piccole macchie sul guscio, senza crepe né rotture visibili.; verità: cracked |
| 136 | [hf_sample39.jpg](../../_pics/hf_sample39.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 7.09 s | Un uovo presenta piccoli puntini e macchie superficiali; non si vedono crepe o rotture. |
| 137 | [figshare_IMG_20220818_154103.jpg](../../_pics/figshare_IMG_20220818_154103.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.69 s | Poche macchie sparse sul guscio; è visibile una crepa irregolare, ma l’uovo è ancora in un pezzo.; verità: cracked |
| 138 | [hf_sample50.jpg](../../_pics/hf_sample50.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 13.43 s | Uova intere; un guscio presenta un piccolo residuo visibile, senza crepe o rotture. |
| 139 | [figshare_IMG_20220818_155617.jpg](../../_pics/figshare_IMG_20220818_155617.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.75 s | Piccole macchie sul guscio e crepe visibili, ma il guscio è ancora in un pezzo.; verità: cracked |
| 140 | [commons_45.jpg](../../_pics/commons_45.jpg) | poche uova | pulito | rotto | **scarta**: rotto | 7.78 s | Un uovo intero è visibile; i gusci in primo piano sono rotti in più pezzi. |
| 141 | [figshare_IMG_20220818_154959.jpg](../../_pics/figshare_IMG_20220818_154959.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.96 s | Guscio con poche macchie e una crepa visibile, ma senza rotture o fuoriuscite.; verità: cracked |
| 142 | [commons_26.jpg](../../_pics/commons_26.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.41 s | Uova integre; una presenta una piccola macchia scura sul guscio. |
| 143 | [figshare_IMG_20220818_153857.jpg](../../_pics/figshare_IMG_20220818_153857.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 3.50 s | Uovo intero senza crepe visibili; presenta poche piccole macchie sul guscio.; verità: cracked |
| 144 | [commons_43.jpg](../../_pics/commons_43.jpg) | poche uova | sporco | rotto | non valutabile | 5.99 s | Uovo sfondato con guscio frantumato e contenuto fuoriuscito; nessun uovo intero visibile. |
| 145 | [figshare_IMG_20220818_154312.jpg](../../_pics/figshare_IMG_20220818_154312.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.19 s | Uovo pulito, con una crepa evidente sul guscio; non si vedono fuoriuscite.; verità: cracked |
| 146 | [commons_08.jpg](../../_pics/commons_08.jpg) | poche uova | pulito | integro | accetta (A) | 7.81 s | Le uova hanno gusci senza sporco evidente né crepe o rotture; i puntini sembrano pigmentazione naturale. |
| 147 | [figshare_IMG_20220818_154335.jpg](../../_pics/figshare_IMG_20220818_154335.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.22 s | Piccole macchie sul guscio e una sottile crepa visibile nella parte superiore.; verità: cracked |
| 148 | [hf_sample15.jpg](../../_pics/hf_sample15.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 3.32 s | Uova intere senza crepe; alcune presentano piccoli segni rossastri e puntini sul guscio. |
| 149 | [figshare_IMG_20220818_155547.jpg](../../_pics/figshare_IMG_20220818_155547.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.79 s | Uovo visibile con una crepa sul guscio e alcune piccole macchie superficiali.; verità: cracked |
| 150 | [commons_12.jpg](../../_pics/commons_12.jpg) | poche uova | pulito | integro | accetta (A) | 4.11 s | Uovo intero con guscio uniforme, senza sporco né crepe visibili. |
| 151 | [figshare_IMG_20220818_155047.jpg](../../_pics/figshare_IMG_20220818_155047.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.96 s | Guscio quasi pulito, con una crepa visibile sulla parte superiore.; verità: cracked |
| 152 | [commons_31.jpg](../../_pics/commons_31.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 4.01 s | L’uovo posteriore destro presenta macchie scure localizzate; tutti i gusci appaiono integri. |
| 153 | [figshare_IMG_20220818_155700.jpg](../../_pics/figshare_IMG_20220818_155700.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.27 s | Guscio con alcune piccole macchie e una sottile crepa visibile sul lato destro.; verità: cracked |
| 154 | [hf_sample44.jpg](../../_pics/hf_sample44.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 6.63 s | Un uovo marrone a sinistra presenta una sottile crepa; i gusci appaiono puliti. |
| 155 | [figshare_IMG_20220818_154613.jpg](../../_pics/figshare_IMG_20220818_154613.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 6.77 s | Guscio pulito, con una crepa sottile e visibile sul lato sinistro.; verità: cracked |
| 156 | [commons_38.jpg](../../_pics/commons_38.jpg) | poche uova | pulito | integro | accetta (A) | 5.54 s | Uovo intero; guscio senza crepe o sporco evidente, con solo minuscoli puntini. |
| 157 | [figshare_IMG_20220818_155436.jpg](../../_pics/figshare_IMG_20220818_155436.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.95 s | Uovo visibile con crepe nel guscio e piccole macchie localizzate.; verità: cracked |
| 158 | [commons_05.jpg](../../_pics/commons_05.jpg) | poche uova | pulito | integro | accetta (A) | 4.80 s | Uovo visibile con guscio pulito e integro, senza macchie o crepe evidenti. |
| 159 | [figshare_IMG_20220818_154407.jpg](../../_pics/figshare_IMG_20220818_154407.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.41 s | Il guscio presenta diverse crepe visibili e pochi piccoli segni di sporco.; verità: cracked |
| 160 | [hf_sample49.jpg](../../_pics/hf_sample49.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 6.06 s | Le uova appaiono pulite; un uovo marrone in basso a destra presenta una crepa visibile. |
| 161 | [figshare_IMG_20220818_155148.jpg](../../_pics/figshare_IMG_20220818_155148.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.15 s | Guscio con poche piccole macchie e una crepa visibile nella parte superiore.; verità: cracked |
| 162 | [hf_sample28.jpg](../../_pics/hf_sample28.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 8.21 s | L’uovo in basso a destra presenta piccole macchie rossastre; non si vedono crepe o rotture. |
| 163 | [figshare_IMG_20220818_155959.jpg](../../_pics/figshare_IMG_20220818_155959.jpg) | uovo singolo | sporco | crepato | **scarta**: crepato, sporco | 5.65 s | Guscio con macchie di sporco evidenti e una crepa visibile, senza perdita di contenuto.; verità: cracked |
| 164 | [hf_sample4.jpg](../../_pics/hf_sample4.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.11 s | Un uovo presenta piccole macchie sul guscio; non sono visibili crepe o rotture. |
| 165 | [figshare_IMG_20220818_155744.jpg](../../_pics/figshare_IMG_20220818_155744.jpg) | uovo singolo | pulito | integro | accetta (A) | 6.61 s | Uovo visibile, guscio pulito e senza crepe o rotture evidenti.; verità: cracked |
| 166 | [hf_sample36.jpg](../../_pics/hf_sample36.jpg) | cartone con più uova | pulito | crepato | **scarta**: crepato | 7.47 s | Uova visibili; una presenta una sottile crepa, mentre i gusci appaiono puliti. |
| 167 | [figshare_IMG_20220818_154731.jpg](../../_pics/figshare_IMG_20220818_154731.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.97 s | Guscio con una crepa visibile e alcune piccole macchie di sporco.; verità: cracked |
| 168 | [commons_09.jpg](../../_pics/commons_09.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 8.14 s | Uovo pulito, con una sottile linea simile a una crepa visibile nella parte superiore del guscio. |
| 169 | [figshare_IMG_20220818_154544.jpg](../../_pics/figshare_IMG_20220818_154544.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.69 s | Piccole macchie e puntini sul guscio; è visibile una sottile crepa nella parte inferiore.; verità: cracked |
| 170 | [hf_sample51.jpg](../../_pics/hf_sample51.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 8.74 s | Un uovo presenta una piccola macchia chiara sul guscio; non sono visibili crepe o rotture. |
| 171 | [figshare_IMG_20220818_154218.jpg](../../_pics/figshare_IMG_20220818_154218.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.98 s | Piccole macchie sparse sul guscio e una sottile crepa longitudinale visibile.; verità: cracked |
| 172 | [commons_21.jpg](../../_pics/commons_21.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 7.01 s | L’uovo in basso a destra presenta piccole macchie rossastre; non si vedono crepe né rotture. |
| 173 | [figshare_IMG_20220818_160033.jpg](../../_pics/figshare_IMG_20220818_160033.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.66 s | Uovo intero visibile, con crepe ramificate nel guscio e pochi piccoli puntini di sporco.; verità: cracked |
| 174 | [hf_sample6.jpg](../../_pics/hf_sample6.jpg) | cartone con più uova | pulito | integro | accetta (A) | 5.92 s | Le uova visibili hanno gusci puliti, senza macchie, crepe o rotture. |
| 175 | [figshare_IMG_20220818_155523.jpg](../../_pics/figshare_IMG_20220818_155523.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 5.51 s | Uovo intero con poche macchioline sul guscio; non si notano crepe né rotture.; verità: cracked |
| 176 | [commons_02.jpg](../../_pics/commons_02.jpg) | poche uova | lievemente sporco | integro | accetta (B) | 5.46 s | L’uovo marrone presenta poche piccole macchie; non si vedono crepe o rotture. |
| 177 | [figshare_IMG_20220818_154011.jpg](../../_pics/figshare_IMG_20220818_154011.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 7.08 s | Piccole macchie sparse sul guscio; non si vedono crepe né rotture.; verità: cracked |
| 178 | [commons_28.jpg](../../_pics/commons_28.jpg) | poche uova | lievemente sporco | crepato | **scarta**: crepato | 8.33 s | L’uovo bianco presenta piccole macchie; sul guscio marrone è visibile una sottile crepa. |
| 179 | [figshare_IMG_20220818_154708.jpg](../../_pics/figshare_IMG_20220818_154708.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.17 s | Piccole macchie visibili sul guscio e una crepa sottile, senza rotture o fuoriuscite.; verità: cracked |
| 180 | [commons_33.jpg](../../_pics/commons_33.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 6.76 s | L’uovo centrale presenta una crepa visibile; i gusci appaiono puliti. |
| 181 | [figshare_IMG_20220818_155812.jpg](../../_pics/figshare_IMG_20220818_155812.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 8.73 s | Uovo intero, con poche macchioline superficiali; non si vedono crepe né rotture.; verità: cracked |
| 182 | [commons_35.jpg](../../_pics/commons_35.jpg) | poche uova | pulito | integro | accetta (A) | 4.97 s | Uovo intero, guscio pulito senza sporco significativo né crepe visibili. |
| 183 | [figshare_IMG_20220818_155915.jpg](../../_pics/figshare_IMG_20220818_155915.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 5.86 s | Guscio pulito, con una sottile crepa visibile nella parte inferiore.; verità: cracked |
| 184 | [commons_07.jpg](../../_pics/commons_07.jpg) | poche uova | pulito | integro | accetta (A) | 6.75 s | Le uova sono intere; le macchioline dell’uovo centrale sembrano pigmentazione naturale del guscio. |
| 185 | [figshare_IMG_20220818_153638.jpg](../../_pics/figshare_IMG_20220818_153638.jpg) | uovo singolo | lievemente sporco | integro | accetta (B) | 7.85 s | Uovo intero con piccoli puntini e macchie sparse sul guscio; non si vedono crepe.; verità: cracked |
| 186 | [commons_29.jpg](../../_pics/commons_29.jpg) | poche uova | pulito | integro | accetta (A) | 5.07 s | Uovo intero con guscio apparentemente pulito e senza crepe o rotture visibili. |
| 187 | [figshare_IMG_20220818_155503.jpg](../../_pics/figshare_IMG_20220818_155503.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 5.62 s | Uovo con una crepa visibile e piccole macchie di sporco sul guscio.; verità: cracked |
| 188 | [hf_sample45.jpg](../../_pics/hf_sample45.jpg) | cartone con più uova | lievemente sporco | integro | accetta (B) | 6.25 s | Un uovo marrone presenta una piccola macchia chiara; tutti i gusci appaiono integri. |
| 189 | [figshare_IMG_20220818_154847.jpg](../../_pics/figshare_IMG_20220818_154847.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 6.96 s | Uovo con macchie di sporco localizzate e una crepa sottile visibile sul guscio.; verità: cracked |
| 190 | [hf_sample21.jpg](../../_pics/hf_sample21.jpg) | cartone con più uova | pulito | integro | accetta (A) | 7.78 s | Le uova visibili hanno gusci puliti e integri; si notano solo piccoli timbri. |
| 191 | [figshare_IMG_20220818_154328.jpg](../../_pics/figshare_IMG_20220818_154328.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.81 s | Guscio quasi pulito, con una sottile crepa visibile nella parte inferiore.; verità: cracked |
| 192 | [commons_22.jpg](../../_pics/commons_22.jpg) | poche uova | sporco | integro | **scarta**: sporco | 8.04 s | L’uovo bianco presenta macchie e residui evidenti sul guscio; non si vedono crepe o rotture. |
| 193 | [figshare_IMG_20220818_154724.jpg](../../_pics/figshare_IMG_20220818_154724.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 7.36 s | Uovo intero con una crepa visibile nel guscio e poche piccole macchie.; verità: cracked |
| 194 | [commons_44.jpg](../../_pics/commons_44.jpg) | poche uova | sporco | rotto | non valutabile | 7.09 s | L’uovo è rotto, con guscio in frammenti e contenuto fuoriuscito. |
| 195 | [figshare_IMG_20220818_155132.jpg](../../_pics/figshare_IMG_20220818_155132.jpg) | uovo singolo | pulito | crepato | **scarta**: crepato | 4.78 s | Guscio quasi pulito, con una crepa sottile visibile ma senza rotture o fuoriuscite.; verità: cracked |
| 196 | [commons_40.jpg](../../_pics/commons_40.jpg) | poche uova | pulito | crepato | **scarta**: crepato | 8.04 s | L’uovo in primo piano presenta crepe evidenti, ma non si vedono parti mancanti o contenuto fuoriuscito. |
| 197 | [figshare_IMG_20220818_154905.jpg](../../_pics/figshare_IMG_20220818_154905.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 3.84 s | Uovo con macchie localizzate e una crepa sottile visibile sul guscio.; verità: cracked |
| 198 | [commons_41.jpg](../../_pics/commons_41.jpg) | poche uova | lievemente sporco | rotto | **scarta**: rotto | 5.35 s | Un uovo presenta un’apertura con guscio mancante; sono visibili anche piccole macchie sul guscio. |
| 199 | [figshare_IMG_20220818_154943.jpg](../../_pics/figshare_IMG_20220818_154943.jpg) | uovo singolo | lievemente sporco | crepato | **scarta**: crepato | 4.22 s | Piccole macchie sul guscio e una crepa sottile visibile, senza parti mancanti.; verità: cracked |
| 200 | [commons_24.jpg](../../_pics/commons_24.jpg) | poche uova | pulito | integro | accetta (A) | 4.06 s | Uovo intero, guscio senza sporco significativo né crepe visibili. |

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.64 s · token 2572 in / 85 out · costo $0.000364
- **Motivazione del modello**: Uovo intero con alcune piccole macchie scure sul guscio, senza crepe o rotture visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 11.09 s · token 3278 in / 303 out · costo $0.000561
- **Motivazione del modello**: Tre uova visibili; gusci puliti, senza crepe o rotture evidenti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.03 s · token 2572 in / 104 out · costo $0.000373
- **Motivazione del modello**: Sono visibili piccole macchie e una sottile crepa sul guscio, senza rotture né fuoriuscite.

</details>

<details>
<summary><b>4. commons_03.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_03.jpg" alt="commons_03.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_3145g.jpg](https://commons.wikimedia.org/wiki/File:Eggs_3145g.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: StaraBlazkova
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1000x669
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.08 s · token 1203 in / 112 out · costo $0.000206
- **Motivazione del modello**: Le uova sono visibili; i gusci non mostrano sporco significativo né crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.07 s · token 2572 in / 81 out · costo $0.000362
- **Motivazione del modello**: Uovo pulito con crepe visibili nel guscio, senza parti mancanti né fuoriuscite.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.32 s · token 2572 in / 215 out · costo $0.000429
- **Motivazione del modello**: Le uova sono pulite; un uovo marrone presenta una crepa visibile nel guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.67 s · token 2572 in / 93 out · costo $0.000368
- **Motivazione del modello**: Uovo intero con alcune macchie di sporco localizzate; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.91 s · token 2572 in / 97 out · costo $0.000370
- **Motivazione del modello**: Quattro uova visibili; gusci puliti, senza macchie significative né crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.28 s · token 2572 in / 86 out · costo $0.000364
- **Motivazione del modello**: Uovo intero con poche macchie marroni localizzate sul guscio; non si vedono crepe.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.35 s · token 2449 in / 80 out · costo $0.000346
- **Motivazione del modello**: Uovo intero con guscio uniforme, senza sporco evidente né crepe visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.86 s · token 2572 in / 117 out · costo $0.000380
- **Motivazione del modello**: Guscio con pochi piccoli puntini di sporco; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.20 s · token 2572 in / 93 out · costo $0.000368
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e senza crepe o rotture; i timbri sono ammessi.

</details>

<details>
<summary><b>13. figshare_IMG_20220818_160114.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160114.jpg" alt="figshare_IMG_20220818_160114.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160114.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.03 s · token 2572 in / 130 out · costo $0.000386
- **Motivazione del modello**: Uovo intero con una sottile crepa visibile e poche piccole macchie sul guscio.

</details>

<details>
<summary><b>14. commons_36.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_36.jpg" alt="commons_36.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:FreeRangeEgg.jpg](https://commons.wikimedia.org/wiki/File:FreeRangeEgg.jpg)
- **Licenza**: CC BY-SA 3.0
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1000x825
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.42 s · token 1395 in / 163 out · costo $0.000256
- **Motivazione del modello**: Guscio pulito, con un sottile segno lineare visibile compatibile con una crepa.

</details>

<details>
<summary><b>15. figshare_IMG_20220818_155859.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155859.jpg" alt="figshare_IMG_20220818_155859.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155859.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.57 s · token 2572 in / 47 out · costo $0.000345
- **Motivazione del modello**: Uovo pulito con una crepa visibile nella parte inferiore del guscio.

</details>

<details>
<summary><b>16. hf_sample3.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample3.jpg" alt="hf_sample3.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample3.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample3.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.63 s · token 2572 in / 125 out · costo $0.000384
- **Motivazione del modello**: Le uova visibili hanno gusci integri e puliti; i piccoli segni sembrano puntini o timbri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.59 s · token 2572 in / 98 out · costo $0.000370
- **Motivazione del modello**: Uovo visibile con poche macchie sul guscio e una crepa sottile; il guscio è ancora intero.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.88 s · token 3278 in / 79 out · costo $0.000449
- **Motivazione del modello**: Uovo visibile con guscio pulito, senza macchie evidenti né crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.72 s · token 2572 in / 119 out · costo $0.000381
- **Motivazione del modello**: Uovo con sporco localizzato nella parte inferiore e una crepa visibile sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.88 s · token 2572 in / 121 out · costo $0.000382
- **Motivazione del modello**: L’uovo marrone in basso presenta piccole macchie sul guscio; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.64 s · token 2572 in / 84 out · costo $0.000363
- **Motivazione del modello**: Guscio con poche macchie piccole; non sono visibili crepe o rotture.

</details>

<details>
<summary><b>22. hf_sample9.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample9.jpg" alt="hf_sample9.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample9.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample9.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.43 s · token 2572 in / 225 out · costo $0.000434
- **Motivazione del modello**: Le uova sono pulite; una presenta una sottile crepa visibile sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.76 s · token 2572 in / 104 out · costo $0.000373
- **Motivazione del modello**: Piccole macchie sul guscio e una crepa visibile, senza perdita di contenuto.

</details>

<details>
<summary><b>24. commons_18.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_18.jpg" alt="commons_18.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Spiral_of_Brown_Eggs.jpg](https://commons.wikimedia.org/wiki/File:Spiral_of_Brown_Eggs.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Krugglesuvu
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1273x1554
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.75 s · token 2749 in / 160 out · costo $0.000424
- **Motivazione del modello**: Le uova sono intere; i puntini visibili sembrano pigmentazione naturale del guscio, senza sporco evidente.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.80 s · token 2572 in / 92 out · costo $0.000367
- **Motivazione del modello**: Uovo intero visibile, con poche macchie superficiali e crepe nel guscio senza aperture.

</details>

<details>
<summary><b>26. commons_23.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_23.jpg" alt="commons_23.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_(7177637421).jpg](https://commons.wikimedia.org/wiki/File:Eggs_(7177637421).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: James Bowe
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.68 s · token 2572 in / 118 out · costo $0.000380
- **Motivazione del modello**: Un guscio presenta piccoli residui e macchie sparse; non si vedono crepe o rotture.

</details>

<details>
<summary><b>27. figshare_IMG_20220818_155457.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155457.jpg" alt="figshare_IMG_20220818_155457.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155457.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 10.05 s · token 2572 in / 290 out · costo $0.000466
- **Motivazione del modello**: Uovo intero, con piccole macchie e irregolarità superficiali; non si distinguono crepe o rotture.

</details>

<details>
<summary><b>28. hf_sample8.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample8.jpg" alt="hf_sample8.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample8.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample8.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.16 s · token 2572 in / 233 out · costo $0.000438
- **Motivazione del modello**: Un uovo presenta una sottile linea visibile sul guscio; gli altri appaiono puliti e integri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.75 s · token 2572 in / 95 out · costo $0.000369
- **Motivazione del modello**: Guscio con poche piccole macchie; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.22 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: Le uova visibili hanno gusci puliti, senza crepe o rotture; i piccoli segni rosa sono stampe.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.83 s · token 2572 in / 126 out · costo $0.000384
- **Motivazione del modello**: Uovo con guscio quasi pulito; è visibile una sottile crepa sulla superficie.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.93 s · token 2572 in / 216 out · costo $0.000429
- **Motivazione del modello**: Un uovo bianco presenta una sottile linea simile a una crepa; sono visibili anche piccole macchie sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.88 s · token 2572 in / 154 out · costo $0.000398
- **Motivazione del modello**: Guscio molto sporco, con macchie diffuse e una zona scheggiata con membrana esposta.

</details>

<details>
<summary><b>34. commons_27.jpg</b> · scarta: sporco</summary>

<img src="../../_pics/commons_27.jpg" alt="commons_27.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Spotted_Brown_Chicken_Eggs_(5719609727).jpg](https://commons.wikimedia.org/wiki/File:Spotted_Brown_Chicken_Eggs_(5719609727).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: spiralmushroom
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1043
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: scarta: sporco
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.90 s · token 2337 in / 280 out · costo $0.000432
- **Motivazione del modello**: L’uovo in basso a sinistra presenta numerose macchie scure diffuse; non si vedono crepe o rotture.

</details>

<details>
<summary><b>35. figshare_IMG_20220818_154535.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154535.jpg" alt="figshare_IMG_20220818_154535.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154535.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.04 s · token 2572 in / 148 out · costo $0.000395
- **Motivazione del modello**: Uovo intero; guscio con pochi puntini e lievi aloni, senza crepe evidenti.

</details>

<details>
<summary><b>36. hf_sample13.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample13.jpg" alt="hf_sample13.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample13.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample13.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.92 s · token 2572 in / 388 out · costo $0.000515
- **Motivazione del modello**: Le uova sono pulite; su un guscio si nota una sottile linea simile a una crepa.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.54 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: Presenti piccole macchie sul guscio e una sottile crepa visibile sul lato sinistro.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.65 s · token 2572 in / 132 out · costo $0.000387
- **Motivazione del modello**: Un uovo presenta piccoli segni superficiali; non sono visibili crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.96 s · token 2572 in / 94 out · costo $0.000368
- **Motivazione del modello**: Uovo intero, con piccole macchie di sporco sul guscio e nessuna crepa visibile.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.88 s · token 2337 in / 92 out · costo $0.000338
- **Motivazione del modello**: Il guscio appare pulito e integro, senza macchie significative né crepe visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.75 s · token 2572 in / 92 out · costo $0.000367
- **Motivazione del modello**: Guscio pulito, con una sottile crepa visibile sul lato destro.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.14 s · token 2572 in / 72 out · costo $0.000357
- **Motivazione del modello**: Uovo visibile con guscio pulito e senza crepe o rotture.

</details>

<details>
<summary><b>43. figshare_IMG_20220818_155137.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155137.jpg" alt="figshare_IMG_20220818_155137.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155137.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.06 s · token 2572 in / 170 out · costo $0.000406
- **Motivazione del modello**: Si notano piccoli residui sul guscio e una sottile linea simile a una crepa.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.96 s · token 1058 in / 141 out · costo $0.000203
- **Motivazione del modello**: Uovo intero con una macchia rossa estesa sul guscio; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.73 s · token 2572 in / 226 out · costo $0.000434
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa diagonale visibile.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.46 s · token 3160 in / 48 out · costo $0.000419
- **Motivazione del modello**: Uovo intero con guscio pulito, senza macchie evidenti né crepe.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.44 s · token 2572 in / 152 out · costo $0.000397
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa visibile sul lato sinistro.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.68 s · token 2337 in / 126 out · costo $0.000355
- **Motivazione del modello**: I gusci visibili appaiono puliti e integri; i piccoli puntini sembrano pigmentazione naturale.

</details>

<details>
<summary><b>49. figshare_IMG_20220818_154759.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154759.jpg" alt="figshare_IMG_20220818_154759.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154759.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.82 s · token 2572 in / 126 out · costo $0.000384
- **Motivazione del modello**: Uovo intero con poche macchie localizzate sul guscio; non si notano crepe o rotture.

</details>

<details>
<summary><b>50. commons_47.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_47.jpg" alt="commons_47.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B4-001.jpg](https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B4-001.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: OhWeh
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.70 s · token 2572 in / 70 out · costo $0.000356
- **Motivazione del modello**: Non è visibile alcun uovo di gallina.

</details>

<details>
<summary><b>51. figshare_IMG_20220818_155540.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155540.jpg" alt="figshare_IMG_20220818_155540.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155540.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.09 s · token 2572 in / 53 out · costo $0.000348
- **Motivazione del modello**: L’uovo è intero ma presenta una crepa visibile e pochi piccoli puntini sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.87 s · token 2572 in / 109 out · costo $0.000376
- **Motivazione del modello**: Un uovo presenta una piccola macchia rosa sul guscio; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.99 s · token 2572 in / 223 out · costo $0.000433
- **Motivazione del modello**: Uovo con poche macchie scure e una sottile crepa visibile sul guscio.

</details>

<details>
<summary><b>54. hf_sample33.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample33.jpg" alt="hf_sample33.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample33.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample33.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.79 s · token 2572 in / 271 out · costo $0.000457
- **Motivazione del modello**: Un uovo presenta una sottile crepa visibile; un altro ha una piccola macchia sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.06 s · token 2572 in / 92 out · costo $0.000367
- **Motivazione del modello**: Uovo visibile con guscio pulito e una crepa evidente, senza perdita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.46 s · token 2572 in / 78 out · costo $0.000360
- **Motivazione del modello**: Uovo intero con guscio uniforme, senza sporco o crepe visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.59 s · token 2572 in / 56 out · costo $0.000349
- **Motivazione del modello**: Uovo intero con poche piccole macchie sul guscio; non si notano crepe o rotture.

</details>

<details>
<summary><b>58. commons_48.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_48.jpg" alt="commons_48.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B16-001.jpg](https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B16-001.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: OhWeh
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.24 s · token 2572 in / 91 out · costo $0.000367
- **Motivazione del modello**: Non è visibile alcun uovo di gallina intero.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.26 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: Il guscio appare pulito, ma presenta una sottile crepa visibile nella parte inferiore.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.02 s · token 2572 in / 108 out · costo $0.000375
- **Motivazione del modello**: Un uovo presenta una piccola macchia sul guscio; non si vedono crepe o rotture.

</details>

<details>
<summary><b>61. figshare_IMG_20220818_155851.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155851.jpg" alt="figshare_IMG_20220818_155851.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155851.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.85 s · token 2572 in / 118 out · costo $0.000380
- **Motivazione del modello**: Piccoli puntini scuri sul guscio e una sottile crepa verticale visibile.

</details>

<details>
<summary><b>62. hf_sample29.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample29.jpg" alt="hf_sample29.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample29.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample29.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.36 s · token 2572 in / 127 out · costo $0.000385
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e senza crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.58 s · token 2572 in / 127 out · costo $0.000385
- **Motivazione del modello**: Uovo pulito; è visibile una sottile crepa sulla parte superiore del guscio.

</details>

<details>
<summary><b>64. hf_sample37.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample37.jpg" alt="hf_sample37.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample37.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample37.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.29 s · token 2572 in / 261 out · costo $0.000452
- **Motivazione del modello**: Un uovo presenta una sottile crepa; sul guscio di un altro si vede una macchia grigiastra.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.64 s · token 2572 in / 124 out · costo $0.000383
- **Motivazione del modello**: Guscio con poche macchioline e una sottile crepa visibile sulla superficie.

</details>

<details>
<summary><b>66. hf_sample40.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample40.jpg" alt="hf_sample40.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample40.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample40.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.12 s · token 2572 in / 126 out · costo $0.000384
- **Motivazione del modello**: Alcuni gusci presentano piccole macchie; nessuna crepa o rottura visibile.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.17 s · token 2572 in / 78 out · costo $0.000360
- **Motivazione del modello**: Uovo pulito, con una crepa visibile sul guscio senza perdita di contenuto.

</details>

<details>
<summary><b>68. hf_sample41.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample41.jpg" alt="hf_sample41.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample41.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample41.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.04 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: Un uovo presenta una piccola macchia rossastra; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.35 s · token 2572 in / 101 out · costo $0.000372
- **Motivazione del modello**: Uovo visibile con poche macchie superficiali e una crepa sottile, senza rotture né fuoriuscite.

</details>

<details>
<summary><b>70. hf_sample43.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample43.jpg" alt="hf_sample43.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample43.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample43.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.24 s · token 2572 in / 223 out · costo $0.000433
- **Motivazione del modello**: Un uovo presenta una sottile crepa; si notano anche piccoli segni isolati sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.92 s · token 2572 in / 115 out · costo $0.000379
- **Motivazione del modello**: Uovo visibile con alcune lievi macchie e una crepa sottile sul guscio.

</details>

<details>
<summary><b>72. commons_20.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_20.jpg" alt="commons_20.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Different_colored_chicken_eggs-01ASD.jpg](https://commons.wikimedia.org/wiki/File:Different_colored_chicken_eggs-01ASD.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Asurnipal
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1567x1532
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.39 s · token 3219 in / 156 out · costo $0.000480
- **Motivazione del modello**: Un uovo presenta piccole macchie superficiali; tutti i gusci appaiono integri, senza crepe o rotture visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.65 s · token 2572 in / 155 out · costo $0.000399
- **Motivazione del modello**: Guscio con macchie diffuse e una porzione mancante; è visibile la membrana sottostante.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.99 s · token 2572 in / 109 out · costo $0.000376
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e integri; i timbri non indicano sporco o danni.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.93 s · token 2572 in / 140 out · costo $0.000391
- **Motivazione del modello**: Uovo visibile con alcune piccole macchie e una crepa con lembo di guscio sollevato.

</details>

<details>
<summary><b>76. commons_49.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/commons_49.jpg" alt="commons_49.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Strange_brown_egg.jpg](https://commons.wikimedia.org/wiki/File:Strange_brown_egg.jpg)
- **Licenza**: CC0 · **Autore**: Smallman12q
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1401
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto, sporco
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.47 s · token 2984 in / 132 out · costo $0.000439
- **Motivazione del modello**: Ampia zona sporca e lesionata, con guscio sfondato e materiale esposto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 10.24 s · token 2572 in / 100 out · costo $0.000371
- **Motivazione del modello**: Uovo con macchie di sporco localizzate e una crepa sottile visibile sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.02 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: L’uovo centrale presenta una piccola macchia; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.57 s · token 2572 in / 106 out · costo $0.000374
- **Motivazione del modello**: Piccole macchie concentrate sul lato destro e una sottile crepa visibile al centro del guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.72 s · token 2337 in / 113 out · costo $0.000349
- **Motivazione del modello**: Entrambe le uova hanno gusci integri e puliti; si vedono solo minuscoli puntini.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.43 s · token 2572 in / 91 out · costo $0.000367
- **Motivazione del modello**: Guscio con poche macchie e una crepa visibile, senza pezzi mancanti né fuoriuscite.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 9.29 s · token 2572 in / 418 out · costo $0.000530
- **Motivazione del modello**: Un uovo presenta una piccola frattura sul bordo inferiore; le altre macchie sono puntini minimi.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.46 s · token 2572 in / 95 out · costo $0.000369
- **Motivazione del modello**: Uovo intero con alcune piccole macchie e una crepa visibile, senza perdita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.86 s · token 2572 in / 221 out · costo $0.000432
- **Motivazione del modello**: Uova visibili con gusci puliti e senza crepe o rotture evidenti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.62 s · token 2572 in / 86 out · costo $0.000364
- **Motivazione del modello**: Uovo intero con poche piccole macchie sul guscio; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.09 s · token 2572 in / 184 out · costo $0.000413
- **Motivazione del modello**: I gusci sono quasi puliti, ma si notano piccoli puntini; non sono visibili crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.07 s · token 2572 in / 122 out · costo $0.000382
- **Motivazione del modello**: Uovo pulito, con una frattura visibile sul guscio; non si osservano pezzi mancanti né fuoriuscite.

</details>

<details>
<summary><b>88. commons_14.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_14.jpg" alt="commons_14.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Deux_oeufs_bruns.jpg](https://commons.wikimedia.org/wiki/File:Deux_oeufs_bruns.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Jeangagnon
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.98 s · token 2572 in / 106 out · costo $0.000374
- **Motivazione del modello**: L’uovo a sinistra presenta piccoli puntini; entrambi i gusci appaiono integri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.49 s · token 2572 in / 117 out · costo $0.000380
- **Motivazione del modello**: Guscio con poche piccole macchie e una crepa visibile, senza perdita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.80 s · token 2572 in / 111 out · costo $0.000377
- **Motivazione del modello**: Un uovo presenta piccole macchie sul guscio; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.41 s · token 2572 in / 110 out · costo $0.000376
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa visibile nella parte centrale.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.86 s · token 2572 in / 112 out · costo $0.000377
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e senza crepe o rotture; il timbro è ammesso.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.46 s · token 2572 in / 56 out · costo $0.000349
- **Motivazione del modello**: Uovo pulito, con una crepa visibile sul guscio; non si vedono rotture o fuoriuscite.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.30 s · token 2572 in / 81 out · costo $0.000362
- **Motivazione del modello**: Entrambe le uova sono visibili, con gusci puliti e senza crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.54 s · token 2572 in / 102 out · costo $0.000372
- **Motivazione del modello**: Piccole macchie sul guscio e una crepa visibile, senza rottura o perdita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.10 s · token 2337 in / 93 out · costo $0.000339
- **Motivazione del modello**: Le uova hanno gusci integri e senza sporco visibile; i piccoli puntini sembrano naturali.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.13 s · token 2572 in / 111 out · costo $0.000377
- **Motivazione del modello**: Guscio con poche macchie e puntini; non si osservano crepe o rotture.

</details>

<details>
<summary><b>98. hf_sample35.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample35.jpg" alt="hf_sample35.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample35.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample35.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 9.41 s · token 2572 in / 346 out · costo $0.000494
- **Motivazione del modello**: Le uova visibili sono integre e non presentano sporco significativo.

</details>

<details>
<summary><b>99. figshare_IMG_20220818_154557.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154557.jpg" alt="figshare_IMG_20220818_154557.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154557.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.87 s · token 2572 in / 149 out · costo $0.000396
- **Motivazione del modello**: Guscio con pochi piccoli aloni e una sottile linea simile a una crepa sul lato sinistro.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.75 s · token 2572 in / 140 out · costo $0.000391
- **Motivazione del modello**: L'uovo in basso a destra presenta una piccola macchia sul guscio; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.34 s · token 2572 in / 82 out · costo $0.000362
- **Motivazione del modello**: Uovo intero con poche piccole macchie sul guscio; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.08 s · token 2572 in / 119 out · costo $0.000381
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e integri; si notano solo piccoli timbri di stampa.

</details>

<details>
<summary><b>103. figshare_IMG_20220818_160014.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160014.jpg" alt="figshare_IMG_20220818_160014.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160014.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.64 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: Guscio con macchie di sporco localizzate e una crepa visibile, senza pezzi mancanti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.56 s · token 2572 in / 117 out · costo $0.000380
- **Motivazione del modello**: Un uovo presenta piccoli aloni e residui sul guscio; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.62 s · token 2572 in / 91 out · costo $0.000367
- **Motivazione del modello**: Guscio con poche macchie e una crepa sottile visibile nella parte superiore.

</details>

<details>
<summary><b>106. hf_sample18.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample18.jpg" alt="hf_sample18.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample18.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample18.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.01 s · token 2572 in / 131 out · costo $0.000387
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e integri; i piccoli segni rosa sono timbri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.74 s · token 2572 in / 97 out · costo $0.000370
- **Motivazione del modello**: Uovo visibile con una crepa sottile e poche piccole macchie sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.38 s · token 2572 in / 168 out · costo $0.000405
- **Motivazione del modello**: Un uovo presenta piccoli puntini e aloni sul guscio; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.33 s · token 2572 in / 106 out · costo $0.000374
- **Motivazione del modello**: Guscio con poche macchie brune localizzate e una crepa visibile, senza perdita di contenuto.

</details>

<details>
<summary><b>110. hf_sample32.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample32.jpg" alt="hf_sample32.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample32.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample32.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.74 s · token 2572 in / 135 out · costo $0.000389
- **Motivazione del modello**: Le uova visibili hanno gusci puliti, senza sporco significativo né crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.53 s · token 2572 in / 95 out · costo $0.000369
- **Motivazione del modello**: Uovo pulito, con crepe visibili sul guscio ma senza rotture o perdita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.41 s · token 2572 in / 149 out · costo $0.000396
- **Motivazione del modello**: Le uova sono integre; una presenta piccoli segni scuri visibili sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.44 s · token 2572 in / 102 out · costo $0.000372
- **Motivazione del modello**: Guscio con piccole macchie e una crepa visibile, senza pezzi mancanti né contenuto fuoriuscito.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.15 s · token 2396 in / 142 out · costo $0.000370
- **Motivazione del modello**: Guscio con poche piccole macchie scure; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.97 s · token 2572 in / 99 out · costo $0.000371
- **Motivazione del modello**: Uovo visibile con poche macchie superficiali e una sottile crepa nel guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.47 s · token 2572 in / 327 out · costo $0.000485
- **Motivazione del modello**: Le uova visibili hanno gusci puliti, senza crepe o rotture evidenti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.74 s · token 2572 in / 79 out · costo $0.000361
- **Motivazione del modello**: Guscio pulito, con una crepa visibile ma senza parti mancanti.

</details>

<details>
<summary><b>118. commons_39.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_39.jpg" alt="commons_39.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huehnereier_2989.jpg](https://commons.wikimedia.org/wiki/File:Huehnereier_2989.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: Rüdiger Wölk       This photo was taken by Rüdiger Wölk.  Please credit this photo Rüdiger Wölk, Münster.    View all photos (large page) of Rüdiger Wölk  I would also appreciate an email to rudiger.wolk@gmail.com with details of use. Für Hinweise auf Veröffentlichungen (rudiger.wolk@gmail.com) oder Belegexemplare bin ich Ihnen dankbar.
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.08 s · token 2337 in / 154 out · costo $0.000369
- **Motivazione del modello**: Alcuni gusci presentano piccole macchie; non si notano crepe o rotture.

</details>

<details>
<summary><b>119. figshare_IMG_20220818_154319.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154319.jpg" alt="figshare_IMG_20220818_154319.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154319.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.20 s · token 2572 in / 150 out · costo $0.000396
- **Motivazione del modello**: Guscio con pochi puntini di sporco e una sottile crepa visibile, senza rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.54 s · token 2572 in / 95 out · costo $0.000369
- **Motivazione del modello**: Entrambe le uova sono intere; una presenta piccole macchie marroni sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.28 s · token 2572 in / 104 out · costo $0.000373
- **Motivazione del modello**: Uovo con alcune piccole macchie e una crepa ramificata; il guscio è ancora in un pezzo.

</details>

<details>
<summary><b>122. hf_sample24.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample24.jpg" alt="hf_sample24.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample24.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample24.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.49 s · token 2572 in / 278 out · costo $0.000460
- **Motivazione del modello**: Le uova sono intere; si vedono solo piccoli puntini e pigmentazioni naturali, senza sporco evidente o crepe.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.55 s · token 2572 in / 114 out · costo $0.000378
- **Motivazione del modello**: Uovo intero con poche macchioline sul guscio; non si notano crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.72 s · token 2572 in / 122 out · costo $0.000382
- **Motivazione del modello**: L’uovo marrone in basso presenta piccoli segni sul guscio; non si vedono crepe o rotture.

</details>

<details>
<summary><b>125. figshare_IMG_20220818_155717.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155717.jpg" alt="figshare_IMG_20220818_155717.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155717.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.12 s · token 2572 in / 114 out · costo $0.000378
- **Motivazione del modello**: Uovo intero, con pochi piccoli puntini sul guscio; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.44 s · token 2572 in / 118 out · costo $0.000380
- **Motivazione del modello**: L’uovo marrone in basso a destra presenta una crepa visibile; gli altri gusci appaiono puliti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.77 s · token 2572 in / 134 out · costo $0.000388
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa visibile.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.05 s · token 2572 in / 164 out · costo $0.000403
- **Motivazione del modello**: Un uovo presenta piccoli segni superficiali; non si vedono crepe o rotture.

</details>

<details>
<summary><b>129. figshare_IMG_20220818_155804.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155804.jpg" alt="figshare_IMG_20220818_155804.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155804.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.25 s · token 2572 in / 191 out · costo $0.000417
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa visibile sul lato sinistro.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.42 s · token 2572 in / 152 out · costo $0.000397
- **Motivazione del modello**: L’uovo a sinistra presenta una piccola macchia chiara; entrambi i gusci appaiono integri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.26 s · token 2572 in / 140 out · costo $0.000391
- **Motivazione del modello**: Guscio con poche macchie nella parte inferiore e una crepa visibile, senza fuoriuscita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.00 s · token 2572 in / 111 out · costo $0.000377
- **Motivazione del modello**: L’uovo in basso a destra presenta piccole macchie sul guscio, senza crepe o rotture visibili.

</details>

<details>
<summary><b>133. figshare_IMG_20220818_155724.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155724.jpg" alt="figshare_IMG_20220818_155724.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155724.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 10.02 s · token 2572 in / 119 out · costo $0.000381
- **Motivazione del modello**: Guscio con poche piccole macchie; non si notano crepe o rotture.

</details>

<details>
<summary><b>134. commons_46.jpg</b> · scarta: rotto</summary>

<img src="../../_pics/commons_46.jpg" alt="commons_46.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Cracked_(85516059).jpeg](https://commons.wikimedia.org/wiki/File:Cracked_(85516059).jpeg)
- **Licenza**: CC BY 3.0 · **Autore**: Cyd Haselton
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1041
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.69 s · token 2337 in / 242 out · costo $0.000413
- **Motivazione del modello**: Uovo visibile, con guscio sfondato e frammenti mancanti; non si notano sporcizia o macchie sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.70 s · token 2572 in / 86 out · costo $0.000364
- **Motivazione del modello**: Uovo intero con poche piccole macchie sul guscio, senza crepe né rotture visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.09 s · token 2572 in / 109 out · costo $0.000376
- **Motivazione del modello**: Un uovo presenta piccoli puntini e macchie superficiali; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.69 s · token 2572 in / 137 out · costo $0.000390
- **Motivazione del modello**: Poche macchie sparse sul guscio; è visibile una crepa irregolare, ma l’uovo è ancora in un pezzo.

</details>

<details>
<summary><b>138. hf_sample50.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample50.jpg" alt="hf_sample50.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample50.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample50.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 13.43 s · token 2572 in / 506 out · costo $0.000574
- **Motivazione del modello**: Uova intere; un guscio presenta un piccolo residuo visibile, senza crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.75 s · token 2572 in / 121 out · costo $0.000382
- **Motivazione del modello**: Piccole macchie sul guscio e crepe visibili, ma il guscio è ancora in un pezzo.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.78 s · token 2572 in / 187 out · costo $0.000415
- **Motivazione del modello**: Un uovo intero è visibile; i gusci in primo piano sono rotti in più pezzi.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.96 s · token 2572 in / 120 out · costo $0.000381
- **Motivazione del modello**: Guscio con poche macchie e una crepa visibile, ma senza rotture o fuoriuscite.

</details>

<details>
<summary><b>142. commons_26.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_26.jpg" alt="commons_26.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Just_lying_there_being_pretty_(4301382316).jpg](https://commons.wikimedia.org/wiki/File:Just_lying_there_being_pretty_(4301382316).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: storebukkebruse
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.41 s · token 2572 in / 124 out · costo $0.000383
- **Motivazione del modello**: Uova integre; una presenta una piccola macchia scura sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.50 s · token 2572 in / 51 out · costo $0.000347
- **Motivazione del modello**: Uovo intero senza crepe visibili; presenta poche piccole macchie sul guscio.

</details>

<details>
<summary><b>144. commons_43.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_43.jpg" alt="commons_43.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Broken_egg_orange.jpg](https://commons.wikimedia.org/wiki/File:Broken_egg_orange.jpg)
- **Licenza**: CC BY 3.0 · **Autore**: Goldmund100
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1490
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.99 s · token 3160 in / 153 out · costo $0.000471
- **Motivazione del modello**: Uovo sfondato con guscio frantumato e contenuto fuoriuscito; nessun uovo intero visibile.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.19 s · token 2572 in / 174 out · costo $0.000408
- **Motivazione del modello**: Uovo pulito, con una crepa evidente sul guscio; non si vedono fuoriuscite.

</details>

<details>
<summary><b>146. commons_08.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_08.jpg" alt="commons_08.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Giriraja_eggs.jpg](https://commons.wikimedia.org/wiki/File:Giriraja_eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Netha Hussain
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.81 s · token 2572 in / 165 out · costo $0.000404
- **Motivazione del modello**: Le uova hanno gusci senza sporco evidente né crepe o rotture; i puntini sembrano pigmentazione naturale.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.22 s · token 2572 in / 130 out · costo $0.000386
- **Motivazione del modello**: Piccole macchie sul guscio e una sottile crepa visibile nella parte superiore.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.32 s · token 2572 in / 55 out · costo $0.000349
- **Motivazione del modello**: Uova intere senza crepe; alcune presentano piccoli segni rossastri e puntini sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.79 s · token 2572 in / 91 out · costo $0.000367
- **Motivazione del modello**: Uovo visibile con una crepa sul guscio e alcune piccole macchie superficiali.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.11 s · token 1719 in / 69 out · costo $0.000249
- **Motivazione del modello**: Uovo intero con guscio uniforme, senza sporco né crepe visibili.

</details>

<details>
<summary><b>151. figshare_IMG_20220818_155047.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155047.jpg" alt="figshare_IMG_20220818_155047.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155047.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.96 s · token 2572 in / 106 out · costo $0.000374
- **Motivazione del modello**: Guscio quasi pulito, con una crepa visibile sulla parte superiore.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.01 s · token 2337 in / 109 out · costo $0.000347
- **Motivazione del modello**: L’uovo posteriore destro presenta macchie scure localizzate; tutti i gusci appaiono integri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.27 s · token 2572 in / 101 out · costo $0.000372
- **Motivazione del modello**: Guscio con alcune piccole macchie e una sottile crepa visibile sul lato destro.

</details>

<details>
<summary><b>154. hf_sample44.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample44.jpg" alt="hf_sample44.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample44.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample44.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.63 s · token 2572 in / 240 out · costo $0.000441
- **Motivazione del modello**: Un uovo marrone a sinistra presenta una sottile crepa; i gusci appaiono puliti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.77 s · token 2572 in / 123 out · costo $0.000383
- **Motivazione del modello**: Guscio pulito, con una crepa sottile e visibile sul lato sinistro.

</details>

<details>
<summary><b>156. commons_38.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_38.jpg" alt="commons_38.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Ei01.jpg](https://commons.wikimedia.org/wiki/File:Ei01.jpg)
- **Licenza**: Public domain · **Autore**: No machine-readable author provided. Acf assumed (based on copyright claims).
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 955x858
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.54 s · token 1369 in / 125 out · costo $0.000234
- **Motivazione del modello**: Uovo intero; guscio senza crepe o sporco evidente, con solo minuscoli puntini.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.95 s · token 2572 in / 95 out · costo $0.000369
- **Motivazione del modello**: Uovo visibile con crepe nel guscio e piccole macchie localizzate.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.80 s · token 2455 in / 80 out · costo $0.000347
- **Motivazione del modello**: Uovo visibile con guscio pulito e integro, senza macchie o crepe evidenti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.41 s · token 2572 in / 100 out · costo $0.000371
- **Motivazione del modello**: Il guscio presenta diverse crepe visibili e pochi piccoli segni di sporco.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.06 s · token 2572 in / 187 out · costo $0.000415
- **Motivazione del modello**: Le uova appaiono pulite; un uovo marrone in basso a destra presenta una crepa visibile.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.15 s · token 2572 in / 89 out · costo $0.000366
- **Motivazione del modello**: Guscio con poche piccole macchie e una crepa visibile nella parte superiore.

</details>

<details>
<summary><b>162. hf_sample28.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample28.jpg" alt="hf_sample28.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample28.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample28.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.21 s · token 2572 in / 129 out · costo $0.000386
- **Motivazione del modello**: L’uovo in basso a destra presenta piccole macchie rossastre; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.65 s · token 2572 in / 107 out · costo $0.000375
- **Motivazione del modello**: Guscio con macchie di sporco evidenti e una crepa visibile, senza perdita di contenuto.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.11 s · token 2572 in / 144 out · costo $0.000393
- **Motivazione del modello**: Un uovo presenta piccole macchie sul guscio; non sono visibili crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.61 s · token 2572 in / 120 out · costo $0.000381
- **Motivazione del modello**: Uovo visibile, guscio pulito e senza crepe o rotture evidenti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.47 s · token 2572 in / 233 out · costo $0.000438
- **Motivazione del modello**: Uova visibili; una presenta una sottile crepa, mentre i gusci appaiono puliti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.97 s · token 2572 in / 96 out · costo $0.000369
- **Motivazione del modello**: Guscio con una crepa visibile e alcune piccole macchie di sporco.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.14 s · token 1661 in / 222 out · costo $0.000319
- **Motivazione del modello**: Uovo pulito, con una sottile linea simile a una crepa visibile nella parte superiore del guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.69 s · token 2572 in / 108 out · costo $0.000375
- **Motivazione del modello**: Piccole macchie e puntini sul guscio; è visibile una sottile crepa nella parte inferiore.

</details>

<details>
<summary><b>170. hf_sample51.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample51.jpg" alt="hf_sample51.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample51.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample51.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.74 s · token 2572 in / 175 out · costo $0.000409
- **Motivazione del modello**: Un uovo presenta una piccola macchia chiara sul guscio; non sono visibili crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.98 s · token 2572 in / 173 out · costo $0.000408
- **Motivazione del modello**: Piccole macchie sparse sul guscio e una sottile crepa longitudinale visibile.

</details>

<details>
<summary><b>172. commons_21.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_21.jpg" alt="commons_21.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Six_eggs_views_from_the_top_on_a_white_background.jpg](https://commons.wikimedia.org/wiki/File:Six_eggs_views_from_the_top_on_a_white_background.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: TudorTulok
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1244
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.01 s · token 2690 in / 242 out · costo $0.000457
- **Motivazione del modello**: L’uovo in basso a destra presenta piccole macchie rossastre; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.66 s · token 2572 in / 111 out · costo $0.000377
- **Motivazione del modello**: Uovo intero visibile, con crepe ramificate nel guscio e pochi piccoli puntini di sporco.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.92 s · token 2572 in / 97 out · costo $0.000370
- **Motivazione del modello**: Le uova visibili hanno gusci puliti, senza macchie, crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.51 s · token 2572 in / 107 out · costo $0.000375
- **Motivazione del modello**: Uovo intero con poche macchioline sul guscio; non si notano crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.46 s · token 2278 in / 98 out · costo $0.000334
- **Motivazione del modello**: L’uovo marrone presenta poche piccole macchie; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.08 s · token 2572 in / 91 out · costo $0.000367
- **Motivazione del modello**: Piccole macchie sparse sul guscio; non si vedono crepe né rotture.

</details>

<details>
<summary><b>178. commons_28.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_28.jpg" alt="commons_28.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_eggs_21.jpg](https://commons.wikimedia.org/wiki/File:Chicken_eggs_21.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: BogTar201213
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1172
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: crepato (`cracked`)
- **Decisione**: scarta: crepato
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.33 s · token 2572 in / 166 out · costo $0.000404
- **Motivazione del modello**: L’uovo bianco presenta piccole macchie; sul guscio marrone è visibile una sottile crepa.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.17 s · token 2572 in / 116 out · costo $0.000379
- **Motivazione del modello**: Piccole macchie visibili sul guscio e una crepa sottile, senza rotture o fuoriuscite.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.76 s · token 2572 in / 99 out · costo $0.000371
- **Motivazione del modello**: L’uovo centrale presenta una crepa visibile; i gusci appaiono puliti.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.73 s · token 2572 in / 260 out · costo $0.000451
- **Motivazione del modello**: Uovo intero, con poche macchioline superficiali; non si vedono crepe né rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.97 s · token 2572 in / 154 out · costo $0.000398
- **Motivazione del modello**: Uovo intero, guscio pulito senza sporco significativo né crepe visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.86 s · token 2572 in / 125 out · costo $0.000384
- **Motivazione del modello**: Guscio pulito, con una sottile crepa visibile nella parte inferiore.

</details>

<details>
<summary><b>184. commons_07.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_07.jpg" alt="commons_07.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_colours.jpg](https://commons.wikimedia.org/wiki/File:Egg_colours.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Timothy Titus
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x922
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.75 s · token 2102 in / 234 out · costo $0.000380
- **Motivazione del modello**: Le uova sono intere; le macchioline dell’uovo centrale sembrano pigmentazione naturale del guscio.

</details>

<details>
<summary><b>185. figshare_IMG_20220818_153638.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153638.jpg" alt="figshare_IMG_20220818_153638.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153638.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (B)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.85 s · token 2572 in / 54 out · costo $0.000348
- **Motivazione del modello**: Uovo intero con piccoli puntini e macchie sparse sul guscio; non si vedono crepe.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.07 s · token 2572 in / 78 out · costo $0.000360
- **Motivazione del modello**: Uovo intero con guscio apparentemente pulito e senza crepe o rotture visibili.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.62 s · token 2572 in / 88 out · costo $0.000365
- **Motivazione del modello**: Uovo con una crepa visibile e piccole macchie di sporco sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.25 s · token 2572 in / 227 out · costo $0.000435
- **Motivazione del modello**: Un uovo marrone presenta una piccola macchia chiara; tutti i gusci appaiono integri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 6.96 s · token 2572 in / 104 out · costo $0.000373
- **Motivazione del modello**: Uovo con macchie di sporco localizzate e una crepa sottile visibile sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.78 s · token 2572 in / 104 out · costo $0.000373
- **Motivazione del modello**: Le uova visibili hanno gusci puliti e integri; si notano solo piccoli timbri.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.81 s · token 2572 in / 143 out · costo $0.000393
- **Motivazione del modello**: Guscio quasi pulito, con una sottile crepa visibile nella parte inferiore.

</details>

<details>
<summary><b>192. commons_22.jpg</b> · scarta: sporco</summary>

<img src="../../_pics/commons_22.jpg" alt="commons_22.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Diff%C3%A9rents_oeufs.jpg](https://commons.wikimedia.org/wiki/File:Diff%C3%A9rents_oeufs.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Tylwyth Eldar
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: integro (`intact`)
- **Decisione**: scarta: sporco
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.04 s · token 2337 in / 100 out · costo $0.000342
- **Motivazione del modello**: L’uovo bianco presenta macchie e residui evidenti sul guscio; non si vedono crepe o rotture.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.36 s · token 2572 in / 129 out · costo $0.000386
- **Motivazione del modello**: Uovo intero con una crepa visibile nel guscio e poche piccole macchie.

</details>

<details>
<summary><b>194. commons_44.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_44.jpg" alt="commons_44.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huevo_Quebrado.jpg](https://commons.wikimedia.org/wiki/File:Huevo_Quebrado.jpg)
- **Licenza**: Public domain · **Autore**: Jorge Barrios
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 965x723
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.00
- **Pulizia**: sporco (`dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: non valutabile
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 7.09 s · token 1252 in / 139 out · costo $0.000226
- **Motivazione del modello**: L’uovo è rotto, con guscio in frammenti e contenuto fuoriuscito.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.78 s · token 2572 in / 158 out · costo $0.000400
- **Motivazione del modello**: Guscio quasi pulito, con una crepa sottile visibile ma senza rotture o fuoriuscite.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 8.04 s · token 2866 in / 119 out · costo $0.000418
- **Motivazione del modello**: L’uovo in primo piano presenta crepe evidenti, ma non si vedono parti mancanti o contenuto fuoriuscito.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 3.84 s · token 2572 in / 51 out · costo $0.000347
- **Motivazione del modello**: Uovo con macchie localizzate e una crepa sottile visibile sul guscio.

</details>

<details>
<summary><b>198. commons_41.jpg</b> · scarta: rotto</summary>

<img src="../../_pics/commons_41.jpg" alt="commons_41.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Bloody-eggs.jpg](https://commons.wikimedia.org/wiki/File:Bloody-eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Maqi
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 900x675
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 1.00
- **Pulizia**: lievemente sporco (`slightly_dirty`)
- **Integrità**: rotto (`broken`)
- **Decisione**: scarta: rotto
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 5.35 s · token 1162 in / 139 out · costo $0.000215
- **Motivazione del modello**: Un uovo presenta un’apertura con guscio mancante; sono visibili anche piccole macchie sul guscio.

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
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.22 s · token 2572 in / 111 out · costo $0.000377
- **Motivazione del modello**: Piccole macchie sul guscio e una crepa sottile visibile, senza parti mancanti.

</details>

<details>
<summary><b>200. commons_24.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_24.jpg" alt="commons_24.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_(394351849).jpg](https://commons.wikimedia.org/wiki/File:Egg_(394351849).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: liz west from Boxborough, MA, USA
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1550x1549
- **Verità nota**: nessuna
- **Uovo visibile**: 1.00
- **Pulizia**: pulito (`clean`)
- **Integrità**: integro (`intact`)
- **Decisione**: accetta (A)
- **Chiamata**: modello `openai/gpt-6-luna` · latenza 4.06 s · token 3278 in / 122 out · costo $0.000471
- **Motivazione del modello**: Uovo intero, guscio senza sporco significativo né crepe visibili.

</details>
