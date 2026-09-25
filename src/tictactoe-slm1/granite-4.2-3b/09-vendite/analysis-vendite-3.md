# Analysis Vendite - Turno 3

## Data di input (CSV)
| canale | categoria | prodotto | unita | prezzo |
|--------|-----------|----------|------:|-------:|
| Ads    | Casa      | Lampada  |     2 |     30 |
| Organico | Tech   | Mouse    |     1 |     25 |
| Ads    | Tech      | Mouse    |     3 |     25 |
| Email  | Casa       | Tazza    |     4 |     10 |
| Organico | Casa      | Lampada  |     1 |     30 |
| Ads    | Casa       | Tazza    |     5 |     10 |
| Email  | Tech        | Mouse    |     2 |     25 |
| Organico | Tech      | Tastiera  |     1 |     80 |

## Calcoli

### Per canale e categoria (aggregazione unita e revenue)

| canale       | categoria  | prodotto           | unita totale | revenue totale (unita*prezzo) |
|--------------|------------|--------------------|-------------:|----------------------------:|
| Ads          | Casa       | Lampada            |         2   |        60 |
| Ads          | Tech       | Mouse              |         3   |        75 |
| Email        | Casa       | Tazza              |         4   |        40 |
| Organico      | Casa       | Lampada            |         1   |        30 |
| Organico      | Tech       | Mouse / Tastiera    |         2   |       105 |

*Nota: Per categorie multiple (es. Organico/Tech), i prodotti sono aggregati.*

### Top prodotto unita (per tutti i prodotti)
- Mouse: 4 unità totali (1 dalla fila Organico,Tech + 3 dalla fila Ads,Tech)
- Lampada: 3 unità totali (2 dalla fila Ads,Casa + 1 dalla fila Organico,Casa)
- Tazza: 4 unità totali (4 dalla fila Email,Casa)
- Tastiera: 1 unita

**Top prodotto**: Mouse con 4 unità vendite.

### AOV (Average Order Value) per 8 ordini
Tre modi possibili:
1. Se ogni riga è un'ordine separato:
   - Revenue totale = 390 (60+25+75+40+30+50+50+80)
   - Numero di ordini = 8
   - AOV = 390 / 8 = **48.75**

2. Se gli ordini sono raggruppati per prodotto/canale:
   (less clear without more order context)

Utilizzeremo il caso semplice: AOV = 48.75

### Quota Ads
- Numero di righe con canale "Ads" = 3
- Totale righe = 8
- Quota Ads = (3 / 8) × 100% = **37.5%**

## Riepilogo finale
- Revenue totale: 390
- Uniti venduti totali: Σ(unita) = 2+1+3+4+1+5+2+1 = 19 unità
- AOV (8 ordini): 48.75
- Quota Ads: 37.5%
- Top prodotto: Mouse (4 unità vendite)