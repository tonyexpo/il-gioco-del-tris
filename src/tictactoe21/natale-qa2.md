# QA aggiornata — natale.html

## Esito: non superato

La versione attuale corregge alcuni problemi della prima QA, in particolare gli import di Three.js e la capacità dell'`InstancedMesh`. Restano però gravi difetti nella geometria e mancano gran parte dei contenuti, delle interazioni e dell'audio richiesti. La cattura PNG è stata migliorata, ma non ripristina integralmente la vista.

**Nome del file:** per questa consegna `natale.html` è corretto; non viene considerata una difformità la mancata presenza di `index.html`.

## Metodo e limiti

- Revisione statica della versione attuale di `natale.html`, confrontata con `../prompt-diorama-natale-js.md` e con `natale-qa.md`.
- Calcolo in Node.js delle altezze degli chalet, delle dimensioni delle terrazze e della memoria nominale del buffer delle istanze usando i parametri e il seed attuali.
- **Non eseguiti:** test in browser o WebGL, verifica visiva, test su dispositivi mobili, acquisizione effettiva del PNG, ascolto audio e misurazione delle prestazioni. L'avvio completo e l'assenza di errori in console non sono quindi verificati.

## Cambiamenti rispetto alla prima QA

| Punto precedente | Stato nella versione attuale |
| --- | --- |
| Import mancanti | **Corretto nel codice:** import espliciti di `THREE` e `OrbitControls`, con import map alla stessa versione (`natale.html:21-28, 48-51, 281`). Non è stata provata l'esecuzione in browser. |
| Capacità delle istanze assente | **Corretto nel codice:** viene passata una capacità e aggiornato `mesh.count` (`natale.html:95-97, 149`). Restano problemi di dimensionamento e geometria. |
| Camera prospettica | **Corretto parzialmente:** ora è ortografica (`natale.html:262-265`), ma il frustum non si adatta al rapporto del viewport e l'inquadratura non è calcolata sulla scena. |
| PNG senza render | **Corretto parzialmente:** ora viene chiamato `renderer.render` e c'è un `finally` (`natale.html:432-459`); restano problemi di vista, proporzioni e ripristino. |
| Base e voxel | **Corretto parzialmente:** esiste una base istanziata e il cubo viene scalato a 0,5 (`natale.html:83-86, 100-112`). Le dimensioni fisiche e le proporzioni richieste non sono comunque rispettate. |
| Mercatino | **Non risolto:** sono stati aggiunti quattro gruppi, ma ciascuno contiene un solo cubo identico e non rappresenta una bancarella distinta (`natale.html:240-246`). |

## Difetti aperti

### 1. Terrazze invertite, sospese e con scala errata — alta

**Riferimenti:** `natale.html:95-149`.

**Atteso:** sette livelli collegati che si restringono salendo, sopra una base spessa di 50 unità circa, con grande roccia centrale e torre sulla cittadella.

**Effettivo:**

- `radiusFactor` cresce con il livello: le terrazze più alte sono più larghe. Con i parametri attuali la semiestensione calcolata passa da circa 9 a 12,5 unità, non si riduce.
- Le superfici sono strati di cubi separati verticalmente di circa 3,57 unità, senza roccia o muri che riempiano gli intervalli. La colonna centrale termina sotto la terrazza superiore anziché formare una torre sulla cittadella.
- La base calcolata va circa da -12,75 a +12,75 unità, inclusa la semidimensione dei cubi: misura circa 25,5 unità, non le 50 dichiarate. Il ciclo verticale crea un solo strato di spessore 0,5, non due unità.
- Il controllo circolare confronta coordinate di griglia con un raggio in unità diverse; con i parametri attuali non ritaglia gli angoli delle terrazze.

**Indicazione:** definire una sola conversione tra coordinate voxel e mondo, ricavare i raggi decrescenti e collegare fisicamente i livelli; verificare dimensioni e inquadratura con bounding box.

### 2. Chalet, oggetti e mercatino non sono costruiti né posizionati correttamente — alta

**Riferimenti:** `natale.html:160-251`.

Gli chalet usano `BASE_SIZE * (random() * NUM_LEVELS)` come altezza, senza alcun legame con la terrazza. Con il seed attuale le posizioni centrali calcolate vanno da circa **36,89 a 350,39** unità, mentre le terrazze sono tra circa 3,57 e 25: sono quindi sospesi o lontani dalla scena. Ogni chalet è composto da quattro cubi; con cubi di lato 0,5 e distanza verticale di 1 rimangono anche spazi vuoti. Mancano camini, finestre e tetti richiesti.

I dieci abeti sono colonne di cubi distanziati; il grande albero non è articolato e manca delle decorazioni previste. Le quattro «bancarelle» sono cubi uguali, non dolci, giocattoli, decorazioni e bevande. Sentiero, slitta, renna e pupazzo sono singoli cubi o gruppi minimi. Mancano, fra l'altro, personaggi, seconda renna, laghetto, pattinatori, alberi spogli e scene narrative.

### 3. Interazioni e rotazione automatica sono segnaposto — alta

**Riferimenti:** `natale.html:331-369`, `natale.html:379-380`.

**Riproduzione prevista:** dopo l'avvio, cliccare albero, regalo o slitta oppure premere «Rotazione Auto».

**Atteso:** cambiare il ritmo delle luci, aprire il regalo mostrando un giocattolo, animare le renne con sonagli o avviare la rotazione, rispettivamente.

**Effettivo dal codice:** i rami gestiti stampano solo messaggi. L'albero di Natale usa il nome `ChristmasTree` sui figli, mentre il gestore cerca `FirTree`; il gruppo stesso non ha nome, quindi nemmeno il ciclo di animazione che cerca un gruppo `ChristmasTree` lo trova. Mancano schede ed evidenziazione. La posizione di puntamento si aggiorna solo su `mousemove`, non sull'evento di clic; non c'è controllo del trascinamento, con possibili interazioni indesiderate e problemi su touch.

### 4. Audio assente — alta

**Riferimenti:** `natale.html:397-422`.

Il pulsante inizializza o sospende l'`AudioContext`, ma `startMusicAndEffects` contiene solo commenti e un messaggio in console. Non sono presenti musica, effetti sonori, sequencer, scheduling, controlli di volume separati o gestione effettiva delle riprese. La dicitura in console che sostiene che siano schedulati non corrisponde al codice.

### 5. Cattura PNG: vista e stato non preservati — alta

**Riferimenti:** `natale.html:425-459`.

Il renderer viene ora effettivamente chiamato dopo il ridimensionamento, ma prima della cattura `controls.reset()` sostituisce la vista scelta dall'utente. Nel `finally` si ripristina la posizione, non l'intero stato di camera e controlli: per esempio zoom ortografico e target possono restare quelli iniziali. Inoltre il frustum non viene adattato al rapporto 16:9 dell'export, con possibili proporzioni errate.

**Atteso:** catturare la vista corrente in 3840×2160 con proiezione coerente e ripristinare integralmente dimensioni, pixel ratio, camera e controlli anche in caso di errore. La validità e le dimensioni del file non sono state provate.

### 6. Resize, zoom e movimento ridotto — media

**Riferimenti:** `natale.html:16-19`, `natale.html:262-265`, `natale.html:281-287`, `natale.html:307-325`, `natale.html:382-386`.

- Il frustum ortografico è quadrato e resta tale al resize: `camera.aspect` non modifica la proiezione ortografica, quindi su viewport non quadrate la scena viene deformata. Va adattato `left/right` o `top/bottom` al rapporto larghezza/altezza.
- Per la camera ortografica i limiti di zoom pertinenti sono `minZoom` e `maxZoom`; `minDistance` e `maxDistance` non impongono il limite di zoom richiesto.
- La preferenza `prefers-reduced-motion` nasconde un pulsante via CSS ma non controlla l'animazione JavaScript; il selettore `data-action="animate"` non corrisponde a `pause-animation`.
- In pausa `controls.update()` è chiamato una volta al clic, ma non nei frame successivi: il damping non viene aggiornato continuamente. Pattinatori e neve animata restano non implementati.

### 7. Risorse, console e gestione degli errori — media

**Riferimenti:** `natale.html:84-86`, `natale.html:95-97`, `natale.html:105-109`, `natale.html:128-130`, `natale.html:170-208`, `natale.html:267-270`, `natale.html:463-464`.

- `maxInstances` alloca 1.000.000 di matrici, circa **61 MiB** per il solo array `Float32Array`, prima delle altre risorse. Il costruttore di Three.js inizializza inoltre le matrici allocate: una capacità calcolata sulle istanze realmente necessarie ridurrebbe lavoro e memoria. Non sono state misurate prestazioni reali.
- Nella generazione delle istanze sono creati ripetutamente `Matrix4` e `Object3D`; molti altri cubi ricevono geometrie e materiali nuovi. Riutilizzare risorse e istanziare o unire le geometrie ripetute.
- `MeshBasicMaterial` riceve `emissive` (`natale.html:208`), proprietà non supportata dal materiale: può generare un avviso in console. La stella non usa un materiale emissivo come richiesto.
- Mancano messaggi comprensibili per errori del renderer o caricamento dei moduli, istruzioni per un server HTTP statico e avviso della necessità di accesso alla CDN.

## Priorità di correzione e regressione

1. Correggere scala, base, terrazze, torre e posizionamento degli oggetti; completare i contenuti minimi richiesti.
2. Implementare davvero interazioni, rotazione e animazioni; verificare mouse, touch, trascinamento e movimento ridotto.
3. Implementare sintesi audio, controlli e sequencer; verificare attivazione, sospensione e ripresa.
4. Correggere proiezione e ripristino dell'export; scaricare e ispezionare un PNG di 3840×2160 dopo aver modificato vista e zoom.
5. Verificare avvio e console in browser, resize e CDN, e misurare tempi di avvio, memoria e draw call.
