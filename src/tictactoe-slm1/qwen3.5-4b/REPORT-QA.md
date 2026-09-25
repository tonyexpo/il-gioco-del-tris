# Report QA - qwen3.5-4b

Data 2026-09-25; provider LM Studio. Scala 1-10. Alcuni task web/Milano avviati prima della richiesta di sequenzialità e poi fermati; successivamente completato questo modello dopo gli altri. Le sessioni di revisione WPF/copy/XLSX sono rimaste bloccate fino al successivo check 5 minuti (limite auspicato 1-3 min non rispettato: annotate come fallite e annullate). Nessun codice gioco scritto/corretto da QA; codice JS controllato con `node --check`.

| Task | Tentativi | Voto | Evidenze |
|---|---:|---:|---|
| 1 Tris web | 4 | **5/10** | Ha prodotto index.html, style.css, script.js con 9 celle e minimax, reset, grafica a blocchi; sintassi JS passa node --check. Tuttavia l'umano può fare click multipli durante timeout PC; reset non cancella timer pendente e produce mossa PC nella nuova partita; se PC vince richiama getBestMove() dopo mossa, può ottenere -1, quindi `cells[-1].classList` causa eccezione. Feedback 2-4 non ha applicato fix. Codice promettente ma runtime fragile, non dichiarato giocabile. |
| 2 Tris WPF | 2 | **1/10** | Nessun file progetto o codice completo dopo due sessioni, seconda interrotta per stallo; impossibile build QA. |
| 3 Tesina Milano | 3 | **3/10** | Tesina lunga strutturata v1 ma origini false "MILANUM", colonia romana fondata 222 a.C. anziché insediamento celtico Mediolanum preesistente, etimo inventato da Olona; altri dati storici non verificati. Revisioni richieste senza output. Struttura non compensa inattendibilità di contenuto. |
| 4 Tesina Obama | 4 | **2/10** | V1 inventa doppia cittadinanza keniana, dottorato letteratura Harvard e Camera dei rappresentanti; V3 corregge JD ma inventa Harvard Law a Washington DC, senatore statale eletto 2004 e viaggio Obama in Iran 2015. V4 peggiora: afferma che nel 2015 NON era presidente e confonde senatore Illinois con senatore USA 1996. Nessuna tesina interamente corretta; contenuto priorità sulla forma. |
| 5 Copy Milano | 5 | **1/10** | V1 tre copioni con hook e CTA ma molti fatti falsi (sede UE, altezza Duomo 157m, museo Novecento nel Castello, cronologia Visconti/Sforza). V3 inventa autori Brunelleschi/Sangallo/Bernini del Duomo, Navigli UNESCO, Pinacoteca con opera inesistente; ultimo feedback non produce revisione. Durata dei testi insufficiente o falsificata; hooks non compensano perdita fiducia. |
| 6 Traduzione marketing | 3 | **6/10** | V1 integrale mantiene significato e lessico tecnico ROAS, CAC, LTV:CAC, MER, marginal CPA, holdout. Calchi "reallocando", "prospezione", "sopprimere acquirenti", "baseline stagionalità-regolate", espressioni poco idiomatiche; v2 assente, v3 solo frase diagnostica. Buona conservazione concetti, scarsa naturalezza per copy destinato a team senior. |
| 7 Multimodale | 2 | **1/10** | Primo nessuna risposta valida; secondo non dichiara impossibilità ma va in stallo, nessun suono/colore percepito. Nessuna deduzione dai nomi conteggiata. |
| 8 DOCX/PDF | 2 | **1/10** | Nessun Word/PDF valido; file spurio todo__todo_write nel task, secondo tentativo senza artefatti. |
| 9 Excel/CSV | 5 | **4/10** | Non dimostrata lettura XLSX; V2 CSV trova totale 410 e unità 19 ma sbaglia aggregazioni e AOV (unità/ordine). V4 trova totale 410, canali 185/135/90, categorie 180/230, AOV 51,25, Ads 45,12%, ma top Tazza attribuito 5 unità/?70 anziché 9/?90 e alcune colonne AOV per canale erronee; V5 degrada drasticamente totale 470 e categorie/canali. Serve verifica aritmetica esterna. |

**Media: 2,67/10 (24/90).** Qwen produce il codice web più articolato ma non un gioco robusto, né documenti.

## Controlli e provenienza
- `node --check qwen3.5-4b/01-tris-web/script.js`: esito 0; nessun test interattivo browser attestato. Non essendoci sorgenti WPF, nessuna compilazione WPF possibile: non penalizzato per non aver lanciato build ma per assenza codice.
- Testi inline v3/v4/v5 archiviati dall'orchestratore senza correggere contenuto, nella cartella del task. Backup tentativo-1.js presente per web; fix non applicato.
- Dati comuni: ricavi 410, unità 19, Ads 185/Organico 135/Email 90, Casa 180/Tech 230, Tazza 9, AOV 51,25, Ads 45,12%.
- Copy test riferito a Milano come richiesto dall'utente (ambiguità tesina 4).

**Verdetto:** codice JS leggibile e traduzione recuperabile con editing professionale; QA necessaria su race condition, factuality dei testi e conteggi.

## Seconda passata: cinque opportunità
Conteggi finali **[5,5,5,5,5,5,3,5,5]**. Copy e vendite già a cinque. Multimodale terzo tentativo dichiara indisponibilità di audio/immagini: stop corretto; la sua pretesa di aver salvato risposta-multimodale-3.md **non è confermata** dal filesystem. Nuove chiamate web v5 e WPF v3–v5 non hanno riparato i giochi: JavaScript esistente supera node --check (sola sintassi), bug timer/click/getBestMove invariati, cartella WPF priva di progetto compilabile. Obama v5 non consegna tesina autonoma; versioni precedenti false. Milano v4 è file vuoto, v5 (4514 byte) ripete invenzioni molto gravi: attribuisce Milano ai Cenomani anziché agli Insubri, conquista a Gaio Mario nel 100 a.C. anziché 222 a.C., inventa ponte sul Ticino come monumento milanese e bibliografia non verificata. Traduzione v4–v5 nessun miglioramento verificabile; documenti v3–v5 nessun DOCX/PDF.

**Voti finali [5,1,2,2,1,6,1,1,4], media 23/90 = 2,56/10.** Milano scende da 3 a 2 per nuove invenzioni nella revisione; qualità della revisione non è prova di correzione. Conteggi nella vecchia tabella sono storici; questi definitivi. Il QA non ha scritto codice di gioco.
