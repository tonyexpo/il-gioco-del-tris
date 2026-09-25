# Analisi dati vendite (8 ordini)

## Dati
| # | Categoria | Canale | Prodotto | Qty | Unità | Fatturato |
|---|-----------|--------|----------|-----|-------|----------|
| 1 | Ads | Casa | Lampada | 2 | €30 | 60 |
| 2 | Organico | Tech | Mouse | 1 | €25 | 25 |
| 3 | Ads | Tech | Mouse | 3 | €25 | 75 |
| 4 | Email | Casa | Tazza | 4 | €10 | 40 |
| 5 | Organico | Casa | Lampada | 1 | €30 | 30 |
| 6 | Ads | Casa | Tazza | 5 | €10 | 50 |
| 7 | Email | Tech | Mouse | 2 | €25 | 50 |
| 8 | Organico | Tech | Tastiera | 1 | €80 | 80 |

## Risultati

### Fatturato unità (per ordine)
- Lampada: 60 + 30 = **90**
- Mouse: 25 + 75 + 50 = **150** ← top prodotto per ordine
- Tazza: 40 + 50 = **90**
- Tastiera: **80**

### Fatturato canali
- Casa: 60 + 40 + 30 + 50 = **180**
- Tech: 25 + 75 + 50 + 80 = **230**
- Email: **0** (nessun ordine)

### Fatturato categorie
- Ads: 60 + 75 + 50 = **185**
- Organico: 25 + 30 + 80 = **135**
- Email: 40 + 50 = **90**

### Top prodotto
**Mouse** → €150 (3 ordini)

### AOV per 8 ordini
Total fatturato = 60+25+75+40+30+50+50+80 = **410**
AOV = 410 / 8 = **€51.25**

### Ads% fatturato
Fatturazione Ads = €185
Ad % = 185 / 410 × 100 = **45,12%**