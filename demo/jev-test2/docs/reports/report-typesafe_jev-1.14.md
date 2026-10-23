# Rapporto di analisi uova: Jev 1.14

- **Modello richiesto**: `typesafe/jev-1.14`
- **Modello servito**: `typesafe/jev-1.14-20261014`
- **Interfaccia**: OpenRouter Decisions API (`POST /api/alpha/decisions`), risposte tipizzate con probabilità
- **Data analisi**: 23 ottobre 2026 alle ore 17:37
- **Foto analizzate**: 200 su 200

## Riepilogo

| Esito | Foto | Quota |
| --- | ---: | ---: |
| Accettate (grado A, pulite e integre) | 61 | 30.5% |
| Accettate (grado B, lievemente sporche) | 50 | 25.0% |
| **Scartate** (rotte, crepate o sporche) | 82 | 41.0% |
| Non valutabili (uovo non rilevato) | 7 | 3.5% |

Motivi di scarto (una foto può averne più d'uno): crepato 77, rotto 5, sporco 5, uovo non rilevato 7.

| Pulizia | Foto |  | Integrità | Foto |
| --- | ---: | --- | --- | ---: |
| pulito | 99 |  | integro | 113 |
| lievemente sporco | 95 |  | crepato | 78 |
| sporco | 6 |  | rotto | 9 |

Etichette con confidenza sotto 0.6, segnalate "da verificare": 97.

### Per tipo di scena

| Scena | Foto | Accettate | Scartate | Non valutabili |
| --- | ---: | ---: | ---: | ---: |
| uovo singolo | 100 | 30 | 69 | 1 |
| poche uova | 49 | 37 | 6 | 6 |
| cartone con più uova | 51 | 44 | 7 | 0 |

### Confronto con la verità nota

Solo le foto Figshare hanno una verità annotata a mano (crepe). Le altre foto non hanno etichette, quindi per pulizia e per le foto Commons/Hugging Face non esiste una misura di accuratezza.

- Uova crepate note: **70 su 100** riconosciute come crepate o rotte (70.0%).
- Le crepe di questo dataset sono sottili e le foto sono ridotte a 1568 px: è una prova difficile, non rappresentativa delle rotture evidenti.

### Tempi e costi

| Metrica | Valore |
| --- | ---: |
| Latenza media | 0.35 s |
| Latenza p50 | 0.31 s |
| Latenza p95 | 0.62 s |
| Token in ingresso | 1069390 |
| Token in uscita | 20554 |
| Costo totale (da `usage.cost`) | $0.0449 |
| Costo per 1000 foto | $0.2246 |

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

Tra parentesi la probabilità dell'etichetta scelta; "Conf." è la confidenza dichiarata dal modello (campo `confidence`), che può essere più bassa della probabilità. Sotto 0.6 la riga è segnalata "da verificare".

| # | Foto | Scena | Pulizia | Conf. | Integrità | Conf. | Decisione | Latenza | Note |
| ---: | --- | --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 1 | [figshare_IMG_20220818_154808.jpg](../../_pics/figshare_IMG_20220818_154808.jpg) | uovo singolo | lievemente sporco (0.81) | 0.72 | integro (0.98) | 0.97 | accetta (B) | 0.61 s | verità: cracked |
| 2 | [commons_04.jpg](../../_pics/commons_04.jpg) | poche uova | pulito (0.81) | 0.72 | integro (0.63) | 0.45 | accetta (A) | 0.62 s | da verificare |
| 3 | [figshare_IMG_20220818_154045.jpg](../../_pics/figshare_IMG_20220818_154045.jpg) | uovo singolo | lievemente sporco (0.66) | 0.49 | crepato (0.65) | 0.48 | **scarta**: crepato | 0.61 s | da verificare; verità: cracked |
| 4 | [commons_03.jpg](../../_pics/commons_03.jpg) | poche uova | lievemente sporco (0.63) | 0.45 | integro (0.58) | 0.37 | accetta (B) | 0.55 s | da verificare |
| 5 | [figshare_IMG_20220818_155841.jpg](../../_pics/figshare_IMG_20220818_155841.jpg) | uovo singolo | pulito (0.89) | 0.83 | crepato (0.99) | 0.98 | **scarta**: crepato | 0.30 s | verità: cracked |
| 6 | [hf_sample47.jpg](../../_pics/hf_sample47.jpg) | cartone con più uova | pulito (0.80) | 0.70 | crepato (0.89) | 0.83 | **scarta**: crepato | 0.37 s |  |
| 7 | [figshare_IMG_20220818_155248.jpg](../../_pics/figshare_IMG_20220818_155248.jpg) | uovo singolo | lievemente sporco (0.95) | 0.92 | integro (0.94) | 0.91 | accetta (B) | 0.30 s | verità: cracked |
| 8 | [commons_30.jpg](../../_pics/commons_30.jpg) | poche uova | pulito (0.86) | 0.79 | integro (0.95) | 0.92 | accetta (A) | 0.31 s |  |
| 9 | [figshare_IMG_20220818_155341.jpg](../../_pics/figshare_IMG_20220818_155341.jpg) | uovo singolo | lievemente sporco (0.95) | 0.92 | integro (0.95) | 0.92 | accetta (B) | 0.28 s | verità: cracked |
| 10 | [commons_15.jpg](../../_pics/commons_15.jpg) | poche uova | pulito (0.90) | 0.85 | integro (0.98) | 0.97 | accetta (A) | 0.35 s |  |
| 11 | [figshare_IMG_20220818_153759.jpg](../../_pics/figshare_IMG_20220818_153759.jpg) | uovo singolo | lievemente sporco (0.80) | 0.70 | integro (0.98) | 0.97 | accetta (B) | 0.60 s | verità: cracked |
| 12 | [hf_sample7.jpg](../../_pics/hf_sample7.jpg) | cartone con più uova | pulito (0.90) | 0.85 | integro (0.87) | 0.80 | accetta (A) | 0.62 s |  |
| 13 | [figshare_IMG_20220818_160114.jpg](../../_pics/figshare_IMG_20220818_160114.jpg) | uovo singolo | pulito (0.73) | 0.59 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.56 s | da verificare; verità: cracked |
| 14 | [commons_36.jpg](../../_pics/commons_36.jpg) | poche uova | pulito (0.88) | 0.82 | crepato (0.69) | 0.53 | **scarta**: crepato | 0.64 s | da verificare |
| 15 | [figshare_IMG_20220818_155859.jpg](../../_pics/figshare_IMG_20220818_155859.jpg) | uovo singolo | pulito (0.57) | 0.35 | crepato (0.93) | 0.89 | **scarta**: crepato | 0.29 s | da verificare; verità: cracked |
| 16 | [hf_sample3.jpg](../../_pics/hf_sample3.jpg) | cartone con più uova | pulito (0.74) | 0.61 | integro (0.91) | 0.86 | accetta (A) | 0.31 s |  |
| 17 | [figshare_IMG_20220818_155422.jpg](../../_pics/figshare_IMG_20220818_155422.jpg) | uovo singolo | lievemente sporco (0.98) | 0.97 | crepato (0.97) | 0.95 | **scarta**: crepato | 0.27 s | verità: cracked |
| 18 | [commons_25.jpg](../../_pics/commons_25.jpg) | poche uova | pulito (0.86) | 0.79 | integro (0.99) | 0.98 | accetta (A) | 0.33 s |  |
| 19 | [figshare_IMG_20220818_154854.jpg](../../_pics/figshare_IMG_20220818_154854.jpg) | uovo singolo | lievemente sporco (0.95) | 0.92 | crepato (0.88) | 0.82 | **scarta**: crepato | 0.30 s | verità: cracked |
| 20 | [hf_sample30.jpg](../../_pics/hf_sample30.jpg) | cartone con più uova | lievemente sporco (0.68) | 0.52 | integro (0.95) | 0.92 | accetta (B) | 0.28 s | da verificare |
| 21 | [figshare_IMG_20220818_154019.jpg](../../_pics/figshare_IMG_20220818_154019.jpg) | uovo singolo | lievemente sporco (0.72) | 0.58 | integro (0.96) | 0.94 | accetta (B) | 1.39 s | da verificare; verità: cracked |
| 22 | [hf_sample9.jpg](../../_pics/hf_sample9.jpg) | cartone con più uova | pulito (0.94) | 0.91 | integro (0.95) | 0.92 | accetta (A) | 0.30 s |  |
| 23 | [figshare_IMG_20220818_154949.jpg](../../_pics/figshare_IMG_20220818_154949.jpg) | uovo singolo | lievemente sporco (0.71) | 0.56 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.26 s | da verificare; verità: cracked |
| 24 | [commons_18.jpg](../../_pics/commons_18.jpg) | poche uova | pulito (0.47) | 0.20 | integro (0.97) | 0.95 | accetta (A) | 0.32 s | da verificare |
| 25 | [figshare_IMG_20220818_155415.jpg](../../_pics/figshare_IMG_20220818_155415.jpg) | uovo singolo | lievemente sporco (0.94) | 0.91 | crepato (0.91) | 0.86 | **scarta**: crepato | 0.31 s | verità: cracked |
| 26 | [commons_23.jpg](../../_pics/commons_23.jpg) | poche uova | lievemente sporco (0.76) | 0.64 | integro (0.94) | 0.91 | accetta (B) | 0.32 s |  |
| 27 | [figshare_IMG_20220818_155457.jpg](../../_pics/figshare_IMG_20220818_155457.jpg) | uovo singolo | lievemente sporco (0.79) | 0.69 | integro (0.67) | 0.51 | accetta (B) | 0.27 s | da verificare; verità: cracked |
| 28 | [hf_sample8.jpg](../../_pics/hf_sample8.jpg) | cartone con più uova | pulito (0.89) | 0.83 | integro (0.93) | 0.89 | accetta (A) | 0.34 s |  |
| 29 | [figshare_IMG_20220818_154636.jpg](../../_pics/figshare_IMG_20220818_154636.jpg) | uovo singolo | lievemente sporco (0.60) | 0.40 | integro (0.94) | 0.91 | accetta (B) | 0.43 s | da verificare; verità: cracked |
| 30 | [hf_sample20.jpg](../../_pics/hf_sample20.jpg) | cartone con più uova | pulito (0.92) | 0.88 | integro (0.94) | 0.91 | accetta (A) | 0.31 s |  |
| 31 | [figshare_IMG_20220818_154528.jpg](../../_pics/figshare_IMG_20220818_154528.jpg) | uovo singolo | pulito (0.67) | 0.51 | crepato (0.91) | 0.86 | **scarta**: crepato | 0.30 s | da verificare; verità: cracked |
| 32 | [hf_sample34.jpg](../../_pics/hf_sample34.jpg) | cartone con più uova | pulito (0.82) | 0.73 | crepato (0.66) | 0.49 | **scarta**: crepato | 0.31 s | da verificare |
| 33 | [figshare_IMG_20220818_160007.jpg](../../_pics/figshare_IMG_20220818_160007.jpg) | uovo singolo | sporco (0.76) | 0.64 | rotto (0.62) | 0.43 | **scarta**: rotto, sporco | 0.26 s | da verificare; verità: cracked |
| 34 | [commons_27.jpg](../../_pics/commons_27.jpg) | poche uova | lievemente sporco (0.52) | 0.28 | integro (0.72) | 0.58 | accetta (B) | 0.27 s | da verificare |
| 35 | [figshare_IMG_20220818_154535.jpg](../../_pics/figshare_IMG_20220818_154535.jpg) | uovo singolo | pulito (0.64) | 0.46 | integro (0.68) | 0.52 | accetta (A) | 0.38 s | da verificare; verità: cracked |
| 36 | [hf_sample13.jpg](../../_pics/hf_sample13.jpg) | cartone con più uova | pulito (0.89) | 0.83 | integro (0.93) | 0.89 | accetta (A) | 0.33 s |  |
| 37 | [figshare_IMG_20220818_155015.jpg](../../_pics/figshare_IMG_20220818_155015.jpg) | uovo singolo | lievemente sporco (0.89) | 0.83 | crepato (0.87) | 0.80 | **scarta**: crepato | 1.22 s | verità: cracked |
| 38 | [hf_sample46.jpg](../../_pics/hf_sample46.jpg) | cartone con più uova | pulito (0.64) | 0.46 | integro (0.80) | 0.70 | accetta (A) | 0.29 s | da verificare |
| 39 | [figshare_IMG_20220818_155401.jpg](../../_pics/figshare_IMG_20220818_155401.jpg) | uovo singolo | lievemente sporco (0.96) | 0.94 | integro (0.98) | 0.97 | accetta (B) | 0.32 s | verità: cracked |
| 40 | [commons_34.jpg](../../_pics/commons_34.jpg) | poche uova | pulito (0.81) | 0.72 | integro (0.99) | 0.98 | accetta (A) | 0.33 s |  |
| 41 | [figshare_IMG_20220818_155709.jpg](../../_pics/figshare_IMG_20220818_155709.jpg) | uovo singolo | pulito (0.71) | 0.56 | crepato (0.97) | 0.95 | **scarta**: crepato | 0.31 s | da verificare; verità: cracked |
| 42 | [commons_32.jpg](../../_pics/commons_32.jpg) | poche uova | pulito (0.93) | 0.89 | integro (0.99) | 0.98 | accetta (A) | 0.39 s |  |
| 43 | [figshare_IMG_20220818_155137.jpg](../../_pics/figshare_IMG_20220818_155137.jpg) | uovo singolo | lievemente sporco (0.51) | 0.27 | integro (0.78) | 0.67 | accetta (B) | 0.28 s | da verificare; verità: cracked |
| 44 | [commons_42.jpg](../../_pics/commons_42.jpg) | poche uova | sporco (0.98) | 0.97 | rotto (0.96) | 0.94 | **scarta**: rotto, sporco | 0.26 s |  |
| 45 | [figshare_IMG_20220818_155511.jpg](../../_pics/figshare_IMG_20220818_155511.jpg) | uovo singolo | lievemente sporco (0.74) | 0.61 | integro (0.74) | 0.61 | accetta (B) | 0.26 s | verità: cracked |
| 46 | [commons_16.jpg](../../_pics/commons_16.jpg) | poche uova | pulito (0.90) | 0.85 | integro (0.87) | 0.80 | accetta (A) | 0.39 s |  |
| 47 | [figshare_IMG_20220818_154136.jpg](../../_pics/figshare_IMG_20220818_154136.jpg) | uovo singolo | lievemente sporco (0.70) | 0.55 | integro (0.56) | 0.34 | accetta (B) | 0.31 s | da verificare; verità: cracked |
| 48 | [commons_19.jpg](../../_pics/commons_19.jpg) | poche uova | pulito (0.75) | 0.62 | integro (0.89) | 0.83 | accetta (A) | 0.27 s |  |
| 49 | [figshare_IMG_20220818_154759.jpg](../../_pics/figshare_IMG_20220818_154759.jpg) | uovo singolo | lievemente sporco (0.75) | 0.62 | integro (0.95) | 0.92 | accetta (B) | 0.32 s | verità: cracked |
| 50 | [commons_47.jpg](../../_pics/commons_47.jpg) | poche uova | lievemente sporco (0.57) | 0.35 | integro (0.84) | 0.76 | non valutabile | 0.28 s |  |
| 51 | [figshare_IMG_20220818_155540.jpg](../../_pics/figshare_IMG_20220818_155540.jpg) | uovo singolo | pulito (0.64) | 0.46 | crepato (0.98) | 0.97 | **scarta**: crepato | 0.60 s | da verificare; verità: cracked |
| 52 | [hf_sample17.jpg](../../_pics/hf_sample17.jpg) | cartone con più uova | pulito (0.83) | 0.74 | integro (0.89) | 0.83 | accetta (A) | 0.65 s |  |
| 53 | [figshare_IMG_20220818_154226.jpg](../../_pics/figshare_IMG_20220818_154226.jpg) | uovo singolo | lievemente sporco (0.64) | 0.46 | crepato (0.92) | 0.88 | **scarta**: crepato | 0.72 s | da verificare; verità: cracked |
| 54 | [hf_sample33.jpg](../../_pics/hf_sample33.jpg) | cartone con più uova | pulito (0.79) | 0.69 | crepato (0.81) | 0.72 | **scarta**: crepato | 0.70 s |  |
| 55 | [figshare_IMG_20220818_155846.jpg](../../_pics/figshare_IMG_20220818_155846.jpg) | uovo singolo | pulito (0.84) | 0.76 | crepato (0.99) | 0.98 | **scarta**: crepato | 0.28 s | verità: cracked |
| 56 | [commons_11.jpg](../../_pics/commons_11.jpg) | poche uova | pulito (0.78) | 0.67 | integro (0.98) | 0.97 | accetta (A) | 0.33 s |  |
| 57 | [figshare_IMG_20220818_153842.jpg](../../_pics/figshare_IMG_20220818_153842.jpg) | uovo singolo | lievemente sporco (0.76) | 0.64 | integro (0.98) | 0.97 | accetta (B) | 0.33 s | verità: cracked |
| 58 | [commons_48.jpg](../../_pics/commons_48.jpg) | poche uova | lievemente sporco (0.50) | 0.25 | integro (0.92) | 0.88 | non valutabile | 0.29 s |  |
| 59 | [figshare_IMG_20220818_160129.jpg](../../_pics/figshare_IMG_20220818_160129.jpg) | uovo singolo | pulito (0.74) | 0.61 | crepato (0.60) | 0.40 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 60 | [hf_sample2.jpg](../../_pics/hf_sample2.jpg) | cartone con più uova | lievemente sporco (0.67) | 0.51 | integro (0.90) | 0.85 | accetta (B) | 0.33 s | da verificare |
| 61 | [figshare_IMG_20220818_155851.jpg](../../_pics/figshare_IMG_20220818_155851.jpg) | uovo singolo | pulito (0.76) | 0.64 | crepato (0.65) | 0.48 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 62 | [hf_sample29.jpg](../../_pics/hf_sample29.jpg) | cartone con più uova | pulito (0.85) | 0.77 | integro (0.85) | 0.77 | accetta (A) | 0.37 s |  |
| 63 | [figshare_IMG_20220818_154436.jpg](../../_pics/figshare_IMG_20220818_154436.jpg) | uovo singolo | pulito (0.62) | 0.43 | crepato (0.89) | 0.83 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 64 | [hf_sample37.jpg](../../_pics/hf_sample37.jpg) | cartone con più uova | pulito (0.84) | 0.76 | crepato (0.60) | 0.40 | **scarta**: crepato | 0.58 s | da verificare |
| 65 | [figshare_IMG_20220818_154051.jpg](../../_pics/figshare_IMG_20220818_154051.jpg) | uovo singolo | lievemente sporco (0.61) | 0.41 | crepato (0.61) | 0.41 | **scarta**: crepato | 0.33 s | da verificare; verità: cracked |
| 66 | [hf_sample40.jpg](../../_pics/hf_sample40.jpg) | cartone con più uova | pulito (0.50) | 0.25 | integro (0.81) | 0.72 | accetta (A) | 0.34 s | da verificare |
| 67 | [figshare_IMG_20220818_155910.jpg](../../_pics/figshare_IMG_20220818_155910.jpg) | uovo singolo | pulito (0.89) | 0.83 | crepato (0.97) | 0.95 | **scarta**: crepato | 0.27 s | verità: cracked |
| 68 | [hf_sample41.jpg](../../_pics/hf_sample41.jpg) | cartone con più uova | pulito (0.69) | 0.53 | integro (0.64) | 0.46 | accetta (A) | 0.34 s | da verificare |
| 69 | [figshare_IMG_20220818_154057.jpg](../../_pics/figshare_IMG_20220818_154057.jpg) | uovo singolo | lievemente sporco (0.85) | 0.77 | crepato (0.95) | 0.92 | **scarta**: crepato | 0.30 s | verità: cracked |
| 70 | [hf_sample43.jpg](../../_pics/hf_sample43.jpg) | cartone con più uova | lievemente sporco (0.49) | 0.23 | integro (0.59) | 0.38 | accetta (B) | 0.40 s | da verificare |
| 71 | [figshare_IMG_20220818_154444.jpg](../../_pics/figshare_IMG_20220818_154444.jpg) | uovo singolo | pulito (0.52) | 0.28 | crepato (0.74) | 0.61 | **scarta**: crepato | 0.29 s | da verificare; verità: cracked |
| 72 | [commons_20.jpg](../../_pics/commons_20.jpg) | poche uova | pulito (0.56) | 0.34 | integro (0.97) | 0.95 | accetta (A) | 0.31 s | da verificare |
| 73 | [figshare_IMG_20220818_155948.jpg](../../_pics/figshare_IMG_20220818_155948.jpg) | uovo singolo | sporco (0.71) | 0.56 | rotto (0.65) | 0.48 | **scarta**: rotto, sporco | 0.27 s | da verificare; verità: cracked |
| 74 | [hf_sample11.jpg](../../_pics/hf_sample11.jpg) | cartone con più uova | pulito (0.90) | 0.85 | integro (0.93) | 0.89 | accetta (A) | 0.36 s |  |
| 75 | [figshare_IMG_20220818_155606.jpg](../../_pics/figshare_IMG_20220818_155606.jpg) | uovo singolo | lievemente sporco (0.75) | 0.62 | crepato (0.81) | 0.72 | **scarta**: crepato | 0.28 s | verità: cracked |
| 76 | [commons_49.jpg](../../_pics/commons_49.jpg) | poche uova | lievemente sporco (0.58) | 0.37 | rotto (0.58) | 0.37 | non valutabile | 0.30 s |  |
| 77 | [figshare_IMG_20220818_154914.jpg](../../_pics/figshare_IMG_20220818_154914.jpg) | uovo singolo | lievemente sporco (0.95) | 0.92 | crepato (0.81) | 0.72 | **scarta**: crepato | 0.28 s | verità: cracked |
| 78 | [hf_sample22.jpg](../../_pics/hf_sample22.jpg) | cartone con più uova | lievemente sporco (0.51) | 0.27 | integro (0.90) | 0.85 | accetta (B) | 0.30 s | da verificare |
| 79 | [figshare_IMG_20220818_155240.jpg](../../_pics/figshare_IMG_20220818_155240.jpg) | uovo singolo | lievemente sporco (0.96) | 0.94 | crepato (0.57) | 0.35 | **scarta**: crepato | 0.31 s | da verificare; verità: cracked |
| 80 | [commons_06.jpg](../../_pics/commons_06.jpg) | poche uova | pulito (0.92) | 0.88 | integro (0.99) | 0.98 | accetta (A) | 0.33 s |  |
| 81 | [figshare_IMG_20220818_160039.jpg](../../_pics/figshare_IMG_20220818_160039.jpg) | uovo singolo | lievemente sporco (0.78) | 0.67 | crepato (0.91) | 0.86 | **scarta**: crepato | 0.27 s | verità: cracked |
| 82 | [hf_sample42.jpg](../../_pics/hf_sample42.jpg) | cartone con più uova | pulito (0.83) | 0.74 | integro (0.91) | 0.86 | accetta (A) | 0.29 s |  |
| 83 | [figshare_IMG_20220818_154715.jpg](../../_pics/figshare_IMG_20220818_154715.jpg) | uovo singolo | lievemente sporco (0.82) | 0.73 | crepato (0.94) | 0.91 | **scarta**: crepato | 0.45 s | verità: cracked |
| 84 | [hf_sample12.jpg](../../_pics/hf_sample12.jpg) | cartone con più uova | pulito (0.93) | 0.89 | integro (0.92) | 0.88 | accetta (A) | 0.31 s |  |
| 85 | [figshare_IMG_20220818_154238.jpg](../../_pics/figshare_IMG_20220818_154238.jpg) | uovo singolo | lievemente sporco (0.68) | 0.52 | integro (0.92) | 0.88 | accetta (B) | 0.33 s | da verificare; verità: cracked |
| 86 | [hf_sample16.jpg](../../_pics/hf_sample16.jpg) | cartone con più uova | pulito (0.95) | 0.92 | integro (0.94) | 0.91 | accetta (A) | 0.34 s |  |
| 87 | [figshare_IMG_20220818_154413.jpg](../../_pics/figshare_IMG_20220818_154413.jpg) | uovo singolo | pulito (0.63) | 0.45 | crepato (0.93) | 0.89 | **scarta**: crepato | 0.25 s | da verificare; verità: cracked |
| 88 | [commons_14.jpg](../../_pics/commons_14.jpg) | poche uova | pulito (0.51) | 0.27 | integro (0.96) | 0.94 | accetta (A) | 0.37 s | da verificare |
| 89 | [figshare_IMG_20220818_155559.jpg](../../_pics/figshare_IMG_20220818_155559.jpg) | uovo singolo | lievemente sporco (0.86) | 0.79 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.30 s | verità: cracked |
| 90 | [hf_sample1.jpg](../../_pics/hf_sample1.jpg) | cartone con più uova | lievemente sporco (0.76) | 0.64 | integro (0.93) | 0.89 | accetta (B) | 0.29 s |  |
| 91 | [figshare_IMG_20220818_155517.jpg](../../_pics/figshare_IMG_20220818_155517.jpg) | uovo singolo | lievemente sporco (0.92) | 0.88 | crepato (0.76) | 0.64 | **scarta**: crepato | 0.26 s | verità: cracked |
| 92 | [hf_sample5.jpg](../../_pics/hf_sample5.jpg) | cartone con più uova | pulito (0.96) | 0.94 | integro (0.94) | 0.91 | accetta (A) | 1.37 s |  |
| 93 | [figshare_IMG_20220818_154429.jpg](../../_pics/figshare_IMG_20220818_154429.jpg) | uovo singolo | pulito (0.78) | 0.67 | crepato (0.95) | 0.92 | **scarta**: crepato | 0.26 s | verità: cracked |
| 94 | [commons_13.jpg](../../_pics/commons_13.jpg) | poche uova | pulito (0.87) | 0.80 | integro (0.98) | 0.97 | accetta (A) | 0.35 s |  |
| 95 | [figshare_IMG_20220818_160049.jpg](../../_pics/figshare_IMG_20220818_160049.jpg) | uovo singolo | lievemente sporco (0.77) | 0.66 | crepato (0.73) | 0.59 | **scarta**: crepato | 0.50 s | da verificare; verità: cracked |
| 96 | [commons_17.jpg](../../_pics/commons_17.jpg) | poche uova | pulito (0.80) | 0.70 | integro (0.95) | 0.92 | accetta (A) | 0.30 s |  |
| 97 | [figshare_IMG_20220818_155353.jpg](../../_pics/figshare_IMG_20220818_155353.jpg) | uovo singolo | lievemente sporco (0.88) | 0.82 | integro (0.92) | 0.88 | accetta (B) | 0.27 s | verità: cracked |
| 98 | [hf_sample35.jpg](../../_pics/hf_sample35.jpg) | cartone con più uova | pulito (0.77) | 0.66 | integro (0.76) | 0.64 | accetta (A) | 0.31 s |  |
| 99 | [figshare_IMG_20220818_154557.jpg](../../_pics/figshare_IMG_20220818_154557.jpg) | uovo singolo | pulito (0.57) | 0.35 | crepato (0.55) | 0.33 | **scarta**: crepato | 0.31 s | da verificare; verità: cracked |
| 100 | [hf_sample27.jpg](../../_pics/hf_sample27.jpg) | cartone con più uova | pulito (0.72) | 0.58 | integro (0.90) | 0.85 | accetta (A) | 0.28 s | da verificare |
| 101 | [figshare_IMG_20220818_153953.jpg](../../_pics/figshare_IMG_20220818_153953.jpg) | uovo singolo | lievemente sporco (0.63) | 0.45 | integro (0.98) | 0.97 | accetta (B) | 0.28 s | da verificare; verità: cracked |
| 102 | [hf_sample14.jpg](../../_pics/hf_sample14.jpg) | cartone con più uova | pulito (0.95) | 0.92 | integro (0.96) | 0.94 | accetta (A) | 0.30 s |  |
| 103 | [figshare_IMG_20220818_160014.jpg](../../_pics/figshare_IMG_20220818_160014.jpg) | uovo singolo | sporco (0.63) | 0.45 | crepato (0.60) | 0.40 | **scarta**: crepato, sporco | 0.28 s | da verificare; verità: cracked |
| 104 | [hf_sample19.jpg](../../_pics/hf_sample19.jpg) | cartone con più uova | pulito (0.56) | 0.34 | integro (0.95) | 0.92 | accetta (A) | 0.32 s | da verificare |
| 105 | [figshare_IMG_20220818_154113.jpg](../../_pics/figshare_IMG_20220818_154113.jpg) | uovo singolo | lievemente sporco (0.87) | 0.80 | crepato (0.83) | 0.74 | non valutabile | 0.29 s | verità: cracked |
| 106 | [hf_sample18.jpg](../../_pics/hf_sample18.jpg) | cartone con più uova | pulito (0.93) | 0.89 | integro (0.95) | 0.92 | accetta (A) | 0.28 s |  |
| 107 | [figshare_IMG_20220818_160123.jpg](../../_pics/figshare_IMG_20220818_160123.jpg) | uovo singolo | lievemente sporco (0.66) | 0.49 | crepato (0.99) | 0.98 | **scarta**: crepato | 0.32 s | da verificare; verità: cracked |
| 108 | [hf_sample26.jpg](../../_pics/hf_sample26.jpg) | cartone con più uova | pulito (0.63) | 0.45 | integro (0.90) | 0.85 | accetta (A) | 0.30 s | da verificare |
| 109 | [figshare_IMG_20220818_155430.jpg](../../_pics/figshare_IMG_20220818_155430.jpg) | uovo singolo | lievemente sporco (0.96) | 0.94 | crepato (0.89) | 0.83 | **scarta**: crepato | 0.27 s | verità: cracked |
| 110 | [hf_sample32.jpg](../../_pics/hf_sample32.jpg) | cartone con più uova | lievemente sporco (0.64) | 0.46 | integro (0.94) | 0.91 | accetta (B) | 0.29 s | da verificare |
| 111 | [figshare_IMG_20220818_154419.jpg](../../_pics/figshare_IMG_20220818_154419.jpg) | uovo singolo | pulito (0.73) | 0.59 | crepato (0.93) | 0.89 | **scarta**: crepato | 0.34 s | da verificare; verità: cracked |
| 112 | [hf_sample25.jpg](../../_pics/hf_sample25.jpg) | cartone con più uova | pulito (0.64) | 0.46 | integro (0.82) | 0.73 | accetta (A) | 0.37 s | da verificare |
| 113 | [figshare_IMG_20220818_160028.jpg](../../_pics/figshare_IMG_20220818_160028.jpg) | uovo singolo | lievemente sporco (0.65) | 0.48 | crepato (0.92) | 0.88 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 114 | [commons_01.jpg](../../_pics/commons_01.jpg) | poche uova | pulito (0.55) | 0.33 | integro (0.98) | 0.97 | accetta (A) | 0.28 s | da verificare |
| 115 | [figshare_IMG_20220818_160055.jpg](../../_pics/figshare_IMG_20220818_160055.jpg) | uovo singolo | lievemente sporco (0.74) | 0.61 | crepato (0.84) | 0.76 | **scarta**: crepato | 0.32 s | verità: cracked |
| 116 | [hf_sample10.jpg](../../_pics/hf_sample10.jpg) | cartone con più uova | pulito (0.94) | 0.91 | integro (0.94) | 0.91 | accetta (A) | 0.32 s |  |
| 117 | [figshare_IMG_20220818_155905.jpg](../../_pics/figshare_IMG_20220818_155905.jpg) | uovo singolo | pulito (0.94) | 0.91 | crepato (0.99) | 0.98 | **scarta**: crepato | 0.28 s | verità: cracked |
| 118 | [commons_39.jpg](../../_pics/commons_39.jpg) | poche uova | lievemente sporco (0.54) | 0.31 | integro (0.84) | 0.76 | accetta (B) | 0.43 s | da verificare |
| 119 | [figshare_IMG_20220818_154319.jpg](../../_pics/figshare_IMG_20220818_154319.jpg) | uovo singolo | lievemente sporco (0.52) | 0.28 | crepato (0.92) | 0.88 | **scarta**: crepato | 0.30 s | da verificare; verità: cracked |
| 120 | [commons_37.jpg](../../_pics/commons_37.jpg) | poche uova | lievemente sporco (0.88) | 0.82 | integro (0.98) | 0.97 | accetta (B) | 0.42 s |  |
| 121 | [figshare_IMG_20220818_160044.jpg](../../_pics/figshare_IMG_20220818_160044.jpg) | uovo singolo | lievemente sporco (0.71) | 0.56 | crepato (0.86) | 0.79 | **scarta**: crepato | 0.38 s | da verificare; verità: cracked |
| 122 | [hf_sample24.jpg](../../_pics/hf_sample24.jpg) | cartone con più uova | pulito (0.80) | 0.70 | integro (0.72) | 0.58 | accetta (A) | 0.28 s | da verificare |
| 123 | [figshare_IMG_20220818_155030.jpg](../../_pics/figshare_IMG_20220818_155030.jpg) | uovo singolo | lievemente sporco (0.60) | 0.40 | integro (0.84) | 0.76 | accetta (B) | 0.43 s | da verificare; verità: cracked |
| 124 | [hf_sample31.jpg](../../_pics/hf_sample31.jpg) | cartone con più uova | lievemente sporco (0.85) | 0.77 | integro (0.90) | 0.85 | accetta (B) | 0.29 s |  |
| 125 | [figshare_IMG_20220818_155717.jpg](../../_pics/figshare_IMG_20220818_155717.jpg) | uovo singolo | lievemente sporco (0.67) | 0.51 | integro (0.75) | 0.62 | accetta (B) | 0.94 s | da verificare; verità: cracked |
| 126 | [hf_sample48.jpg](../../_pics/hf_sample48.jpg) | cartone con più uova | pulito (0.87) | 0.80 | crepato (0.79) | 0.69 | **scarta**: crepato | 0.32 s |  |
| 127 | [figshare_IMG_20220818_154752.jpg](../../_pics/figshare_IMG_20220818_154752.jpg) | uovo singolo | lievemente sporco (0.84) | 0.76 | integro (0.65) | 0.48 | accetta (B) | 0.34 s | da verificare; verità: cracked |
| 128 | [hf_sample23.jpg](../../_pics/hf_sample23.jpg) | cartone con più uova | pulito (0.74) | 0.61 | integro (0.88) | 0.82 | accetta (A) | 0.32 s |  |
| 129 | [figshare_IMG_20220818_155804.jpg](../../_pics/figshare_IMG_20220818_155804.jpg) | uovo singolo | pulito (0.55) | 0.33 | crepato (0.86) | 0.79 | **scarta**: crepato | 0.29 s | da verificare; verità: cracked |
| 130 | [commons_10.jpg](../../_pics/commons_10.jpg) | poche uova | pulito (0.54) | 0.31 | integro (0.91) | 0.86 | accetta (A) | 0.28 s | da verificare |
| 131 | [figshare_IMG_20220818_155611.jpg](../../_pics/figshare_IMG_20220818_155611.jpg) | uovo singolo | lievemente sporco (0.92) | 0.88 | crepato (0.98) | 0.97 | **scarta**: crepato | 0.30 s | verità: cracked |
| 132 | [hf_sample38.jpg](../../_pics/hf_sample38.jpg) | cartone con più uova | lievemente sporco (0.65) | 0.48 | integro (0.92) | 0.88 | accetta (B) | 0.27 s | da verificare |
| 133 | [figshare_IMG_20220818_155724.jpg](../../_pics/figshare_IMG_20220818_155724.jpg) | uovo singolo | pulito (0.75) | 0.62 | integro (0.97) | 0.95 | accetta (A) | 0.29 s | verità: cracked |
| 134 | [commons_46.jpg](../../_pics/commons_46.jpg) | poche uova | pulito (0.68) | 0.52 | rotto (0.94) | 0.91 | non valutabile | 0.27 s |  |
| 135 | [figshare_IMG_20220818_154818.jpg](../../_pics/figshare_IMG_20220818_154818.jpg) | uovo singolo | lievemente sporco (0.87) | 0.80 | integro (0.99) | 0.98 | accetta (B) | 0.30 s | verità: cracked |
| 136 | [hf_sample39.jpg](../../_pics/hf_sample39.jpg) | cartone con più uova | lievemente sporco (0.61) | 0.41 | integro (0.90) | 0.85 | accetta (B) | 0.32 s | da verificare |
| 137 | [figshare_IMG_20220818_154103.jpg](../../_pics/figshare_IMG_20220818_154103.jpg) | uovo singolo | lievemente sporco (0.76) | 0.64 | crepato (0.63) | 0.45 | **scarta**: crepato | 0.31 s | da verificare; verità: cracked |
| 138 | [hf_sample50.jpg](../../_pics/hf_sample50.jpg) | cartone con più uova | pulito (0.85) | 0.77 | integro (0.77) | 0.66 | accetta (A) | 0.40 s |  |
| 139 | [figshare_IMG_20220818_155617.jpg](../../_pics/figshare_IMG_20220818_155617.jpg) | uovo singolo | lievemente sporco (0.87) | 0.80 | crepato (0.69) | 0.53 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 140 | [commons_45.jpg](../../_pics/commons_45.jpg) | poche uova | pulito (0.89) | 0.83 | rotto (0.93) | 0.89 | **scarta**: rotto | 0.27 s |  |
| 141 | [figshare_IMG_20220818_154959.jpg](../../_pics/figshare_IMG_20220818_154959.jpg) | uovo singolo | lievemente sporco (0.73) | 0.59 | crepato (0.83) | 0.74 | **scarta**: crepato | 0.32 s | da verificare; verità: cracked |
| 142 | [commons_26.jpg](../../_pics/commons_26.jpg) | poche uova | pulito (0.80) | 0.70 | integro (0.81) | 0.72 | accetta (A) | 0.32 s |  |
| 143 | [figshare_IMG_20220818_153857.jpg](../../_pics/figshare_IMG_20220818_153857.jpg) | uovo singolo | lievemente sporco (0.74) | 0.61 | integro (0.98) | 0.97 | accetta (B) | 0.34 s | verità: cracked |
| 144 | [commons_43.jpg](../../_pics/commons_43.jpg) | poche uova | pulito (0.55) | 0.33 | rotto (0.99) | 0.98 | non valutabile | 0.49 s |  |
| 145 | [figshare_IMG_20220818_154312.jpg](../../_pics/figshare_IMG_20220818_154312.jpg) | uovo singolo | pulito (0.63) | 0.45 | crepato (0.49) | 0.23 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 146 | [commons_08.jpg](../../_pics/commons_08.jpg) | poche uova | pulito (0.52) | 0.28 | integro (0.81) | 0.72 | accetta (A) | 0.29 s | da verificare |
| 147 | [figshare_IMG_20220818_154335.jpg](../../_pics/figshare_IMG_20220818_154335.jpg) | uovo singolo | lievemente sporco (0.71) | 0.56 | integro (0.57) | 0.35 | accetta (B) | 0.30 s | da verificare; verità: cracked |
| 148 | [hf_sample15.jpg](../../_pics/hf_sample15.jpg) | cartone con più uova | pulito (0.76) | 0.64 | integro (0.86) | 0.79 | accetta (A) | 0.34 s |  |
| 149 | [figshare_IMG_20220818_155547.jpg](../../_pics/figshare_IMG_20220818_155547.jpg) | uovo singolo | lievemente sporco (0.60) | 0.40 | crepato (0.94) | 0.91 | **scarta**: crepato | 0.34 s | da verificare; verità: cracked |
| 150 | [commons_12.jpg](../../_pics/commons_12.jpg) | poche uova | pulito (0.97) | 0.95 | integro (0.99) | 0.98 | accetta (A) | 0.26 s |  |
| 151 | [figshare_IMG_20220818_155047.jpg](../../_pics/figshare_IMG_20220818_155047.jpg) | uovo singolo | pulito (0.51) | 0.27 | crepato (0.90) | 0.85 | **scarta**: crepato | 0.28 s | da verificare; verità: cracked |
| 152 | [commons_31.jpg](../../_pics/commons_31.jpg) | poche uova | lievemente sporco (0.90) | 0.85 | integro (0.98) | 0.97 | accetta (B) | 0.29 s |  |
| 153 | [figshare_IMG_20220818_155700.jpg](../../_pics/figshare_IMG_20220818_155700.jpg) | uovo singolo | lievemente sporco (0.50) | 0.25 | crepato (0.94) | 0.91 | **scarta**: crepato | 0.29 s | da verificare; verità: cracked |
| 154 | [hf_sample44.jpg](../../_pics/hf_sample44.jpg) | cartone con più uova | lievemente sporco (0.59) | 0.38 | integro (0.59) | 0.38 | accetta (B) | 0.34 s | da verificare |
| 155 | [figshare_IMG_20220818_154613.jpg](../../_pics/figshare_IMG_20220818_154613.jpg) | uovo singolo | pulito (0.83) | 0.74 | crepato (0.88) | 0.82 | **scarta**: crepato | 0.29 s | verità: cracked |
| 156 | [commons_38.jpg](../../_pics/commons_38.jpg) | poche uova | lievemente sporco (0.60) | 0.40 | integro (0.85) | 0.77 | accetta (B) | 0.27 s | da verificare |
| 157 | [figshare_IMG_20220818_155436.jpg](../../_pics/figshare_IMG_20220818_155436.jpg) | uovo singolo | lievemente sporco (0.97) | 0.95 | crepato (0.94) | 0.91 | **scarta**: crepato | 0.32 s | verità: cracked |
| 158 | [commons_05.jpg](../../_pics/commons_05.jpg) | poche uova | pulito (0.92) | 0.88 | integro (0.98) | 0.97 | accetta (A) | 0.31 s |  |
| 159 | [figshare_IMG_20220818_154407.jpg](../../_pics/figshare_IMG_20220818_154407.jpg) | uovo singolo | pulito (0.54) | 0.31 | crepato (0.91) | 0.86 | **scarta**: crepato | 0.27 s | da verificare; verità: cracked |
| 160 | [hf_sample49.jpg](../../_pics/hf_sample49.jpg) | cartone con più uova | pulito (0.93) | 0.89 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.33 s |  |
| 161 | [figshare_IMG_20220818_155148.jpg](../../_pics/figshare_IMG_20220818_155148.jpg) | uovo singolo | pulito (0.58) | 0.37 | crepato (0.88) | 0.82 | **scarta**: crepato | 0.32 s | da verificare; verità: cracked |
| 162 | [hf_sample28.jpg](../../_pics/hf_sample28.jpg) | cartone con più uova | pulito (0.74) | 0.61 | integro (0.94) | 0.91 | accetta (A) | 0.32 s |  |
| 163 | [figshare_IMG_20220818_155959.jpg](../../_pics/figshare_IMG_20220818_155959.jpg) | uovo singolo | lievemente sporco (0.64) | 0.46 | crepato (0.76) | 0.64 | **scarta**: crepato | 0.31 s | da verificare; verità: cracked |
| 164 | [hf_sample4.jpg](../../_pics/hf_sample4.jpg) | cartone con più uova | lievemente sporco (0.81) | 0.72 | integro (0.95) | 0.92 | accetta (B) | 0.31 s |  |
| 165 | [figshare_IMG_20220818_155744.jpg](../../_pics/figshare_IMG_20220818_155744.jpg) | uovo singolo | pulito (0.86) | 0.79 | integro (0.83) | 0.74 | accetta (A) | 0.29 s | verità: cracked |
| 166 | [hf_sample36.jpg](../../_pics/hf_sample36.jpg) | cartone con più uova | pulito (0.87) | 0.80 | integro (0.59) | 0.38 | accetta (A) | 0.32 s | da verificare |
| 167 | [figshare_IMG_20220818_154731.jpg](../../_pics/figshare_IMG_20220818_154731.jpg) | uovo singolo | lievemente sporco (0.64) | 0.46 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.27 s | da verificare; verità: cracked |
| 168 | [commons_09.jpg](../../_pics/commons_09.jpg) | poche uova | pulito (0.77) | 0.66 | integro (0.99) | 0.98 | accetta (A) | 0.23 s |  |
| 169 | [figshare_IMG_20220818_154544.jpg](../../_pics/figshare_IMG_20220818_154544.jpg) | uovo singolo | lievemente sporco (0.60) | 0.40 | crepato (0.78) | 0.67 | **scarta**: crepato | 0.33 s | da verificare; verità: cracked |
| 170 | [hf_sample51.jpg](../../_pics/hf_sample51.jpg) | cartone con più uova | pulito (0.84) | 0.76 | crepato (0.74) | 0.61 | **scarta**: crepato | 0.32 s |  |
| 171 | [figshare_IMG_20220818_154218.jpg](../../_pics/figshare_IMG_20220818_154218.jpg) | uovo singolo | lievemente sporco (0.57) | 0.35 | integro (0.57) | 0.36 | accetta (B) | 0.31 s | da verificare; verità: cracked |
| 172 | [commons_21.jpg](../../_pics/commons_21.jpg) | poche uova | lievemente sporco (0.60) | 0.40 | integro (0.87) | 0.80 | accetta (B) | 0.33 s | da verificare |
| 173 | [figshare_IMG_20220818_160033.jpg](../../_pics/figshare_IMG_20220818_160033.jpg) | uovo singolo | lievemente sporco (0.64) | 0.46 | crepato (0.95) | 0.92 | **scarta**: crepato | 0.32 s | da verificare; verità: cracked |
| 174 | [hf_sample6.jpg](../../_pics/hf_sample6.jpg) | cartone con più uova | pulito (0.97) | 0.95 | integro (0.95) | 0.92 | accetta (A) | 0.29 s |  |
| 175 | [figshare_IMG_20220818_155523.jpg](../../_pics/figshare_IMG_20220818_155523.jpg) | uovo singolo | lievemente sporco (0.86) | 0.79 | integro (0.68) | 0.52 | accetta (B) | 0.29 s | da verificare; verità: cracked |
| 176 | [commons_02.jpg](../../_pics/commons_02.jpg) | poche uova | lievemente sporco (0.77) | 0.66 | integro (0.93) | 0.89 | accetta (B) | 0.28 s |  |
| 177 | [figshare_IMG_20220818_154011.jpg](../../_pics/figshare_IMG_20220818_154011.jpg) | uovo singolo | lievemente sporco (0.56) | 0.34 | integro (0.91) | 0.86 | accetta (B) | 0.27 s | da verificare; verità: cracked |
| 178 | [commons_28.jpg](../../_pics/commons_28.jpg) | poche uova | lievemente sporco (0.75) | 0.62 | integro (0.91) | 0.86 | accetta (B) | 0.33 s |  |
| 179 | [figshare_IMG_20220818_154708.jpg](../../_pics/figshare_IMG_20220818_154708.jpg) | uovo singolo | lievemente sporco (0.56) | 0.34 | crepato (0.89) | 0.83 | **scarta**: crepato | 0.27 s | da verificare; verità: cracked |
| 180 | [commons_33.jpg](../../_pics/commons_33.jpg) | poche uova | pulito (0.75) | 0.62 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.31 s |  |
| 181 | [figshare_IMG_20220818_155812.jpg](../../_pics/figshare_IMG_20220818_155812.jpg) | uovo singolo | lievemente sporco (0.67) | 0.51 | integro (0.90) | 0.85 | accetta (B) | 0.28 s | da verificare; verità: cracked |
| 182 | [commons_35.jpg](../../_pics/commons_35.jpg) | poche uova | pulito (0.52) | 0.28 | integro (0.57) | 0.35 | accetta (A) | 0.33 s | da verificare |
| 183 | [figshare_IMG_20220818_155915.jpg](../../_pics/figshare_IMG_20220818_155915.jpg) | uovo singolo | pulito (0.69) | 0.53 | crepato (0.86) | 0.79 | **scarta**: crepato | 0.32 s | da verificare; verità: cracked |
| 184 | [commons_07.jpg](../../_pics/commons_07.jpg) | poche uova | lievemente sporco (0.52) | 0.28 | integro (0.50) | 0.25 | accetta (B) | 0.37 s | da verificare |
| 185 | [figshare_IMG_20220818_153638.jpg](../../_pics/figshare_IMG_20220818_153638.jpg) | uovo singolo | lievemente sporco (0.74) | 0.61 | integro (0.91) | 0.86 | accetta (B) | 0.26 s | verità: cracked |
| 186 | [commons_29.jpg](../../_pics/commons_29.jpg) | poche uova | pulito (0.89) | 0.83 | integro (0.98) | 0.97 | accetta (A) | 0.30 s |  |
| 187 | [figshare_IMG_20220818_155503.jpg](../../_pics/figshare_IMG_20220818_155503.jpg) | uovo singolo | lievemente sporco (0.92) | 0.88 | crepato (0.96) | 0.94 | **scarta**: crepato | 0.31 s | verità: cracked |
| 188 | [hf_sample45.jpg](../../_pics/hf_sample45.jpg) | cartone con più uova | pulito (0.73) | 0.59 | integro (0.83) | 0.74 | accetta (A) | 0.33 s | da verificare |
| 189 | [figshare_IMG_20220818_154847.jpg](../../_pics/figshare_IMG_20220818_154847.jpg) | uovo singolo | lievemente sporco (0.95) | 0.92 | crepato (0.87) | 0.80 | **scarta**: crepato | 0.27 s | verità: cracked |
| 190 | [hf_sample21.jpg](../../_pics/hf_sample21.jpg) | cartone con più uova | pulito (0.95) | 0.92 | integro (0.97) | 0.95 | accetta (A) | 0.30 s |  |
| 191 | [figshare_IMG_20220818_154328.jpg](../../_pics/figshare_IMG_20220818_154328.jpg) | uovo singolo | pulito (0.52) | 0.28 | crepato (0.82) | 0.73 | **scarta**: crepato | 0.41 s | da verificare; verità: cracked |
| 192 | [commons_22.jpg](../../_pics/commons_22.jpg) | poche uova | lievemente sporco (0.86) | 0.79 | integro (0.95) | 0.92 | accetta (B) | 0.34 s |  |
| 193 | [figshare_IMG_20220818_154724.jpg](../../_pics/figshare_IMG_20220818_154724.jpg) | uovo singolo | lievemente sporco (0.61) | 0.41 | crepato (0.74) | 0.61 | **scarta**: crepato | 0.25 s | da verificare; verità: cracked |
| 194 | [commons_44.jpg](../../_pics/commons_44.jpg) | poche uova | sporco (0.63) | 0.45 | rotto (1.00) | 1.00 | non valutabile | 0.29 s |  |
| 195 | [figshare_IMG_20220818_155132.jpg](../../_pics/figshare_IMG_20220818_155132.jpg) | uovo singolo | lievemente sporco (0.55) | 0.33 | crepato (0.98) | 0.97 | **scarta**: crepato | 0.30 s | da verificare; verità: cracked |
| 196 | [commons_40.jpg](../../_pics/commons_40.jpg) | poche uova | pulito (0.91) | 0.86 | crepato (0.94) | 0.91 | **scarta**: crepato | 0.27 s |  |
| 197 | [figshare_IMG_20220818_154905.jpg](../../_pics/figshare_IMG_20220818_154905.jpg) | uovo singolo | lievemente sporco (0.94) | 0.91 | crepato (0.53) | 0.30 | **scarta**: crepato | 0.33 s | da verificare; verità: cracked |
| 198 | [commons_41.jpg](../../_pics/commons_41.jpg) | poche uova | sporco (0.58) | 0.37 | rotto (0.88) | 0.82 | **scarta**: rotto, sporco | 0.37 s | da verificare |
| 199 | [figshare_IMG_20220818_154943.jpg](../../_pics/figshare_IMG_20220818_154943.jpg) | uovo singolo | lievemente sporco (0.79) | 0.69 | crepato (0.86) | 0.79 | **scarta**: crepato | 0.28 s | verità: cracked |
| 200 | [commons_24.jpg](../../_pics/commons_24.jpg) | poche uova | pulito (0.86) | 0.79 | integro (0.92) | 0.88 | accetta (A) | 0.34 s |  |

## Dettaglio completo per foto

Un blocco per foto analizzata, nello stesso ordine della tabella sopra: clicca sul titolo per aprirlo. L'origine di tutte le 200 foto del campione è anche in `_pics/manifest.json`. Per ogni domanda sono indicate le probabilità di tutte le opzioni (in grassetto quella scelta) e la confidenza dichiarata dal modello.

<details>
<summary><b>1. figshare_IMG_20220818_154808.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154808.jpg" alt="figshare_IMG_20220818_154808.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154808.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.19 · **slightly_dirty 0.81** · dirty 0.00 · confidenza 0.72
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.61 s · token 5429 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>2. commons_04.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_04.jpg" alt="commons_04.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:AraucanaEgg_vs_Brown_White.jpg](https://commons.wikimedia.org/wiki/File:AraucanaEgg_vs_Brown_White.jpg)
- **Licenza**: Public domain · **Autore**: Gmoose1
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1549x1550
- **Verità nota**: nessuna
- **Uovo visibile**: 0.97
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.81** · slightly_dirty 0.19 · dirty 0.00 · confidenza 0.72
- **Integrità**: integro (`intact`) · probabilità: **intact 0.63** · cracked 0.37 · broken 0.00 · confidenza 0.45
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.62 s · token 6995 in / 101 out · costo $0.000294

</details>

<details>
<summary><b>3. figshare_IMG_20220818_154045.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154045.jpg" alt="figshare_IMG_20220818_154045.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154045.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.74
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.34 · **slightly_dirty 0.66** · dirty 0.00 · confidenza 0.49
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.35 · **cracked 0.65** · broken 0.00 · confidenza 0.48
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.61 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>4. commons_03.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_03.jpg" alt="commons_03.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_3145g.jpg](https://commons.wikimedia.org/wiki/File:Eggs_3145g.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: StaraBlazkova
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1000x669
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.35 · **slightly_dirty 0.63** · dirty 0.02 · confidenza 0.45
- **Integrità**: integro (`intact`) · probabilità: **intact 0.58** · cracked 0.42 · broken 0.00 · confidenza 0.37
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.55 s · token 2449 in / 104 out · costo $0.000103

</details>

<details>
<summary><b>5. figshare_IMG_20220818_155841.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155841.jpg" alt="figshare_IMG_20220818_155841.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155841.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.89** · slightly_dirty 0.11 · dirty 0.00 · confidenza 0.83
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.99** · broken 0.00 · confidenza 0.98
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>6. hf_sample47.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample47.jpg" alt="hf_sample47.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample47.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample47.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.80** · slightly_dirty 0.19 · dirty 0.01 · confidenza 0.70
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.11 · **cracked 0.89** · broken 0.00 · confidenza 0.83
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.37 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>7. figshare_IMG_20220818_155248.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155248.jpg" alt="figshare_IMG_20220818_155248.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155248.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.92
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.03 · **slightly_dirty 0.95** · dirty 0.02 · confidenza 0.92
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>8. commons_30.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_30.jpg" alt="commons_30.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_(8501854880).jpg](https://commons.wikimedia.org/wiki/File:Eggs_(8501854880).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: liz west from Boxborough, MA, USA
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1181
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.86** · slightly_dirty 0.13 · dirty 0.01 · confidenza 0.79
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.04 · broken 0.01 · confidenza 0.92
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5538 in / 101 out · costo $0.000233

</details>

<details>
<summary><b>9. figshare_IMG_20220818_155341.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155341.jpg" alt="figshare_IMG_20220818_155341.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155341.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.95** · dirty 0.03 · confidenza 0.92
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5429 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>10. commons_15.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_15.jpg" alt="commons_15.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Oeuf_de_poule.jpg](https://commons.wikimedia.org/wiki/File:Oeuf_de_poule.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Jeangagnon
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1198x1432
- **Verità nota**: nessuna
- **Uovo visibile**: 0.97
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.90** · slightly_dirty 0.10 · dirty 0.00 · confidenza 0.85
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.35 s · token 5195 in / 101 out · costo $0.000218

</details>

<details>
<summary><b>11. figshare_IMG_20220818_153759.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153759.jpg" alt="figshare_IMG_20220818_153759.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153759.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.19 · **slightly_dirty 0.80** · dirty 0.01 · confidenza 0.70
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.60 s · token 5431 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>12. hf_sample7.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample7.jpg" alt="hf_sample7.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample7.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample7.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.90** · slightly_dirty 0.09 · dirty 0.01 · confidenza 0.85
- **Integrità**: integro (`intact`) · probabilità: **intact 0.87** · cracked 0.12 · broken 0.01 · confidenza 0.80
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.62 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>13. figshare_IMG_20220818_160114.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160114.jpg" alt="figshare_IMG_20220818_160114.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160114.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.73** · slightly_dirty 0.27 · dirty 0.00 · confidenza 0.59
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.96** · broken 0.00 · confidenza 0.94
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.56 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>14. commons_36.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_36.jpg" alt="commons_36.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:FreeRangeEgg.jpg](https://commons.wikimedia.org/wiki/File:FreeRangeEgg.jpg)
- **Licenza**: CC BY-SA 3.0
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1000x825
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.88** · slightly_dirty 0.11 · dirty 0.01 · confidenza 0.82
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.31 · **cracked 0.69** · broken 0.00 · confidenza 0.53
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.64 s · token 2881 in / 102 out · costo $0.000121

</details>

<details>
<summary><b>15. figshare_IMG_20220818_155859.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155859.jpg" alt="figshare_IMG_20220818_155859.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155859.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.57** · slightly_dirty 0.42 · dirty 0.01 · confidenza 0.35
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.06 · **cracked 0.93** · broken 0.01 · confidenza 0.89
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>16. hf_sample3.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample3.jpg" alt="hf_sample3.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample3.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample3.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.74** · slightly_dirty 0.26 · dirty 0.00 · confidenza 0.61
- **Integrità**: integro (`intact`) · probabilità: **intact 0.91** · cracked 0.07 · broken 0.02 · confidenza 0.86
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5423 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>17. figshare_IMG_20220818_155422.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155422.jpg" alt="figshare_IMG_20220818_155422.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155422.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.01 · **slightly_dirty 0.98** · dirty 0.01 · confidenza 0.97
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.03 · **cracked 0.97** · broken 0.00 · confidenza 0.95
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>18. commons_25.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_25.jpg" alt="commons_25.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:First_egg_(7680068562).jpg](https://commons.wikimedia.org/wiki/File:First_egg_(7680068562).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: normanack
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1549x1549
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.86** · slightly_dirty 0.13 · dirty 0.01 · confidenza 0.79
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 6993 in / 101 out · costo $0.000294

</details>

<details>
<summary><b>19. figshare_IMG_20220818_154854.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154854.jpg" alt="figshare_IMG_20220818_154854.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154854.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.03 · **slightly_dirty 0.95** · dirty 0.02 · confidenza 0.92
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.12 · **cracked 0.88** · broken 0.00 · confidenza 0.82
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5423 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>20. hf_sample30.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample30.jpg" alt="hf_sample30.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample30.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample30.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.31 · **slightly_dirty 0.68** · dirty 0.01 · confidenza 0.52
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5423 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>21. figshare_IMG_20220818_154019.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154019.jpg" alt="figshare_IMG_20220818_154019.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154019.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.87
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.28 · **slightly_dirty 0.72** · dirty 0.00 · confidenza 0.58
- **Integrità**: integro (`intact`) · probabilità: **intact 0.96** · cracked 0.04 · broken 0.00 · confidenza 0.94
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 1.39 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>22. hf_sample9.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample9.jpg" alt="hf_sample9.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample9.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample9.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.94** · slightly_dirty 0.06 · dirty 0.00 · confidenza 0.91
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.04 · broken 0.01 · confidenza 0.92
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>23. figshare_IMG_20220818_154949.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154949.jpg" alt="figshare_IMG_20220818_154949.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154949.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.84
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.29 · **slightly_dirty 0.71** · dirty 0.00 · confidenza 0.56
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.03 · **cracked 0.96** · broken 0.01 · confidenza 0.94
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>24. commons_18.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_18.jpg" alt="commons_18.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Spiral_of_Brown_Eggs.jpg](https://commons.wikimedia.org/wiki/File:Spiral_of_Brown_Eggs.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Krugglesuvu
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1273x1554
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.47** · slightly_dirty 0.46 · dirty 0.07 · confidenza 0.20
- **Integrità**: integro (`intact`) · probabilità: **intact 0.97** · cracked 0.03 · broken 0.00 · confidenza 0.95
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5875 in / 101 out · costo $0.000247

</details>

<details>
<summary><b>25. figshare_IMG_20220818_155415.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155415.jpg" alt="figshare_IMG_20220818_155415.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155415.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.91
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.05 · **slightly_dirty 0.94** · dirty 0.01 · confidenza 0.91
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.08 · **cracked 0.91** · broken 0.01 · confidenza 0.86
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>26. commons_23.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_23.jpg" alt="commons_23.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_(7177637421).jpg](https://commons.wikimedia.org/wiki/File:Eggs_(7177637421).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: James Bowe
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.21 · **slightly_dirty 0.76** · dirty 0.03 · confidenza 0.64
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>27. figshare_IMG_20220818_155457.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155457.jpg" alt="figshare_IMG_20220818_155457.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155457.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.87
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.20 · **slightly_dirty 0.79** · dirty 0.01 · confidenza 0.69
- **Integrità**: integro (`intact`) · probabilità: **intact 0.67** · cracked 0.31 · broken 0.02 · confidenza 0.51
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5429 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>28. hf_sample8.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample8.jpg" alt="hf_sample8.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample8.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample8.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.89** · slightly_dirty 0.10 · dirty 0.01 · confidenza 0.83
- **Integrità**: integro (`intact`) · probabilità: **intact 0.93** · cracked 0.07 · broken 0.00 · confidenza 0.89
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>29. figshare_IMG_20220818_154636.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154636.jpg" alt="figshare_IMG_20220818_154636.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154636.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.40 · **slightly_dirty 0.60** · dirty 0.00 · confidenza 0.40
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.06 · broken 0.00 · confidenza 0.91
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.43 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>30. hf_sample20.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample20.jpg" alt="hf_sample20.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample20.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample20.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.92** · slightly_dirty 0.08 · dirty 0.00 · confidenza 0.88
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5425 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>31. figshare_IMG_20220818_154528.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154528.jpg" alt="figshare_IMG_20220818_154528.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154528.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.96
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.67** · slightly_dirty 0.33 · dirty 0.00 · confidenza 0.51
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.09 · **cracked 0.91** · broken 0.00 · confidenza 0.86
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>32. hf_sample34.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample34.jpg" alt="hf_sample34.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample34.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample34.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.82** · slightly_dirty 0.17 · dirty 0.01 · confidenza 0.73
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.33 · **cracked 0.66** · broken 0.01 · confidenza 0.49
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>33. figshare_IMG_20220818_160007.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_160007.jpg" alt="figshare_IMG_20220818_160007.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160007.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.71
- **Pulizia**: sporco (`dirty`) · probabilità: clean 0.00 · slightly_dirty 0.24 · **dirty 0.76** · confidenza 0.64
- **Integrità**: rotto (`broken`) · probabilità: intact 0.01 · cracked 0.37 · **broken 0.62** · confidenza 0.43
- **Decisione**: scarta: rotto, sporco · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 5431 in / 100 out · costo $0.000228

</details>

<details>
<summary><b>34. commons_27.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_27.jpg" alt="commons_27.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Spotted_Brown_Chicken_Eggs_(5719609727).jpg](https://commons.wikimedia.org/wiki/File:Spotted_Brown_Chicken_Eggs_(5719609727).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: spiralmushroom
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1043
- **Verità nota**: nessuna
- **Uovo visibile**: 0.97
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.41 · **slightly_dirty 0.52** · dirty 0.07 · confidenza 0.28
- **Integrità**: integro (`intact`) · probabilità: **intact 0.72** · cracked 0.27 · broken 0.01 · confidenza 0.58
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 4982 in / 104 out · costo $0.000209

</details>

<details>
<summary><b>35. figshare_IMG_20220818_154535.jpg</b> · accetta (A)</summary>

<img src="../../_pics/figshare_IMG_20220818_154535.jpg" alt="figshare_IMG_20220818_154535.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154535.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.64** · slightly_dirty 0.35 · dirty 0.01 · confidenza 0.46
- **Integrità**: integro (`intact`) · probabilità: **intact 0.68** · cracked 0.32 · broken 0.00 · confidenza 0.52
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.38 s · token 5430 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>36. hf_sample13.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample13.jpg" alt="hf_sample13.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample13.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample13.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.89** · slightly_dirty 0.10 · dirty 0.01 · confidenza 0.83
- **Integrità**: integro (`intact`) · probabilità: **intact 0.93** · cracked 0.07 · broken 0.00 · confidenza 0.89
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5427 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>37. figshare_IMG_20220818_155015.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155015.jpg" alt="figshare_IMG_20220818_155015.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155015.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.10 · **slightly_dirty 0.89** · dirty 0.01 · confidenza 0.83
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.12 · **cracked 0.87** · broken 0.01 · confidenza 0.80
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 1.22 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>38. hf_sample46.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample46.jpg" alt="hf_sample46.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample46.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample46.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.64** · slightly_dirty 0.35 · dirty 0.01 · confidenza 0.46
- **Integrità**: integro (`intact`) · probabilità: **intact 0.80** · cracked 0.20 · broken 0.00 · confidenza 0.70
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5427 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>39. figshare_IMG_20220818_155401.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155401.jpg" alt="figshare_IMG_20220818_155401.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155401.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.96** · dirty 0.02 · confidenza 0.94
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5430 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>40. commons_34.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_34.jpg" alt="commons_34.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_on_Table.jpg](https://commons.wikimedia.org/wiki/File:Egg_on_Table.jpg)
- **Licenza**: CC BY-SA 2.0 · **Autore**: Eric Petruno
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.81** · slightly_dirty 0.19 · dirty 0.00 · confidenza 0.72
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 4982 in / 101 out · costo $0.000209

</details>

<details>
<summary><b>41. figshare_IMG_20220818_155709.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155709.jpg" alt="figshare_IMG_20220818_155709.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155709.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.71** · slightly_dirty 0.29 · dirty 0.00 · confidenza 0.56
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.03 · **cracked 0.97** · broken 0.00 · confidenza 0.95
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>42. commons_32.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_32.jpg" alt="commons_32.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Tiny_treasure,_first_egg_(7680059460).jpg](https://commons.wikimedia.org/wiki/File:Tiny_treasure,_first_egg_(7680059460).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: normanack
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.93** · slightly_dirty 0.07 · dirty 0.00 · confidenza 0.89
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.39 s · token 5431 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>43. figshare_IMG_20220818_155137.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155137.jpg" alt="figshare_IMG_20220818_155137.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155137.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.48 · **slightly_dirty 0.51** · dirty 0.01 · confidenza 0.27
- **Integrità**: integro (`intact`) · probabilità: **intact 0.78** · cracked 0.21 · broken 0.01 · confidenza 0.67
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>44. commons_42.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/commons_42.jpg" alt="commons_42.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Bloody-egg.jpg](https://commons.wikimedia.org/wiki/File:Bloody-egg.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Maqi
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 600x902
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.78
- **Pulizia**: sporco (`dirty`) · probabilità: clean 0.01 · slightly_dirty 0.01 · **dirty 0.98** · confidenza 0.97
- **Integrità**: rotto (`broken`) · probabilità: intact 0.03 · cracked 0.01 · **broken 0.96** · confidenza 0.94
- **Decisione**: scarta: rotto, sporco
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 2175 in / 100 out · costo $0.000091

</details>

<details>
<summary><b>45. figshare_IMG_20220818_155511.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155511.jpg" alt="figshare_IMG_20220818_155511.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155511.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.26 · **slightly_dirty 0.74** · dirty 0.00 · confidenza 0.61
- **Integrità**: integro (`intact`) · probabilità: **intact 0.74** · cracked 0.26 · broken 0.00 · confidenza 0.61
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>46. commons_16.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_16.jpg" alt="commons_16.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_upright.jpg](https://commons.wikimedia.org/wiki/File:Egg_upright.jpg)
- **Licenza**: Public domain · **Autore**: Paolo Neo
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1491
- **Verità nota**: nessuna
- **Uovo visibile**: 0.96
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.90** · slightly_dirty 0.10 · dirty 0.00 · confidenza 0.85
- **Integrità**: integro (`intact`) · probabilità: **intact 0.87** · cracked 0.11 · broken 0.02 · confidenza 0.80
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.39 s · token 6772 in / 101 out · costo $0.000284

</details>

<details>
<summary><b>47. figshare_IMG_20220818_154136.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154136.jpg" alt="figshare_IMG_20220818_154136.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154136.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.76
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.30 · **slightly_dirty 0.70** · dirty 0.00 · confidenza 0.55
- **Integrità**: integro (`intact`) · probabilità: **intact 0.56** · cracked 0.44 · broken 0.00 · confidenza 0.34
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>48. commons_19.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_19.jpg" alt="commons_19.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Fresh_Eggs_(Unsplash_fBturNUtd8).jpg](https://commons.wikimedia.org/wiki/File:Fresh_Eggs_(Unsplash_fBturNUtd8).jpg)
- **Licenza**: CC0 · **Autore**: Brina Blum brina_blum
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 0.97
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.75** · slightly_dirty 0.24 · dirty 0.01 · confidenza 0.62
- **Integrità**: integro (`intact`) · probabilità: **intact 0.89** · cracked 0.11 · broken 0.00 · confidenza 0.83
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 4979 in / 101 out · costo $0.000209

</details>

<details>
<summary><b>49. figshare_IMG_20220818_154759.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154759.jpg" alt="figshare_IMG_20220818_154759.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154759.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.25 · **slightly_dirty 0.75** · dirty 0.00 · confidenza 0.62
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>50. commons_47.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_47.jpg" alt="commons_47.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B4-001.jpg](https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B4-001.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: OhWeh
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.10
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.19 · **slightly_dirty 0.57** · dirty 0.24 · confidenza 0.35
- **Integrità**: integro (`intact`) · probabilità: **intact 0.84** · cracked 0.15 · broken 0.01 · confidenza 0.76
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>51. figshare_IMG_20220818_155540.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155540.jpg" alt="figshare_IMG_20220818_155540.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155540.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.84
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.64** · slightly_dirty 0.36 · dirty 0.00 · confidenza 0.46
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.98** · broken 0.01 · confidenza 0.97
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.60 s · token 5430 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>52. hf_sample17.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample17.jpg" alt="hf_sample17.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample17.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample17.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.83** · slightly_dirty 0.17 · dirty 0.00 · confidenza 0.74
- **Integrità**: integro (`intact`) · probabilità: **intact 0.89** · cracked 0.10 · broken 0.01 · confidenza 0.83
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.65 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>53. figshare_IMG_20220818_154226.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154226.jpg" alt="figshare_IMG_20220818_154226.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154226.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.75
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.36 · **slightly_dirty 0.64** · dirty 0.00 · confidenza 0.46
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.08 · **cracked 0.92** · broken 0.00 · confidenza 0.88
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.72 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>54. hf_sample33.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample33.jpg" alt="hf_sample33.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample33.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample33.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.79** · slightly_dirty 0.21 · dirty 0.00 · confidenza 0.69
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.19 · **cracked 0.81** · broken 0.00 · confidenza 0.72
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.70 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>55. figshare_IMG_20220818_155846.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155846.jpg" alt="figshare_IMG_20220818_155846.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155846.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.91
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.84** · slightly_dirty 0.16 · dirty 0.00 · confidenza 0.76
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.99** · broken 0.00 · confidenza 0.98
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>56. commons_11.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_11.jpg" alt="commons_11.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_on_white_background.jpg](https://commons.wikimedia.org/wiki/File:Egg_on_white_background.jpg)
- **Licenza**: Public domain · **Autore**: Paolo Neo
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.81
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.78** · slightly_dirty 0.22 · dirty 0.00 · confidenza 0.67
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>57. figshare_IMG_20220818_153842.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153842.jpg" alt="figshare_IMG_20220818_153842.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153842.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.77
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.23 · **slightly_dirty 0.76** · dirty 0.01 · confidenza 0.64
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5430 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>58. commons_48.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_48.jpg" alt="commons_48.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B16-001.jpg](https://commons.wikimedia.org/wiki/File:Flaumfeder_auf_H%C3%BChnerei-B16-001.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: OhWeh
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.19
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.11 · **slightly_dirty 0.50** · dirty 0.39 · confidenza 0.25
- **Integrità**: integro (`intact`) · probabilità: **intact 0.92** · cracked 0.07 · broken 0.01 · confidenza 0.88
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5422 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>59. figshare_IMG_20220818_160129.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160129.jpg" alt="figshare_IMG_20220818_160129.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160129.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.74** · slightly_dirty 0.26 · dirty 0.00 · confidenza 0.61
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.40 · **cracked 0.60** · broken 0.00 · confidenza 0.40
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>60. hf_sample2.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample2.jpg" alt="hf_sample2.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample2.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample2.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.33 · **slightly_dirty 0.67** · dirty 0.00 · confidenza 0.51
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.09 · broken 0.01 · confidenza 0.85
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>61. figshare_IMG_20220818_155851.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155851.jpg" alt="figshare_IMG_20220818_155851.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155851.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.91
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.76** · slightly_dirty 0.24 · dirty 0.00 · confidenza 0.64
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.35 · **cracked 0.65** · broken 0.00 · confidenza 0.48
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>62. hf_sample29.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample29.jpg" alt="hf_sample29.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample29.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample29.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.85** · slightly_dirty 0.15 · dirty 0.00 · confidenza 0.77
- **Integrità**: integro (`intact`) · probabilità: **intact 0.85** · cracked 0.14 · broken 0.01 · confidenza 0.77
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.37 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>63. figshare_IMG_20220818_154436.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154436.jpg" alt="figshare_IMG_20220818_154436.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154436.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.62** · slightly_dirty 0.38 · dirty 0.00 · confidenza 0.43
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.11 · **cracked 0.89** · broken 0.00 · confidenza 0.83
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5426 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>64. hf_sample37.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample37.jpg" alt="hf_sample37.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample37.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample37.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.84** · slightly_dirty 0.15 · dirty 0.01 · confidenza 0.76
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.40 · **cracked 0.60** · broken 0.00 · confidenza 0.40
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.58 s · token 5430 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>65. figshare_IMG_20220818_154051.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154051.jpg" alt="figshare_IMG_20220818_154051.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154051.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.56
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.39 · **slightly_dirty 0.61** · dirty 0.00 · confidenza 0.41
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.39 · **cracked 0.61** · broken 0.00 · confidenza 0.41
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5429 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>66. hf_sample40.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample40.jpg" alt="hf_sample40.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample40.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample40.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.50** · slightly_dirty 0.49 · dirty 0.01 · confidenza 0.25
- **Integrità**: integro (`intact`) · probabilità: **intact 0.81** · cracked 0.19 · broken 0.00 · confidenza 0.72
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>67. figshare_IMG_20220818_155910.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155910.jpg" alt="figshare_IMG_20220818_155910.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155910.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.89** · slightly_dirty 0.11 · dirty 0.00 · confidenza 0.83
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.02 · **cracked 0.97** · broken 0.01 · confidenza 0.95
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>68. hf_sample41.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample41.jpg" alt="hf_sample41.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample41.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample41.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.69** · slightly_dirty 0.30 · dirty 0.01 · confidenza 0.53
- **Integrità**: integro (`intact`) · probabilità: **intact 0.64** · cracked 0.36 · broken 0.00 · confidenza 0.46
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5427 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>69. figshare_IMG_20220818_154057.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154057.jpg" alt="figshare_IMG_20220818_154057.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154057.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.67
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.15 · **slightly_dirty 0.85** · dirty 0.00 · confidenza 0.77
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.05 · **cracked 0.95** · broken 0.00 · confidenza 0.92
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>70. hf_sample43.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample43.jpg" alt="hf_sample43.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample43.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample43.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.44 · **slightly_dirty 0.49** · dirty 0.07 · confidenza 0.23
- **Integrità**: integro (`intact`) · probabilità: **intact 0.59** · cracked 0.39 · broken 0.02 · confidenza 0.38
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.40 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>71. figshare_IMG_20220818_154444.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154444.jpg" alt="figshare_IMG_20220818_154444.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154444.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.52** · slightly_dirty 0.47 · dirty 0.01 · confidenza 0.28
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.21 · **cracked 0.74** · broken 0.05 · confidenza 0.61
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5423 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>72. commons_20.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_20.jpg" alt="commons_20.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Different_colored_chicken_eggs-01ASD.jpg](https://commons.wikimedia.org/wiki/File:Different_colored_chicken_eggs-01ASD.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Asurnipal
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1567x1532
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.56** · slightly_dirty 0.44 · dirty 0.00 · confidenza 0.34
- **Integrità**: integro (`intact`) · probabilità: **intact 0.97** · cracked 0.03 · broken 0.00 · confidenza 0.95
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 6883 in / 101 out · costo $0.000289

</details>

<details>
<summary><b>73. figshare_IMG_20220818_155948.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_155948.jpg" alt="figshare_IMG_20220818_155948.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155948.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.74
- **Pulizia**: sporco (`dirty`) · probabilità: clean 0.00 · slightly_dirty 0.29 · **dirty 0.71** · confidenza 0.56
- **Integrità**: rotto (`broken`) · probabilità: intact 0.01 · cracked 0.34 · **broken 0.65** · confidenza 0.48
- **Decisione**: scarta: rotto, sporco · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5430 in / 100 out · costo $0.000228

</details>

<details>
<summary><b>74. hf_sample11.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample11.jpg" alt="hf_sample11.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample11.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample11.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.90** · slightly_dirty 0.10 · dirty 0.00 · confidenza 0.85
- **Integrità**: integro (`intact`) · probabilità: **intact 0.93** · cracked 0.07 · broken 0.00 · confidenza 0.89
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.36 s · token 5430 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>75. figshare_IMG_20220818_155606.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155606.jpg" alt="figshare_IMG_20220818_155606.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155606.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.91
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.25 · **slightly_dirty 0.75** · dirty 0.00 · confidenza 0.62
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.11 · **cracked 0.81** · broken 0.08 · confidenza 0.72
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>76. commons_49.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_49.jpg" alt="commons_49.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Strange_brown_egg.jpg](https://commons.wikimedia.org/wiki/File:Strange_brown_egg.jpg)
- **Licenza**: CC0 · **Autore**: Smallman12q
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1401
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.08
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.01 · **slightly_dirty 0.58** · dirty 0.41 · confidenza 0.37
- **Integrità**: rotto (`broken`) · probabilità: intact 0.08 · cracked 0.34 · **broken 0.58** · confidenza 0.37
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 6439 in / 103 out · costo $0.000270

</details>

<details>
<summary><b>77. figshare_IMG_20220818_154914.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154914.jpg" alt="figshare_IMG_20220818_154914.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154914.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.86
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.95** · dirty 0.03 · confidenza 0.92
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.19 · **cracked 0.81** · broken 0.00 · confidenza 0.72
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>78. hf_sample22.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample22.jpg" alt="hf_sample22.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample22.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample22.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.49 · **slightly_dirty 0.51** · dirty 0.00 · confidenza 0.27
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.09 · broken 0.01 · confidenza 0.85
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>79. figshare_IMG_20220818_155240.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155240.jpg" alt="figshare_IMG_20220818_155240.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155240.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.92
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.96** · dirty 0.02 · confidenza 0.94
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.43 · **cracked 0.57** · broken 0.00 · confidenza 0.35
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5432 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>80. commons_06.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_06.jpg" alt="commons_06.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Brown_chicken_eggs.jpg](https://commons.wikimedia.org/wiki/File:Brown_chicken_eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Piasoft
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1041
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.92** · slightly_dirty 0.08 · dirty 0.00 · confidenza 0.88
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 4981 in / 101 out · costo $0.000209

</details>

<details>
<summary><b>81. figshare_IMG_20220818_160039.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160039.jpg" alt="figshare_IMG_20220818_160039.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160039.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.84
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.21 · **slightly_dirty 0.78** · dirty 0.01 · confidenza 0.67
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.91** · broken 0.05 · confidenza 0.86
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5426 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>82. hf_sample42.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample42.jpg" alt="hf_sample42.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample42.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample42.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.83** · slightly_dirty 0.16 · dirty 0.01 · confidenza 0.74
- **Integrità**: integro (`intact`) · probabilità: **intact 0.91** · cracked 0.09 · broken 0.00 · confidenza 0.86
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5427 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>83. figshare_IMG_20220818_154715.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154715.jpg" alt="figshare_IMG_20220818_154715.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154715.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.79
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.18 · **slightly_dirty 0.82** · dirty 0.00 · confidenza 0.73
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.05 · **cracked 0.94** · broken 0.01 · confidenza 0.91
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.45 s · token 5431 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>84. hf_sample12.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample12.jpg" alt="hf_sample12.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample12.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample12.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.93** · slightly_dirty 0.07 · dirty 0.00 · confidenza 0.89
- **Integrità**: integro (`intact`) · probabilità: **intact 0.92** · cracked 0.07 · broken 0.01 · confidenza 0.88
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5430 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>85. figshare_IMG_20220818_154238.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154238.jpg" alt="figshare_IMG_20220818_154238.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154238.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.85
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.32 · **slightly_dirty 0.68** · dirty 0.00 · confidenza 0.52
- **Integrità**: integro (`intact`) · probabilità: **intact 0.92** · cracked 0.08 · broken 0.00 · confidenza 0.88
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>86. hf_sample16.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample16.jpg" alt="hf_sample16.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample16.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample16.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.95** · slightly_dirty 0.05 · dirty 0.00 · confidenza 0.92
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.06 · broken 0.00 · confidenza 0.91
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>87. figshare_IMG_20220818_154413.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154413.jpg" alt="figshare_IMG_20220818_154413.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154413.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.79
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.63** · slightly_dirty 0.37 · dirty 0.00 · confidenza 0.45
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.05 · **cracked 0.93** · broken 0.02 · confidenza 0.89
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.25 s · token 5428 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>88. commons_14.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_14.jpg" alt="commons_14.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Deux_oeufs_bruns.jpg](https://commons.wikimedia.org/wiki/File:Deux_oeufs_bruns.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Jeangagnon
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.51** · slightly_dirty 0.49 · dirty 0.00 · confidenza 0.27
- **Integrità**: integro (`intact`) · probabilità: **intact 0.96** · cracked 0.04 · broken 0.00 · confidenza 0.94
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.37 s · token 5430 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>89. figshare_IMG_20220818_155559.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155559.jpg" alt="figshare_IMG_20220818_155559.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155559.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.12 · **slightly_dirty 0.86** · dirty 0.02 · confidenza 0.79
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.03 · **cracked 0.96** · broken 0.01 · confidenza 0.94
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>90. hf_sample1.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample1.jpg" alt="hf_sample1.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample1.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample1.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.24 · **slightly_dirty 0.76** · dirty 0.00 · confidenza 0.64
- **Integrità**: integro (`intact`) · probabilità: **intact 0.93** · cracked 0.07 · broken 0.00 · confidenza 0.89
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5430 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>91. figshare_IMG_20220818_155517.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155517.jpg" alt="figshare_IMG_20220818_155517.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155517.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.96
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.06 · **slightly_dirty 0.92** · dirty 0.02 · confidenza 0.88
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.24 · **cracked 0.76** · broken 0.00 · confidenza 0.64
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>92. hf_sample5.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample5.jpg" alt="hf_sample5.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample5.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample5.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.96** · slightly_dirty 0.04 · dirty 0.00 · confidenza 0.94
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 1.37 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>93. figshare_IMG_20220818_154429.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154429.jpg" alt="figshare_IMG_20220818_154429.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154429.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.78** · slightly_dirty 0.22 · dirty 0.00 · confidenza 0.67
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.05 · **cracked 0.95** · broken 0.00 · confidenza 0.92
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>94. commons_13.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_13.jpg" alt="commons_13.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:2_eggs.JPG](https://commons.wikimedia.org/wiki/File:2_eggs.JPG)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Hannahdownes
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.87** · slightly_dirty 0.13 · dirty 0.00 · confidenza 0.80
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.35 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>95. figshare_IMG_20220818_160049.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160049.jpg" alt="figshare_IMG_20220818_160049.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160049.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.85
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.22 · **slightly_dirty 0.77** · dirty 0.01 · confidenza 0.66
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.15 · **cracked 0.73** · broken 0.12 · confidenza 0.59
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.50 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>96. commons_17.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_17.jpg" alt="commons_17.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Three_chicken_eggs.jpg](https://commons.wikimedia.org/wiki/File:Three_chicken_eggs.jpg)
- **Licenza**: CC0 · **Autore**: www.Pixel.la Free Stock Photos
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.80** · slightly_dirty 0.19 · dirty 0.01 · confidenza 0.70
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 4980 in / 101 out · costo $0.000209

</details>

<details>
<summary><b>97. figshare_IMG_20220818_155353.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155353.jpg" alt="figshare_IMG_20220818_155353.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155353.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.89
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.11 · **slightly_dirty 0.88** · dirty 0.01 · confidenza 0.82
- **Integrità**: integro (`intact`) · probabilità: **intact 0.92** · cracked 0.06 · broken 0.02 · confidenza 0.88
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>98. hf_sample35.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample35.jpg" alt="hf_sample35.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample35.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample35.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.77** · slightly_dirty 0.22 · dirty 0.01 · confidenza 0.66
- **Integrità**: integro (`intact`) · probabilità: **intact 0.76** · cracked 0.23 · broken 0.01 · confidenza 0.64
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>99. figshare_IMG_20220818_154557.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154557.jpg" alt="figshare_IMG_20220818_154557.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154557.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.74
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.57** · slightly_dirty 0.43 · dirty 0.00 · confidenza 0.35
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.45 · **cracked 0.55** · broken 0.00 · confidenza 0.33
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>100. hf_sample27.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample27.jpg" alt="hf_sample27.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample27.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample27.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.72** · slightly_dirty 0.28 · dirty 0.00 · confidenza 0.58
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.09 · broken 0.01 · confidenza 0.85
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>101. figshare_IMG_20220818_153953.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153953.jpg" alt="figshare_IMG_20220818_153953.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153953.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.80
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.37 · **slightly_dirty 0.63** · dirty 0.00 · confidenza 0.45
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>102. hf_sample14.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample14.jpg" alt="hf_sample14.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample14.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample14.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.95** · slightly_dirty 0.05 · dirty 0.00 · confidenza 0.92
- **Integrità**: integro (`intact`) · probabilità: **intact 0.96** · cracked 0.04 · broken 0.00 · confidenza 0.94
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5426 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>103. figshare_IMG_20220818_160014.jpg</b> · scarta: crepato, sporco</summary>

<img src="../../_pics/figshare_IMG_20220818_160014.jpg" alt="figshare_IMG_20220818_160014.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160014.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.73
- **Pulizia**: sporco (`dirty`) · probabilità: clean 0.00 · slightly_dirty 0.37 · **dirty 0.63** · confidenza 0.45
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.02 · **cracked 0.60** · broken 0.38 · confidenza 0.40
- **Decisione**: scarta: crepato, sporco · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>104. hf_sample19.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample19.jpg" alt="hf_sample19.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample19.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample19.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.56** · slightly_dirty 0.44 · dirty 0.00 · confidenza 0.34
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>105. figshare_IMG_20220818_154113.jpg</b> · non valutabile</summary>

<img src="../../_pics/figshare_IMG_20220818_154113.jpg" alt="figshare_IMG_20220818_154113.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154113.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.37
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.12 · **slightly_dirty 0.87** · dirty 0.01 · confidenza 0.80
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.17 · **cracked 0.83** · broken 0.00 · confidenza 0.74
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>106. hf_sample18.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample18.jpg" alt="hf_sample18.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample18.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample18.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.93** · slightly_dirty 0.07 · dirty 0.00 · confidenza 0.89
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5426 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>107. figshare_IMG_20220818_160123.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160123.jpg" alt="figshare_IMG_20220818_160123.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160123.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.88
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.34 · **slightly_dirty 0.66** · dirty 0.00 · confidenza 0.49
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.99** · broken 0.00 · confidenza 0.98
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>108. hf_sample26.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample26.jpg" alt="hf_sample26.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample26.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample26.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.63** · slightly_dirty 0.36 · dirty 0.01 · confidenza 0.45
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.09 · broken 0.01 · confidenza 0.85
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>109. figshare_IMG_20220818_155430.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155430.jpg" alt="figshare_IMG_20220818_155430.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155430.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.86
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.03 · **slightly_dirty 0.96** · dirty 0.01 · confidenza 0.94
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.09 · **cracked 0.89** · broken 0.02 · confidenza 0.83
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5429 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>110. hf_sample32.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample32.jpg" alt="hf_sample32.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample32.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample32.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.35 · **slightly_dirty 0.64** · dirty 0.01 · confidenza 0.46
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>111. figshare_IMG_20220818_154419.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154419.jpg" alt="figshare_IMG_20220818_154419.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154419.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.73** · slightly_dirty 0.27 · dirty 0.00 · confidenza 0.59
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.07 · **cracked 0.93** · broken 0.00 · confidenza 0.89
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5422 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>112. hf_sample25.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample25.jpg" alt="hf_sample25.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample25.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample25.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.64** · slightly_dirty 0.36 · dirty 0.00 · confidenza 0.46
- **Integrità**: integro (`intact`) · probabilità: **intact 0.82** · cracked 0.17 · broken 0.01 · confidenza 0.73
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.37 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>113. figshare_IMG_20220818_160028.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160028.jpg" alt="figshare_IMG_20220818_160028.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160028.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.61
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.34 · **slightly_dirty 0.65** · dirty 0.01 · confidenza 0.48
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.92** · broken 0.04 · confidenza 0.88
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>114. commons_01.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_01.jpg" alt="commons_01.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Brown_egg.jpg](https://commons.wikimedia.org/wiki/File:Brown_egg.jpg)
- **Licenza**: CC BY-SA 1.0 · **Autore**: George Shuklin
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1088
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.55** · slightly_dirty 0.45 · dirty 0.00 · confidenza 0.33
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5092 in / 101 out · costo $0.000214

</details>

<details>
<summary><b>115. figshare_IMG_20220818_160055.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160055.jpg" alt="figshare_IMG_20220818_160055.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160055.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.78
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.25 · **slightly_dirty 0.74** · dirty 0.01 · confidenza 0.61
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.16 · **cracked 0.84** · broken 0.00 · confidenza 0.76
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5429 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>116. hf_sample10.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample10.jpg" alt="hf_sample10.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample10.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample10.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.94** · slightly_dirty 0.06 · dirty 0.00 · confidenza 0.91
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5430 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>117. figshare_IMG_20220818_155905.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155905.jpg" alt="figshare_IMG_20220818_155905.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155905.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.89
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.94** · slightly_dirty 0.06 · dirty 0.00 · confidenza 0.91
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.99** · broken 0.00 · confidenza 0.98
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>118. commons_39.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_39.jpg" alt="commons_39.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huehnereier_2989.jpg](https://commons.wikimedia.org/wiki/File:Huehnereier_2989.jpg)
- **Licenza**: CC BY-SA 2.5 · **Autore**: Rüdiger Wölk       This photo was taken by Rüdiger Wölk.  Please credit this photo Rüdiger Wölk, Münster.    View all photos (large page) of Rüdiger Wölk  I would also appreciate an email to rudiger.wolk@gmail.com with details of use. Für Hinweise auf Veröffentlichungen (rudiger.wolk@gmail.com) oder Belegexemplare bin ich Ihnen dankbar.
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.43 · **slightly_dirty 0.54** · dirty 0.03 · confidenza 0.31
- **Integrità**: integro (`intact`) · probabilità: **intact 0.84** · cracked 0.15 · broken 0.01 · confidenza 0.76
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.43 s · token 4980 in / 104 out · costo $0.000209

</details>

<details>
<summary><b>119. figshare_IMG_20220818_154319.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154319.jpg" alt="figshare_IMG_20220818_154319.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154319.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.48 · **slightly_dirty 0.52** · dirty 0.00 · confidenza 0.28
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.08 · **cracked 0.92** · broken 0.00 · confidenza 0.88
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>120. commons_37.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_37.jpg" alt="commons_37.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown.JPG](https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown.JPG)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Lanntaron
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.88** · dirty 0.10 · confidenza 0.82
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.42 s · token 5430 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>121. figshare_IMG_20220818_160044.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160044.jpg" alt="figshare_IMG_20220818_160044.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160044.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.69
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.28 · **slightly_dirty 0.71** · dirty 0.01 · confidenza 0.56
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.03 · **cracked 0.86** · broken 0.11 · confidenza 0.79
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.38 s · token 5429 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>122. hf_sample24.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample24.jpg" alt="hf_sample24.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample24.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample24.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.80** · slightly_dirty 0.19 · dirty 0.01 · confidenza 0.70
- **Integrità**: integro (`intact`) · probabilità: **intact 0.72** · cracked 0.27 · broken 0.01 · confidenza 0.58
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5427 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>123. figshare_IMG_20220818_155030.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155030.jpg" alt="figshare_IMG_20220818_155030.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155030.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.40 · **slightly_dirty 0.60** · dirty 0.00 · confidenza 0.40
- **Integrità**: integro (`intact`) · probabilità: **intact 0.84** · cracked 0.15 · broken 0.01 · confidenza 0.76
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.43 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>124. hf_sample31.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample31.jpg" alt="hf_sample31.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample31.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample31.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.14 · **slightly_dirty 0.85** · dirty 0.01 · confidenza 0.77
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.09 · broken 0.01 · confidenza 0.85
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5426 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>125. figshare_IMG_20220818_155717.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155717.jpg" alt="figshare_IMG_20220818_155717.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155717.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.92
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.32 · **slightly_dirty 0.67** · dirty 0.01 · confidenza 0.51
- **Integrità**: integro (`intact`) · probabilità: **intact 0.75** · cracked 0.25 · broken 0.00 · confidenza 0.62
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.94 s · token 5425 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>126. hf_sample48.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample48.jpg" alt="hf_sample48.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample48.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample48.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.87** · slightly_dirty 0.13 · dirty 0.00 · confidenza 0.80
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.21 · **cracked 0.79** · broken 0.00 · confidenza 0.69
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>127. figshare_IMG_20220818_154752.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154752.jpg" alt="figshare_IMG_20220818_154752.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154752.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.89
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.16 · **slightly_dirty 0.84** · dirty 0.00 · confidenza 0.76
- **Integrità**: integro (`intact`) · probabilità: **intact 0.65** · cracked 0.35 · broken 0.00 · confidenza 0.48
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5425 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>128. hf_sample23.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample23.jpg" alt="hf_sample23.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample23.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample23.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.74** · slightly_dirty 0.25 · dirty 0.01 · confidenza 0.61
- **Integrità**: integro (`intact`) · probabilità: **intact 0.88** · cracked 0.11 · broken 0.01 · confidenza 0.82
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>129. figshare_IMG_20220818_155804.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155804.jpg" alt="figshare_IMG_20220818_155804.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155804.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.55** · slightly_dirty 0.45 · dirty 0.00 · confidenza 0.33
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.14 · **cracked 0.86** · broken 0.00 · confidenza 0.79
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5425 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>130. commons_10.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_10.jpg" alt="commons_10.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown_(6).JPG](https://commons.wikimedia.org/wiki/File:2_primeros_huevos_isa_brown_(6).JPG)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Lanntaron
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.54** · slightly_dirty 0.45 · dirty 0.01 · confidenza 0.31
- **Integrità**: integro (`intact`) · probabilità: **intact 0.91** · cracked 0.09 · broken 0.00 · confidenza 0.86
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>131. figshare_IMG_20220818_155611.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155611.jpg" alt="figshare_IMG_20220818_155611.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155611.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.88
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.07 · **slightly_dirty 0.92** · dirty 0.01 · confidenza 0.88
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.98** · broken 0.01 · confidenza 0.97
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5429 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>132. hf_sample38.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample38.jpg" alt="hf_sample38.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample38.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample38.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.34 · **slightly_dirty 0.65** · dirty 0.01 · confidenza 0.48
- **Integrità**: integro (`intact`) · probabilità: **intact 0.92** · cracked 0.08 · broken 0.00 · confidenza 0.88
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>133. figshare_IMG_20220818_155724.jpg</b> · accetta (A)</summary>

<img src="../../_pics/figshare_IMG_20220818_155724.jpg" alt="figshare_IMG_20220818_155724.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155724.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.96
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.75** · slightly_dirty 0.25 · dirty 0.00 · confidenza 0.62
- **Integrità**: integro (`intact`) · probabilità: **intact 0.97** · cracked 0.03 · broken 0.00 · confidenza 0.95
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>134. commons_46.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_46.jpg" alt="commons_46.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Cracked_(85516059).jpeg](https://commons.wikimedia.org/wiki/File:Cracked_(85516059).jpeg)
- **Licenza**: CC BY 3.0 · **Autore**: Cyd Haselton
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1041
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.43
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.68** · slightly_dirty 0.19 · dirty 0.13 · confidenza 0.52
- **Integrità**: rotto (`broken`) · probabilità: intact 0.00 · cracked 0.06 · **broken 0.94** · confidenza 0.91
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 4981 in / 100 out · costo $0.000209

</details>

<details>
<summary><b>135. figshare_IMG_20220818_154818.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154818.jpg" alt="figshare_IMG_20220818_154818.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154818.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.13 · **slightly_dirty 0.87** · dirty 0.00 · confidenza 0.80
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>136. hf_sample39.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample39.jpg" alt="hf_sample39.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample39.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample39.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.38 · **slightly_dirty 0.61** · dirty 0.01 · confidenza 0.41
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.10 · broken 0.00 · confidenza 0.85
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5429 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>137. figshare_IMG_20220818_154103.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154103.jpg" alt="figshare_IMG_20220818_154103.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154103.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.60
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.23 · **slightly_dirty 0.76** · dirty 0.01 · confidenza 0.64
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.25 · **cracked 0.63** · broken 0.12 · confidenza 0.45
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>138. hf_sample50.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample50.jpg" alt="hf_sample50.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample50.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample50.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.85** · slightly_dirty 0.14 · dirty 0.01 · confidenza 0.77
- **Integrità**: integro (`intact`) · probabilità: **intact 0.77** · cracked 0.22 · broken 0.01 · confidenza 0.66
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.40 s · token 5426 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>139. figshare_IMG_20220818_155617.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155617.jpg" alt="figshare_IMG_20220818_155617.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155617.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.91
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.10 · **slightly_dirty 0.87** · dirty 0.03 · confidenza 0.80
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.26 · **cracked 0.69** · broken 0.05 · confidenza 0.53
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>140. commons_45.jpg</b> · scarta: rotto</summary>

<img src="../../_pics/commons_45.jpg" alt="commons_45.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggshell_001.jpg](https://commons.wikimedia.org/wiki/File:Eggshell_001.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: H. Zell
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.89** · slightly_dirty 0.06 · dirty 0.05 · confidenza 0.83
- **Integrità**: rotto (`broken`) · probabilità: intact 0.06 · cracked 0.01 · **broken 0.93** · confidenza 0.89
- **Decisione**: scarta: rotto
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5429 in / 100 out · costo $0.000228

</details>

<details>
<summary><b>141. figshare_IMG_20220818_154959.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154959.jpg" alt="figshare_IMG_20220818_154959.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154959.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.84
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.26 · **slightly_dirty 0.73** · dirty 0.01 · confidenza 0.59
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.10 · **cracked 0.83** · broken 0.07 · confidenza 0.74
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>142. commons_26.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_26.jpg" alt="commons_26.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Just_lying_there_being_pretty_(4301382316).jpg](https://commons.wikimedia.org/wiki/File:Just_lying_there_being_pretty_(4301382316).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: storebukkebruse
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.80** · slightly_dirty 0.19 · dirty 0.01 · confidenza 0.70
- **Integrità**: integro (`intact`) · probabilità: **intact 0.81** · cracked 0.19 · broken 0.00 · confidenza 0.72
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5425 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>143. figshare_IMG_20220818_153857.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153857.jpg" alt="figshare_IMG_20220818_153857.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153857.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.87
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.26 · **slightly_dirty 0.74** · dirty 0.00 · confidenza 0.61
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>144. commons_43.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_43.jpg" alt="commons_43.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Broken_egg_orange.jpg](https://commons.wikimedia.org/wiki/File:Broken_egg_orange.jpg)
- **Licenza**: CC BY 3.0 · **Autore**: Goldmund100
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1490
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.12
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.55** · slightly_dirty 0.11 · dirty 0.34 · confidenza 0.33
- **Integrità**: rotto (`broken`) · probabilità: intact 0.00 · cracked 0.01 · **broken 0.99** · confidenza 0.98
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.49 s · token 6772 in / 100 out · costo $0.000284

</details>

<details>
<summary><b>145. figshare_IMG_20220818_154312.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154312.jpg" alt="figshare_IMG_20220818_154312.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154312.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.79
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.63** · slightly_dirty 0.34 · dirty 0.03 · confidenza 0.45
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.32 · **cracked 0.49** · broken 0.19 · confidenza 0.23
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>146. commons_08.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_08.jpg" alt="commons_08.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Giriraja_eggs.jpg](https://commons.wikimedia.org/wiki/File:Giriraja_eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Netha Hussain
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.52** · slightly_dirty 0.47 · dirty 0.01 · confidenza 0.28
- **Integrità**: integro (`intact`) · probabilità: **intact 0.81** · cracked 0.18 · broken 0.01 · confidenza 0.72
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>147. figshare_IMG_20220818_154335.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154335.jpg" alt="figshare_IMG_20220818_154335.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154335.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.92
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.28 · **slightly_dirty 0.71** · dirty 0.01 · confidenza 0.56
- **Integrità**: integro (`intact`) · probabilità: **intact 0.57** · cracked 0.43 · broken 0.00 · confidenza 0.35
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>148. hf_sample15.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample15.jpg" alt="hf_sample15.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample15.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample15.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.76** · slightly_dirty 0.23 · dirty 0.01 · confidenza 0.64
- **Integrità**: integro (`intact`) · probabilità: **intact 0.86** · cracked 0.13 · broken 0.01 · confidenza 0.79
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>149. figshare_IMG_20220818_155547.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155547.jpg" alt="figshare_IMG_20220818_155547.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155547.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.39 · **slightly_dirty 0.60** · dirty 0.01 · confidenza 0.40
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.94** · broken 0.05 · confidenza 0.91
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>150. commons_12.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_12.jpg" alt="commons_12.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_egg.jpg](https://commons.wikimedia.org/wiki/File:Chicken_egg.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Javier8aflores
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1200x900
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.97** · slightly_dirty 0.03 · dirty 0.00 · confidenza 0.95
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 3562 in / 101 out · costo $0.000150

</details>

<details>
<summary><b>151. figshare_IMG_20220818_155047.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155047.jpg" alt="figshare_IMG_20220818_155047.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155047.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.77
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.51** · slightly_dirty 0.49 · dirty 0.00 · confidenza 0.27
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.10 · **cracked 0.90** · broken 0.00 · confidenza 0.85
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>152. commons_31.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_31.jpg" alt="commons_31.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_-_Home_Grown_(or_laid)_(7147848749).jpg](https://commons.wikimedia.org/wiki/File:Eggs_-_Home_Grown_(or_laid)_(7147848749).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: craigles75
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.90** · dirty 0.08 · confidenza 0.85
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 4981 in / 104 out · costo $0.000209

</details>

<details>
<summary><b>153. figshare_IMG_20220818_155700.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155700.jpg" alt="figshare_IMG_20220818_155700.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155700.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.50 · **slightly_dirty 0.50** · dirty 0.00 · confidenza 0.25
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.94** · broken 0.02 · confidenza 0.91
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5429 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>154. hf_sample44.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample44.jpg" alt="hf_sample44.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample44.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample44.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.27 · **slightly_dirty 0.59** · dirty 0.14 · confidenza 0.38
- **Integrità**: integro (`intact`) · probabilità: **intact 0.59** · cracked 0.40 · broken 0.01 · confidenza 0.38
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 5425 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>155. figshare_IMG_20220818_154613.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154613.jpg" alt="figshare_IMG_20220818_154613.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154613.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.87
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.83** · slightly_dirty 0.17 · dirty 0.00 · confidenza 0.74
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.12 · **cracked 0.88** · broken 0.00 · confidenza 0.82
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5430 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>156. commons_38.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_38.jpg" alt="commons_38.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Ei01.jpg](https://commons.wikimedia.org/wiki/File:Ei01.jpg)
- **Licenza**: Public domain · **Autore**: No machine-readable author provided. Acf assumed (based on copyright claims).
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 955x858
- **Verità nota**: nessuna
- **Uovo visibile**: 0.91
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.39 · **slightly_dirty 0.60** · dirty 0.01 · confidenza 0.40
- **Integrità**: integro (`intact`) · probabilità: **intact 0.85** · cracked 0.15 · broken 0.00 · confidenza 0.77
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 2893 in / 104 out · costo $0.000122

</details>

<details>
<summary><b>157. figshare_IMG_20220818_155436.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155436.jpg" alt="figshare_IMG_20220818_155436.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155436.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.89
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.97** · dirty 0.01 · confidenza 0.95
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.06 · **cracked 0.94** · broken 0.00 · confidenza 0.91
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>158. commons_05.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_05.jpg" alt="commons_05.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_egg_2009-06-04.jpg](https://commons.wikimedia.org/wiki/File:Chicken_egg_2009-06-04.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Sun Ladder
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1120x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.92** · slightly_dirty 0.08 · dirty 0.00 · confidenza 0.88
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5198 in / 101 out · costo $0.000218

</details>

<details>
<summary><b>159. figshare_IMG_20220818_154407.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154407.jpg" alt="figshare_IMG_20220818_154407.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154407.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.83
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.54** · slightly_dirty 0.45 · dirty 0.01 · confidenza 0.31
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.08 · **cracked 0.91** · broken 0.01 · confidenza 0.86
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>160. hf_sample49.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample49.jpg" alt="hf_sample49.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample49.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample49.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.93** · slightly_dirty 0.07 · dirty 0.00 · confidenza 0.89
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.96** · broken 0.00 · confidenza 0.94
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5430 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>161. figshare_IMG_20220818_155148.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155148.jpg" alt="figshare_IMG_20220818_155148.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155148.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.70
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.58** · slightly_dirty 0.42 · dirty 0.00 · confidenza 0.37
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.12 · **cracked 0.88** · broken 0.00 · confidenza 0.82
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5429 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>162. hf_sample28.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample28.jpg" alt="hf_sample28.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample28.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample28.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.74** · slightly_dirty 0.26 · dirty 0.00 · confidenza 0.61
- **Integrità**: integro (`intact`) · probabilità: **intact 0.94** · cracked 0.05 · broken 0.01 · confidenza 0.91
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5422 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>163. figshare_IMG_20220818_155959.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155959.jpg" alt="figshare_IMG_20220818_155959.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155959.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.81
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.00 · **slightly_dirty 0.64** · dirty 0.36 · confidenza 0.46
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.02 · **cracked 0.76** · broken 0.22 · confidenza 0.64
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5424 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>164. hf_sample4.jpg</b> · accetta (B)</summary>

<img src="../../_pics/hf_sample4.jpg" alt="hf_sample4.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample4.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample4.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.19 · **slightly_dirty 0.81** · dirty 0.00 · confidenza 0.72
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>165. figshare_IMG_20220818_155744.jpg</b> · accetta (A)</summary>

<img src="../../_pics/figshare_IMG_20220818_155744.jpg" alt="figshare_IMG_20220818_155744.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155744.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.86** · slightly_dirty 0.14 · dirty 0.00 · confidenza 0.79
- **Integrità**: integro (`intact`) · probabilità: **intact 0.83** · cracked 0.17 · broken 0.00 · confidenza 0.74
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5426 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>166. hf_sample36.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample36.jpg" alt="hf_sample36.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample36.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample36.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.87** · slightly_dirty 0.13 · dirty 0.00 · confidenza 0.80
- **Integrità**: integro (`intact`) · probabilità: **intact 0.59** · cracked 0.41 · broken 0.00 · confidenza 0.38
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5426 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>167. figshare_IMG_20220818_154731.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154731.jpg" alt="figshare_IMG_20220818_154731.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154731.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.36 · **slightly_dirty 0.64** · dirty 0.00 · confidenza 0.46
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.96** · broken 0.00 · confidenza 0.94
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>168. commons_09.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_09.jpg" alt="commons_09.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Toj%C3%A1s.jpg](https://commons.wikimedia.org/wiki/File:Toj%C3%A1s.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Safranyl
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 962x1088
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.77** · slightly_dirty 0.23 · dirty 0.00 · confidenza 0.66
- **Integrità**: integro (`intact`) · probabilità: **intact 0.99** · cracked 0.01 · broken 0.00 · confidenza 0.98
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.23 s · token 3454 in / 101 out · costo $0.000145

</details>

<details>
<summary><b>169. figshare_IMG_20220818_154544.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154544.jpg" alt="figshare_IMG_20220818_154544.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154544.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.40 · **slightly_dirty 0.60** · dirty 0.00 · confidenza 0.40
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.22 · **cracked 0.78** · broken 0.00 · confidenza 0.67
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>170. hf_sample51.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/hf_sample51.jpg" alt="hf_sample51.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample51.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/val/sample51.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.84** · slightly_dirty 0.15 · dirty 0.01 · confidenza 0.76
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.25 · **cracked 0.74** · broken 0.01 · confidenza 0.61
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5426 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>171. figshare_IMG_20220818_154218.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154218.jpg" alt="figshare_IMG_20220818_154218.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154218.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.53
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.42 · **slightly_dirty 0.57** · dirty 0.01 · confidenza 0.35
- **Integrità**: integro (`intact`) · probabilità: **intact 0.57** · cracked 0.43 · broken 0.00 · confidenza 0.36
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5430 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>172. commons_21.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_21.jpg" alt="commons_21.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Six_eggs_views_from_the_top_on_a_white_background.jpg](https://commons.wikimedia.org/wiki/File:Six_eggs_views_from_the_top_on_a_white_background.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: TudorTulok
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1244
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.39 · **slightly_dirty 0.60** · dirty 0.01 · confidenza 0.40
- **Integrità**: integro (`intact`) · probabilità: **intact 0.87** · cracked 0.13 · broken 0.00 · confidenza 0.80
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5761 in / 104 out · costo $0.000242

</details>

<details>
<summary><b>173. figshare_IMG_20220818_160033.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_160033.jpg" alt="figshare_IMG_20220818_160033.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_160033.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.81
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.35 · **slightly_dirty 0.64** · dirty 0.01 · confidenza 0.46
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.95** · broken 0.01 · confidenza 0.92
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>174. hf_sample6.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample6.jpg" alt="hf_sample6.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample6.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample6.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.97** · slightly_dirty 0.03 · dirty 0.00 · confidenza 0.95
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.04 · broken 0.01 · confidenza 0.92
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5430 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>175. figshare_IMG_20220818_155523.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155523.jpg" alt="figshare_IMG_20220818_155523.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155523.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.10 · **slightly_dirty 0.86** · dirty 0.04 · confidenza 0.79
- **Integrità**: integro (`intact`) · probabilità: **intact 0.68** · cracked 0.32 · broken 0.00 · confidenza 0.52
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>176. commons_02.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_02.jpg" alt="commons_02.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Eggs_green_brown_on_end.jpg](https://commons.wikimedia.org/wiki/File:Eggs_green_brown_on_end.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Hustvedt
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1019
- **Verità nota**: nessuna
- **Uovo visibile**: 0.96
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.21 · **slightly_dirty 0.77** · dirty 0.02 · confidenza 0.66
- **Integrità**: integro (`intact`) · probabilità: **intact 0.93** · cracked 0.05 · broken 0.02 · confidenza 0.89
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 4870 in / 104 out · costo $0.000205

</details>

<details>
<summary><b>177. figshare_IMG_20220818_154011.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_154011.jpg" alt="figshare_IMG_20220818_154011.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154011.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.92
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.44 · **slightly_dirty 0.56** · dirty 0.00 · confidenza 0.34
- **Integrità**: integro (`intact`) · probabilità: **intact 0.91** · cracked 0.07 · broken 0.02 · confidenza 0.86
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5429 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>178. commons_28.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_28.jpg" alt="commons_28.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Chicken_eggs_21.jpg](https://commons.wikimedia.org/wiki/File:Chicken_eggs_21.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: BogTar201213
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1172
- **Verità nota**: nessuna
- **Uovo visibile**: 0.97
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.75** · dirty 0.23 · confidenza 0.62
- **Integrità**: integro (`intact`) · probabilità: **intact 0.91** · cracked 0.09 · broken 0.00 · confidenza 0.86
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5430 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>179. figshare_IMG_20220818_154708.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154708.jpg" alt="figshare_IMG_20220818_154708.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154708.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.44 · **slightly_dirty 0.56** · dirty 0.00 · confidenza 0.34
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.11 · **cracked 0.89** · broken 0.00 · confidenza 0.83
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5426 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>180. commons_33.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_33.jpg" alt="commons_33.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Flickr_-_cyclonebill_-_%C3%86g_(1).jpg](https://commons.wikimedia.org/wiki/File:Flickr_-_cyclonebill_-_%C3%86g_(1).jpg)
- **Licenza**: CC BY-SA 2.0 · **Autore**: cyclonebill
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.95
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.75** · slightly_dirty 0.24 · dirty 0.01 · confidenza 0.62
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.01 · **cracked 0.96** · broken 0.03 · confidenza 0.94
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>181. figshare_IMG_20220818_155812.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_155812.jpg" alt="figshare_IMG_20220818_155812.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155812.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.88
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.31 · **slightly_dirty 0.67** · dirty 0.02 · confidenza 0.51
- **Integrità**: integro (`intact`) · probabilità: **intact 0.90** · cracked 0.09 · broken 0.01 · confidenza 0.85
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>182. commons_35.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_35.jpg" alt="commons_35.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:MonstereiXXXL.jpg](https://commons.wikimedia.org/wiki/File:MonstereiXXXL.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: -jkb-
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.52** · slightly_dirty 0.48 · dirty 0.00 · confidenza 0.28
- **Integrità**: integro (`intact`) · probabilità: **intact 0.57** · cracked 0.43 · broken 0.00 · confidenza 0.35
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>183. figshare_IMG_20220818_155915.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155915.jpg" alt="figshare_IMG_20220818_155915.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155915.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.69** · slightly_dirty 0.31 · dirty 0.00 · confidenza 0.53
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.13 · **cracked 0.86** · broken 0.01 · confidenza 0.79
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.32 s · token 5428 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>184. commons_07.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_07.jpg" alt="commons_07.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_colours.jpg](https://commons.wikimedia.org/wiki/File:Egg_colours.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Timothy Titus
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x922
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.41 · **slightly_dirty 0.52** · dirty 0.07 · confidenza 0.28
- **Integrità**: integro (`intact`) · probabilità: **intact 0.50** · cracked 0.50 · broken 0.00 · confidenza 0.25
- **Decisione**: accetta (B) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.37 s · token 4421 in / 104 out · costo $0.000186

</details>

<details>
<summary><b>185. figshare_IMG_20220818_153638.jpg</b> · accetta (B)</summary>

<img src="../../_pics/figshare_IMG_20220818_153638.jpg" alt="figshare_IMG_20220818_153638.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_153638.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.95
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.25 · **slightly_dirty 0.74** · dirty 0.01 · confidenza 0.61
- **Integrità**: integro (`intact`) · probabilità: **intact 0.91** · cracked 0.09 · broken 0.00 · confidenza 0.86
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.26 s · token 5428 in / 104 out · costo $0.000228

</details>

<details>
<summary><b>186. commons_29.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_29.jpg" alt="commons_29.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Braunes_H%C3%BChnerei.JPG](https://commons.wikimedia.org/wiki/File:Braunes_H%C3%BChnerei.JPG)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Fiver, der Hellseher
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1176
- **Verità nota**: nessuna
- **Uovo visibile**: 0.92
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.89** · slightly_dirty 0.10 · dirty 0.01 · confidenza 0.83
- **Integrità**: integro (`intact`) · probabilità: **intact 0.98** · cracked 0.02 · broken 0.00 · confidenza 0.97
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5428 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>187. figshare_IMG_20220818_155503.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155503.jpg" alt="figshare_IMG_20220818_155503.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155503.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.90
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.07 · **slightly_dirty 0.92** · dirty 0.01 · confidenza 0.88
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.04 · **cracked 0.96** · broken 0.00 · confidenza 0.94
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.31 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>188. hf_sample45.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample45.jpg" alt="hf_sample45.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample45.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample45.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.73** · slightly_dirty 0.26 · dirty 0.01 · confidenza 0.59
- **Integrità**: integro (`intact`) · probabilità: **intact 0.83** · cracked 0.17 · broken 0.00 · confidenza 0.74
- **Decisione**: accetta (A) · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5429 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>189. figshare_IMG_20220818_154847.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154847.jpg" alt="figshare_IMG_20220818_154847.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154847.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.89
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.03 · **slightly_dirty 0.95** · dirty 0.02 · confidenza 0.92
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.11 · **cracked 0.87** · broken 0.02 · confidenza 0.80
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>190. hf_sample21.jpg</b> · accetta (A)</summary>

<img src="../../_pics/hf_sample21.jpg" alt="hf_sample21.jpg" width="260">

- **Origine**: [https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample21.jpg](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/train/sample21.jpg)
- **Licenza**: MIT · **Autore**: afshin-dini
- **Scena**: cartone con più uova · **Uova**: bianche e marroni · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: nessuna
- **Uovo visibile**: 0.99
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.95** · slightly_dirty 0.05 · dirty 0.00 · confidenza 0.92
- **Integrità**: integro (`intact`) · probabilità: **intact 0.97** · cracked 0.02 · broken 0.01 · confidenza 0.95
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5427 in / 101 out · costo $0.000228

</details>

<details>
<summary><b>191. figshare_IMG_20220818_154328.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154328.jpg" alt="figshare_IMG_20220818_154328.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154328.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.80
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.52** · slightly_dirty 0.48 · dirty 0.00 · confidenza 0.28
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.18 · **cracked 0.82** · broken 0.00 · confidenza 0.73
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.41 s · token 5427 in / 102 out · costo $0.000228

</details>

<details>
<summary><b>192. commons_22.jpg</b> · accetta (B)</summary>

<img src="../../_pics/commons_22.jpg" alt="commons_22.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Diff%C3%A9rents_oeufs.jpg](https://commons.wikimedia.org/wiki/File:Diff%C3%A9rents_oeufs.jpg)
- **Licenza**: CC BY-SA 4.0 · **Autore**: Tylwyth Eldar
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1045
- **Verità nota**: nessuna
- **Uovo visibile**: 0.96
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.01 · **slightly_dirty 0.86** · dirty 0.13 · confidenza 0.79
- **Integrità**: integro (`intact`) · probabilità: **intact 0.95** · cracked 0.05 · broken 0.00 · confidenza 0.92
- **Decisione**: accetta (B)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 4981 in / 104 out · costo $0.000209

</details>

<details>
<summary><b>193. figshare_IMG_20220818_154724.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154724.jpg" alt="figshare_IMG_20220818_154724.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154724.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.93
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.38 · **slightly_dirty 0.61** · dirty 0.01 · confidenza 0.41
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.16 · **cracked 0.74** · broken 0.10 · confidenza 0.61
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.25 s · token 5430 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>194. commons_44.jpg</b> · non valutabile</summary>

<img src="../../_pics/commons_44.jpg" alt="commons_44.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huevo_Quebrado.jpg](https://commons.wikimedia.org/wiki/File:Huevo_Quebrado.jpg)
- **Licenza**: Public domain · **Autore**: Jorge Barrios
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 965x723
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.23
- **Pulizia**: sporco (`dirty`) · probabilità: clean 0.26 · slightly_dirty 0.11 · **dirty 0.63** · confidenza 0.45
- **Integrità**: rotto (`broken`) · probabilità: intact 0.00 · cracked 0.00 · **broken 1.00** · confidenza 1.00
- **Decisione**: non valutabile
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.29 s · token 2545 in / 100 out · costo $0.000107

</details>

<details>
<summary><b>195. figshare_IMG_20220818_155132.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_155132.jpg" alt="figshare_IMG_20220818_155132.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_155132.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.91
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.45 · **slightly_dirty 0.55** · dirty 0.00 · confidenza 0.33
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.02 · **cracked 0.98** · broken 0.00 · confidenza 0.97
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.30 s · token 5427 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>196. commons_40.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/commons_40.jpg" alt="commons_40.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Huehnerei_mit_Sprung_(fcm).jpg](https://commons.wikimedia.org/wiki/File:Huehnerei_mit_Sprung_(fcm).jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Frank C. Müller
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1568x1314
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.90
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.91** · slightly_dirty 0.08 · dirty 0.01 · confidenza 0.86
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.00 · **cracked 0.94** · broken 0.06 · confidenza 0.91
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.27 s · token 5989 in / 102 out · costo $0.000252

</details>

<details>
<summary><b>197. figshare_IMG_20220818_154905.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154905.jpg" alt="figshare_IMG_20220818_154905.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154905.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.94
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.02 · **slightly_dirty 0.94** · dirty 0.04 · confidenza 0.91
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.47 · **cracked 0.53** · broken 0.00 · confidenza 0.30
- **Decisione**: scarta: crepato · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.33 s · token 5426 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>198. commons_41.jpg</b> · scarta: rotto, sporco</summary>

<img src="../../_pics/commons_41.jpg" alt="commons_41.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Bloody-eggs.jpg](https://commons.wikimedia.org/wiki/File:Bloody-eggs.jpg)
- **Licenza**: CC BY-SA 3.0 · **Autore**: Maqi
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 900x675
- **Verità nota**: nessuna (foto scelta perché mostra un difetto visibile, non annotata)
- **Uovo visibile**: 0.99
- **Pulizia**: sporco (`dirty`) · probabilità: clean 0.22 · slightly_dirty 0.20 · **dirty 0.58** · confidenza 0.37
- **Integrità**: rotto (`broken`) · probabilità: intact 0.00 · cracked 0.12 · **broken 0.88** · confidenza 0.82
- **Decisione**: scarta: rotto, sporco · da verificare (confidenza bassa)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.37 s · token 2374 in / 100 out · costo $0.000100

</details>

<details>
<summary><b>199. figshare_IMG_20220818_154943.jpg</b> · scarta: crepato</summary>

<img src="../../_pics/figshare_IMG_20220818_154943.jpg" alt="figshare_IMG_20220818_154943.jpg" width="260">

- **Origine**: [https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) (zip entry: test_100/IMG_20220818_154943.jpg)
- **Licenza**: CC BY 4.0 · **Autore**: Bhavya Botta, Ashis Kumar Datta
- **Scena**: uovo singolo · **Uova**: bianche · **Dimensioni analizzate**: 1176x1568
- **Verità nota**: cracked
- **Uovo visibile**: 0.79
- **Pulizia**: lievemente sporco (`slightly_dirty`) · probabilità: clean 0.21 · **slightly_dirty 0.79** · dirty 0.00 · confidenza 0.69
- **Integrità**: crepato (`cracked`) · probabilità: intact 0.06 · **cracked 0.86** · broken 0.08 · confidenza 0.79
- **Decisione**: scarta: crepato
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.28 s · token 5428 in / 105 out · costo $0.000228

</details>

<details>
<summary><b>200. commons_24.jpg</b> · accetta (A)</summary>

<img src="../../_pics/commons_24.jpg" alt="commons_24.jpg" width="260">

- **Origine**: [https://commons.wikimedia.org/wiki/File:Egg_(394351849).jpg](https://commons.wikimedia.org/wiki/File:Egg_(394351849).jpg)
- **Licenza**: CC BY 2.0 · **Autore**: liz west from Boxborough, MA, USA
- **Scena**: poche uova · **Uova**: marroni (varie tonalità) · **Dimensioni analizzate**: 1550x1549
- **Verità nota**: nessuna
- **Uovo visibile**: 0.98
- **Pulizia**: pulito (`clean`) · probabilità: **clean 0.86** · slightly_dirty 0.14 · dirty 0.00 · confidenza 0.79
- **Integrità**: integro (`intact`) · probabilità: **intact 0.92** · cracked 0.08 · broken 0.00 · confidenza 0.88
- **Decisione**: accetta (A)
- **Chiamata**: modello `typesafe/jev-1.14-20261014` · latenza 0.34 s · token 6997 in / 101 out · costo $0.000294

</details>
