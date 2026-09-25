# Protocollo QA aggiornato — 2026-09-25

- Completare il report di ogni modello prima di procedere al successivo. Massimo quattro task paralleli sullo stesso modello.
- Timeout 1–3 minuti per comando o sessione; interrompere e registrare fallimento se scade.
- Dare cinque opportunità effettive di sviluppo/scrittura/test per ciascun task idoneo, anche dopo un successo apparente. Eccezioni: test multimodale fermato alla prima indisponibilità comprovata della modalità, oppure impedimento genuinamente insormontabile documentato (es. file non supportato senza fallback). Ogni tentativo va numerato e verificato; non confondere risultati QA con output del modello.
- Per i modelli piccoli distinguere qualità del codice, compilazione/esecuzione e capacità agentica di gestire i file. QA può compilare il codice prodotto dal modello, senza scriverlo o correggerlo, annotando chi ha eseguito la build.
- Controllare i file realmente prodotti e conservare le risposte numerate. Gli input comuni restano fuori dagli alberi dei modelli; copy su Milano.
