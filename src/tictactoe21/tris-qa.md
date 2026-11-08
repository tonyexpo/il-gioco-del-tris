# QA — tris.html

## Ambito e metodo

Revisione statica di `tris.html` e verifiche mirate della logica JavaScript con Node.js, usando un DOM e un'API audio simulati. Non sono stati eseguiti test in browser reali, su dispositivi mobili o con tecnologie assistive.

## Risultato

**Esito: non superato.** Sono presenti problemi nella strategia del PC, nel reset e nell'accessibilità; l'audio può inoltre impedire il funzionamento del gioco.

## Problemi rilevati

### 1. Il minimax valuta erroneamente i pareggi — alta

- **Riferimenti:** `tris.html:157-165`, `tris.html:169-195`.
- **Riproduzione:** chiamare `minimax(['X','O','X','X','O','O','O','X','X'], 0, true)` su un tabellone pieno e in pareggio.
- **Atteso:** punteggio `0`.
- **Effettivo:** `-Infinity`; con `isMaximizing` falso il risultato sarebbe `Infinity`. `evaluate` restituisce `0` sia per il pareggio sia per una partita in corso, quindi `minimax` non riconosce il pareggio come stato terminale e restituisce il valore iniziale quando non ci sono celle libere.
- **Impatto:** le valutazioni delle mosse sono errate e il PC può scegliere una strategia non ottimale.
- **Correzione suggerita:** terminare la ricorsione con `0` quando il tabellone è pieno e non c'è un vincitore.

### 2. Un timer della partita precedente può eseguire una mossa nella nuova partita — media

- **Riferimenti:** `tris.html:244`, `tris.html:264-265`, `tris.html:278-295`.
- **Riproduzione:** giocare una X, premere subito «Nuova Partita» e giocare una nuova X prima che trascorrano 500 ms dalla prima mossa.
- **Atteso:** solo il timer della nuova partita deve gestire la risposta del PC, dopo il ritardo previsto per quella mossa.
- **Effettivo:** il timer della partita precedente trova il nuovo gioco attivo e il turno su O, quindi esegue una mossa nel nuovo tabellone. Il timer successivo può essere ignorato oppure, se nel frattempo l'utente ha già giocato di nuovo, anticipare un'ulteriore risposta.
- **Correzione suggerita:** conservare l'identificativo del timer e annullarlo con `clearTimeout` al reset; eventualmente associare anche una versione della partita al callback.

### 3. L'audio è obbligatorio e può bloccare il gioco — alta

- **Riferimenti:** `tris.html:88-96`, `tris.html:247-260`, `tris.html:294-301`.
- **Riproduzione:** avviare la pagina in un ambiente senza `AudioContext` né `webkitAudioContext`.
- **Atteso:** il gioco resta utilizzabile senza audio.
- **Effettivo:** `initAudio()` genera un'eccezione durante l'inizializzazione. Anche un errore audio durante una mossa interromperebbe `handleMove` prima della verifica del risultato e del cambio di turno, lasciando uno stato incoerente.
- **Correzione suggerita:** trattare l'audio come funzionalità opzionale, controllare la disponibilità dell'API e gestire gli errori senza interrompere la logica di gioco. Inizializzare o riattivare il contesto in risposta a un'interazione dell'utente.

### 4. Le celle non sono utilizzabili da tastiera — alta

- **Riferimenti:** `tris.html:285-291`, `tris.html:64-67`.
- **Riproduzione:** provare a raggiungere e attivare le celle usando Tab e Invio o Spazio.
- **Atteso:** ogni mossa è eseguibile da tastiera, con indicazione comprensibile di posizione e stato; i cambiamenti di turno e risultato sono annunciabili.
- **Effettivo:** le celle sono `div` senza focus, semantica di controllo o gestione della tastiera; lo stato non è una regione live.
- **Correzione suggerita:** usare pulsanti con etichette accessibili per le celle, prevedere uno stato di focus visibile e una regione `aria-live` per gli aggiornamenti.

### 5. Il risultato di una mossa umana viene gestito due volte — bassa

- **Riferimenti:** `tris.html:231-239`, `tris.html:247-257`.
- **Riproduzione:** completare una partita con una mossa umana vincente o di pareggio.
- **Atteso:** un'unica gestione del risultato e un solo suono finale.
- **Effettivo:** `handleMove` chiama `handleResult`, poi `handleCellClick` verifica nuovamente il vincitore e richiama `handleResult`, riproducendo due volte il suono finale.
- **Correzione suggerita:** centralizzare la verifica e la gestione del risultato in un solo punto.

## Verifiche eseguite

| Caso | Esito |
| --- | --- |
| Avvio con API audio simulata e prima mossa umana | Superato: X viene inserita e il turno passa al PC. |
| Minimax su tabellone pieno in pareggio | Fallito: restituisce `-Infinity` anziché `0`. |
| Reset e nuova mossa prima dello scadere del vecchio timer | Fallito: il vecchio timer muove nel nuovo gioco. |
| Avvio senza API audio | Fallito: eccezione nel costruttore audio. |
| Accessibilità da tastiera e doppia gestione del risultato | Problemi rilevati tramite analisi del codice; non verificati in un browser. |

## Priorità di intervento

Correggere prima la condizione terminale del minimax, rendere l'audio non bloccante e garantire l'uso da tastiera; quindi risolvere il timer del reset e la doppia gestione del risultato. Ripetere infine i test in browser, inclusi tastiera, lettore di schermo e viewport mobili.
