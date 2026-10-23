# Confronto tra modelli: ispezione uova

Data: 23 ottobre 2026 alle ore 17:37. Stesse 200 foto (su 200 disponibili), stesse domande, stessa regola di decisione.

## In breve

- **Più veloce**: Jev 1.14, latenza mediana 0.31 s. **Più economico**: Jev 1.14, $0.2246 ogni 1000 foto.
- **Crepe note riconosciute** (100 foto Figshare): Jev 1.14 70, GPT-6 Luna Decisions 75, GPT-6 Luna (LLM, raffronto) 76, GPT-6.1 Sol (LLM, raffronto) 82.
- **Decisione identica** (accetta o scarta) in 158 foto su 200; nelle altre 42 almeno un modello decide diversamente (elenco più sotto).
- **GPT-6.1 Sol** è il modello più costoso ($7.2520 ogni 1000 foto) e scarta di più: 107 foto su 200. È usato come secondo parere, non come verità: analisi in una sezione dedicata più sotto.
- Una quota di scarti più alta non significa risultati migliori: solo le foto con crepa nota permettono di dire chi ha ragione, per le altre manca una verità di riferimento.

## Risultati a confronto

| Metrica | Jev 1.14 | GPT-6 Luna Decisions | GPT-6 Luna (LLM, raffronto) | GPT-6.1 Sol (LLM, raffronto) |
| --- | ---: | ---: | ---: | ---: |
| Modello servito | `typesafe/jev-1.14-20261014` | `openai/gpt-6-luna-decisions-20261006` | `openai/gpt-6-luna` | `openai/gpt-6.1-sol` |
| Foto analizzate | 200 | 200 | 200 | 200 |
| Errori | 0 | 0 | 0 | 0 |
| Accettate (A + B) | 111 (55.5%) | 103 (51.5%) | 95 (47.5%) | 90 (45.0%) |
| di cui grado B (lievemente sporche) | 50 | 53 | 57 | 54 |
| Scartate | 82 (41.0%) | 89 (44.5%) | 101 (50.5%) | 107 (53.5%) |
| Non valutabili | 7 | 8 | 4 | 3 |
| Pulite / lievemente sporche / sporche | 99 / 95 / 6 | 79 / 111 / 10 | 73 / 118 / 9 | 82 / 111 / 7 |
| Integre / crepate / rotte | 113 / 78 / 9 | 107 / 85 / 8 | 100 / 92 / 8 | 92 / 99 / 9 |
| Etichette "da verificare" | 97 | 85 | n/d | n/d |
| Probabilità media dell'etichetta scelta | 0.80 | 0.84 | n/d | n/d |
| Latenza media | 0.35 s | 0.61 s | 5.91 s | 6.95 s |
| Latenza p50 | 0.31 s | 0.56 s | 5.69 s | 5.96 s |
| Latenza p95 | 0.62 s | 1.11 s | 8.73 s | 13.15 s |
| Token in ingresso (totale) | 1069390 | 484235 | 506290 | 506290 |
| Token in uscita (totale) | 20554 | 0 | 27130 | 18497 |
| Costo totale | $0.0449 | $0.0484 | $0.0768 | $1.4504 |
| Costo per 1000 foto | $0.2246 | $0.2421 | $0.3842 | $7.2520 |

Le latenze sono misurate dal client e includono la rete. Il costo è la somma di `usage.cost` restituito da OpenRouter.

## Per tipo di scena

Foto scartate su foto analizzate.

| Scena | Foto | Jev 1.14 | GPT-6 Luna Decisions | GPT-6 Luna (LLM, raffronto) | GPT-6.1 Sol (LLM, raffronto) |
| --- | ---: | ---: | ---: | ---: | ---: |
| uovo singolo | 100 | 69 | 73 | 76 | 82 |
| poche uova | 49 | 6 | 7 | 12 | 10 |
| cartone con più uova | 51 | 7 | 9 | 13 | 15 |

## Crepe note (foto Figshare)

Le 100 foto Figshare analizzate hanno una crepa annotata a mano. Un modello "riconosce" la crepa se giudica l'integrità `cracked` o `broken`.

| Modello | Riconosciute | Quota |
| --- | ---: | ---: |
| Jev 1.14 | 70 su 100 | 70.0% |
| GPT-6 Luna Decisions | 75 su 100 | 75.0% |
| GPT-6 Luna (LLM, raffronto) | 76 su 100 | 76.0% |
| GPT-6.1 Sol (LLM, raffronto) | 82 su 100 | 82.0% |

- Riconosciute da **tutti** i modelli: 70
- Riconosciute da **alcuni**: 12
- Mancate da **tutti**: 18

Mancate da tutti: [figshare_IMG_20220818_154808.jpg](../../_pics/figshare_IMG_20220818_154808.jpg), [figshare_IMG_20220818_155248.jpg](../../_pics/figshare_IMG_20220818_155248.jpg), [figshare_IMG_20220818_155341.jpg](../../_pics/figshare_IMG_20220818_155341.jpg), [figshare_IMG_20220818_153759.jpg](../../_pics/figshare_IMG_20220818_153759.jpg), [figshare_IMG_20220818_154019.jpg](../../_pics/figshare_IMG_20220818_154019.jpg), [figshare_IMG_20220818_154636.jpg](../../_pics/figshare_IMG_20220818_154636.jpg), [figshare_IMG_20220818_155401.jpg](../../_pics/figshare_IMG_20220818_155401.jpg), [figshare_IMG_20220818_153842.jpg](../../_pics/figshare_IMG_20220818_153842.jpg), [figshare_IMG_20220818_154238.jpg](../../_pics/figshare_IMG_20220818_154238.jpg), [figshare_IMG_20220818_155353.jpg](../../_pics/figshare_IMG_20220818_155353.jpg), [figshare_IMG_20220818_153953.jpg](../../_pics/figshare_IMG_20220818_153953.jpg), [figshare_IMG_20220818_155030.jpg](../../_pics/figshare_IMG_20220818_155030.jpg), [figshare_IMG_20220818_154818.jpg](../../_pics/figshare_IMG_20220818_154818.jpg), [figshare_IMG_20220818_153857.jpg](../../_pics/figshare_IMG_20220818_153857.jpg), [figshare_IMG_20220818_155744.jpg](../../_pics/figshare_IMG_20220818_155744.jpg), [figshare_IMG_20220818_155523.jpg](../../_pics/figshare_IMG_20220818_155523.jpg), [figshare_IMG_20220818_154011.jpg](../../_pics/figshare_IMG_20220818_154011.jpg), [figshare_IMG_20220818_155812.jpg](../../_pics/figshare_IMG_20220818_155812.jpg).

Il set non contiene uova integre con etichetta certa, quindi i falsi allarmi (uova integre scartate) non si possono misurare. Le crepe sono sottili e le foto sono ridotte a 1568 px.

## Accordo tra modelli

Decisione identica (accetta, scarta o non valutabile) sulle 200 foto in comune.

| Coppia | Stessa decisione |
| --- | ---: |
| Jev 1.14 / GPT-6 Luna Decisions | 181 su 200 (90.5%) |
| Jev 1.14 / GPT-6 Luna (LLM, raffronto) | 179 su 200 (89.5%) |
| Jev 1.14 / GPT-6.1 Sol (LLM, raffronto) | 171 su 200 (85.5%) |
| GPT-6 Luna Decisions / GPT-6 Luna (LLM, raffronto) | 184 su 200 (92.0%) |
| GPT-6 Luna Decisions / GPT-6.1 Sol (LLM, raffronto) | 174 su 200 (87.0%) |
| GPT-6 Luna (LLM, raffronto) / GPT-6.1 Sol (LLM, raffronto) | 176 su 200 (88.0%) |
| Tutti e 4 | 158 su 200 (79.0%) |

## Foto con decisioni discordanti

| Foto | Scena | Verità nota | Jev 1.14 | GPT-6 Luna Decisions | GPT-6 Luna (LLM, raffronto) | GPT-6.1 Sol (LLM, raffronto) |
| --- | --- | --- | --- | --- | --- | --- |
| [commons_03.jpg](../../_pics/commons_03.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato |
| [commons_36.jpg](../../_pics/commons_36.jpg) | poche uova | n/d | **scarta**: pulito, crepato | accetta: pulito, integro | **scarta**: pulito, crepato | accetta: pulito, integro |
| [hf_sample9.jpg](../../_pics/hf_sample9.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato | accetta: pulito, integro |
| [figshare_IMG_20220818_155457.jpg](../../_pics/figshare_IMG_20220818_155457.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato |
| [hf_sample8.jpg](../../_pics/hf_sample8.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato | accetta: pulito, integro |
| [commons_27.jpg](../../_pics/commons_27.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: sporco, integro | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_154535.jpg](../../_pics/figshare_IMG_20220818_154535.jpg) | uovo singolo | cracked | accetta: pulito, integro | accetta: pulito, integro | accetta: lievemente sporco, integro | **scarta**: pulito, crepato |
| [hf_sample13.jpg](../../_pics/hf_sample13.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato | accetta: pulito, integro |
| [figshare_IMG_20220818_155137.jpg](../../_pics/figshare_IMG_20220818_155137.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: pulito, crepato |
| [commons_42.jpg](../../_pics/commons_42.jpg) | poche uova | n/d | **scarta**: sporco, rotto | non valutabile: sporco, integro | **scarta**: sporco, integro | **scarta**: sporco, integro |
| [figshare_IMG_20220818_155511.jpg](../../_pics/figshare_IMG_20220818_155511.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato |
| [figshare_IMG_20220818_154136.jpg](../../_pics/figshare_IMG_20220818_154136.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato |
| [figshare_IMG_20220818_154759.jpg](../../_pics/figshare_IMG_20220818_154759.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato |
| [commons_47.jpg](../../_pics/commons_47.jpg) | poche uova | n/d | non valutabile: lievemente sporco, integro | non valutabile: pulito, integro | non valutabile: pulito, integro | accetta: lievemente sporco, integro |
| [hf_sample17.jpg](../../_pics/hf_sample17.jpg) | cartone con più uova | n/d | accetta: pulito, integro | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_155846.jpg](../../_pics/figshare_IMG_20220818_155846.jpg) | uovo singolo | cracked | **scarta**: pulito, crepato | non valutabile: pulito, crepato | **scarta**: pulito, crepato | **scarta**: pulito, crepato |
| [commons_48.jpg](../../_pics/commons_48.jpg) | poche uova | n/d | non valutabile: lievemente sporco, integro | non valutabile: pulito, integro | non valutabile: pulito, integro | accetta: lievemente sporco, integro |
| [hf_sample37.jpg](../../_pics/hf_sample37.jpg) | cartone con più uova | n/d | **scarta**: pulito, crepato | accetta: pulito, integro | **scarta**: lievemente sporco, crepato | **scarta**: pulito, crepato |
| [hf_sample40.jpg](../../_pics/hf_sample40.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato |
| [hf_sample41.jpg](../../_pics/hf_sample41.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: pulito, crepato |
| [hf_sample43.jpg](../../_pics/hf_sample43.jpg) | cartone con più uova | n/d | accetta: lievemente sporco, integro | **scarta**: pulito, crepato | **scarta**: lievemente sporco, crepato | **scarta**: pulito, crepato |
| [commons_49.jpg](../../_pics/commons_49.jpg) | poche uova | n/d | non valutabile: lievemente sporco, rotto | **scarta**: sporco, rotto | **scarta**: sporco, rotto | **scarta**: lievemente sporco, rotto |
| [hf_sample42.jpg](../../_pics/hf_sample42.jpg) | cartone con più uova | n/d | accetta: pulito, integro | **scarta**: lievemente sporco, crepato | **scarta**: pulito, crepato | **scarta**: pulito, crepato |
| [hf_sample35.jpg](../../_pics/hf_sample35.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: lievemente sporco, integro | accetta: pulito, integro | **scarta**: pulito, crepato |
| [figshare_IMG_20220818_154113.jpg](../../_pics/figshare_IMG_20220818_154113.jpg) | uovo singolo | cracked | non valutabile: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato |
| [commons_39.jpg](../../_pics/commons_39.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | accetta: pulito, integro | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato |
| [figshare_IMG_20220818_155717.jpg](../../_pics/figshare_IMG_20220818_155717.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: pulito, crepato |
| [figshare_IMG_20220818_154752.jpg](../../_pics/figshare_IMG_20220818_154752.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato |
| [figshare_IMG_20220818_155724.jpg](../../_pics/figshare_IMG_20220818_155724.jpg) | uovo singolo | cracked | accetta: pulito, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: pulito, crepato |
| [commons_46.jpg](../../_pics/commons_46.jpg) | poche uova | n/d | non valutabile: pulito, rotto | non valutabile: pulito, rotto | **scarta**: pulito, rotto | non valutabile: pulito, rotto |
| [hf_sample50.jpg](../../_pics/hf_sample50.jpg) | cartone con più uova | n/d | accetta: pulito, integro | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato |
| [figshare_IMG_20220818_154335.jpg](../../_pics/figshare_IMG_20220818_154335.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato |
| [hf_sample44.jpg](../../_pics/hf_sample44.jpg) | cartone con più uova | n/d | accetta: lievemente sporco, integro | accetta: pulito, integro | **scarta**: pulito, crepato | **scarta**: sporco, integro |
| [figshare_IMG_20220818_155959.jpg](../../_pics/figshare_IMG_20220818_155959.jpg) | uovo singolo | cracked | **scarta**: lievemente sporco, crepato | non valutabile: sporco, crepato | **scarta**: sporco, crepato | **scarta**: sporco, crepato |
| [hf_sample36.jpg](../../_pics/hf_sample36.jpg) | cartone con più uova | n/d | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato | **scarta**: pulito, crepato |
| [commons_09.jpg](../../_pics/commons_09.jpg) | poche uova | n/d | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato | **scarta**: pulito, crepato |
| [hf_sample51.jpg](../../_pics/hf_sample51.jpg) | cartone con più uova | n/d | **scarta**: pulito, crepato | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: pulito, crepato |
| [figshare_IMG_20220818_154218.jpg](../../_pics/figshare_IMG_20220818_154218.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato |
| [commons_28.jpg](../../_pics/commons_28.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_153638.jpg](../../_pics/figshare_IMG_20220818_153638.jpg) | uovo singolo | cracked | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | accetta: lievemente sporco, integro | **scarta**: lievemente sporco, crepato |
| [commons_22.jpg](../../_pics/commons_22.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | **scarta**: sporco, integro | **scarta**: sporco, integro | accetta: lievemente sporco, integro |
| [commons_24.jpg](../../_pics/commons_24.jpg) | poche uova | n/d | accetta: pulito, integro | accetta: pulito, integro | accetta: pulito, integro | **scarta**: pulito, crepato |

## GPT-6.1 Sol come ulteriore termine di confronto

Sol è un modello generativo più grande e più costoso degli altri. Qui è usato come **secondo parere**: le sue risposte non sono una verità certificata, quindi un accordo con Sol non dimostra che un modello abbia ragione, e un disaccordo non dimostra che abbia torto. Sull'unica verità nota, la crepa delle foto Figshare, il confronto è nella sezione sopra.

| Modello | Stessa decisione di Sol | Stessa pulizia | Stessa integrità |
| --- | ---: | ---: | ---: |
| Jev 1.14 | 171 su 200 (85.5%) | 163 (81.5%) | 174 (87.0%) |
| GPT-6 Luna Decisions | 174 su 200 (87.0%) | 159 (79.5%) | 180 (90.0%) |
| GPT-6 Luna (LLM, raffronto) | 176 su 200 (88.0%) | 158 (79.0%) | 179 (89.5%) |

- Gli altri 3 modelli concordano tra loro e **solo Sol decide diversamente** in 14 foto su 200: in 12 Sol scarta e gli altri accettano, in 2 Sol accetta e gli altri scartano.
- Gli altri 3 modelli non concordano tra loro in 28 foto.
- **Voto di maggioranza** dei 4 modelli (i "non valutabili" non votano): 99 foto da accettare, 90 da scartare, 9 in parità, 2 senza voti.
  - Jev 1.14 coincide con la maggioranza in 177 foto su 189 (93.7%).
  - GPT-6 Luna Decisions coincide con la maggioranza in 181 foto su 189 (95.8%).
  - GPT-6 Luna (LLM, raffronto) coincide con la maggioranza in 183 foto su 189 (96.8%).
  - GPT-6.1 Sol (LLM, raffronto) coincide con la maggioranza in 176 foto su 189 (93.1%).

Sulle 100 foto con crepa nota: **6** crepe sono riconosciute solo da Sol, **0** sono mancate da Sol ma riconosciute da almeno un altro modello, **18** sono mancate da tutti i 4 modelli.

Costo e tempo di Sol rispetto agli altri: Jev 1.14 costa 32.3 volte meno di Sol; GPT-6 Luna Decisions costa 30.0 volte meno di Sol; GPT-6 Luna (LLM, raffronto) costa 18.9 volte meno di Sol. Latenza mediana di Sol 5.96 s contro 0.31 s (Jev 1.14), 0.56 s (GPT-6 Luna Decisions), 5.69 s (GPT-6 Luna (LLM, raffronto)).

### Foto in cui solo Sol decide diversamente

| Foto | Scena | Verità nota | Sol | Gli altri 3 (stessa decisione; etichette di Jev 1.14) |
| --- | --- | --- | --- | --- |
| [commons_03.jpg](../../_pics/commons_03.jpg) | poche uova | n/d | **scarta**: pulito, crepato | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_155457.jpg](../../_pics/figshare_IMG_20220818_155457.jpg) | uovo singolo | cracked | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_154535.jpg](../../_pics/figshare_IMG_20220818_154535.jpg) | uovo singolo | cracked | **scarta**: pulito, crepato | accetta: pulito, integro |
| [figshare_IMG_20220818_154759.jpg](../../_pics/figshare_IMG_20220818_154759.jpg) | uovo singolo | cracked | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro |
| [commons_47.jpg](../../_pics/commons_47.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | non valutabile: lievemente sporco, integro |
| [commons_48.jpg](../../_pics/commons_48.jpg) | poche uova | n/d | accetta: lievemente sporco, integro | non valutabile: lievemente sporco, integro |
| [hf_sample40.jpg](../../_pics/hf_sample40.jpg) | cartone con più uova | n/d | **scarta**: lievemente sporco, crepato | accetta: pulito, integro |
| [hf_sample41.jpg](../../_pics/hf_sample41.jpg) | cartone con più uova | n/d | **scarta**: pulito, crepato | accetta: pulito, integro |
| [hf_sample35.jpg](../../_pics/hf_sample35.jpg) | cartone con più uova | n/d | **scarta**: pulito, crepato | accetta: pulito, integro |
| [commons_39.jpg](../../_pics/commons_39.jpg) | poche uova | n/d | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_155717.jpg](../../_pics/figshare_IMG_20220818_155717.jpg) | uovo singolo | cracked | **scarta**: pulito, crepato | accetta: lievemente sporco, integro |
| [figshare_IMG_20220818_155724.jpg](../../_pics/figshare_IMG_20220818_155724.jpg) | uovo singolo | cracked | **scarta**: pulito, crepato | accetta: pulito, integro |
| [figshare_IMG_20220818_153638.jpg](../../_pics/figshare_IMG_20220818_153638.jpg) | uovo singolo | cracked | **scarta**: lievemente sporco, crepato | accetta: lievemente sporco, integro |
| [commons_24.jpg](../../_pics/commons_24.jpg) | poche uova | n/d | **scarta**: pulito, crepato | accetta: pulito, integro |

## Come leggere questi numeri

- Le pipeline usano le stesse definizioni di pulizia e integrità, le stesse foto e la stessa regola di scarto; cambia solo il modello.
- Solo la crepa delle foto Figshare ha una verità annotata. Per la pulizia e per le altre foto i report mostrano cosa decide ogni modello, non chi ha ragione.
- Il modello LLM non dà probabilità e, senza `temperature`, può rispondere in modo diverso tra due esecuzioni.
- Il campione è piccolo: le differenze di pochi punti percentuali non sono significative.

## Report per modello

- [Jev 1.14](report-typesafe_jev-1.14.md)
- [GPT-6 Luna Decisions](report-openai_gpt-6-luna-decisions.md)
- [GPT-6 Luna (LLM, raffronto)](report-openai_gpt-6-luna.md)
- [GPT-6.1 Sol (LLM, raffronto)](report-openai_gpt-6.1-sol.md)

## Dataset di origine delle foto

| Dataset | Autori | Licenza | Foto nella demo | URL originali |
| --- | --- | --- | ---: | --- |
| Dataset for real-time crack detection on chicken eggs (split test) | Bhavya Botta, Ashis Kumar Datta | CC BY 4.0 | 100 | [pagina](https://figshare.com/articles/dataset/Dataset_for_real-time_crack_detection_on_chicken_eggs/21568425) · [DOI](https://doi.org/10.6084/m9.figshare.21568425.v1) · [file](https://ndownloader.figshare.com/files/38230539) |
| Wikimedia Commons: Category:Brown chicken eggs, Category:Chicken eggs, Category:Cracked eggs | Vari (autore e licenza per file nel manifest) | CC0 / CC BY / CC BY-SA / pubblico dominio (per file) | 49 | [pagina](https://commons.wikimedia.org/wiki/Category:Brown_chicken_eggs) |
| Egg-Detection (white-egg / brown-egg) | afshin-dini | MIT | 51 | [pagina](https://huggingface.co/datasets/afshin-dini/Egg-Detection) · [file](https://huggingface.co/datasets/afshin-dini/Egg-Detection/resolve/d425996c959623b3960fca27f53b16f060b0a474/data/images/) |

- **figshare_test**: Uova di gallina bianche singole con crepe sottili, annotazioni VOC (classi egg, crack).
- **wikimedia_commons**: Selezione manuale di 49 foto: uova marroni di varie tonalitÃ  e alcune con crepe, rotture, sangue o piume. Non annotate.
- **hf_egg_detection**: Cartoni con piÃ¹ uova bianche e marroni. afshin-dini/Egg-Instance-Segmentation contiene le stesse immagini.
