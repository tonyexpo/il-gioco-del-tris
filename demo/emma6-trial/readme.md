# Milano alla prova dei modelli locali

Materiali della demo per YouTube del 25 ottobre 2026: prova di scrittura storica su Milano, eseguita con modelli locali tramite LM Studio, e correzione dell'assistente principale nel ruolo di docente multidisciplinare.

## Da dove iniziare

Aprire **[comparativa.html](comparativa.html)** in un browser. Contiene risultati, differenze fra le prove, esempi degli errori e collegamenti agli elaborati e alle review.

Le review HTML mostrano il testo originale e le correzioni affiancati, con il voto in fondo. I file Markdown conservano le risposte dei modelli o le trascrizioni fornite dall'utente. Tenere i file nella stessa cartella per mantenere funzionanti i collegamenti. La review di Spark usa JavaScript incorporato per disporre testo e commenti; le altre review sono statiche. Non occorrono gli script di generazione.

## Obiettivo e procedura

La traccia comune era **«Milano da Mediolanum alla metropoli industriale: continuità e trasformazioni»**, in italiano, da 1.200 a 1.600 parole. Richiedeva:

1. Origini preromane, romanizzazione, ruolo imperiale e cristianesimo tardoantico.
2. Comune, signorie, dominazioni straniere, riforme settecentesche e fase napoleonica.
3. Economia e industria nell'Ottocento e Novecento: infrastrutture, credito, imprese, lavoro, migrazioni e trasformazioni postindustriali.
4. Distinzione fra fatti, interpretazioni e incertezze; sintesi critica e 4–6 riferimenti identificabili.

Spark, MiniCPM5 e Gemma hanno ricevuto **lo stesso messaggio**, in subagenti separati avviati **in serie**, con un solo tentativo completato per modello e senza richiesta di revisione. La consegna vietava strumenti, ricerche, creazione di file e deleghe. Era un'istruzione al modello, non una rimozione tecnica degli strumenti dal contesto del subagente: MiniCPM5 ha comunque prodotto un file aggiuntivo.

L'assistente principale, GPT-6 Astra, ha corretto le risposte dopo la consegna, consultando fonti esterne. I testi originali sono conservati separatamente dalle correzioni.

**Prompt integrali, sessioni, tentativi ed eccezioni:** [registro della prova](milano-da-mediolanum-alla-metropoli-industriale-prompt.md).

## Risultati

| Modello / prova | Condizioni | Voto |
|---|---|---:|
| Gemma 4 12B IT · Q4_K_XL | Traccia comune, subagente LM Studio | 5,5/10 |
| Spark X2.5 1.7B | Traccia comune, subagente LM Studio | 2/10 |
| MiniCPM5-2B | Traccia comune, subagente LM Studio | 1,5/10 |
| Emma-6 — tentativo di tesina | Tre risposte riportate da chat esterna, dopo proposta di prompt ridotto | 1/10 |
| **«milano» — Emma-6 BF16** | Export di chat diretta: un saluto e nove domande sul tema | 2/10 |

Gemma offre la sintesi più chiara e plausibile della prova comune, ma resta insufficiente per omissioni, genericità e riferimenti non confermati. Spark e MiniCPM5 presentano gravi errori storici. Emma-6 non svolge la tesina nella conversazione riportata e mostra difficoltà anche nelle domande brevi.

### Griglia delle tesine

- Accuratezza storica: **4 punti**.
- Copertura ed equilibrio cronologico: **2 punti**.
- Analisi economica e collegamenti: **2 punti**.
- Chiarezza: **1 punto**.
- Fonti e loro uso: **1 punto**.

Per Emma-6 questa griglia è stata applicata dal docente ai testi manualmente riportati; i pesi non erano inclusi nel prompt ridotto proposto all'utente.

### Caso Emma-6

I tentativi tramite subagente sono falliti con un errore di gestione del contesto, anche con una domanda minima. L'utente ha indicato un limite di 4K token: è compatibile con il problema, ma la causa non è stata accertata tramite log.

Sono stati poi raccolti materiali distinti:

- **Tentativo manuale di tesina:** tre risposte incollate dall'utente. Era stato proposto un prompt da 600–800 parole; il primo messaggio effettivamente inviato non è stato confermato integralmente.
- **Prova diagnostica diretta via API:** senza messaggio di sistema né strumenti nella richiesta, Emma-6 BF16 ha risposto «Milano, capitale della Lombardia» alla richiesta di descriverne brevemente la storia. Esito e parametri sono nel registro; nessun voto assegnato.
- **Voce «milano»:** export fornito dall'utente da LM Studio 0.4.26+4, conservato in [milano-domande-dirette-emma-6.md](milano-domande-dirette-emma-6.md). Review di nove quesiti, escluso il saluto, con griglia specifica: correttezza (4), pertinenza (3), chiarezza e contesto (2), gestione dell'incertezza (1). Questa griglia è stata definita dopo la prova.

I voti delle due prove manuali di Emma-6 **non misurano un miglioramento**: riguardano compiti e criteri diversi. Gli errori tecnici dei subagenti non sono stati conteggiati come insufficienze accademiche.

## File conservati

- `comparativa.html`: pagina riepilogativa, inclusa la sezione `#milano`.
- `milano-da-mediolanum-alla-metropoli-industriale-prompt.md`: protocollo e registro completo.
- `milano-da-mediolanum-alla-metropoli-industriale-[modello].md`: risposte originali o trascrizione della prova manuale.
- `milano-da-mediolanum-alla-metropoli-industriale-[modello]-review.html`: correzioni e valutazioni.
- `milano-domande-dirette-emma-6.md` e relativo `-review.html`: export dell'utente e review della voce «milano».
- `Milan_da_Mediolanum_alla_metropoli_industriale.md`: **artefatto aggiuntivo prodotto da MiniCPM5**, conservato per tracciabilità. Differisce dalla risposta finale in alcuni passaggi e nella bibliografia; la valutazione usa la risposta finale con nome standard, non questo file.

Gli script di generazione e i due file della prova diagnostica breve sono stati rimossi alla chiusura. Il contenuto utile del test diagnostico è stato riportato nel registro. Gli elaborati, le fonti dell'utente e le review restano disponibili.

## Limiti di interpretazione

- È una demo qualitativa su un argomento, non un benchmark statistico né una classifica generale dei modelli.
- Le prove condividono il prompt dove indicato, ma non sono stati controllati tutti i parametri di esecuzione. Campionamento, configurazioni complete, tempi e consumi non sono stati rilevati sistematicamente.
- Dimensione e quantizzazione riportate sono quelle dei nomi dei modelli o dei metadati disponibili. Il risultato di Gemma non isola l'effetto della sola dimensione.
- La chat diretta contiene turni successivi nello stesso contesto: non sono domande eseguite indipendentemente. L'export non rende visibili tutte le impostazioni.
- Le fonti della correzione e il livello delle verifiche sono indicati nelle review. Un riferimento **non confermato** non è automaticamente un'opera di cui sia dimostrata l'inesistenza.
- I voti sono giudizi dell'assistente sui prodotti osservati, non valutazioni ufficiali universitarie.

LFM2.5 non è stato avviato: l'utente ha corretto la scelta prima della prova.

---

**Redazione e valutazioni:** GPT-6 Astra (OpenAI), assistente AI in OpenCode, nel ruolo di docente multidisciplinare per questa demo.  
**Data:** 25 ottobre 2026.
