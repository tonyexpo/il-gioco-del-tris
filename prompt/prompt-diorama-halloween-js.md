# Diorama voxel di Halloween — JavaScript / Three.js

Sviluppa una single page application in JavaScript con Three.js che generi proceduralmente un diorama di Halloween ispirato alla struttura di Minas Tirith: cittadina fortificata con sette livelli/anelli concentrici su terrazze, grande roccia centrale e cittadella con torre in cima. Reinterpreta la città come un borgo stregato. Restituisci un unico file `halloween.html` completo con HTML, CSS e JavaScript, senza build o backend. Importa Three.js e OrbitControls da CDN tramite classici tag `<script>` (build UMD/globale, non moduli ES, niente import map), fissando la stessa versione per entrambi, in modo che il file funzioni apribile direttamente via `file://` senza bisogno di un server HTTP locale. Nessun asset esterno oltre agli script CDN.

## Stile e scena
- Minecraft/voxel, non fotorealistico: geometrie a blocchi, materiali semplici, colori piatti. Risoluzione voxel doppia rispetto a una costruzione minimale: blocchi grandi la metà, stesse dimensioni fisiche della città. La risoluzione del canvas è un parametro distinto.
- Base quadrata spessa con sezioni di terra e roccia, radici e bordi curati. Sentiero dal primo piano al portone e rampe fra i sette livelli. Vista ortografica iniziale a tre quarti dall'alto, base e torre interamente visibili.
- Mura merlate, archi a blocchi, scale, ponticelli e almeno 12 casette con tetti viola scuro, camini e finestre illuminate. Torre stregata con orologio, tetto a gradoni e luna cubica sullo sfondo.
- Almeno 10 alberi voxel: querce con foglie arancio/rosse, alberi secchi e un grande albero contorto presso la cittadella.
- Almeno 12 personaggi voxel con teste, arti, occhi e accessori: strega con scopa, scheletro, vampiro, fantasma, guardiano e bambini in costume con secchielli. Proporzioni coerenti con gli edifici.
- Zucche di varie dimensioni, almeno 8 jack-o'-lantern luminose, calderone verde, dolci, cimitero con lapidi e cancello, ragnatele stilizzate, pipistrelli cubici, funghi e foglie cadute.
- Scene narrative: bambini al portone, strega al calderone, fantasma fra le lapidi. Nessun elemento splatter.
- Palette arancio, viola, nero e verde acido; atmosfera serale con luce blu-viola e finestre calde. Ombre curate e dettagli leggibili, senza nebbia densa. Limita le luci dinamiche costose; simula quelle secondarie con materiali emissivi.

## Interazione e animazione
- Interfaccia responsive con titolo, legenda e controlli discreti; canvas a piena finestra. OrbitControls con smorzamento, zoom e rotazione limitati, mouse e touch.
- Pulsanti per ripristino camera, rotazione automatica, pausa animazioni, audio e cattura PNG. Rispetta `prefers-reduced-motion`.
- Raycasting su zucche, calderone e torre: clic su una zucca alterna la luce; sul calderone attiva bolle cubiche; sulla torre fa suonare la campana. Evidenzia gli oggetti interattivi e mostra brevi schede. Non attivare clic durante il trascinamento della camera.
- Anima pipistrelli, lieve galleggiamento del fantasma, bolle e tremolio delle luci con delta time. Niente crescita illimitata di particelle.
- Canvas nitido, pixel ratio limitato e qualità configurabile. Esporta un vero PNG 3840×2160 con un pulsante, senza semplice upscaling, ripristinando dopo la cattura dimensioni, camera e pixel ratio originali.

## Suoni e musica sintetizzati
- Solo Web Audio API: oscillatori, inviluppi, filtri e rumore generato. Nessun file audio o campione esterno.
- Componi un motivo originale a piacere, giocoso e misterioso in tonalità minore: almeno 8 battute con melodia, armonia e basso, timbri sintetici tipo carillon e organo morbido. Loop musicale coerente senza clic, volume non invadente.
- Crea vento leggero, gorgoglio del calderone, campana scura, fruscio dei pipistrelli e suono breve per le zucche. Le interazioni devono avere riscontri sonori distinguibili.
- L'audio parte soltanto dopo «Attiva audio», che crea o riprende l'AudioContext. Prevedi mute, volume generale e controlli separati per musica ed effetti, gain ramp e livelli iniziali moderati.
- Sequencer con scheduling sul clock audio e look-ahead, indipendente dal frame rate. Gestisci cambio scheda, sospensione e ripresa senza duplicare le note o gli scheduler; ferma e disconnetti i nodi terminati.

## Requisiti tecnici e consegna
- Usa InstancedMesh o geometrie unite per i voxel ripetuti, riutilizza materiali e geometrie e ometti blocchi interni invisibili. Evita migliaia di draw call e risorse allocate a ogni frame.
- Seed deterministico e funzioni riutilizzabili; parametri iniziali per dimensioni, dettaglio, qualità, animazione e audio. Evita compenetrazioni vistose, z-fighting e oggetti accidentalmente sospesi.
- Gestisci resize, errori del renderer e caricamento delle dipendenze con messaggi comprensibili; nessun errore in console durante l'uso normale.
- Restituisci il codice completo in un solo blocco, senza pseudocodice, TODO, segnaposto o parti omesse. Il file deve funzionare apribile direttamente nel browser via doppio clic (`file://`), senza server HTTP locale; segnala solo che il caricamento da CDN richiede una connessione internet.
