# Report QA - lfm2.5-2.6b

Data 2026-09-25; LM Studio. Valutazione su artefatti verificati, testo inline archiviato senza interventi. Molte richieste hanno prodotto errore provider 500 "output does not match expected peg-native format": impossibile attribuire con certezza al solo modello (integrazione agente/provider). Timeout richiesto 1-3 min non superato nelle sessioni di questo modello.

| Task | Tentativi | Voto | Evidenze |
|---|---:|---:|---|
| 1 Tris web | 4 | **1/10** | Nessun codice HTML/CSS/JS utilizzabile né file; più errori provider 500 peg-native, tentativo diretto inconcludente. Nessuna build possibile. |
| 2 Tris WPF net10 | 2 | **1/10** | Nessun file/codebehind né codice completo inline; nessun progetto da compilare. QA non ha potuto eseguire build sul codice inesistente. |
| 3 Tesina Milano | 4 | **2/10** | tesina-milano-1.md contiene falsità importanti: fabbrica Tesla in "Zona Frigida", falso quartiere Termo, Museo Reale della Scultura, Milano in Emilia-Romagna, Santa Maria delle Grazie definita cattedrale. Revisioni non consegnate. Forma ordinata ma contenuto inattendibile. |
| 4 Tesina Obama | 4 | **1/10** | Tutti i tentativi senza tesina: ripetuti errori protocollo 500; nessun contenuto giudicabile. Non si inferisce incompetenza storica dai soli errori provider. |
| 5 Copy Milano | 2 | **3/10** | V1 tre testi abbastanza lunghi con CTA, ma "998 coppelle", 8 milioni turisti, Ponte Leonardo, bacari triestini fra i Navigli: invenzioni. V2 elimina alcune cifre, resta generico e ripete bacari, hook poco incisivi, CTA generiche, durata ~45-60s. Risposte inline archiviate da QA; asserzione di file separati in V1 non verificata. |
| 6 Traduzione marketing | 2 | **5/10** | Primo tentativo inline archiviato. Significato tecnico in parte preservato (ROAS incrementale, CAC, LTV:CAC, MER), ma "social payment ampio", "CAC a prima ordine", "sopprimere acquirenti recenti", calchi e registro non professionale. Secondo fallisce provider 500. |
| 7 Multimodale | 2 | **1/10** | Nessun colore/frequenza identificati. Primo e secondo rispondono "massimo numero azioni" senza chiara ammissione di impossibilità; interrotto senza ulteriori prove poiché nessuna analisi. |
| 8 Word/PDF | 2 | **1/10** | Entrambi errori provider 500, nessun PDF o DOCX. Test di produzione file fallito. |
| 9 Excel/CSV | 4 | **2/10** | Non dimostrata lettura XLSX; fallback CSV inconcludente, terzo errore provider 500. Quarto fornisce numeri inline 430,19,185,135,90,180,230: categorie/canali/unità corretti ma fatturato totale dovrebbe essere 410, non 430, e omette top prodotto, AOV, Ads%. Non confondere risposta incompleta con analisi corretta. |

**Media: 1,89/10 (17/90).** Punteggi riferiti all'intera catena modello + integrazione locale; i fallimenti 500 vanno distinti dalle falsità contenutistiche osservate.

## Evidenze operative
- File verificati: tesina-milano-1.md (modello); copy-milano-1/2.md, traduzione-marketing-1.md, analisi-vendite-4.md (risposte inline del modello, salvate verbatim da QA); risposta-multimodale-1.md (messaggio di stallo). Non esistono progetti compilabili nei due task di sviluppo; QA non ha scritto alcun codice di gioco.
- Valori dataset veri: fatturato 410, unità 19; Ads 185, Organico 135, Email 90; Casa 180, Tech 230; Tazza 9 unità; AOV 51,25; quota Ads 45,12%.
- Nessun tentativo ha raggiunto 3 minuti; quando il provider non ha restituito materiale non è stato inventato un artefatto.

**Verdetto:** in questa configurazione LFM è instabile per workflow agentici; produce alcuni testi inline ma richiede fact-checking e non consegna codice verificabile né file pratici.

## Seconda passata: opportunità e verifica
Conteggi **[5,5,5,5,5,5,3,5,5]**. Il test multimodale è fermato dopo il terzo tentativo: non c'è un canale verificato per fornire audio/immagini al modello; terza risposta è solo «maximum number of actions», non una dichiarazione esplicita di impossibilità. L'esenzione è pertanto operativa, non attribuibile come ammissione del modello. I ripetuti HTTP 500 peg-native sono errori di integrazione/provider e vanno distinti da errori fattuali. Le chiamate 3–5 di WPF, copy, traduzione, documenti, vendite e le quinte di web, Milano, Obama non hanno prodotto consegne verificabili; alcune terminano 500, altre action-limit. Nessun DOCX/PDF, nessun codice di gioco e nessun miglioramento dimostrato ai testi originali. Sono apparsi file spurii chiamati '-p', non progetti.

**Punteggi finali invariati:** [1,1,2,1,3,5,1,1,2], **17/90 = 1,89/10**. La tabella iniziale registra la prima passata; i conteggi di questa appendice sono quelli finali. Nessuna build possibile in assenza di progetto WPF.
