# Diorama voxel di Minas Tirith — JavaScript / Three.js

Sviluppa una single page application in JavaScript con Three.js che generi proceduralmente un diorama 3D della città di Minas Tirith in stile Minecraft/voxel: blocchi, colori semplici, geometrie squadrate, nessun fotorealismo. Restituisci un unico file `index.html` completo con HTML, CSS e JavaScript, senza build o backend. Importa Three.js e OrbitControls tramite import map da CDN, fissando la stessa versione per entrambi. Nessun asset esterno oltre ai moduli JavaScript: geometrie, materiali, effetti sonori e musica devono essere generati dal codice.

## Scena
- Città bianca con sette livelli/anelli concentrici su terrazze, mura merlate, porte, rampe percorribili visivamente e una grande roccia centrale a sperone. Cittadella e torre svettano in cima.
- Risoluzione voxel doppia rispetto a una costruzione minimale: dimezza il lato dei blocchi a parità di dimensioni fisiche. Distingui il dettaglio geometrico dalla risoluzione del canvas.
- Miniatura completa su una base quadrata spessa, con bordi rifiniti e sezioni visibili di terra e pietra, pianura davanti alla porta e pendice montuosa sul retro. Niente terreno infinito: anche la montagna è un volume delimitato integrato nella base. Inquadra base, montagna e torre interamente, con margine attorno alla composizione e sfondo neutro.
- Almeno 20 edifici con tetti, porte, finestre e camini; piazze, scale, ponti, stendardi e piccoli banchi del mercato. Albero bianco nella corte sommitale e almeno 10 alberi distribuiti fra città e pendici.
- Almeno 12 personaggi voxel con teste, arti e accessori: guardie, mercanti, viandanti e abitanti. Piccole scene narrative presso il mercato, il portone e la corte; niente cubi casuali usati come sostituto dei personaggi.
- Luce diurna calda, ombre morbide e occlusione suggerita dalla palette. Materiali semplici, silhouette pulite, colori leggibili e nessuna texture scaricata.

## Interazione e presentazione
- Interfaccia responsive curata con titolo, breve legenda e controlli discreti; canvas a piena finestra. Vista iniziale ortografica a tre quarti dall'alto che includa base e torre.
- OrbitControls con smorzamento, rotazione e zoom limitati per non attraversare il terreno; supporto mouse e touch. Pulsanti per ripristino camera, rotazione automatica, pausa animazioni, audio e cattura PNG.
- Clic su almeno tre punti d'interesse con raycasting: portone, mercato e cittadella. Mostra una breve scheda e un riscontro sonoro quando l'audio è attivo. Distingui un clic da un trascinamento.
- Anima con discrezione bandiere, alcuni personaggi e luci; usa delta time e un seed deterministico. Rispetta `prefers-reduced-motion` e consenti di mettere in pausa le animazioni.
- Canvas nitido su schermi ad alta densità, pixel ratio limitato e qualità configurabile. Pulsante per esportare una vera immagine PNG 3840×2160, ripristinando poi dimensioni, rapporto della camera e pixel ratio originali; l'esportazione non deve essere uno screenshot vuoto o un semplice ingrandimento del canvas a bassa risoluzione.

## Suoni e musica sintetizzati
- Usa esclusivamente Web Audio API: oscillatori, inviluppi, filtri, rumore generato e semplici effetti. Vietati file audio esterni, campioni scaricati e tracce preregistrate.
- Componi un motivo originale a piacere, epico e sereno, con melodia, armonia e basso: almeno 8 battute, loop coerente senza clic, timbri che suggeriscano corni morbidi, arpa e campane, ottenuti per sintesi.
- Aggiungi ambiente leggero di vento e suoni distinti per selezione, campana della cittadella e interazioni. Evita suoni continui invadenti.
- Avvia o riprendi l'AudioContext solo dopo il pulsante «Attiva audio». Prevedi mute, volume generale e controlli separati per musica ed effetti, con livelli iniziali moderati e gain ramp per evitare clic.
- Pianifica le note sul clock audio con look-ahead; non affidare il tempo musicale al frame rate. Gestisci sospensione della scheda, ripresa e spegnimento senza duplicare sequencer o creare nodi illimitati. Ferma e disconnetti i nodi terminati.

## Qualità tecnica e consegna
- Usa InstancedMesh o geometrie unite per blocchi ripetuti, riutilizza geometrie/materiali ed evita cubi interni invisibili. Nessun oggetto separato per ogni voxel se porta a migliaia di draw call.
- Gestisci ridimensionamento, fallimento del renderer e mancato caricamento delle dipendenze con messaggi comprensibili. Nessun errore in console durante l'uso normale.
- Codice organizzato in funzioni leggibili con parametri iniziali per scala, dettaglio, seed, animazione e audio. Nessun pseudocodice, TODO o parte lasciata da implementare.
- Restituisci l'intero `index.html` in un solo blocco di codice e poi istruzioni minime per servirlo con un server HTTP statico locale. Indica che il primo caricamento delle dipendenze CDN richiede internet.
