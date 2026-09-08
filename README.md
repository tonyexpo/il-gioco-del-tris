# Il gioco del Tris — modelli LLM alla prova del codice

Un banco di prova ripetibile per capire quanto un modello linguistico regge davvero su un lavoro di sviluppo reale.

L'idea è semplice: **stesso progetto, stesso prompt, modelli diversi.** Un gioco del tris in WPF/MVVM, scritto da zero dal modello, con il codice conservato esattamente come viene prodotto — senza correzioni, senza ritocchi, senza il "poi l'ho sistemato io" che rende inutile qualsiasi confronto.

Ogni prova è raccontata in un episodio video della **Saga del gioco del Tris**: [guarda la playlist](https://www.youtube.com/@developerreactsita) *(← sostituisci con il link diretto alla playlist)*

## Perché non un benchmark classico

I benchmark misurano risposte su task sintetici. Qui si misura una cosa diversa e più scomoda: se il codice compila, se l'applicazione parte, se la logica di gioco funziona, e quante iterazioni servono per arrivarci. È il tipo di verifica che conta quando devi decidere se un modello locale può stare dentro un flusso di lavoro vero.

## Il metodo

1. Prompt identico per tutti i modelli (vedi [`PROMPT.md`](PROMPT.md))
2. Nessuna correzione manuale al codice generato
3. Massimo N iterazioni di follow-up, sempre le stesse per tutti
4. Il risultato viene committato così com'è, in una cartella per modello — **codice sorgente e binari compilati**, così che nulla venga alterato a posteriori e chiunque possa verificare l'eseguibile che ho effettivamente provato
5. Valutazione su criteri fissi: compila / parte / la logica è corretta / qualità dell'architettura MVVM

## La classifica

| # | Modello | Quantizzazione | Compila | Parte | Logica OK | Iterazioni | Esito | Episodio |
|---|---------|----------------|---------|-------|-----------|------------|-------|----------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

*(da compilare con gli esiti già registrati: Gemma-4 2B, 4B, 12B, Qwen 27B nelle sue quantizzazioni, i modelli di frontiera usati come termine di paragone)*

## Ambiente di prova

Le prove locali girano su hardware consumer, non su una workstation da datacenter: è parte del punto. Configurazione di riferimento:

- GPU: *(da specificare)*
- RAM: *(da specificare)*
- Runtime: *(LM Studio / llama.cpp / altro)*

## Struttura del repository

```
/prompt         il prompt usato, invariato tra le prove
/risultati      una cartella per modello: codice generato as-is + binari compilati
/note           osservazioni per singola prova
```

## Licenza

*(da definire — MIT è la scelta usuale per un progetto dimostrativo)*

---

Progetto di [Antonio Esposito](https://antonioesposito.it) — Head of Software Development & Solution Architect.
