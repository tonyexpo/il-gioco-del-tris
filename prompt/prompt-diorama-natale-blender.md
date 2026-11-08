# Diorama voxel di Natale — Blender

Sviluppa uno script Python per Blender (bpy) che generi proceduralmente un diorama natalizio ispirato alla struttura di Minas Tirith: una cittadina fortificata con sette livelli/anelli concentrici su terrazze ascendenti, una grande roccia centrale e una cittadella con torre in cima. Reinterpreta la città come un villaggio natalizio alpino, riconoscibile nella disposizione a livelli ma originale negli edifici e nelle decorazioni.

## Stile e composizione
- Stile Minecraft/voxel, non fotorealistico: geometrie a blocchi, superfici piatte, materiali semplici e colori leggibili. Niente texture o asset esterni.
- Usa una risoluzione voxel doppia rispetto a una costruzione minimale: blocchi grandi la metà a parità di dimensioni fisiche, dettagli più fini senza perdere l'estetica cubica. La risoluzione geometrica è distinta da quella del render.
- Diorama su una base quadrata spessa con sezioni visibili di terra, roccia e neve, bordi curati e piccoli ghiaccioli. La città occupa il centro; un sentiero dal primo piano conduce al portone e prosegue con rampe fra i livelli.
- Inquadratura ortografica a tre quarti leggermente dall'alto, con tutta la base e la torre visibili, senza tagli. Distribuisci i dettagli anche sui livelli posteriori, mantenendo visibili quelli principali.

## Elementi obbligatori
- Mura merlate innevate, porte ad arco costruite con blocchi, scalinate, ponticelli e almeno 12 chalet con tetti a gradoni, camini, davanzali innevati e finestre illuminate.
- Una torre dell'orologio in cima e una grande stella luminosa sopra la cittadella.
- Almeno 10 abeti voxel di altezze diverse con neve sui rami, due alberi spogli e un grande albero di Natale nella piazza principale, decorato con palline cubiche, ghirlande luminose, stella e regali alla base.
- Almeno 12 personaggi voxel chiaramente riconoscibili: Babbo Natale, elfi, bambini con sciarpe e cappelli, venditore di cioccolata, pattinatori e abitanti che trasportano regali. Personaggi fatti di blocchi, con teste, arti, occhi e accessori leggibili, proporzionati agli edifici.
- Slitta con sacco di regali e due renne voxel con corna, pupazzi di neve con carote e cappelli, pacchetti con nastri, cassette postali, lampioni, bastoncini di zucchero e ghirlande sulle porte.
- Mercatino con almeno 4 bancarelle diverse: dolci, giocattoli, decorazioni e bevande calde. Un laghetto ghiacciato con pattinatori occupa uno spazio laterale sulla base.
- Piccole scene narrative: elfi che caricano la slitta, bambini che costruiscono un pupazzo, famiglia al mercatino. Aggiungi impronte squadrate nella neve e una catasta di legna.
- Palette dominante bianco neve, verde abete, rosso e oro; atmosfera al crepuscolo con cielo blu e luci calde. Neve a strati geometrici leggibili; pochi fiocchi cubici sospesi, senza oscurare la scena.

## Requisiti tecnici e consegna
- Compatibilità Blender 4.2 LTS; un unico file .py eseguibile dal Text Editor di Blender, senza dipendenze, download o passaggi manuali.
- Pulisci la scena iniziale e organizza gli oggetti in collezioni. Usa funzioni riutilizzabili, un seed deterministico e parametri iniziali per dimensioni, densità voxel, quantità di dettagli, percorso di output e qualità del render.
- Riduci l'overhead: riutilizza mesh/materiali e raggruppa la geometria ripetuta; evita un oggetto distinto per ciascuno dei milioni di voxel. Costruisci solo la geometria necessaria, senza riempire di cubi invisibili gli edifici.
- Non basta assemblare cubi casuali: devono essere leggibili i sette livelli, il percorso, la cittadella e le scene con personaggi. Evita oggetti sospesi accidentalmente, compenetrazioni vistose e z-fighting.
- Configura camera, materiali, luci e motore di rendering via script. Render finale PNG 3840×2160, ombre morbide, antialiasing e qualità alta; usa Cycles con denoising e campioni configurabili, senza richiedere una GPU specifica.
- Salva automaticamente `diorama_natale.blend` e `diorama_natale.png` in una cartella di output creata dallo script. Se il progetto non è ancora salvato, usa una cartella nella home dell'utente; stampa i percorsi assoluti al termine.
- Restituisci lo script completo in un solo blocco di codice, senza parti omesse, pseudocodice o segnaposto, seguito da istruzioni essenziali per eseguirlo.
