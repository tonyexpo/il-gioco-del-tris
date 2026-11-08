# QA 2 — Tris 2D

## Esito

**Non approvato.** La versione attuale corregge la classe della griglia e introduce un controllo di fine partita nel percorso principale, ma il gioco rimane inutilizzabile: i simboli non rappresentano lo stato, il controllo delle vittorie continua ad accettare linee miste e il PC non usa minimax.

**Ambito:** riesame di `tris.html` rispetto a `../prompt-tris.md` e a `tris-qa.md`, con lettura del codice e prove dello script in un DOM simulato. Non sono stati eseguiti test visivi, audio o con tecnologie assistive in un browser reale. I riferimenti alle righe riguardano la versione attuale di `tris.html`.

Nelle sequenze sotto le caselle sono numerate da 1 a 9, da sinistra a destra e dall'alto in basso.

## Problemi aperti

### 1. Critico — La scacchiera visualizzata non rappresenta le mosse

- **Dove:** `tris.html:33-51`, `79-89`, `133-148`, `163-165`.
- In `renderBoard`, `boardState[i] === 'X' ? 'X' : 'O'` assegna O anche alle caselle vuote. Il rendering avviene solo all'avvio: dopo le mosse non viene aggiornato il testo delle celle. Il DOM simulato conferma nove testi `O` all'inizio e ancora nove `O` dopo le mosse.
- Inoltre la regola generale `button { color: #fff }` assegna testo bianco anche alle celle, che hanno sfondo bianco o verde molto chiaro: i simboli hanno contrasto insufficiente. L'aspetto preciso resta da verificare in browser.
- **Atteso:** celle vuote inizialmente, X e O aggiornate dopo ogni mossa e testo sufficientemente contrastato. Il colore da solo non deve distinguere i giocatori.

### 2. Critico — Le linee miste continuano a risultare vincenti

- **Dove:** `tris.html:94-102`, `106-110`.
- La nuova condizione `vals.every(v => v === v[0])` non confronta i valori tra loro: per i simboli di un carattere `v[0]` è sempre uguale a `v`. Una linea piena viene quindi ancora attribuita al simbolo della prima casella. Anche la valutazione del PC ha lo stesso errore.
- **Riproduzione confermata nel DOM simulato:** selezionare 5 e poi 4. Il PC sceglie 1 e poi 2; la prima riga interna è `O O X`, ma compare «Il PC ha vinto con O!».
- **Atteso:** confrontare tutte le caselle della linea con il primo elemento della linea, assicurandosi che non sia vuoto; applicare lo stesso criterio alla valutazione delle mosse.

### 3. Alto — Il PC non implementa minimax

- **Dove:** `tris.html:106-130`, `151-176`.
- Il PC valuta soltanto il risultato immediato di ogni possibile O; non esplora ricorsivamente le mosse successive di X e O. Per giunta la valutazione usa il controllo errato descritto sopra. `chooseBestForO` non viene chiamata, mentre `handleComputerMove` contiene una valutazione duplicata.
- **Atteso:** minimax semplice sugli stati successivi, con punteggi terminali corretti e scelta della migliore mossa per O; verificare in particolare blocchi e vittorie immediate.

### 4. Alto — Il pulsante aggiuntivo rompe i turni e la fine partita

- **Dove:** `tris.html:63`, `221-245`.
- «Scegli la tua mossa (X)» non consente di scegliere: assegna automaticamente X alla prima casella libera e non fa rispondere il PC. Il confronto `score < bestScore` parte da `-Infinity` e non può riuscire con i punteggi restituiti, perciò si usa sempre il fallback. Il pulsante aggiorna lo stato testuale, ma non imposta `gameOver` quando produce una vittoria.
- **Riproduzione confermata nel DOM simulato:** premere il pulsante tre volte all'avvio. Il messaggio annuncia la vittoria di X senza alcuna mossa O; selezionando poi la casella 4 viene accettata un'ulteriore X prima che il percorso principale imposti `gameOver`.
- **Atteso:** rimuovere il pulsante superfluo o farlo passare per la stessa gestione di mosse, turni e fine partita delle celle.

### 5. Medio — Fine partita gestita solo parzialmente

- **Dove:** `tris.html:133-148`, `171-176`, `221-245`.
- Il percorso delle celle ora impedisce nuove mosse dopo una vittoria rilevata e ferma il PC dopo una vittoria di X. Tuttavia il controllo della vittoria è errato e il pulsante aggiuntivo può concludere la partita senza impostare `gameOver`. In caso di pareggio non viene impostato `gameOver`; la scacchiera piena impedisce comunque ulteriori inserimenti, ma lo stato interno non rappresenta esplicitamente la fine.
- **Atteso:** un'unica gestione degli esiti terminali, inclusi i pareggi, dopo ogni mossa e per ogni percorso di input.

### 6. Medio — Nessuna nuova partita senza ricaricare

- **Dove:** `tris.html:59-64`, `70-77`.
- Non c'è un comando di reset. Non è un requisito esplicito del prompt, ma è una lacuna di usabilità.
- **Atteso:** comando che ripristini scacchiera, stato terminale e messaggio iniziale.

### 7. Medio — Accessibilità e adattamento agli schermi piccoli incompleti

- **Dove:** `tris.html:5`, `9-15`, `18-35`, `79-89`.
- Il viewport ora è presente. Restano dimensioni fisse delle celle e altezza `100vh` con centratura verticale, che possono creare overflow o tagli su schermi piccoli. Le celle non hanno etichette che ne identifichino posizione e stato; inoltre il loro testo attuale è scorretto.
- **Atteso:** layout adattabile, etichette accessibili per posizione e contenuto e verifica in browser con tastiera e screen reader.

## Confronto con la prima QA

| Segnalazione precedente | Stato attuale |
| --- | --- |
| Classe della griglia errata | Corretta: il contenitore usa `board`. |
| Simboli assenti | Non risolta; nuova regressione: il DOM iniziale contiene nove O e non aggiorna i testi. |
| Vittorie su linee miste | Non risolta: il confronto aggiunto verifica ogni carattere contro sé stesso. |
| Minimax assente | Non risolta. |
| Mosse dopo fine partita | Parzialmente corretta nel percorso delle celle; restano il pulsante aggiuntivo e la gestione del pareggio. |
| Pulsante aggiuntivo e turni | Non risolta. |
| Reset assente | Non risolta. |
| Viewport e accessibilità | Viewport aggiunto; layout adattabile ed etichette restano da sistemare e verificare. |

## Verifiche residue

- La pagina resta un file HTML singolo con JavaScript vanilla; i valori interni assegnati dal percorso principale sono X per l'umano e O per il PC.
- È ancora presente un beep sintetizzato Web Audio per i clic validi sulle celle; non è stato verificato in browser e il pulsante aggiuntivo non lo riproduce.
- Dopo le correzioni, testare tutte le otto linee per entrambi i simboli, linee miste, pareggio, blocco delle mosse dopo ogni esito e reset. Testare minimax sugli stati raggiungibili, oltre a visualizzazione, contrasto, tastiera, schermi piccoli e audio in un browser reale.
