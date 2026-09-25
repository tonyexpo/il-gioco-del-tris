# Report finale comparativo - test locali Goose

Data 2026-09-25. Ordine richiesto: `gemma-4-e2b-it@q4_k_m`, `granite-4.2-3b`, `lfm2.5-2.6b`, `minicpm5-2b`, `mistralai/ministral-3-3b`, `qwen3.5-4b`. I report analitici sono nelle rispettive root come `REPORT-QA.md`; gli input comuni sono in `artefatti-comuni/`. I copy sono riferiti a **Milano** (la dicitura originaria "tesina 4 (Milano)" era internamente contraddittoria: Milano è task 3). I voti sono sul risultato osservato, inclusi limiti d'integrazione LM Studio/Goose, non una classifica universale dei pesi.

| Modello completo | Web | WPF | Milano | Obama | Shorts | Traduzione | Multimodale | DOCX/PDF | XLSX/CSV | Media /10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| gemma-4-e2b-it@q4_k_m | 1 | 2 | 5 | 2 | 3 | 5 | 1 | 1 | 1 | **2,33** |
| granite-4.2-3b | 3 | 2 | 1 | 1 | 1 | 3 | 1 | 1 | 4 | **1,89** |
| lfm2.5-2.6b | 1 | 1 | 2 | 1 | 3 | 5 | 1 | 1 | 2 | **1,89** |
| minicpm5-2b | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 4 | **1,67** |
| mistralai/ministral-3-3b | 1 | 1 | 3 | 2 | 1 | 4 | 1 | 1 | 1 | **1,67** |
| qwen3.5-4b | 5 | 1 | 2 | 2 | 1 | 6 | 1 | 1 | 4 | **2,56** |

## Lettura comparativa

- **Sviluppo web:** Qwen produce lo scheletro più solido (9 celle, minimax, stile a blocchi) ma lascia race condition fra timer/reset/click e un possibile errore dopo vittoria PC. Granite consegna codice inline completo che QA archivia, ma la mossa PC è rotta; MiniCPM produce file ma board/rendering impediscono di giocare; Gemma, nella quinta revisione, importa uno script.js sovrascritto con Markdown: node --check fallisce. Nessun tris web è stato certificato giocabile con test UI interattivo.
- **WPF .NET 10:** Nessun progetto consegnato compila correttamente. Gemma fallisce BG1002/BG1003 (App.xaml directory, codice errato); Granite fallisce NU1101 (pacchetto `System.Windows` inesistente); MiniCPM fallisce NETSDK1136 (target `net10.0` anziché `net10.0-windows`); LFM/Ministral/Qwen non consegnano progetti compilabili. **Le build sono state avviate dall'orchestratore**, sul codice dei modelli senza modifiche. L'assenza di abilità nellanciare build da parte del modello non è stata equiparata all'assenza di codice.
- **Tesine, contenuto prima della struttura:** Milano di Gemma è la più affidabile, sebbene generica. Altri testi inventano date, luoghi o enti. Su Obama nessuna tesina è pronta per l'uso: errori biografici significativi persistono anche dopo feedback. La buona formattazione non compensa fatti falsi.
- **Shorts Milano:** hook e CTA spesso presenti formalmente, ma metriche inventate o attribuzioni storiche false compromettono credibilità e retention. Più modelli presentano copy di 20-40 secondi come se fossero 60; alcuni offrono istruzioni per scriverli, non copioni leggibili. Nessun set di tre copy è raccomandabile per pubblicazione senza revisione fattuale/creativa.
- **Traduzione:** Gemma e Qwen mantengono più concetti tecnici; editing necessario per calchi e scelta lessicale. LFM è mediamente fedele ma poco naturale, Ministral confonde MER (Marketing Efficiency Ratio) e aggiunge conclusioni non presenti; Granite altera sfumature e forma. Testi condivisi identici salvo fallback inline quando lettura file fallisce.
- **Multimodale e file quotidiani:** nessun modello identifica validamente tutti i cinque colori e cinque toni; quando dichiara impossibilità l'esperimento si interrompe. Nessun DOCX e PDF reale prodotto da alcun sub-agente. La semplice risposta testuale non è un file Word/PDF.
- **Vendite:** fallback CSV distingue lettura XLSX da capacità analitica; nessun modello dimostra lettura dell'XLSX. MiniCPM, Qwen e Granite individuano almeno in un tentativo alcuni totali corretti, ma commettono errori sui gruppi, top prodotto o quote. Dati QA: ricavi **410**, unità **19**, Ads **185**, Organico **135**, Email **90**; Casa **180**, Tech **230**; Tazza **9 unità**; AOV **51,25** su 8 ordini; Ads **45,12%** dei ricavi. Queste cifre sono riferimento QA e non sono output attribuibili ai modelli.

## Metodo, timeout e integrità

- Cinque opportunità per ciascun task idoneo e max 4 task simultanei **sullo stesso modello** dopo aggiornamento utente; chiuso il report di un modello prima di passare al successivo. Alcuni task su Granite/LFM/MiniCPM/Ministral/Qwen erano stati avviati prematuramente prima di tale aggiornamento: registrati nei rispettivi report, senza presentarli come sessioni conformi alla nuova sequenza.
- Limite richiesto **1-3 minuti per comando**: le sessioni in corso al momento dell'aggiornamento avevano già superato il limite (Granite/Ministral); un successivo controllo Qwen ha rilevato tardivamente tre sessioni a 5 minuti, annullate e considerate fallite. Un probe sincrono numerico Ministral ha raggiunto il timeout infrastrutturale di 5 minuti senza testo; evidenziato nel report, **non** nascosto come prova riuscita. La gestione timeout non è stata quindi perfettamente rispettata: è una limitazione del processo QA.
- Alcune risposte "raggiunto massimo numero azioni" indicano stallo dell'integrazione agentica, non un giudizio di incapacità pura del modello. LFM presenta ripetuti errori provider 500 `peg-native format`; punteggi si riferiscono all'uso concreto in questa configurazione.
- L'orchestratore ha soltanto creato **input fissi condivisi**, salvato verbatim risposte inline e lanciato controlli `node --check`/`dotnet build`; non ha scritto né corretto il codice dei giochi dei sub-agenti. L'archiviazione di risposte inline non è attribuita alla loro capacità autonoma di creare file.
- Gli input comuni comprendono WAV 2s con toni consecutivi 220/330/440/550/660 Hz, PNG 16×16 rosso/verde/blu/giallo/magenta, prompt marketing, CSV e XLSX vendite. Le voci ZIP e l'XML dell'XLSX sono stati verificati, non è stata attestata apertura con Excel desktop.

**Conclusione:** nessun modello supera i nove task in modo autonomo affidabile. Per codice web e traduzione Qwen/Gemma forniscono basi su cui un umano può intervenire; per tesina Milano Gemma è preferibile. Per software pronto all'uso, storia verificata, documenti Office/PDF e analisi numeriche serve ancora QA esterno e revisione.

## Aggiornamento definitivo dopo la seconda passata obbligatoria
Questo paragrafo prevale sulle descrizioni storiche in contrasto sopra. Sono state completate le seconde passate nell'ordine Gemma, Granite, LFM, MiniCPM, Ministral, Qwen, aggiornando ciascun report prima del modello successivo. Conteggi finali dei tentativi avviati, task 1–9 (l'eccezione riguarda il multimodale):

| Modello | Tentativi finali per task 1–9 | Totale punti /90 | Media |
|---|---|---:|---:|
| Gemma | 5,5,5,5,5,5,1,5,5 | 21 | 2,33 |
| Granite | 5,5,5,5,5,5,3,5,5 | 17 | 1,89 |
| LFM | 5,5,5,5,5,5,3,5,5 | 17 | 1,89 |
| MiniCPM | 5,5,5,5,5,5,3,5,5 | 15 | 1,67 |
| Ministral | 5,5,5,5,5,5,2,5,5 | 15 | 1,67 |
| Qwen | 5,5,5,5,5,5,3,5,5 | 23 | 2,56 |

Gemma peggiora nel web: il JS è Markdown non interpretabile; Milano v5 colloca erroneamente le origini nel Medioevo; traduzione v4 inserisce istruzioni operative nella traduzione. Qwen Milano v5 corregge l'idea di colonia romana appena fondata ma introduce invenzioni ancora più gravi: Cenomani al posto degli Insubri, conquista attribuita a Gaio Mario nel 100 a.C. e un ponte sul Ticino presentato quale monumento della città; voto Milano scende a 2. Le versioni migliori non vengono sostituite automaticamente da revisioni peggiori. Granite dichiara un nuovo file Milano in una cartella duplicata, non nella posizione richiesta. Molte opportunità ulteriori di LFM/MiniCPM/Ministral/Qwen terminano con errore provider o limite di azioni, senza artefatto: sono fallimenti, non output tacitamente accettati.

Eccezioni multimodali: Gemma e Ministral dichiarano impossibilità, Granite riceve HTTP 400 per immagini non supportate, Qwen dichiara impossibilità al terzo tentativo (la sua dichiarazione di file salvato non è confermata). Per LFM e MiniCPM la terza sessione non contiene una dichiarazione esplicita, ma il canale di accesso/percezione media non è verificabilmente disponibile: l'esenzione è un limite operativo di questa configurazione, **non** prova che i modelli abbiano riconosciuto autonomamente l'incapacità. Non si accreditano colori desunti dai nomi. Per il task vendite il fallback CSV resta valido anche se XLSX non leggibile; nessun nuovo modello ha dimostrato lettura XLSX. Nessun subagente ha prodotto la coppia DOCX/PDF reale; build WPF ripetute da QA: Gemma BG1002/BG1003, Granite NU1101, MiniCPM NETSDK1136, senza correzioni del QA.

**Conformità dei tempi imperfetta:** nella seconda passata il quarto tentativo Gemma vendite è rimasto aperto circa cinque minuti prima dell'annullamento, per un errore di supervisione, e va contato fallito; si aggiunge alle violazioni precedenti già documentate. I punteggi misurano il sistema modello+provider+strumenti in questo ambiente, non la sola capacità linguistica del modello. «Cinque tentativi» significa cinque opportunità avviate, non cinque documenti riusciti: nelle relazioni singole sono documentate le mancate consegne. Il protocollo comune è stato aggiornato con questa regola.
