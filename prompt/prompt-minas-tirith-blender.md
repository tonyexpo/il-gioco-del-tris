# Minas Tirith — Blender (alta risoluzione)

Sviluppa uno script Python per Blender (bpy) che disegni proceduralmente la città di Minas Tirith in stile Minecraft/voxel: non fotorealistico, blocchi/cubi, colori semplici, nessuna texture esterna.

## Scena
- Struttura a sette livelli/anelli concentrici su terrazze ascendenti, mura bianche merlate, sperone roccioso centrale, cittadella e torre in cima, mantenendo proporzioni e silhouette riconoscibili della città originale.
- Alta risoluzione voxel: cubi dimezzati rispetto a una costruzione minimale (il doppio del dettaglio), a parità di dimensioni fisiche complessive della città.
- Inquadratura ortografica a tre quarti leggermente dall'alto, città interamente visibile con margine attorno, sfondo neutro, luce diurna calda, ombre morbide.

## Requisiti tecnici e consegna
- Compatibilità Blender 4.2 LTS; singolo file .py eseguibile nel Text Editor, senza dipendenze o asset esterni. Pulisci la scena iniziale.
- Funzioni riutilizzabili, seed deterministico, riutilizzo di mesh e materiali; evita un oggetto per ogni voxel e blocchi interni invisibili. Nessuno z-fighting.
- Configura via script camera, luci e motore di render (Cycles o EEVEE, con denoising/campioni configurabili, senza richiedere una GPU specifica). Render PNG finale alta risoluzione (3840×2160).
- Salva automaticamente il file .blend e il render .png in una cartella creata dallo script; se il progetto non è ancora salvato usa una cartella nella home dell'utente. Stampa i percorsi assoluti al termine.
- Restituisci tutto lo script in un solo blocco di codice, senza pseudocodice, segnaposto o parti omesse, seguito da istruzioni essenziali per eseguirlo.
