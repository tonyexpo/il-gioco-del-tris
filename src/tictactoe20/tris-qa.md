# QA — Tris 2D

## Esito

**Non approvato.** Il gioco non è utilizzabile come partita di tris: le caselle non mostrano i simboli, il rilevamento della vittoria è errato e la partita non si ferma. Inoltre la logica del PC non implementa minimax, richiesto dal prompt.

**Ambito:** verifica statica di `tris.html` rispetto a `../prompt-tris.md` e prova dello script JavaScript con un DOM simulato. Non è stata eseguita una prova visiva o audio in un browser reale. Righe riferite alla versione esaminata del file.

## Problemi

### 1. Critico — X e O non sono visibili e la griglia non viene applicata

- **Dove:** `tris.html:25-30`, `60`, `77-88`, `131-150`.
- Il contenitore ha classe `grid`, mentre le regole CSS della griglia sono definite per `.board`. Le caselle quindi non vengono disposte secondo la griglia 3×3 prevista.
- Ogni pulsante viene creato con testo vuoto; dopo le mosse si aggiorna solo lo stato interno e si aggiunge la stessa classe `selected` sia a X sia a O. I simboli non vengono mai scritti nelle caselle, né i due giocatori sono distinguibili dal colore.
- **Riproduzione:** aprire la pagina e selezionare una casella. Anche dopo la risposta del PC, nessuna casella mostra X o O. La prova dello script con DOM simulato ha confermato i nove testi vuoti.
- **Atteso:** griglia 3×3 e simboli X/O visibili e distinguibili nelle posizioni occupate.

### 2. Critico — Una linea piena di simboli diversi viene considerata una vittoria

- **Dove:** `tris.html:92-100` e `104-109`.
- `checkWinner` e `evaluateBoard` verificano solo che le tre caselle non siano vuote, senza verificare che contengano lo stesso simbolo. L'esito viene attribuito al simbolo nella prima casella della linea.
- **Riproduzione:** su pagina iniziale selezionare la casella centrale (5), poi quella centrale sinistra (4), numerando da 1 a 9 per righe. Il PC occupa prima la 1 e poi la 2: la prima riga è `O O X`, ma lo stato annuncia la vittoria del PC. Sequenza confermata con DOM simulato.
- **Atteso:** vittoria solo per tre simboli uguali sulla stessa linea; la stessa condizione deve essere usata dalla valutazione del PC.

### 3. Alto — Il PC non usa minimax e non prevede le minacce

- **Dove:** `tris.html:104-128`, `138-150`, `161-180`.
- Si valuta solo la posizione immediatamente successiva alla mossa O; non vengono esplorate ricorsivamente le risposte dell'avversario. Inoltre `chooseBestForO` e `handleComputerMove` non sono chiamate nel flusso principale, che duplica la stessa valutazione. Il difetto di rilevamento delle linee altera anche questi punteggi.
- **Riproduzione per ispezione del codice:** dall'inizio selezionare 1, poi 4. Il PC risponde rispettivamente con 2 e 5, lasciando libera la 7, che completa la colonna di X alla mossa successiva. Le posizioni sono numerate per righe da 1 a 9.
- **Atteso:** un minimax semplice che consideri le mosse successive di entrambi i giocatori, blocchi le vittorie immediate di X e scelga correttamente gli esiti terminali.

### 4. Alto — Si continua a giocare dopo la fine e il PC muove dopo una vittoria di X

- **Dove:** `tris.html:131-159`, `227-248`.
- Le chiamate a `checkWinner()` dopo le mosse ignorano il valore restituito; non esiste un controllo di partita terminata all'inizio degli handler. Il PC viene eseguito subito dopo X anche se X ha già vinto. Anche il pulsante separato può modificare la partita conclusa.
- **Riproduzione:** seguire la sequenza 5, 4 del problema 2; dopo l'annuncio della vittoria del PC, selezionare la casella 7. La casella viene comunque accettata e il PC effettua un'altra mossa; la continuazione è stata confermata con DOM simulato.
- **Atteso:** verificare vittoria o pareggio subito dopo ogni mossa, fermare la sequenza e impedire ulteriori mosse fino a una nuova partita.

### 5. Alto — Il pulsante aggiuntivo inserisce X senza rispettare i turni

- **Dove:** `tris.html:62`, `227-249`.
- Il pulsante «Scegli la tua mossa (X)» non permette di scegliere una casella: inserisce X automaticamente nella prima libera. `bestScore` parte da `-Infinity` e il confronto `score < bestScore` non può riuscire con i punteggi restituiti, quindi viene sempre usato il fallback. Non segue una mossa del PC; clic ripetuti consentono più X consecutive.
- **Riproduzione:** all'avvio premere due volte il pulsante: lo stato interno contiene X nelle prime due caselle e nessuna O.
- **Atteso:** eliminare il pulsante superfluo oppure assegnargli un comportamento coerente con scelta della casella, alternanza e fine partita.

### 6. Medio — Nessun comando per iniziare una nuova partita

- **Dove:** interfaccia e stato in `tris.html:58-63`, `69-70`.
- Non è previsto un reset della scacchiera; per rigiocare occorre ricaricare la pagina. La funzionalità non è esplicitamente richiesta dal prompt, ma è importante per l'usabilità.
- **Atteso:** un comando di nuova partita che ripristini stato, caselle e messaggio iniziale.

### 7. Medio — Layout e accessibilità da verificare

- **Dove:** `tris.html:3-5`, `13`, `27-28`, `32-40`, `77-87`.
- Manca il viewport per dispositivi mobili; griglia e celle hanno dimensioni fisse e il contenitore è centrato in un'area alta esattamente `100vh`, con rischio di tagli su schermi piccoli. Le celle sono pulsanti senza testo né etichetta accessibile, quindi posizione e contenuto non sono comunicati chiaramente agli screen reader.
- **Atteso:** layout adattabile, viewport configurato ed etichette accessibili che identifichino posizione e stato di ogni casella. Da confermare con test su dispositivi e tecnologie assistive.

## Requisiti e verifiche residue

- **File singolo / JavaScript vanilla:** presenti in `tris.html`, senza dipendenze esterne apparenti.
- **Umano X e PC O:** rispettati nei valori assegnati dal percorso principale, ma non visibili; il pulsante aggiuntivo rompe l'alternanza.
- **Suoni sintetizzati:** presente un beep Web Audio sulle selezioni valide delle celle, con fallback silenzioso in caso di errore. Riproduzione effettiva non verificata in browser.
- Dopo le correzioni, verificare in browser: tutte le otto linee vincenti per entrambi i giocatori, linee miste non vincenti, pareggio, blocco delle mosse a fine partita, reset, input da tastiera, schermi piccoli e audio. Verificare inoltre minimax su tutti gli stati raggiungibili, inclusa l'impossibilità per X di vincere contro un PC perfetto.
