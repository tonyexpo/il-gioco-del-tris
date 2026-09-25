# Report QA - minicpm5-2b

Data 2026-09-25, provider LM Studio. Scala 1-10. Solo artefatti reali e risposte inline; QA ha eseguito le build senza correggere codice. Sessioni tutte sotto 3 minuti, max quattro simultanee sullo stesso modello. "Maximum number of actions" non equivale a esito positivo.

| Task | Tentativi | Voto | Evidenze |
|---|---:|---:|---|
| 1 Tris web | 4 | **2/10** | index.html/style.css/script.js reali, `node --check` passa, ma gioco non parte: HTML board vuota, NodeList iniziale `.square` vuota, `renderBoard()` non crea celle; `board` 3×3 ma indicizzato come 9 righe; reset riassegna `const board`, `NodeList.filter` inesistente, mossa PC impraticabile. QA ha segnalato difetti, modello non li ha corretti. Codice presente/sintassi OK, runtime fallito. |
| 2 Tris WPF | 3 | **2/10** | csproj, App.xaml, MainWindow.xaml e MainWindow.cs presenti. `dotnet build` avviato da QA fallisce NETSDK1136: UseWPF=true con TargetFramework net10.0 anziché net10.0-windows. Dopo feedback csproj invariato; codice parziale non costituisce app verificata. |
| 3 Tesina Milano | 4 | **1/10** | tesina-milano-1.md contiene 1870 come nascita Repubblica Italiana, Milano capitale nazionale, museo delle Marche e riferimenti urbani inventati. Revisioni non concluse. Struttura apparente presente, contenuto storicamente inattendibile. |
| 4 Tesina Obama | 3 | **1/10** | file 04-tesina-obama.md nella root modello anziché task: nascita attribuita a Chicago 8 giugno 1961, padre israeliano e madre cubana, insediamento giugno 2009 e pandemia durante mandato: falsità gravi. Feedback e revisioni non hanno prodotto testo corretto. |
| 5 Copy Milano | 5 | **2/10** | shorts_italiani.txt (nome non conforme .md) contiene 2 testi lunghi e terzo solo hook/CTA. Inventa "San Giovanni a Due Torri", "giardino Cascate di Brera", colline milanesi; hook ripetuti, lingua debole. Diagnostico copy-milano-3.md è uno solo e corto. Nessuno dei 5 tentativi consegna 3 copy affidabili da 60s. |
| 6 Traduzione marketing | 3 | **1/10** | Nessuna traduzione integrale del prompt tecnico, nemmeno dopo prova diagnostica ridotta; solo stalli max actions. Niente giudizio linguistico possibile. |
| 7 Multimodale | 2 | **1/10** | Nessun audio o immagine realmente analizzati, né frequenze/colori. Primo tentativo non ammette impossibilità ma va in stallo; secondo chiarimento identico. Interrotto senza ulteriore azione. |
| 8 DOCX/PDF | 2 | **1/10** | Nessun Word/PDF genuino, soltanto stalli e nessun output utile. |
| 9 Excel/CSV | 4 | **4/10** | Nessuna lettura XLSX verificata; fallback CSV inline calcola correttamente totale 410, AOV 51,25, quota Ads 45,12% e subtotali, ma inverte intestazioni categoria/canale, sostiene Email 0, seleziona Mouse per ricavi invece di Tazza per unità, omette unità totali 19. Dopo feedback risultato non corretto. |

**Media: 1,67/10 (15/90).** Produzione di file sorgente autonoma migliore di alcuni modelli, ma validità funzionale e fattuale insufficiente.

## Tracciamento QA
- Artefatti web/WPF, tesine e shorts creati dal modello; risposte inline diagnostiche copy e vendite salvate dall'orchestratore *verbatim* (non sono modifiche al contenuto). Versioni fallite senza file annotate qui; nessun codice gioco scritto o corretto da QA.
- Build realmente lanciata da QA: JS sintassi OK, WPF NETSDK1136. Non è stata simulata esecuzione UI.
- Valori dataset: ricavi 410; unità 19; canali Ads 185, Organico 135, Email 90; categorie Casa 180, Tech 230; Tazza 9; AOV 51,25; Ads 45,12%.
- L'assenza di ammissione di impossibilità nel multimodale è criticità di trasparenza: il test non ha fornito dati sufficienti a giudicare capacità nativa.

**Verdetto:** capace di creare file e scheletri di codice, non ancora affidabile per gioco funzionante, accuratezza storica o documenti quotidiani.

## Seconda passata: cinque opportunità
Conteggi finali **[5,5,5,5,5,5,3,5,5]**. Il multimodale v3 termina con limite azioni senza dichiarazione esplicita; stop operativo per input media non verificabilmente disponibile, non per successiva percezione. Il copy era già a cinque. Tutte le nuove deleghe non hanno prodotto versioni finali verificabili: ritorno ripetuto «maximum number of actions». Non attribuire al modello i nomi di file suggeriti nel prompt. QA ha ricontrollato node --check sul JS esistente (sola sintassi) e dotnet build WPF: **NETSDK1136** persiste perché il modello non ha corretto net10.0 in net10.0-windows. Nessun DOCX/PDF nei documenti; nessun miglioramento dimostrato nelle tesine o nei conteggi delle vendite.

**Voti invariati [2,2,1,1,2,1,1,1,4], media 15/90 = 1,67/10.** I conteggi storici soprastanti non sono quelli della seconda passata; mancata consegna e qualità vanno giudicate separatamente.
