# Report QA - mistralai/ministral-3-3b

Data 2026-09-25; nome completo modello nel titolo, cartella abbreviata ministral-3-3b. Provider LM Studio. Scala 1-10. Primo tentativo web e Milano avviato prima della precisazione sul timeout: rimasto 5 minuti e poi annullato; le sessioni successive entro 1-3 minuti salvo ultimo probe numerico senza contenuto, registrato fallito. Max 4 task dello stesso modello simultanei. File inline salvati verbatim dall'orchestratore, nessun codice di gioco scritto/corretto da QA.

| Task | Tentativi | Voto | Evidenze |
|---|---:|---:|---|
| 1 Tris web | 3 | **1/10** | Primo tentativo interrotto per stallo >3 minuti, ulteriori due nessun codice/file. Compilazione QA impossibile senza sorgenti. |
| 2 Tris WPF | 2 | **1/10** | Nessun csproj/XAML/C# prodotto anche dopo richiesta di solo codice; niente da compilare. |
| 3 Tesina Milano | 3 | **3/10** | Tesina inline archiviata in tesina-milano-3.md: riferimenti pertinenti Visconti/Sforza, Duomo, Navigli, affitti/smog. Ma testo molto corto (~200 parole dichiarate, meno nella realtà), non racconta Mediolanum; attribuisce erroneamente ai Visconti fondazione ducato, smog fabbriche Navigli e mercato Brera storicizzati senza fonti. Struttura sintetica; contenuto superficiale. |
| 4 Tesina Obama | 3 | **2/10** | Testo lungo in tesina-obama-2.md con ACA 2010 e alcuni temi corretti, ma inventa Yale dottorato 1991 (Harvard Law), padre "Annan", primo senatore afroamericano, accordo Iran "firmato a Parigi" (confonde con accordo clima). Revisione non consegnata. Contenuto erroneo pesa più della forma. |
| 5 Copy YouTube Milano | 4 | **1/10** | Tre script in copy-milano-2.md solo ~35-45 parole, non ~60s; claims falsi "Duomo più grande cimitero della cristianità" e "Brera quartiere più antico", frasi [mute] incomplete, CTA generiche. Feedback non ha prodotto revisioni. Hook potenzialmente forti ma falsi non accettabili. |
| 6 Traduzione marketing | 3 | **4/10** | Prima non consegnata; seconda è analisi/riscrittura con aggiunte assenti dal testo (LTV:CAC >3x, churn), MER erroneamente espanso "Monetization Efficiency Rate". Terza cerca fedeltà, corregge MER ma inserisce MER nella metrica della coorte e produce calchi "reallocando", "intervalli di fiducia"; perde first-order CAC distinto. Qualità insufficiente per testo marketing senior. |
| 7 Multimodale | 2 | **1/10** | Primo stallo senza risultato; al chiarimento secondo dichiara impossibilità di accesso nativo media. Arresto immediato all'ammissione, nessun RGB/frequenza realmente identificato. |
| 8 DOCX/PDF | 2 | **1/10** | Nessuno dei due file esiste, due risposte inconcludenti. |
| 9 Excel/CSV | 5 | **1/10** | Nessuna lettura XLSX; CSV fallback inconcludente. Quarto tentativo produce totale 380 (vero 410), canali Organico 145 (135), Casa 170 (180), Tech 225 (230), AOV 26,25 (51,25), Ads 70,38% (45,12%); solo unità 19/Ads 185/Tazza 9 corretti. Quinto probe senza testo valido. |

**Media: 1,67/10 (15/90).** I punteggi distinguono risultati osservabili da mere dichiarazioni e stalli.

## Riferimenti QA
- File condivisi ../artefatti-comuni; dati veri ricavi 410, unità 19, canali 185/135/90, categorie 180/230, Tazza 9, AOV 51,25, Ads 45,12%.
- Output inline del modello archiviati da QA come tentativi numerati. I tentativi senza file sono registrati nel report. Nessuna build possibile in assenza di codice, non imputata automaticamente al mero non saper avviare `dotnet`.
- Multimodale fermato al primo esplicito "impossibile".

**Verdetto:** in questa integrazione agentica il modello non riesce a consegnare programmi/file; testi talvolta fluenti ma accuratezza insufficiente, numeri non affidabili.

## Seconda passata: cinque opportunità
Conteggi finali **[5,5,5,5,5,5,2,5,5]**. Multimodale esentato dopo esplicita dichiarazione al tentativo 2. Le nuove opportunità web 4–5, WPF 3–5, Milano 4–5, Obama 4–5, copy 5, traduzione 4–5 e documenti 3–5 non hanno generato file validi nelle cartelle attese: nella quasi totalità il subagente ritorna «maximum number of actions». WPF v3 ha fornito inline soltanto una guida con esempi incompleti («... 9 bottoni», logica di vittoria non implementata), non progetto compilabile; non archiviarlo come gioco completo. Nessun PDF/DOCX. Le precedenti falsità fattuali nelle tesine e nel copy rimangono. Vendite già a cinque.

**Punteggi invariati [1,1,3,2,1,4,1,1,1], 15/90 = 1,67/10.** La tabella precedente fotografa la prima passata: usare i conteggi della presente appendice come definitivi. Nessuna build possibile senza progetto completo.
