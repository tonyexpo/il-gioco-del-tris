# Prompt della prova

Testo integrale del messaggio assegnato al subagente, senza modifiche retroattive. La traccia e la griglia saranno riutilizzate per i modelli successivi.

## Messaggio inviato

```text
Sei uno studente universitario che sostiene una prova individuale multidisciplinare. Scrivi in italiano una tesina dal titolo «Milano da Mediolanum alla metropoli industriale: continuità e trasformazioni». Lunghezza richiesta: 1200–1600 parole. Copri obbligatoriamente: 1) origini preromane, romanizzazione, ruolo imperiale e cristianesimo tardoantico; 2) passaggio dal comune alle signorie e storia moderna, con dominazioni straniere, riforme settecentesche e fase napoleonica; 3) Ottocento e Novecento economico-industriali: infrastrutture, credito, settori e imprese, lavoro e migrazioni, trasformazioni postindustriali. Distingui fatti, interpretazioni e incertezze. Collega i mutamenti politici allo sviluppo economico senza determinismi. Concludi con una sintesi critica e una bibliografia di 4–6 riferimenti identificabili; non inventare fonti o dati. Sarai valutato su accuratezza storica (4 punti), copertura ed equilibrio cronologico (2), analisi economica e collegamenti (2), chiarezza (1), fonti e loro uso (1). Non usare strumenti, non cercare sul web, non creare file e non delegare: la prova valuta le tue conoscenze autonome. Restituisci soltanto la tesina completa in Markdown, senza preamboli. Il docente salverà il tuo testo originale e lo correggerà separatamente.
```

## Registro di esecuzione

- Modello richiesto e selezionato: `lmstudio/spark-x2.5-1.7b`.
- Provider: LM Studio.
- Tipo di subagente: `general`.
- Sessione restituita: `ses_e8d93ea4cffeYTTMz131pOWJle`.
- Modalità: singola esecuzione in primo piano; nessun altro subagente avviato contemporaneamente, nessun secondo tentativo richiesto.
- Output: `milano-da-mediolanum-alla-metropoli-industriale-spark-x2.5-1.7b.md`, inclusi preambolo e nota finale prodotti dal modello.
- Il testo sopra è il messaggio della prova, non un'esportazione delle istruzioni di sistema del subagente. Parametri di campionamento e configurazione del server LM Studio non sono stati impostati né rilevati per questa prova.
- La correzione è svolta dall'assistente principale dopo la consegna, con consultazione di fonti esterne; tali fonti non sono state fornite al candidato.

## Registro di esecuzione — Emma-6

- Modello richiesto e selezionato: `lmstudio/emma-6`.
- Provider: LM Studio; tipo di subagente: `general`.
- Messaggio inviato: identico al testo integrale riportato sopra in entrambi i tentativi.
- Esecuzione in serie, dopo il completamento della prova Spark.
- Primo tentativo: sessione `ses_e8d896669ffeNlcIQ6cQGWfYZR`.
- Secondo tentativo, in una nuova sessione: `ses_e8d8932e7ffe4lrtMGxa5cKmdU`.
- Entrambi i tentativi hanno restituito l'errore dello strumento: `The compaction request cannot be reduced further without losing the latest exchange or checkpoint`.
- Nessun testo di tesina restituito al docente. Non è possibile stabilire da questo errore se il modello abbia prodotto contenuto non restituito dallo strumento.
- Esito: prova bloccata da errore tecnico; nessun voto assegnato e nessuna tesina o review accademica creata. Non è un giudizio sulle capacità del modello.
- Parametri di campionamento e configurazione del server LM Studio non modificati.
- Informazione successiva dell'utente: Emma-6 è limitato a 4K token. Questo vincolo è compatibile con l'errore di gestione del contesto osservato, ma non è stato verificato tramite configurazione o log. Nel budget devono rientrare istruzioni di sistema, prompt, eventuali definizioni degli strumenti e risposta; la traccia originale da 1200–1600 parole lascia quindi poco spazio all'infrastruttura del subagente.

### Test diagnostico con domanda minima

- Su richiesta dell'utente, nuova sessione `ses_e8d882293ffeinilqICcJySCAa`, stesso modello e tipo di subagente.
- Prompt esatto: `Perché Milano è importante? Rispondi brevemente.`
- Esito: stesso errore, `The compaction request cannot be reduced further without losing the latest exchange or checkpoint`.
- Nessuna risposta restituita. Accorciare il solo messaggio della prova non risolve il blocco; resta da verificare il peso delle istruzioni e degli strumenti del subagente e la configurazione del contesto. Test diagnostico escluso dalla valutazione accademica.

## Prova manuale esterna — Emma-6

Per aggirare il blocco, è stato fornito all'utente questo prompt ridotto da usare in una chat pulita:

```text
Scrivi una breve tesina in italiano su «Milano da Mediolanum alla metropoli industriale», di circa 600–800 parole.

Copri:
1. Origini preromane, romanizzazione, ruolo imperiale e cristianesimo tardoantico.
2. Comune, Visconti e Sforza, dominazioni straniere, riforme settecentesche e fase napoleonica.
3. Sviluppo economico-industriale nell’Ottocento e Novecento: infrastrutture, banche, imprese, lavoro, migrazioni e trasformazioni postindustriali.

Collega storia politica ed economica con esempi concreti. Distingui fatti accertati e incertezze; non inventare date, eventi o fonti. Concludi con una sintesi critica e 4 riferimenti bibliografici identificabili, solo se li conosci con sicurezza.

Restituisci soltanto la tesina in Markdown.
```

L'utente ha successivamente riportato tre risposte, conservate in `milano-da-mediolanum-alla-metropoli-industriale-emma-6.md`. Il messaggio iniziale effettivamente incollato nella chat esterna non è stato confermato integralmente. Le due richieste successive riportate sono, nell'ordine:

1. `no, tu devi scrivermi una tesina su milano`
2. `scrivimi una tesina su milano`

La review valuta i contenuti riportati e il rispetto delle richieste esplicite. Si mantengono le cinque categorie e i pesi della griglia originale come criterio del docente; tali pesi non erano inclusi nel prompt ridotto. La prova esterna, multi-turno e con lunghezza richiesta diversa, non costituisce un confronto controllato con l'esecuzione Spark. Configurazione, istruzioni di sistema, campionamento e conteggi dei token della chat esterna non sono stati verificati.

## Registro di esecuzione — MiniCPM5-2B

- Modello selezionato: `lmstudio/minicpm5-2b`; provider LM Studio; subagente `general`.
- Sessione: `ses_e8d827e7bffeyqj9S8QIDpyV46`.
- Prompt: messaggio originale integrale da 1200–1600 parole riportato all'inizio di questo file, identico a quello di Spark.
- Una singola esecuzione in primo piano, in serie. LFM2.5 non avviato: l'utente ha corretto la scelta prima dell'esecuzione.
- Risposta finale conservata in `milano-da-mediolanum-alla-metropoli-industriale-minicpm5-2b.md`, inclusi preambolo inglese e residui di marcatori finali.
- Dopo l'esecuzione è comparso anche `Milan_da_Mediolanum_alla_metropoli_industriale.md`, che il subagente dichiara di aver salvato nonostante il divieto nel prompt. Il file è conservato come artefatto distinto: differisce dalla risposta finale per separatori, un refuso, un inciso sulla presunta battaglia del 1866 e il secondo riferimento bibliografico. La review valuta la risposta finale, non combina le due versioni.
- Parametri di campionamento e configurazione LM Studio non impostati né rilevati. Verifica delle fonti svolta dal docente dopo la consegna.

## Registro di esecuzione — Gemma 4 12B IT Q4_K_XL

- Modello selezionato: `lmstudio/gemma-4-12b-it@q4_k_xl`; nome restituito dal catalogo: Gemma 4 12B Instruct UD.
- Provider LM Studio; subagente `general`; sessione `ses_e8d76f142ffezjL2eOyr3EeK0E`.
- Prompt: messaggio originale integrale da 1200–1600 parole riportato all'inizio di questo file, identico a Spark e MiniCPM5.
- Una singola esecuzione in primo piano, successiva alle altre prove; nessuna richiesta di revisione.
- Risposta finale conservata in `milano-da-mediolanum-alla-metropoli-industriale-gemma-4-12b-it-q4_k_xl.md`. Nel nome del file `@` è sostituito con `-`.
- Aggiunto come riferimento 12B nella comparativa. Dimensione nominale e variante sono quelle dichiarate dal nome del modello; configurazione e parametri di campionamento non verificati. Non è una prova controllata dell'effetto della sola dimensione.

## Test successivo — Emma-6 BF16, LM Studio classico

Su richiesta dell'utente è stata eseguita una prova breve in italiano. Il subagente continua a restituire l'errore di contesto; una richiesta diretta all'API locale, senza messaggio di sistema né strumenti, ha invece restituito una risposta. I due file diagnostici separati sono stati rimossi nella pulizia finale richiesta dall'utente; i dati sono conservati qui sotto. Test diagnostico separato, senza modifica dei voti precedenti.

### Dati del test diagnostico conservati alla chiusura

- Il precedente identificativo `lmstudio/emma-6` non era più disponibile; il catalogo ha restituito `lmstudio/emma-6@bf16`.
- Un subagente con il messaggio `Descrivi brevemente la storia di Milano. Rispondi solo in italiano, senza usare strumenti.` ha restituito lo stesso errore di compattazione del contesto, sessione `ses_e8d6b98caffezLwgTELfKgFNGZ`.
- Richiesta diretta successiva: `POST http://localhost:1234/v1/chat/completions`, modello `emma-6@bf16`, un solo messaggio `user`: `Descrivi brevemente la storia di Milano. Rispondi solo in italiano.`
- Nessun messaggio `system`, cronologia o definizione di strumenti nella richiesta; `max_tokens: 700`, `stream: false`; temperatura e altri parametri non impostati nella richiesta, configurazione del server non rilevata.
- Risposta `chatcmpl-mei392zidzam0na6x9dbl`; modello restituito `emma-6@bf16`; utilizzo dichiarato: 20 token di prompt, 9 di completamento, 29 totali; `finish_reason: stop`; nessuna chiamata a strumenti restituita.
- Testo originale, compreso lo spazio iniziale:

```text
 **Milano**, capitale della Lombardia.
```

- Esito: API funzionante, ma risposta insufficiente alla richiesta di una descrizione storica. “Capoluogo della Lombardia” sarebbe la formulazione amministrativa appropriata. Nessun voto assegnato; la riuscita diretta non dimostra da sola la causa dell'errore del subagente.

## Export della chat diretta — voce «milano»

- Fonte fornita dall'utente: `milano-domande-dirette-emma-6.md`, conservata senza modifiche.
- Metadati dell'export: `emma-6@bf16`, LM Studio `0.4.26+4`, creazione `25/10/2026, 11:18:50`.
- Dieci scambi nella stessa conversazione: saluto iniziale escluso dal voto e nove domande sul tema Milano. Domande e risposte integrali sono nell'export e nella review affiancata.
- Istruzioni di sistema, campionamento, limiti di generazione e gestione del contesto non visibili nell'export. Non si dichiara che tutti questi parametri fossero assenti o disattivati.
- Review: `milano-domande-dirette-emma-6-review.html`; voto 2/10 con griglia specifica per domande brevi: correttezza (4), pertinenza (3), chiarezza e contesto (2), gestione dell'incertezza (1). Griglia definita dopo la prova, non comunicata al modello.
- Inclusa in `comparativa.html#milano` come prova distinta; il voto non sostituisce né ricalcola le valutazioni delle tesine.
