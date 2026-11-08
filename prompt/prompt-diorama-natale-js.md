# Diorama voxel di Natale — JavaScript / Three.js

Sviluppa una single page application in JavaScript con Three.js che generi proceduralmente un diorama natalizio ispirato alla struttura di Minas Tirith: cittadina fortificata con sette livelli/anelli concentrici su terrazze, grande roccia centrale e cittadella con torre in cima. Reinterpreta la città come un villaggio natalizio alpino. Restituisci un unico file `natale.html` completo con HTML, CSS e JavaScript, senza build o backend. Importa Three.js e OrbitControls da CDN tramite classici tag `<script>` (build UMD/globale, non moduli ES, niente import map), fissando la stessa versione per entrambi, in modo che il file funzioni apribile direttamente via `file://` senza bisogno di un server HTTP locale. Nessun asset esterno oltre agli script CDN.

## Stile e scena
- Minecraft/voxel, non fotorealistico: geometrie a blocchi, materiali semplici, colori piatti. Risoluzione voxel doppia rispetto a una costruzione minimale: blocchi grandi la metà, stesse dimensioni fisiche della città. La risoluzione del canvas è un parametro distinto.
- Base quadrata spessa con sezioni di terra, roccia e neve, ghiaccioli e bordi curati. Sentiero dal primo piano al portone e rampe fra i sette livelli. Vista ortografica iniziale a tre quarti dall'alto, base e torre interamente visibili.
- Mura merlate innevate, archi a blocchi, scale, ponticelli e almeno 12 chalet con tetti a gradoni, camini, neve e finestre illuminate. Torre dell'orologio e stella luminosa sulla cittadella.
- Almeno 10 abeti voxel innevati di altezze diverse, due alberi spogli e un grande albero di Natale con palline cubiche, ghirlande, stella e regali.
- Almeno 12 personaggi voxel con teste, arti, occhi e accessori: Babbo Natale, elfi, bambini con sciarpe, venditore di cioccolata, pattinatori e abitanti con regali. Proporzioni coerenti con gli edifici.
- Slitta con sacco e due renne con corna, pupazzi di neve con carote e cappelli, pacchetti con nastri, cassette postali, lampioni, bastoncini di zucchero, ghirlande e catasta di legna.
- Mercatino con almeno 4 bancarelle diverse: dolci, giocattoli, decorazioni e bevande. Laghetto ghiacciato laterale con pattinatori, impronte squadrate nella neve.
- Scene narrative: elfi che caricano la slitta, bambini che costruiscono un pupazzo, famiglia al mercatino.
- Palette bianco, verde abete, rosso e oro; crepuscolo blu e luci calde. Neve a strati geometrici; pochi fiocchi cubici, senza oscurare i dettagli. Limita le luci dinamiche costose; simula quelle secondarie con materiali emissivi.

## Interazione e animazione
- Interfaccia responsive con titolo, legenda e controlli discreti; canvas a piena finestra. OrbitControls con smorzamento, zoom e rotazione limitati, mouse e touch.
- Pulsanti per ripristino camera, rotazione automatica, pausa animazioni, audio e cattura PNG. Rispetta `prefers-reduced-motion`.
- Raycasting su albero, regalo e slitta: clic sull'albero cambia il ritmo delle luci; su un regalo apre il coperchio e rivela un giocattolo voxel; sulla slitta muove brevemente le renne e attiva i sonagli. Evidenzia gli oggetti interattivi e mostra brevi schede. Non attivare clic durante il trascinamento della camera.
- Anima pattinatori su percorsi chiusi, fiocchi riciclati in un pool e leggere oscillazioni delle decorazioni con delta time. Niente crescita illimitata di particelle.
- Canvas nitido, pixel ratio limitato e qualità configurabile. Esporta un vero PNG 3840×2160 con un pulsante, senza semplice upscaling, ripristinando dopo la cattura dimensioni, camera e pixel ratio originali.

## Suoni e musica sintetizzati
- Solo Web Audio API: oscillatori, inviluppi, filtri e rumore generato. Nessun file audio o campione esterno.
- Componi un motivo originale a piacere, caldo e natalizio: almeno 8 battute con melodia, armonia e basso, timbri sintetici tipo celesta, campanelli e pad morbido. Loop coerente senza clic, volume non invadente.
- Crea sonagli per la slitta, breve arpeggio per il regalo, campane della torre, passi ovattati nella neve e vento delicato. Le interazioni devono avere riscontri sonori distinguibili.
- L'audio parte soltanto dopo «Attiva audio», che crea o riprende l'AudioContext. Prevedi mute, volume generale e controlli separati per musica ed effetti, gain ramp e livelli iniziali moderati.
- Sequencer con scheduling sul clock audio e look-ahead, indipendente dal frame rate. Gestisci cambio scheda, sospensione e ripresa senza duplicare le note o gli scheduler; ferma e disconnetti i nodi terminati.

## Requisiti tecnici e consegna
- Usa InstancedMesh o geometrie unite per i voxel ripetuti, riutilizza materiali e geometrie e ometti blocchi interni invisibili. Evita migliaia di draw call e risorse allocate a ogni frame.
- Seed deterministico e funzioni riutilizzabili; parametri iniziali per dimensioni, dettaglio, qualità, animazione e audio. Evita compenetrazioni vistose, z-fighting e oggetti accidentalmente sospesi.
- Gestisci resize, errori del renderer e caricamento delle dipendenze con messaggi comprensibili; nessun errore in console durante l'uso normale.
- Restituisci il codice completo in un solo blocco, senza pseudocodice, TODO, segnaposto o parti omesse. Il file deve funzionare apribile direttamente nel browser via doppio clic (`file://`), senza server HTTP locale; segnala solo che il caricamento da CDN richiede una connessione internet.
