# QA avversariale — Valsesia / SP299

**Autore della QA:** GPT-6.1 Terra (OpenAI), agente OpenCode.  
**Data:** 31 ottobre 2026  
**File esaminato:** `C:\temp\tictactoe20\valsesia.html`  
**Prompt:** `C:\temp\prompt-sito-premium-valsesia-sp299.md`  
**SHA-256 del file esaminato:** `F7CC073177D29D6250D9526A519E7E6A0DCA6FA9F666938226713EEE3141AE4D`

## Esito: non conforme, non rilasciabile

La consegna è un singolo HTML con CSS e JavaScript incorporati, ma non realizza le funzioni e la regia centrali richieste: la strada non è visibile, l'indice non si apre, le destinazioni delle località sono errate, mancano le scene sticky e la galleria delle esperienze non è completa. Sono inoltre presenti un link senza destinazione, un segnaposto visibile e immagini non conformi al manifest. L'aspetto risulta definito nel codice come una sequenza di contenitori e card semplici, lontana dalla direzione immersiva richiesta; la qualità visiva effettiva non è stata valutata mediante screenshot.

## Metodo e limiti

- Confronto puntuale del sorgente con requisiti, manifest fotografico e collegamenti del prompt.
- Esecuzione dello script con Node.js e DOM simulato per osservare indicatore, listener e aggiornamento del percorso.
- Apertura del file locale con Chrome headless e acquisizione del DOM risultante: confermato che l'indicatore inizializza a `chapter2` e che gli attributi del percorso vengono applicati a un `div`.
- Non sono stati eseguiti collaudi visivi, da tastiera o con screen reader in un browser interattivo, né test effettivi ai quattro viewport richiesti, verifica dell'udibilità o controllo della disponibilità remota delle immagini. Le valutazioni responsive e di accessibilità sotto derivano dal codice. Nessuna modifica è stata apportata a `valsesia.html`.

## Difetti prioritari

### P0 — La strada distintiva non viene disegnata

**Riferimenti:** `valsesia.html:30-31`, `61-62`, `180-196`.

Il solo `path` si trova in `<defs>` e non viene richiamato da alcun elemento SVG visibile. `progress-path` è invece un `div`: JavaScript gli assegna `stroke-dasharray` e `stroke-dashoffset`, attributi che non disegnano una strada. Chrome headless conferma che tali attributi finiscono sul `div`. Mancano anche indicatore che segue il tracciato, continuità tra capitoli, marker e intrecci davanti/dietro le fotografie.

**Atteso:** percorso SVG effettivamente renderizzato e continuo su una parte significativa della pagina, avanzamento legato allo scroll, indicatore sul percorso e almeno due intrecci visibili desktop, senza coprire contenuti.

### P0 — Indice delle 17 località inaccessibile e destinazioni errate

**Riferimenti:** `valsesia.html:53`, `136-176`, `207-217`.

Il link «Esplora la 299» punta a `#esplora`, ID inesistente. Nessun comando invoca `showModal()` o rende visibile il pannello: il `<dialog>` resta chiuso e il pannello alternativo ha `display:none`. Anche il pulsante «Chiudi» non ha un gestore. Il listener Escape non sostituisce apertura, chiusura tramite pulsante e gestione del focus.

Anche se il dialogo fosse aperto, l'elenco contiene solo 16 link selezionabili: **Pila è presente soltanto nella frase riepilogativa**. Numerosi link portano al capitolo sbagliato: per esempio Varallo a `#chapter7` invece di `#chapter4`; Alagna a `#chapter6` invece di `#chapter7`; Scopello ha testo «Capitolo 6» ma punta a `#chapter1`. Le selezioni non aprono schede pertinenti né evidenziano la tappa. Vocca, Balmuccia e Scopa non hanno una trattazione editoriale nel capitolo del fiume.

**Atteso:** indice sempre raggiungibile, 17 tappe nell'ordine richiesto, ciascuna selezionabile con scheda e link alla sezione corretta, con evidenziazione della località. Il dialogo deve aprirsi e chiudersi anche da tastiera e restituire il focus.

### P1 — Mancano le due scene sticky e la regia legata allo scroll

**Riferimenti:** `valsesia.html:27-29`, `86-91`, `113-125`, `198-205`.

I commenti dichiarano scene sticky, ma `.sticky-gallery` imposta soltanto un contenitore flex con overflow orizzontale: non esistono `position: sticky`, durata di circa due viewport, cambi di scala progressivi o entrate graduali del testo. Lo script imposta solo `overflowX`. Non si rilevano parallasse della hero, `IntersectionObserver`, gestione delle geometrie dopo il caricamento o animazione continua coordinata allo scroll con `requestAnimationFrame`.

**Atteso:** due sequenze realmente sticky o equivalenti per Sesia e Monte Rosa, reversibili con lo scroll e senza intercettare lo scorrimento principale; movimento ridotto supportato.

### P1 — Galleria delle esperienze priva di contenuti, fonti e controlli

**Riferimenti:** `valsesia.html:120-125`.

La sezione contiene due immagini senza titoli di esperienza, descrizioni o link alle fonti. Mancano le quattro categorie richieste — camminare, fiume, arte e tradizioni — e i pulsanti precedente/successivo. L'overflow nativo è previsto nel CSS, ma dal sorgente non risulta una gestione esplicita della navigazione da tastiera del contenitore; non è stato eseguito un test interattivo.

**Atteso:** esperienze riconoscibili e collegate alle fonti reali indicate, scorribili con swipe, tastiera e pulsanti.

### P1 — Navigazione e chiusura non funzionanti

**Riferimenti:** `valsesia.html:36-42`, `53`, `127-132`.

Non esiste la navigazione richiesta «Il viaggio», «Da vivere», «Esplora la 299». Il link «Come arrivare» punta a `#come-arrivare`, che non esiste, anziché alla fonte esterna prevista. La chiusura mostra letteralmente «A frase memorabile e l'invito a esplorare tutte le tappe», un segnaposto. Mancano footer, fonti, crediti fotografici, avviso di concept indipendente e nota sul carattere schematico del percorso.

**Atteso:** ancore funzionanti, link reale per arrivare, testo finale completo e footer con fonti e crediti consultabili.

### P1 — Fotografie non conformi e contesto errato

**Riferimenti:** `valsesia.html:50`, `79-82`, `89-90`, `106-109`, `115-117`, `123-124`.

Il file usa 8 URL di immagini distinti, ma solo **7 coincidono** con quelli del manifest. Per `trekking-1.jpg` usa `/2022/12/`, mentre il prompt prescrive `/2022/11/`: non raggiunge quindi il minimo di 8 URL esatti, indipendentemente dall'eventuale disponibilità del link diverso. La foto `Mera2-scaled.jpg` compare due volte con alt «Scorcio estivo su Alagna Valsesia», anziché identificare il panorama dall'Alpe di Mera; non è inserita nella scena di Scopello. Mancano le immagini previste per Campertogno e Mollia nel relativo capitolo. Le immagini non hanno fallback esplicito in caso di errore e la maggior parte non riserva dimensioni; solo quelle nelle gallerie ricevono una regola di larghezza.

**Atteso:** almeno 8 fotografie diverse con URL esatti, testi alternativi e contesto coerenti, dimensioni riservate e fallback leggibile senza immagini rotte. Verificare separatamente l'effettiva disponibilità degli URL consentiti.

### P1 — Indicatore di avanzamento falso e non persistente

**Riferimenti:** `valsesia.html:44`, `219-249`.

`setIndicator()` incrementa una variabile da `chapter1` a `chapter2` una sola volta all'avvio; non è collegata allo scroll. Nelle prove simulate e nel DOM Chrome iniziale compare `chapter2` anche all'inizio. Dopo uno scroll simulato il valore resta invariato. Non indica una percentuale né è definito come persistente.

**Atteso:** capitolo realmente corrente e avanzamento comprensibile, aggiornati anche risalendo la pagina e disponibili durante il viaggio.

### P2 — Responsive, accessibilità e robustezza insufficienti

**Riferimenti:** `valsesia.html:3-32`, `44-50`, `61`, `136-176`.

- Mancano meta viewport, media query, `clamp()` e trattamento `prefers-reduced-motion`; le immagini principali non hanno regole generali di adattamento. `#path-svg` è largo `100vw` dentro un contenitore con padding e overflow nascosto. Non si può certificare l'assenza di ritagli o overflow ai viewport richiesti senza prova visiva.
- Il percorso decorativo non ha `aria-hidden`; l'indicatore iniziale espone una stringa tecnica in inglese. La navigazione e le schede non sono utilizzabili perché non implementate.
- Il pannello alternativo apre `<section>` ma termina con `</dialog>` invece di `</section>`. Chrome ripara il DOM, includendo anche lo script nel pannello nascosto; il markup resta invalido e fragile.
- Non è disponibile una versione senza JavaScript dell'indice delle tappe: il dialogo chiuso e il pannello nascosto non forniscono navigazione utilizzabile. I capitoli editoriali principali, invece, restano nel markup.

**Atteso:** markup valido, responsive verificato su 1440/1024/768/390 px, controlli e stati accessibili, alternativa leggibile senza JS e rispetto del movimento ridotto.

## Matrice sintetica di accettazione

| Requisito | Esito |
|---|---|
| File unico, CSS e JS incorporati | Presente; assenza di dipendenze locali rilevata nel sorgente |
| Strada continua visibile, progressiva e intrecciata | Fallito |
| 17 località selezionabili con schede e destinazioni corrette | Fallito |
| Due scene sticky o equivalenti | Fallito |
| Almeno 8 immagini diverse con URL esatti del manifest | Fallito: 7 URL distinti esatti |
| Dialogo, ancore e link esterni | Fallito |
| Galleria esperienze con tastiera e pulsanti | Fallito |
| Indicatore persistente e corretto | Fallito |
| Geografia: arrivo strada ad Alagna e quota Capanna | Alagna indicata come arrivo; quota della Capanna indicata nell'alt, senza confonderla esplicitamente con il paese. La strada grafica non è realizzata, quindi il suo termine non è verificabile. |
| Versioni mobile, contrasto, focus e screen reader | Non collaudati in modo interattivo; criticità statiche sopra |
| Risorse remote, resa delle immagini e fallback | Non verificati in rete; fallback esplicito non rilevato |

## Priorità di correzione e nuova QA

1. Implementare un vero percorso SVG continuo e visibile, con progresso e intrecci; realizzare le due sequenze sticky e i relativi contenuti.
2. Ricostruire indice, schede, ancore e dialogo con mappatura corretta delle 17 località, focus gestito e alternativa senza JS.
3. Correggere URL, contesto e alt delle immagini; aggiungere fonti, crediti, link reali, chiusura e galleria delle esperienze funzionante.
4. Rifinire semantica, responsive e reduced motion; validare HTML e verificare immagini mancanti e funzionamento da file locale.
5. Ripetere il collaudo in browser reale a 1440, 1024, 768 e 390 px, con tastiera, screen reader, movimento ridotto, JavaScript disattivato e risorse remote bloccate; verificare avanti/indietro nello scroll, tutte le località e il ritorno del focus.
