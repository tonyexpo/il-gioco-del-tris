# Minas Tirith — Blender (voxel)

Sviluppa uno script Python per Blender (bpy) che disegni la città di Minas Tirith (Il Signore degli Anelli) in stile Minecraft/voxel: blocchi/cubi, colori semplici, nessuna texture esterna, non fotorealistico. Interpreta liberamente aspetto e dettagli della città — livelli, mura, edifici, cittadella, eventuali abitanti o elementi di contorno — purché il risultato resti riconoscibile come Minas Tirith e non un semplice cumulo di blocchi.

## Limiti e contesto
- Alta risoluzione voxel: usa cubi piccoli abbastanza da rendere leggibili i dettagli della città, non un blocco informe o una forma troppo astratta.
- Compatibilità Blender 4.2 LTS; singolo file .py eseguibile dal Text Editor, senza dipendenze o asset esterni. Pulisci la scena iniziale.
- Riutilizza mesh e materiali invece di creare un oggetto per ogni singolo voxel; evita migliaia di oggetti separati e blocchi interamente nascosti alla vista.
- Configura via script camera, luci e motore di render (Cycles o EEVEE, senza richiedere una GPU specifica); inquadratura che mostri la città per intero.
- Salva automaticamente il file .blend e un render PNG finale in alta risoluzione in una cartella creata dallo script; se il progetto non è ancora salvato usa una cartella nella home dell'utente. Stampa i percorsi assoluti al termine.
- Restituisci tutto lo script in un solo blocco di codice, senza pseudocodice, segnaposto o parti omesse, seguito da istruzioni essenziali per eseguirlo.
