# Diorama voxel di Minas Tirith — Blender

Sviluppa uno script Python per Blender (bpy) che generi proceduralmente un diorama della città di Minas Tirith in stile Minecraft/voxel: non fotorealistico, geometrie a blocchi, colori semplici e materiali senza texture esterne.

## Diorama e composizione
- Costruisci una miniatura completa su una base quadrata spessa, con bordi rifiniti e strati visibili di terra e roccia. Tutto deve appartenere al diorama: niente terreno infinito. La montagna sul retro è un volume delimitato e integrato nella base.
- Riproduci sette livelli/anelli concentrici su terrazze ascendenti, mura bianche merlate, grande sperone roccioso centrale e torre/cittadella in cima, mantenendo proporzioni e silhouette riconoscibili.
- Inserisci una pianura in primo piano, un sentiero verso il portone, rampe che collegano i livelli, scale e piccoli ponti. Gli edifici devono poggiare sulle terrazze senza compenetrazioni evidenti.
- Usa una risoluzione voxel doppia rispetto al minimo: blocchi grandi la metà, più dettagli, stesse dimensioni fisiche complessive. Distingui densità geometrica e risoluzione del render.
- Almeno 20 edifici con tetti, porte, finestre e camini; corti, fontana voxel, stendardi, carri, casse, barili e mercato con bancarelle.
- Albero bianco nella corte sommitale e almeno 10 alberi distribuiti fra città e pendici, con tronchi e chiome costruiti a blocchi.
- Almeno 12 personaggi voxel riconoscibili con teste, arti, occhi e accessori: guardie, mercanti, viandanti e abitanti. Crea piccole scene presso il portone, il mercato e la corte, con personaggi proporzionati agli edifici.
- Inquadratura ortografica a tre quarti leggermente dall'alto: base, montagna e torre interamente visibili, con margine attorno alla composizione. Sfondo neutro e luce diurna calda, ombre morbide e dettagli leggibili.

## Requisiti tecnici e consegna
- Compatibilità Blender 4.2 LTS; singolo file .py eseguibile nel Text Editor, senza dipendenze o asset esterni. Pulisci la scena iniziale e organizza gli oggetti in collezioni.
- Funzioni riutilizzabili, seed deterministico e parametri iniziali per scala, densità voxel, dettagli, qualità e percorso di output.
- Riutilizza mesh e materiali, raggruppa la geometria ripetuta ed evita un oggetto per ogni voxel o blocchi interni invisibili. Nessuno z-fighting o oggetto accidentalmente sospeso.
- Configura via script camera, luci e Cycles con denoising e campioni configurabili, senza richiedere una GPU specifica. Render PNG finale 3840×2160, antialiasing e qualità alta.
- Salva automaticamente `diorama_minas_tirith.blend` e `diorama_minas_tirith.png` in una cartella creata dallo script. Se il progetto non è ancora salvato, usa una cartella nella home dell'utente. Stampa i percorsi assoluti al termine.
- Restituisci tutto lo script in un solo blocco di codice, senza pseudocodice, segnaposto o parti omesse, seguito da istruzioni essenziali per eseguirlo.
