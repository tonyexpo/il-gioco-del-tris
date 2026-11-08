# Diorama voxel di Halloween — Blender

Sviluppa uno script Python per Blender (bpy) che generi proceduralmente un diorama di Halloween ispirato alla struttura di Minas Tirith: una cittadina fortificata con sette livelli/anelli concentrici su terrazze ascendenti, una grande roccia centrale e una cittadella con torre in cima. Reinterpreta la città come un borgo stregato, riconoscibile nella disposizione a livelli ma originale negli edifici e nelle decorazioni.

## Stile e composizione
- Stile Minecraft/voxel, non fotorealistico: geometrie a blocchi, superfici piatte, materiali semplici e colori leggibili. Niente texture o asset esterni.
- Usa una risoluzione voxel doppia rispetto a una costruzione minimale: blocchi grandi la metà a parità di dimensioni fisiche, dettagli più fini senza perdere l'estetica cubica. La risoluzione geometrica è distinta da quella del render.
- Diorama su una base quadrata spessa con sezioni visibili di terra e roccia, bordi curati e qualche radice sporgente. La città occupa il centro; un sentiero dal primo piano conduce al portone e prosegue con rampe fra i livelli.
- Inquadratura ortografica a tre quarti leggermente dall'alto, con tutta la base e la torre visibili, senza tagli. Distribuisci i dettagli anche sui livelli posteriori, mantenendo visibili quelli principali.

## Elementi obbligatori
- Mura merlate, porte ad arco costruite con blocchi, scalinate, ponticelli e almeno 12 casette con tetti viola scuro, camini e finestre illuminate.
- Una torre stregata in cima con orologio, tetto appuntito a gradoni e luna cubica sullo sfondo.
- Almeno 10 alberi voxel: querce con fogliame autunnale arancio/rosso, alberi secchi con rami spigolosi e un grande albero contorto presso la cittadella.
- Almeno 12 personaggi voxel chiaramente riconoscibili: strega con cappello e scopa, scheletro, vampiro con mantello, fantasma, guardiano e bambini in costume con secchielli per dolci. Personaggi fatti di blocchi, con teste, arti, occhi e accessori leggibili, proporzionati agli edifici.
- Zucche di varie dimensioni, almeno 8 jack-o'-lantern con occhi e bocca luminosi, calderone con pozione verde, banchetto di dolci, lapidi in un piccolo cimitero, cancellata, ragnatele stilizzate, pipistrelli cubici sospesi, funghi e foglie cadute.
- Piccole scene narrative: bambini al portone di una casa, strega al calderone, fantasma fra le lapidi. Nessun elemento splatter.
- Palette dominante arancio, viola, nero e verde acido; illuminazione serale blu-viola con luci calde nelle finestre e nelle zucche. La scena deve restare nitida: niente nebbia densa che nasconda il lavoro.

## Requisiti tecnici e consegna
- Compatibilità Blender 4.2 LTS; un unico file .py eseguibile dal Text Editor di Blender, senza dipendenze, download o passaggi manuali.
- Pulisci la scena iniziale e organizza gli oggetti in collezioni. Usa funzioni riutilizzabili, un seed deterministico e parametri iniziali per dimensioni, densità voxel, quantità di dettagli, percorso di output e qualità del render.
- Riduci l'overhead: riutilizza mesh/materiali e raggruppa la geometria ripetuta; evita un oggetto distinto per ciascuno dei milioni di voxel. Costruisci solo la geometria necessaria, senza riempire di cubi invisibili gli edifici.
- Non basta assemblare cubi casuali: devono essere leggibili i sette livelli, il percorso, la cittadella e le scene con personaggi. Evita oggetti sospesi accidentalmente, compenetrazioni vistose e z-fighting.
- Configura camera, materiali, luci e motore di rendering via script. Render finale PNG 3840×2160, ombre morbide, antialiasing e qualità alta; usa Cycles con denoising e campioni configurabili, senza richiedere una GPU specifica.
- Salva automaticamente `diorama_halloween.blend` e `diorama_halloween.png` in una cartella di output creata dallo script. Se il progetto non è ancora salvato, usa una cartella nella home dell'utente; stampa i percorsi assoluti al termine.
- Restituisci lo script completo in un solo blocco di codice, senza parti omesse, pseudocodice o segnaposto, seguito da istruzioni essenziali per eseguirlo.
