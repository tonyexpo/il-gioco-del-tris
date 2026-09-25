# Report QA - gemma-4-e2b-it@q4_k_m

Data: 2026-09-25. Provider LM Studio. Valutati file reali, non sole dichiarazioni del modello. Copy riferiti a Milano. Scala 1-10. Massimo 5 tentativi consentiti per task (non necessariamente esauriti); multimodale interrotto alla prima impossibilità.

| Task | Tentativi | Voto | Esito verificato |
|---|---:|---:|---|
| 1 Tris web | 4 | **2/10** | HTML non importa script.js e non contiene celle; board JS ha solo 3 elementi e test pareggio errato. Tentativo 4 dichiara correzione non applicata; tentativo-1.js vuoto. Non giocabile. |
| 2 Tris WPF net10 | 3 | **2/10** | App.xaml è directory, non file; dotnet build --no-restore fallisce BG1002/BG1003. UpdateStatus ricorsivo infinito, algoritmo vittoria errato, PC assente. |
| 3 Tesina Milano | 1 | **6/10** | Testo organizzato, ragionevole ma generico, senza fonti, dati o molti riferimenti storici specifici. Struttura corretta. |
| 4 Tesina Obama | 2 | **2/10** | Primo file inventa carriera musicale R&B di Obama, errore storico grave. Secondo file corregge l'affermazione, ma è nota brevissima, non tesina autonoma. ACA citato correttamente. Priorità al contenuto sulla struttura. |
| 5 Copy Milano | 2 | **3/10** | Primo file inglese e con placeholder; secondo italiano senza placeholder, ma 3 varianti ripetitive di ~40-50 parole, circa 20-30 secondi e non 60, hook e CTA generici. Debole retention. |
| 6 Traduzione marketing | 2 | **6/10** | Primo tentativo non accede al prompt; secondo traduce testo identico inline con concetti tecnici generalmente fedeli. Calchi: "social pubblicitari ampi", "hook netti nuovi", "sopprimere gli acquirenti", "stime dei punti del dashboard". Preferibili "paid social broad", "angoli creativi inediti", "escludere acquirenti recenti", "stime puntuali". |
| 7 Multimodale | 1 | **1/10** | Dichiara impossibilità di ascoltare/vedere; stop corretto, nessun suono/colore identificato. |
| 8 Word + PDF | 1 | **1/10** | Solo file markdown con checklist; nessun DOCX né PDF autentico. |
| 9 Analisi vendite | 2 | **1/10** | XLSX non letto; fallback CSV inline restituisce report in francese con numeri sbagliati: 235 ricavi, 18 unità, AOV 13,06, Ads 43,48%. |

**Media: 2,67/10** (24 punti su 90). Valutazione descrittiva, non certificazione.

## Controlli numerici indipendenti sul dataset comune
Fatturato 410; unità 19; canali Ads 185, Organico 135, Email 90; categorie Casa 180, Tech 230; top unità Tazza 9; AOV 51,25 su 8 ordini; Ads 45,12%. Il report del modello è incompatibile persino con le righe che riporta.

## Tentativi e limiti
- Milano 1; Obama 1-2; copy 1-2; traduzione 2 (tentativo 1 non riuscito senza file); multimodale 1; documenti 1; vendite 2 (tentativo 1 impossibilità XLSX senza file). Tentativi falliti senza file documentati qui, non ricostruiti fittiziamente.
- Tris web: tentativi 2 e 3 impossibilità dichiarata di leggere file; tentativo 4 correzione dichiarata ma non presente. WPF: tentativo 2 parziale, tentativo 3 dichiara impossibilità di correggere. Build realmente eseguita e fallita.
- Test browser non effettuato: HTML già privo del collegamento allo script e di celle; non si dichiara prova interattiva.
- Input comuni in ../artefatti-comuni: WAV 2 s con toni 220,330,440,550,660 Hz; 5 PNG 16×16 rosso/verde/blu/giallo/magenta; XLSX, CSV, prompt tecnico marketing. Orchestratore non ha corretto i giochi.

**Verdetto:** disponibile ma inaffidabile come agente autonomo: spesso dichiara modifiche non verificate. Necessaria revisione umana rigorosa. Report comparativo rinviato alla conclusione dei modelli successivi.

## Rivalutazione: cinque opportunità (seconda passata)
Conteggi finali tentativi avviati: **[5,5,5,5,5,5,1,5,5]**. Multimodale esentato per dichiarata indisponibilità. Questa appendice prevale sulla tabella storica precedente; tentativi privi di artefatti sono fallimenti, non file inventati.

| Task | Voto finale | Riscontri aggiuntivi |
|---|---:|---|
| Web | **1** | Il quinto tentativo ha sovrascritto script.js con prosa Markdown; node --check restituisce SyntaxError alla prima riga. HTML ora importa quel file invalido. La dichiarazione di correzione è falsa. |
| WPF | **2** | Tentativi 4–5 non riparano App.xaml, ancora directory; QA dotnet build --no-restore: BG1002/BG1003. |
| Milano | **5** | v2–v5 archiviate; v4 è solo 102 byte, v5 fa risalire erroneamente le origini di Milano al Medioevo, ignorando Mediolanum; testo generico. |
| Obama | **2** | v3–v5 archiviate; v4 è una traccia con placeholder e v5 42 byte. Nessuna tesina corretta sostituisce la falsa biografia iniziale. |
| Shorts | **3** | v3–v5: tre testi con CTA, ma v5 troppo brevi per ~60 s e dichiara senza fondamento Milano «capitale indiscussa della gastronomia italiana». |
| Traduzione | **5** | v3 e v5 chiedono testo già disponibile; v4 traduce quasi tutto, ma usa calchi, interpreta holdout come «mercati di riferimento» e incorpora «Limite 120 secondi» nel testo. v2 migliore. |
| Multimodale | **1** | Interrotto legittimamente al primo tentativo. |
| Word/PDF | **1** | Tentativi 2–5 senza DOCX/PDF; presenti soltanto due TXT di 61 byte. Il quinto chiede dati non necessari per il tema libero. |
| Vendite | **1** | Tentativi 3–5 senza analisi affidabile; il quarto è stato interrotto dopo ~5 minuti per errore dell'orchestratore, oltre il limite richiesto 1–3 minuti; quinto termina con limite di azioni. |

**Media aggiornata: 21/90 = 2,33/10.** Il superamento del timeout è un errore di supervisione, documentato separatamente. Il QA non ha corretto il codice del modello. I conteggi originari nella tabella sopra sono storici e non rappresentano lo stato finale.
