# QA — natale.html

## Esito: non superato

La pagina non si avvia: lo script usa `THREE` senza importarlo. Anche risolvendo questo blocco iniziale, la scena e numerose funzioni richieste risultano incomplete o errate. Il file contiene segnaposto espliciti, nonostante la consegna richieda un'applicazione completa.

## Ambito e verifiche

- Confronto statico di `natale.html` con `../prompt-diorama-natale-js.md`.
- Esecuzione mirata del blocco JavaScript in Node.js: `ReferenceError: THREE is not defined`; rilevate zero dichiarazioni `import`.
- Verifica della firma di `InstancedMesh` nel [codice Three.js 0.165.0](https://unpkg.com/three@0.165.0/src/objects/InstancedMesh.js).
- **Non eseguiti:** test in browser reale, WebGL, touchscreen, accessibilità, resa visiva, ascolto audio, prestazioni e download PNG. I problemi successivi al blocco iniziale sono ricavati dal codice, non da un'esecuzione completa della pagina.

## Difetti principali

### 1. Avvio bloccato: moduli non importati — bloccante

**Riferimenti:** `natale.html:23-30`, `natale.html:50-63`, `natale.html:255`.

**Riproduzione:** aprire la pagina: il primo accesso a `new THREE.Clock()` avviene prima di `init()`.

**Atteso:** importazione e inizializzazione di Three.js e OrbitControls; visualizzazione della scena.

**Effettivo:** `THREE` non è definito. L'import map associa i nomi agli URL, ma non importa automaticamente i moduli. Inoltre `OrbitControls` va importato esplicitamente dal modulo addon: non è una proprietà del namespace `THREE` nella versione ES module indicata. Nessun messaggio di errore viene mostrato nell'interfaccia.

**Indicazione:** usare `import * as THREE from 'three'` e importare `OrbitControls` dal relativo addon, istanziandolo direttamente; gestire gli errori di caricamento.

### 2. Geometria della base istanziata senza capacità — alta

**Riferimenti:** `natale.html:87-123`.

`new THREE.InstancedMesh(...)` riceve solo geometria e materiale: manca il terzo argomento, il numero di istanze. Nella versione indicata ciò comporta un buffer delle matrici di lunghezza zero e un conteggio non valido: le successive `setMatrixAt` non costruiscono una base renderizzabile. Il numero effettivamente usato non viene assegnato a `mesh.count`.

**Atteso:** allocare una capacità sufficiente, scrivere le matrici e impostare il numero effettivo delle istanze. Da verificare in browser dopo aver corretto gli import.

### 3. Diorama incompleto e disposizione geometrica incoerente — alta

**Riferimenti:** `natale.html:87-123`, `natale.html:126-227`, `natale.html:236-239`.

- Le terrazze calcolate aumentano di raggio **e** altezza insieme: quelle più alte sono le più larghe, anziché formare una cittadella che si restringe verso l'alto. Sono piani sottili, non una base quadrata spessa con terra, roccia e neve; mancano roccia centrale, rampe, mura, portone, sentiero e molti dettagli architettonici.
- L'altezza degli chalet è casuale tra 0 e quasi 350 unità, indipendentemente dalle terrazze: possono risultare sospesi o fuori inquadratura. Ogni chalet è solo una colonna di quattro cubi, senza gli elementi richiesti. Gli abeti sono anch'essi colonne, non alberi articolati.
- Mancano i personaggi, le quattro bancarelle, il laghetto, i pattinatori, gli alberi spogli e le scene narrative. Slitta, renna e pupazzo sono rappresentati ciascuno da un solo cubo; non ci sono due renne complete. Il codice delle bancarelle è un segnaposto.
- La camera è prospettica, non ortografica, e non viene adattata alle dimensioni effettive della scena per garantire che base e torre siano interamente visibili.
- `VOXEL_RESOLUTION` modifica la dimensione dei cicli della base, ma `BoxGeometry` resta di lato 1: non realizza il dimezzamento della dimensione dei blocchi a parità di dimensioni fisiche.

### 4. Interazioni e rotazione automatica non implementate — alta

**Riferimenti:** `natale.html:323-351`, `natale.html:362-365`.

I clic su abeti, regalo e slitta stampano solo messaggi in console: non cambiano il ritmo delle luci, non aprono un coperchio e non animano renne o sonagli. L'albero natalizio è chiamato `ChristmasTree`, ma il gestore verifica `FirTree`, quindi non ha neppure un ramo dedicato. Mancano evidenziazione e schede informative. Il pulsante di rotazione automatica scrive solo in console.

La posizione del raycaster viene aggiornata solo su `mousemove`, non dal punto del clic: il primo clic e l'uso touch possono usare coordinate obsolete. Non è inoltre implementata la distinzione tra clic e trascinamento della camera.

### 5. Audio richiesto assente — alta

**Riferimenti:** `natale.html:379-415`.

Il pulsante crea o riprende un `AudioContext`, ma `startMusicAndEffects` contiene solo commenti e un log: non genera musica né effetti. Mancano motivo di otto battute, sintesi degli strumenti e dei suoni, sequencer con look-ahead, controlli di volume generale/musica/effetti e gestione della ripresa. L'attivazione del contesto dopo un gesto è prevista, ma non equivale a un'implementazione audio funzionante.

### 6. Esportazione PNG non affidabile — alta

**Riferimenti:** `natale.html:418-447`.

La funzione ridimensiona il renderer ma chiama `toDataURL()` **senza eseguire un nuovo `renderer.render(scene, camera)`** alla risoluzione richiesta. Il PNG potrebbe quindi risultare vuoto o non contenere il rendering atteso. Non aggiorna l'aspetto della camera per 3840×2160; inoltre `controls.reset()` cambia la vista prima della cattura e vengono ripristinate solo alcune proprietà, non l'intero stato della camera e dei controlli. Non c'è `try/finally` per garantire il ripristino in caso di errore.

**Atteso:** renderizzare realmente a 3840×2160 con camera coerente e ripristinare integralmente dimensioni, pixel ratio, camera e controlli anche in caso di errore. Da verificare con un'immagine scaricata dopo la correzione del blocco di avvio.

### 7. Animazioni, pausa e preferenza di movimento ridotto — media

**Riferimenti:** `natale.html:17-21`, `natale.html:289-319`, `natale.html:366-369`.

Pattinatori, pool di neve e movimento delle renne sono segnaposto; l'unica animazione effettiva descritta è la rotazione dell'albero. `prefers-reduced-motion` agisce solo sul CSS e non disattiva l'animazione JavaScript; il selettore `data-action="animate"` non corrisponde al pulsante `pause-animation`. In pausa viene saltato anche `controls.update()`, necessario allo smorzamento dei controlli, anziché fermare soltanto le animazioni della scena.

### 8. Ottimizzazione e gestione errori insufficienti — media

**Riferimenti:** `natale.html:81-84`, `natale.html:126-185`, `natale.html:230-255`, `natale.html:453-454`.

Molti cubi creano nuove geometrie e materiali anziché riutilizzarli; l'uso di `InstancedMesh` è limitato alla base e attualmente difettoso. La qualità configurabile modifica solo il pixel ratio tra due valori; mancano parametri effettivi per dettaglio, animazione e audio. Non sono gestiti errori del renderer o delle dipendenze, né sono presenti istruzioni per server HTTP e accesso CDN. I costi effettivi e il numero di draw call non sono stati misurati.

## Elementi presenti

- Import map con versione `0.165.0` coerente per Three.js e addon, anche se gli import mancano.
- Seed deterministico e generatore pseudo-casuale.
- Struttura HTML con titolo, legenda e pulsanti richiesti; listener di resize previsto.
- Una luce ambientale e una direzionale, quindi nessuna proliferazione di luci dinamiche nel codice attuale.

La presenza di questi elementi non implica che le funzionalità siano operative: lo script si interrompe prima dell'inizializzazione.

## Priorità e regressione consigliata

1. Correggere import, inizializzazione e capacità delle istanze; verificare in browser e console che la scena si avvii.
2. Realizzare e inquadrare la città, collocando edifici e personaggi sulle superfici corrette; completare contenuti e dettagli richiesti.
3. Implementare interazioni, animazioni, accessibilità dei controlli e rispetto della preferenza di movimento ridotto; verificare mouse e touch.
4. Implementare e provare audio e PNG reale, controllando dimensioni del file e ripristino dello stato.
5. Misurare prestazioni e draw call, verificare resize, errori CDN/WebGL e fornire istruzioni di avvio locale.
