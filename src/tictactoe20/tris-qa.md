# QA avversariale — gioco del tris

**Autore della QA:** GPT-6.1 Terra (OpenAI), agente OpenCode.

## Riesame dopo le fix segnalate — 31 ottobre 2026

**Esito: non rilasciabile; nessuna delle correzioni precedentemente richieste è riscontrabile nel `tris.html` presente in questa cartella.** Il codice rilevante corrisponde a quello descritto nel rapporto precedente. Non è possibile stabilire se l'agente di sviluppo abbia salvato le modifiche altrove o non le abbia ancora applicate a questo file.

Ho ripetuto le prove eseguendo lo script attuale con DOM e Web Audio simulati:

| Verifica di regressione | Risultato attuale |
|---|---|
| Prima mossa al centro | X presente nello stato interno, tutte le celle visualizzate vuote; la O viene scritta in `board[-1]`. |
| Cella occupata | Dopo centro e alto sinistra, la O in alto al centro può ancora essere sovrascritta con X. |
| Audio | L'oscillatore viene avviato ma non viene collegato; senza `AudioContext` il primo clic genera ancora `ReferenceError` dopo aver scritto X. |
| Pareggio con ultima X | Compare «Pareggio!», ma viene ancora scritta una O in `board[-1]`. |
| Tastiera e riavvio | Dall'analisi del codice persistono celle `div` con solo `click` e assenza di un comando di nuova partita. |

**Stato dei difetti precedenti:** tutti aperti. Le prove di blocco e vittoria del PC riportate sotto non sono state ripetute separatamente in questo riesame; la logica Minimax interessata è tuttora invariata. Nessun test in browser reale è stato eseguito. Per un nuovo collaudo serve la versione corretta di `C:\temp\tictactoe20\tris.html`.

---

## Esito: non conforme, non rilasciabile

Il gioco non è utilizzabile: le mosse non vengono mostrate, il PC non inserisce una O valida al primo turno e i suoni non raggiungono l'uscita audio. La logica consente inoltre di sovrascrivere le caselle. Il file richiesto esiste ed è una pagina HTML autonoma con JavaScript vanilla, ma i requisiti funzionali principali non sono soddisfatti.

## Ambito e metodo

- Prompt di riferimento: `C:\temp\prompt-tris.md`: tris in JavaScript vanilla, pagina singola `tris.html`, umano sempre X, PC sempre O, Minimax facile e suoni sintetizzati.
- File esaminato: `tris.html`. Nessuna modifica al gioco è stata effettuata.
- Analisi statica e prove con Node.js eseguendo lo script originale in un contesto isolato con DOM e Web Audio simulati. Le prove verificano la logica e le chiamate, non sostituiscono un collaudo visivo, sonoro o di accessibilità in un browser reale.
- Indici interni da 0 a 8, in ordine di lettura; nella descrizione utente le caselle sono da 1 a 9.

## Difetti

### P0 — Nessuna mossa viene visualizzata

**Riferimenti:** `tris.html:165-176`, `tris.html:193-201`.

Le celle sono create vuote e non esiste alcuna funzione che aggiorni il loro contenuto dopo una mossa. Cliccando la cella centrale, la X viene scritta nello stato interno, ma tutte le nove celle restano vuote. L'utente non può conoscere la posizione dei simboli né giocare una partita verificabile.

**Atteso:** aggiornare la cella corrispondente a ogni mossa valida, mostrando X o O e mantenendo sincronizzati interfaccia e stato.

### P0 — Minimax valuta la scacchiera sbagliata e la prima O finisce fuori griglia

**Riferimenti:** `tris.html:70-81`, `tris.html:85-109`, `tris.html:118-132`, `tris.html:175-176`.

`minimax` simula le mosse sulle copie `boardArr`, ma `checkWin` e `isBoardFull` leggono sempre la `board` globale. Le posizioni simulate non sono quindi valutate: quando la copia si riempie, la ricorsione può restituire valori infiniti anziché un punteggio valido. Alla prima mossa umana, `getBestMoveForO` restituisce `-1`; l'assegnazione successiva crea la proprietà `board[-1] = 'O'` invece di occupare una delle nove caselle.

**Riproduzione verificata:** clic sulla cella centrale: tra gli indici 0–8 rimane solo la X centrale, senza alcuna O. In una posizione di prova con `X, X, vuota` sulla prima riga, il calcolo ha restituito `-1` anziché bloccare la minaccia; in un'altra con due O consecutive ha scelto l'indice 1 anziché completare la riga all'indice 5.

**Atteso:** valutare vittoria e pareggio sulla posizione simulata, restituire sempre una casella libera valida quando disponibile e verificare il risultato prima di scrivere. Il prompt dice «minimax facile», senza definire precisamente il livello: in ogni caso la simulazione deve operare correttamente.

### P1 — Le caselle occupate possono essere sovrascritte

**Riferimenti:** `tris.html:165-167`.

`handleHumanClick` controlla solo `gameOver`, non se la casella sia libera. Con il DOM simulato, dopo un clic al centro e uno sulla cella in alto a sinistra, il PC colloca una O nella cella in alto al centro; cliccando quest'ultima, la O viene sovrascritta con una X e il PC gioca un'ulteriore O. Anche ricliccare una X può provocare un turno aggiuntivo del PC.

**Atteso:** ignorare una selezione su una casella occupata senza cambiare stato, turno o suono.

### P1 — I suoni sintetizzati sono silenziosi

**Riferimenti:** `tris.html:151-161`.

L'oscillatore viene creato e avviato, e il gain viene collegato alla destinazione, ma manca il collegamento dall'oscillatore al gain. Nella prova simulata sono state osservate chiamate a `gain.connect` e `osc.start`, ma nessuna a `osc.connect`: il segnale non raggiunge l'uscita. Inoltre non viene mai richiamato un suono specifico di vittoria o pareggio, nonostante i tipi siano previsti.

**Atteso:** collegare oscillatore → gain → destinazione e verificare l'udibilità in un browser reale; gestire coerentemente anche gli eventi di fine partita se si vogliono distinguere.

### P1 — Se l'audio non è disponibile la partita si interrompe a metà mossa

**Riferimenti:** `tris.html:147-150`, `tris.html:165-169`.

In un ambiente simulato senza `AudioContext`, il primo clic genera `ReferenceError: AudioContext is not defined` dopo aver già scritto la X, ma prima di aggiornare lo stato o far giocare il PC. L'espressione accede all'identificatore non dichiarato prima di provare `window.AudioContext`. Anche altri errori di inizializzazione audio non sono gestiti.

**Atteso:** rilevare in sicurezza il supporto audio e trattare l'audio come opzionale: se non disponibile o fallisce, la partita deve proseguire normalmente.

### P2 — Il pareggio viene controllato dopo un turno PC inesistente

**Riferimenti:** `tris.html:170-176`, `tris.html:184-186`.

Se l'ultima X riempie la griglia senza vincere, il codice tenta comunque la mossa del PC. Nella prova con posizione iniziale `X O X / X O O / O X vuota`, l'ultima X produce correttamente il testo «Pareggio!», ma prima viene scritto `board[-1] = 'O'` e viene tentato un suono per una mossa PC inesistente.

**Atteso:** controllare il pareggio subito dopo la mossa umana e terminare senza chiamare il PC quando la griglia è piena.

### P2 — Mancano comandi accessibili e nuova partita

**Riferimenti:** `tris.html:50-52`, `tris.html:193-201`, `tris.html:205-210`.

Le celle sono `div` con solo un gestore `click`: non sono pulsanti nativi, non sono normalmente raggiungibili da tastiera e non dichiarano posizione o stato accessibile. Lo stato iniziale è vuoto e non c'è un comando per ricominciare senza ricaricare la pagina. Mancano inoltre il meta viewport e una verifica del layout su schermi stretti. La UX era libera nel prompt, ma questi aspetti riducono l'usabilità.

**Atteso:** celle utilizzabili da tastiera e con nome/stato accessibile, stato iniziale comprensibile, comando di nuova partita e verifica responsive.

## Copertura delle verifiche

| Verifica | Esito |
|---|---|
| Pagina singola `tris.html`, JavaScript vanilla | Presente |
| Prima mossa umana e risposta PC nella griglia | Fallita: PC scrive in `board[-1]` |
| Visualizzazione delle mosse | Fallita: celle sempre vuote |
| Blocco minaccia e scelta vittoria PC | Fallita nelle posizioni di prova |
| Clic su casella occupata | Fallita: casella sovrascritta |
| Pareggio sull'ultima X | Messaggio corretto, ma tentata mossa PC non valida |
| Collegamento del segnale audio | Fallita: oscillatore scollegato |
| Indisponibilità API audio | Fallita: eccezione dopo modifica parziale dello stato |
| Browser reale, ascolto, dispositivi mobili e screen reader | Non eseguiti |

## Priorità di correzione e regressione

1. Correggere le funzioni di valutazione del Minimax affinché usino la scacchiera simulata; impedire indici non validi e controllare le condizioni terminali dopo ogni mossa.
2. Implementare il rendering delle celle e bloccare le mosse su celle occupate; aggiungere una nuova partita che ripristini stato e interfaccia.
3. Collegare il grafo audio e rendere innocui gli errori audio.
4. Ripetere le prove in browser, comprese tutte le otto linee di vittoria per entrambi i giocatori, pareggio, clic ripetuti, riavvio, tastiera e schermi stretti. Per il Minimax, esplorare sistematicamente le partite raggiungibili e verificare mosse legali e comportamento rispetto al livello di difficoltà scelto.
