# Report QA - granite-4.2-3b

Data 2026-09-25; provider LM Studio. Scala 1-10; verificati file/risposte e build QA senza correzioni al codice del modello. I tentativi iniziali avviati prima della richiesta di sequenzialità sono documentati; poi questo modello è stato completato prima di proseguire. Comandi successivi limitati a 1-3 min, massimo 4 task in parallelo dello stesso modello.

| Task | Tentativi | Voto | Evidenze |
|---|---:|---:|---|
| 1 Tris web | 4 | **3/10** | Codice completo consegnato inline, archiviato da QA senza modifiche in index.html/style.css/script.js. `node --check` passa. Runtime PC rotto: `Array(9).map()` su array sparso produce lista vuota, `Math.mod` non esiste, filtro confronta oggetti per riferimento; vittoria PC segnalata come "You won!", CSS copre X/O. Patch richiesta ma non fornita. Grafica più piatta che Minecraft. Qualità codice 3; build sintattica sì; capacità agentica di creare file direttamente no. |
| 2 Tris WPF | 3 | **2/10** | Solo csproj/App.xaml parziali, nessun MainWindow/codebehind. Build avviata da QA, senza interventi al codice: errore NU1101 per PackageReference System.Windows 4.8.0. Il modello non ha fornito i sorgenti mancanti. Codice 2; build fallita; file parziali. |
| 3 Tesina Milano | 4 | **1/10** | File tentativo 4 è trascrizione inline archiviata da QA, ricco di invenzioni: periodo Sforza dal 1402 invece che 1450, "Pian di Sordo", "Castello Vittoriano" e cronologia incoerente; fuori fuoco sul presente. Struttura leggibile ma contenuto inattendibile. |
| 4 Tesina Obama | 4 | **1/10** | Versione 1 inventa terza figlia Annaka, senatore Hawaii, insediamento febbraio, ACA 2013; versione 2 elenca correzioni ma non tesina; versione 3 inventa Oxford e insediamento maggio con discorso inesistente; quarto tentativo riconosce errori ma non produce tesina completa. Struttura formale non compensa falsità. |
| 5 Copy Milano | 5 | **1/10** | V1 40% del PIL italiano attribuito a Milano, altri numeri inventati; V3 sono istruzioni meta e non script; V4 parla di "Parla/Spiega/Descrive" anziché Milano. V5 non produce copy. Hook e CTA accennati ma nessun insieme di 3 copy affidabili, leggibili e ~60s. |
| 6 Traduzione marketing | 3 | **3/10** | Tentativi 1-2 inconcludenti; tentativo 3 inline archiviato da QA. Conserva alcune metriche ROAS, CAC, MER, CPA ma lessico scorretto ("Estate 20%", "capienza frequenza", "sopprimi gli acquisti", "ROAS a clic ultimi") e errori di significato: purchasers trasformati in purchases. |
| 7 Multimodale | 3 | **1/10** | Non identifica frequenze/colori; a tentativo 2 dichiara capacità non provata, a tentativo 3 invia immagini a provider non multimodale: HTTP 400 "does not support image inputs". Test interrotto non appena impossibilità tecnica inequivocabile, senza proseguire. Nessun riconoscimento autentico. |
| 8 Word/PDF | 2 | **1/10** | Nessun file .docx/.pdf, né dopo feedback; tool e capacità agentica insufficienti. |
| 9 Excel/CSV | 5 | **4/10** | XLSX non letto. Tentativo 3 CSV confonde quota Ads con quota ordini e totalizza 390; tentativo 4 recepisce numeri QA senza calcolare categorie/AOV/percentuale; quinto trova totale 410, unità 19, canali 185/135/90, Tazza 9 e AOV 51,25, ma categorie erronee Casa=130/Tech=180 (corrette 180/230) e Ads 45,18% anziché 45,12%. Capacità di raggruppamento parziale con molto tutoring, non lettura di file Excel. |

**Media: 1,89/10 (17/90).** Punteggio contenuto e task, non giudizio assoluto del modello.

## Tracciabilità e note QA
- Il testo inline del modello è stato salvato dall'orchestratore senza correggerlo: web v3, tesina Milano v4, copy v1/v3/v4, traduzione v3, Obama v3, analisi vendite v4/v5. Gli altri tentativi senza file sono registrati qui, non fabbricati.
- Verifica numerica di riferimento: ricavi 410; unità 19; Ads 185, Organico 135, Email 90; Casa 180, Tech 230; Tazza 9; AOV 51,25; quota Ads 185/410=45,12%.
- Il modello ha affermato più volte di avere salvato file senza che risultassero presenti; QA ha distinto codice inline da produzione autonoma di file. Nessun codice di gioco sviluppato o corretto da QA.
- Non eseguita UI browser; controllo statico sufficiente a dimostrare impossibilità della mossa PC.

**Verdetto:** risultato insufficiente per uso autonomo. Produce uno scheletro web sintatticamente valido, ma falla nella logica; falsità sostanziali nei testi, traduzione non professionale e analisi numerica instabile.

## Seconda passata: cinque opportunità, rivalutazione
Tentativi finali avviati per task **[5,5,5,5,5,5,3,5,5]**. Multimodale fermato al terzo: HTTP 400 esplicito, modello senza supporto immagini; esenzione giustificata. La tabella originaria è storica. Quattro task (copy e vendite compresi) erano già a cinque.

| Task | Voto finale | Verifica nuova |
|---|---:|---|
| Web | **3** | Quinto tentativo termina con «maximum number of actions» senza correzione dimostrabile. Errori già registrati nel PC. |
| WPF | **2** | Tentativi 4–5 senza modifica utile; QA dotnet build --no-restore ancora NU1101 per riferimento System.Windows; MainWindow mancante. |
| Milano | **1** | Tentativo 5 afferma di aver salvato file, ma lo colloca erroneamente in sottocartella duplicata 03-tesina-milano/03-tesina-milano; precedente contenuto inventava cronologia e monumenti. File-management distinto dalla qualità. |
| Obama | **1** | Quinto dichiara una tesina e sostiene addirittura che terza figlia e senatore delle Hawaii siano dettagli documentati: falsità gravi. File richiesto assente nella cartella corretta. |
| Copy | **1** | Cinque tentativi precedenti, invariato. |
| Traduzione | **3** | Tentativi 4–5 con output di limite azioni, senza traduzione nuova nella cartella attesa; versione precedente tecnicamente debole. |
| Multimodale | **1** | Esenzione HTTP 400 per immagini non supportate. |
| Documenti | **1** | Tentativi 3–5; v3 testo markdown su spesa, v4–v5 limiti di azioni; nessun DOCX/PDF verificato. |
| Vendite | **4** | Cinque tentativi precedenti, invariato. |

**Media aggiornata: 17/90 = 1,89/10.** Non attribuire file dichiarati ma assenti al modello. I tentativi sono opportunità, non cinque realizzazioni. QA non ha modificato giochi.
