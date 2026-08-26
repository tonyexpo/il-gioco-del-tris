# Il gioco del tris — demo multi-modello

Questa repository raccoglie il codice prodotto durante una serie di video per il
mio canale YouTube, in formato orizzontale, in cui uso lo **stesso identico
prompt** per far sviluppare da modelli AI diversi — quasi sempre modelli
**locali**, raramente un servizio SaaS — la stessa piccola applicazione
desktop: il gioco del tris (tic-tac-toe).

Ogni cartella dentro `src/` corrisponde a una registrazione/modello diverso:
è l'output ottenuto in quella specifica live, così com'è uscito dal modello.

## Il prompt

Il prompt usato è sempre lo stesso, per garantire un confronto equo tra i
vari modelli:

> Sei uno sviluppatore senior. Sviluppa in WPF un gioco del tris (tic-tac-toe)
> seguendo il pattern MVVM. L'UX è a discrezione ma deve restare semplice. La
> logica del PC è randomica. Il giocatore umano è sempre X, il PC è sempre O.
> È presente un pulsante di reset in basso. Cliccando su uno dei 9 pulsanti
> della griglia la partita parte.

## Perché questa repo è "diversa" dal solito

Lo scopo di questa repository **non è distribuire codice sorgente pulito da
ricompilare**, ma fornire l'accesso esatto a quanto avvenuto sul PC durante
ogni live registrata. Per questo, di proposito:

- **Non è presente alcun `.gitignore`**: cartelle di build come `bin/`,
  `obj/`, `.vs/` sono incluse così come generate durante la registrazione.
- **Eventuali refusi nei nomi di cartelle/file vengono mantenuti**, non
  corretti (es. `toctactoe2` invece di `tictactoe2`), perché riflettono
  esattamente ciò che è stato scritto/generato durante la live.

In altre parole: quello che scarichi è garantito identico a quello mostrato
nel video, senza alcuna "pulizia" successiva che potrebbe introdurre
differenze rispetto a quanto visto on-screen.

## Struttura

```
src/
  tictactoe1/   → output della live/modello 1
  toctactoe2/   → output della live/modello 2
  tictactoe3/   → output della live/modello 3
  tictactoe4/   → output della live/modello 4
  tictactoe5/   → output della live/modello 5
```

## Licenza

Distribuito con licenza [Apache 2.0](LICENSE).
