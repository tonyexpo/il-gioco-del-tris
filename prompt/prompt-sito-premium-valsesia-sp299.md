# Prompt di sviluppo — Valsesia / SP299

> Prompt autonomo da consegnare a un modello di test. Le immagini sono già selezionate: usa gli URL pubblici indicati direttamente nell’HTML, senza scaricare i file nel progetto.

---

## Ruolo e risultato richiesto

Agisci come un senior creative developer e art director specializzato in siti immersivi di fascia alta.

Sviluppa una **prima anteprima completa e funzionante di un sito premium dedicato alla Valsesia**, nell’Alto Piemonte. Il riferimento qualitativo sono le grandi pagine prodotto Apple: scorrimento lungo, regia precisa, immagini importanti, composizioni che cambiano mentre si scorre, elementi che si intrecciano e tipografia molto curata. Crea un’identità originale legata al territorio.

**L’idea centrale è la SP299: una strada continua che unisce il sito e accompagna il visitatore dalla bassa valle fino ad Alagna Valsesia.** Deve diventare il filo conduttore visivo e narrativo: come una corda che attraversa le scene, compare davanti a un elemento, passa dietro una fotografia e riemerge nel capitolo successivo.

Non fermarti a una proposta o a uno scheletro. Realizza subito l’anteprima, scegliendo autonomamente i dettagli mancanti.

## Consegna e vincoli tecnici

1. Produci **un unico file chiamato esattamente `valsesia.html`, single page**, con tutti i capitoli nella stessa pagina, CSS in `<style>` e JavaScript in `<script>`. Non creare altre pagine HTML, file CSS/JS separati, cartelle di progetto o archivi ZIP. Le schede dei paesi devono essere pannelli o dialoghi nella stessa pagina; la navigazione interna usa ancore.
2. Deve funzionare anche aprendo direttamente `valsesia.html` nel browser, senza server locale, build, npm, framework, backend, account o chiavi API. La connessione Internet serve solo per le risorse remote ammesse, come immagini e font.
3. Usa HTML semantico, CSS moderno, SVG inline e JavaScript vanilla. Non sono necessarie librerie di animazione.
4. **Non scaricare, copiare, incorporare in Base64 o convertire le fotografie.** Non creare una cartella di immagini. Il browser deve caricarle dagli URL esterni indicati tramite `src`, `srcset` solo se fornito, oppure `background-image: url(...)`.
5. Non eseguire scraping o `fetch()` delle immagini. Non usare proxy, servizi di trasformazione, URL temporanei o endpoint con autenticazione.
6. Gli SVG decorativi, il percorso della strada e l’eventuale marchio geometrico possono essere scritti inline nel codice.
7. Sono ammessi i Google Fonts tramite il link fornito, con fallback di sistema. Tutto il resto deve essere contenuto nel file HTML.
8. Lingua dell’interfaccia e dei testi: **italiano**.
9. Se il tuo ambiente consente di creare file, crea `valsesia.html` e rendilo disponibile. Altrimenti restituisci il documento completo in un solo blocco `html`, senza porzioni omesse o segnaposto.

## Identità e direzione artistica

Nome principale: **VALSESIA**.

Possibile firma: **Una strada. Mille mondi.**

Possibile titolo iniziale: **La bellezza prende strada.**

Queste frasi sono proposte utilizzabili, non un obbligo di impaginazione identica. La direzione visiva deve comunicare calma, materia, paesaggio e precisione.

- Verde bosco profondo: `#172720`.
- Avorio caldo: `#F1EFE7`.
- Oro desaturato per strada e dettagli: `#C7B488`.
- Grigi e verdi naturali per i testi secondari.
- Tipografia sans contemporanea per struttura e testi; eventuale serif elegante per poche parole chiave.
- Titoli grandi, spazi ben calibrati, immagini generose, composizioni asimmetriche.
- Alterna scene scure e capitoli chiari. Gestisci bene il passaggio tra queste atmosfere.
- Il carattere premium deve emergere da proporzioni, ritmo e movimento: evita un accumulo di effetti.

Evita l’aspetto di un portale turistico standard, una landing con tre card ripetute, un catalogo di servizi o un template con gradienti viola e icone generiche. Evita caroselli automatici, loader lunghi, cursori personalizzati invasivi, audio automatico e animazioni casuali.

## Geografia e percorso narrativo

Il cuore del racconto è la Valsesia vercellese, con l’accesso dal territorio novarese. Il Biellese può comparire come **deviazione verso un territorio vicino**, non come una località attraversata dalla SP299. Non far passare la strada per Biella o Vercelli città.

L’asse della 299 prosegue a sud verso Novara; per questa anteprima scegli il tratto narrativo **Romagnano Sesia → Alagna Valsesia**. Presenta le seguenti **17 località in questo ordine**:

| Ordine | Località | Gruppo narrativo |
| --- | --- | --- |
| 01 | Romagnano Sesia | Accesso alla valle |
| 02 | Prato Sesia | Accesso alla valle |
| 03 | Grignasco | Accesso alla valle |
| 04 | Serravalle Sesia | Accesso alla valle |
| 05 | Borgosesia | Bassa valle |
| 06 | Quarona | Verso Varallo |
| 07 | Varallo | Arte e patrimonio |
| 08 | Vocca | Il fiume e il paesaggio |
| 09 | Balmuccia | Il fiume e il paesaggio |
| 10 | Scopa | I piccoli centri |
| 11 | Scopello | La montagna si apre |
| 12 | Pila | I piccoli centri |
| 13 | Piode | I piccoli centri |
| 14 | Campertogno | I piccoli centri |
| 15 | Mollia | I piccoli centri |
| 16 | Riva Valdobbia | Verso Alagna |
| 17 | Alagna Valsesia | Arrivo ai piedi del Monte Rosa |

Sono località lungo il corridoio della strada e i suoi accessi: non affermare che la carreggiata attraversi ogni centro storico. Riva Valdobbia è una località del comune di Alagna Valsesia dal 2019: non presentarla come comune autonomo attuale.

La linea sul sito è **una rappresentazione narrativa e schematica**, non una mappa stradale esatta. Non inventare chilometraggi ufficiali, distanze, tempi di viaggio o coordinate delle singole tappe. I numeri 01–17 indicano l’ordine nel racconto, non i chilometri.

La SP299 arriva ad Alagna: non disegnarla come una strada asfaltata che prosegue fino ai ghiacciai o alla Capanna Regina Margherita. Dopo l’arrivo, puoi trasformare il filo grafico in una linea dello sguardo verso le montagne.

## Struttura della pagina e regia

Realizza un’esperienza lunga, indicativamente **14–20 altezze di viewport desktop**, senza riempitivi. Alterna capitoli editoriali, sequenze sticky e fotografie. Non assegnare necessariamente una sezione enorme a ciascuno dei 17 luoghi: tutte le tappe devono però essere rappresentate e raggiungibili.

### 1. Apertura cinematografica

- Una fotografia reale della valle o di Alagna a pieno schermo, con ritaglio accurato.
- Navigazione essenziale: marchio Valsesia, “Il viaggio”, “Da vivere”, “Esplora la 299”.
- Titolo forte, poche righe introduttive e invito chiaro a scorrere.
- Il primo tratto della strada deve già essere visibile o comparire molto presto.
- Animazione iniziale breve e misurata. Parallasse leggera durante lo scorrimento.
- L’immagine di apertura può anticipare il punto di arrivo; la sequenza delle tappe successive deve rimanere coerente.

### 2. La strada come invito

- Spiega in poche frasi la scelta della 299 come filo del viaggio.
- Introduci la relazione tra strada, acqua e paesi.
- La strada attraversa lo spazio tra i testi e comincia a segnare le prime tappe.
- Usa un’impaginazione editoriale, diversa dalla hero.

### 3. Le porte della valle

- Racconta l’ingresso da Romagnano, poi Prato Sesia, Grignasco, Serravalle, Borgosesia e Quarona.
- Preferisci una sequenza di nomi, tappe o segni tipografici alla ripetizione di sei card identiche.
- Non attribuire a questi paesi una fotografia che rappresenta Varallo: in assenza di immagini specifiche, usa tipografia, percorso e una transizione fotografica esplicitamente dedicata alla tappa successiva.

### 4. Varallo, l’arte cambia il paesaggio

- Una scena importante sul Sacro Monte e sulla dimensione artistica della città.
- Fotografia ampia, titolo sovrapposto e breve testo laterale.
- Puoi citare il Sacro Monte come patrimonio UNESCO; non aggiungere numeri storici non necessari.
- La strada deve passare dietro una parte della composizione e tornare visibile oltre la fotografia.

### 5. La Sesia, il ritmo del viaggio

- Collega Vocca, Balmuccia e Scopa attraverso il tema del fiume.
- Crea una sequenza sticky di circa due viewport: il paesaggio cambia scala lentamente e il testo entra per fasi.
- La strada accompagna la scena; un eventuale secondo segno, più sottile, può suggerire il fiume senza confondere le due linee.
- La foto fornita per questo tema mostra attività fluviali: descrivila coerentemente. Non presentarla come un’immagine di una specifica località non documentata.

### 6. I borghi e il tempo lento

- Scopello e la vista dall’Alpe di Mera; poi Pila, Piode, Campertogno e Mollia.
- Componi fotografie di formati diversi con titoli, nomi delle tappe e brevi didascalie.
- L’immagine di Mera rappresenta il panorama dall’alpe, non il centro di Scopello.
- L’immagine di Campertogno è associata alla fiera del bestiame: usala per il paese e le tradizioni, con una didascalia coerente.
- Mollia può essere raccontata attraverso il Mulino Fucina e il rapporto tra acqua e lavoro.
- Questa sequenza deve avere un ritmo distinto dalla scena sticky precedente.

### 7. Riva Valdobbia e Alagna, radici alpine

- Introduci la cultura Walser con un testo essenziale e una fotografia pertinente delle case.
- Una composizione con immagine e titolo che si sovrappongono parzialmente.
- Marca chiaramente Alagna come arrivo della strada.

### 8. Il finale sul Monte Rosa

- Una seconda scena sticky di circa due viewport, con un’immagine d’alta quota e un lento movimento di scala.
- Titolo possibile: “La strada finisce. La meraviglia no.”
- Distingui l’arrivo ad Alagna dall’orizzonte alpinistico oltre il paese.
- Se mostri una quota, **4.554 m è la quota della Capanna Regina Margherita sulla Punta Gnifetti**: non è la quota del paese e non è la massima altezza del massiccio.
- Non presentare l’ascesa al rifugio come una passeggiata generica o un’estensione in auto della 299.

### 9. Da vedere a da vivere

- Una galleria orizzontale o una composizione equivalente per camminare, vivere il fiume, incontrare l’arte e scoprire le tradizioni.
- Le esperienze rimandano a fonti reali fornite sotto.
- La galleria deve funzionare con trascinamento o swipe, tastiera e pulsanti precedenti/successivi; può usare lo scroll orizzontale nativo senza implementare il trascinamento del mouse.
- Eventuale breve nota sul Biellese come deviazione laterale. Non servono immagini generiche per riempirla.

### 10. Chiusura

- Una frase memorabile, invito a esplorare tutte le tappe e link “Come arrivare”.
- Footer essenziale con fonti e crediti immagini consultabili.
- Indica discretamente che si tratta di un concept indipendente; non simulare un sito ufficiale dell’ente turistico.

## La strada: requisito distintivo obbligatorio

La strada non deve essere una semplice linea verticale laterale o un elemento che appare soltanto nel menu.

Implementa un tracciato SVG curvo che percorra una parte significativa della pagina:

- Curve ampie e raccordi morbidi, coordinate a fotografie e blocchi di testo.
- Traccia di fondo discreta e tratto di avanzamento che si disegna in relazione allo scroll, ad esempio con `stroke-dasharray` e `stroke-dashoffset`.
- Un piccolo indicatore segue il punto raggiunto sul percorso.
- Nomi e marker delle tappe distribuiti nei capitoli appropriati; l’indice completo deve restare disponibile in ogni momento.
- Il percorso deve apparire davanti ad alcuni dettagli e dietro alcune immagini: realizza una gerarchia di livelli deliberata, con almeno due intrecci chiaramente visibili su desktop.
- Conserva la continuità tra i capitoli. Se il percorso è diviso in più SVG per gestire i livelli, allinea le estremità e sincronizza l’avanzamento.
- Non coprire i testi, i controlli o i volti eventualmente presenti nelle fotografie.
- Su mobile puoi semplificare il tracciato e spostarlo verso un margine, mantenendo la leggibilità e il senso del viaggio.

La strada è schematica, ma l’ordine dei luoghi deve rimanere corretto.

## Interazioni obbligatorie

- Menu “Esplora la 299” che apre un pannello o un dialogo con tutte le 17 località.
- Clic su una località: mostra una breve scheda pertinente e un comando per raggiungere il tratto corrispondente della pagina. Se più località condividono un capitolo, evidenzia quella scelta o portala in vista.
- Un piccolo indicatore persistente mostra il capitolo corrente e l’avanzamento nel viaggio.
- I link di navigazione interna devono raggiungere sezioni esistenti senza nascondere i titoli sotto l’header.
- I collegamenti esterni devono avere URL reali. Nessun pulsante finto, `href="#"` generico o azione “in arrivo”.
- Il dialogo deve chiudersi con il pulsante dedicato e con Esc, gestire il focus e restituirlo al comando di apertura. Preferisci `<dialog>` nativo.

## Risorse fotografiche da usare direttamente

Gli URL seguenti sono stati ricavati dai collegamenti immagine delle pagine del portale turistico **Visit Valsesia Vercelli** il **23 ottobre 2026**. Usa gli indirizzi esatti, senza dedurre varianti dai nomi dei file e senza sostituire le immagini con paesaggi alpini generici.

La disponibilità futura e l’accettazione dell’hotlink dipendono dal sito che le ospita. Il codice deve prevedere un fallback sobrio senza tentare di aggirare eventuali blocchi. Un URL pubblico non equivale a una licenza di riutilizzo: mantieni i crediti e considera queste risorse riferimenti per un’anteprima di test.

Il seguente manifest può essere copiato nel JavaScript del sito oppure tradotto direttamente in tag `<img>`:

```json
[
  {
    "id": "alagna_drone",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/12/ALAGNA-VALSESIA-DRONE-2-1.jpg",
    "uso": "Hero o grande apertura sul paesaggio di Alagna",
    "alt": "Veduta aerea di Alagna Valsesia nel paesaggio montano",
    "fonte": "https://visitvalsesiavercelli.it/vivi/arte-e-cultura/alagna/"
  },
  {
    "id": "alagna_estate",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/12/alagna_038-scaled.jpg",
    "uso": "Scorcio estivo di Alagna o capitolo sul camminare",
    "alt": "Scorcio estivo su Alagna Valsesia",
    "fonte": "https://visitvalsesiavercelli.it/vivi/arte-e-cultura/alagna/"
  },
  {
    "id": "alagna_centro",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/12/ALAGNA-VALSESIA-6.jpg",
    "uso": "Arrivo ad Alagna e atmosfera del centro abitato",
    "alt": "Il centro di Alagna Valsesia",
    "fonte": "https://visitvalsesiavercelli.it/vivi/arte-e-cultura/alagna/"
  },
  {
    "id": "case_walser",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/11/A9A00119.jpg",
    "uso": "Cultura e architettura Walser",
    "alt": "Case Walser ad Alagna Valsesia",
    "fonte": "https://visitvalsesiavercelli.it/organizza/informazioni/come-arrivare/"
  },
  {
    "id": "verso_monte_rosa",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/11/trekking-1.jpg",
    "uso": "Passaggio visivo dal paese alla montagna o esperienza trekking",
    "alt": "Paesaggio verso il Monte Rosa da Alagna",
    "fonte": "https://visitvalsesiavercelli.it/organizza/informazioni/come-arrivare/"
  },
  {
    "id": "capanna_margherita",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/09/Rifugio_Capanna_Regina_Margherita.jpeg",
    "uso": "Finale d’alta quota: non raffigura il paese di Alagna",
    "alt": "La Capanna Regina Margherita nel paesaggio d’alta quota del Monte Rosa",
    "fonte": "https://visitvalsesiavercelli.it/vivi/arte-e-cultura/alagna/"
  },
  {
    "id": "varallo",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/08/varallo.jpg",
    "uso": "Introduzione a Varallo o transizione dalla bassa valle alla città d’arte",
    "alt": "Veduta di Varallo nel paesaggio della Valsesia",
    "fonte": "https://visitvalsesiavercelli.it/vivi/arte-e-cultura/varallo/"
  },
  {
    "id": "sacro_monte",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/09/Sacro-Monte-Varallo.jpg",
    "uso": "Scena principale dedicata al Sacro Monte",
    "alt": "Il Sacro Monte di Varallo",
    "fonte": "https://visitvalsesiavercelli.it/vivi/arte-e-cultura/varallo/"
  },
  {
    "id": "sesia_attivita",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/08/Valsesia-attivita-fluviali-immagine-copertina-scaled.jpg",
    "uso": "Scena sul fiume e sulle attività fluviali",
    "alt": "Attività fluviali sul fiume Sesia",
    "fonte": "https://visitvalsesiavercelli.it/scopri/itinerari/alla-scoperta-della-val-grande-2/"
  },
  {
    "id": "mera_panorama",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/08/Mera2-scaled.jpg",
    "uso": "Panorama dall’Alpe di Mera, nel capitolo dedicato a Scopello",
    "alt": "Panorama dall’Alpe di Mera",
    "fonte": "https://visitvalsesiavercelli.it/scopri/itinerari/alla-scoperta-della-val-grande-2/"
  },
  {
    "id": "campertogno_tradizioni",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/08/Campertogno-fiera-del-bestiame-1-scaled.jpg",
    "uso": "Campertogno e le tradizioni locali",
    "alt": "Campertogno, immagine associata alla fiera del bestiame",
    "fonte": "https://visitvalsesiavercelli.it/scopri/itinerari/alla-scoperta-della-val-grande-2/"
  },
  {
    "id": "mollia_mulino",
    "url": "https://visitvalsesiavercelli.it/wp-content/uploads/2022/08/Mulino-fucina-mollia.jpg",
    "uso": "Mollia, acqua, lavoro e memoria del territorio",
    "alt": "Il Mulino Fucina di Mollia",
    "fonte": "https://visitvalsesiavercelli.it/scopri/itinerari/alla-scoperta-della-val-grande-2/"
  }
]
```

Usa almeno **8 immagini differenti** di questo manifest. Non è necessario usarle tutte. Puoi riutilizzare una fotografia in un richiamo secondario, ma evita che tutte le scene importanti mostrino la stessa immagine.

Esempio del comportamento richiesto:

```html
<img
  src="https://visitvalsesiavercelli.it/wp-content/uploads/2022/12/ALAGNA-VALSESIA-DRONE-2-1.jpg"
  alt="Veduta aerea di Alagna Valsesia nel paesaggio montano"
  fetchpriority="high"
  decoding="async"
>
```

La fotografia della hero non deve avere `loading="lazy"`. Le fotografie successive possono usare `loading="lazy"`. Riserva lo spazio con contenitori dimensionati o `aspect-ratio`, così il caricamento non sposta il percorso.

### Font esterni facoltativi

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Italiana&display=swap" rel="stylesheet">
```

Usa `DM Sans, Arial, sans-serif` per il testo e, se utile, `Italiana, Georgia, serif` per gli accenti editoriali. Non rendere il caricamento dei font indispensabile per leggere o navigare la pagina.

## Fonti e destinazioni dei collegamenti

Usa queste pagine per gli approfondimenti; non metterle nel `src` delle immagini:

| Destinazione | URL |
| --- | --- |
| Portale turistico del territorio | https://visitvalsesiavercelli.it/ |
| Varallo | https://visitvalsesiavercelli.it/vivi/arte-e-cultura/varallo/ |
| Alagna Valsesia | https://visitvalsesiavercelli.it/vivi/arte-e-cultura/alagna/ |
| Itinerario della Val Grande | https://visitvalsesiavercelli.it/scopri/itinerari/alla-scoperta-della-val-grande-2/ |
| Percorso ciclopedonale Balmuccia–Alagna | https://visitvalsesiavercelli.it/vivi/outdoor-e-natura/balmuccia-alagna-valsesia/ |
| Come arrivare | https://visitvalsesiavercelli.it/organizza/informazioni/come-arrivare/ |

Per i link esterni aperti in una nuova scheda usa `target="_blank"` e `rel="noopener noreferrer"`. Non inventare prenotazioni, disponibilità, prezzi, orari, servizi aggiornati o recensioni.

## Qualità delle animazioni e prestazioni

- I movimenti principali devono essere **legati alla posizione dello scroll**, reversibili quando si torna indietro, e non soltanto avviati da timer.
- Usa `IntersectionObserver` per ingressi semplici e `requestAnimationFrame` per gli aggiornamenti continui.
- Calcola e memorizza geometrie e lunghezze del percorso all’avvio e quando il layout cambia; non ricalcolare l’intera pagina a ogni evento di scroll.
- Ricalcola le misure dopo il caricamento dei font, delle immagini rilevanti e al ridimensionamento. Puoi usare `ResizeObserver`.
- Favorisci `transform` e `opacity`. Evita filtri molto pesanti e `will-change` su ogni elemento.
- Le sezioni sticky devono funzionare senza bloccare la rotella o intercettare il gesto di scorrimento principale.
- Non introdurre salti quando una scena entra o esce dallo stato sticky.
- Evita lavori eccessivi fuori schermo: le animazioni dei capitoli non visibili non devono continuare inutilmente.
- Un’immagine remota non disponibile deve lasciare una composizione leggibile, con uno sfondo coerente e una didascalia testuale; niente icone rotte, loop di retry o sostituti casuali.

## Responsive e accessibilità

- Verifica desktop ampio, notebook, tablet e smartphone; considera almeno le larghezze 1440, 1024, 768 e 390 px.
- Niente overflow orizzontale della pagina. L’eventuale galleria può scorrere orizzontalmente nel proprio contenitore.
- Usa `clamp()` per la tipografia e `svh` dove aiuta sui dispositivi mobili.
- I testi restano leggibili sulle fotografie, anche dopo i cambi di scala: aggiungi overlay misurati e contrasto sufficiente.
- Non affidare informazioni essenziali al passaggio del mouse.
- Un solo `h1`, titoli in ordine logico, etichette accessibili per i pulsanti con sole icone e stato corrente comprensibile anche senza colore.
- Elementi decorativi e percorso SVG con `aria-hidden="true"` quando non aggiungono informazioni accessibili. Le località devono esistere anche come testo HTML o controlli accessibili.
- Supporta `prefers-reduced-motion: reduce`: riduci parallasse e zoom, rendi stabili le scene e lascia tutti i contenuti visibili. Il percorso e la navigazione devono rimanere comprensibili.
- In assenza di JavaScript i contenuti editoriali e i link principali devono essere comunque leggibili: non nascondere preventivamente tutto via CSS.

## Testi e tono

Scrivi testi originali, brevi e specifici. Evita slogan ripetuti e grandi quantità di testo generico. Il protagonista è il luogo, non il codice o il fatto che il sito sia stato generato.

Non inserire nel corpo dell’esperienza spiegazioni come “animazione SVG con requestAnimationFrame” o “scorri per vedere il parallax”. Le istruzioni al visitatore devono essere naturali: “Inizia il viaggio”, “Esplora la 299”, “Scopri la tappa”.

Nel footer puoi inserire un piccolo pannello “Fonti e crediti”, con i link delle pagine sorgente e una nota sul carattere schematico del percorso.

## Criteri di accettazione prima della consegna

- [ ] La consegna è un solo file `valsesia.html`: sito single page completo, con CSS e JavaScript incorporati e nessun altro file locale richiesto.
- [ ] La strada continua è il segno distintivo e si disegna con lo scorrimento.
- [ ] Sono visibili intrecci tra percorso, immagini e altri elementi.
- [ ] Tutte le 17 località sono presenti, nell’ordine corretto e selezionabili nell’indice.
- [ ] Almeno due sequenze hanno una regia sticky o un comportamento di scorrimento equivalente realmente implementato.
- [ ] Sono usate almeno 8 fotografie diverse dai relativi URL esatti.
- [ ] Nessuna fotografia è stata scaricata nel progetto o trasformata in Base64.
- [ ] Il percorso termina ad Alagna; la montagna è un orizzonte successivo.
- [ ] Dialogo, galleria, ancore e collegamenti funzionano.
- [ ] La versione mobile è progettata e non semplicemente rimpicciolita.
- [ ] La preferenza di movimento ridotto è rispettata e il contenuto resta accessibile.
- [ ] Non ci sono errori JavaScript evidenti, immagini con percorsi locali inesistenti o elementi interattivi finti.

**Ora realizza e consegna esclusivamente `valsesia.html`, un unico sito single page completo. Dai priorità alla qualità visiva e alla continuità del viaggio, mantenendo tutti i requisiti funzionali.**
