# 🎯 Progetto Tic Tac Toe WPF - Requisiti di Sviluppo

Questo documento elenca tutti i requisiti per lo sviluppo del gioco del Tris (Tic Tac Toe) utilizzando la tecnologia WPF e seguendo le best practice architetturali.

## ✅ Requisiti Espliciti (Core Features)
1. **Obiettivo:** Sviluppare un gioco demo di Tic Tac Toe.
2. **Tecnologia Target:** Utilizzare esclusivamente WPF per l'interfaccia grafica.
3. **Target Framework:** Deve essere compatibile con .NET 10 o .NET 9.
4. **Interfaccia Utente (UI):**
    *   Griglia composta da 9 pulsanti cliccabili.
    *   Un pulsante di "Reset" posizionato in basso.
5. **Logica Gioco:**
    *   Il giocatore umano è sempre rappresentato dalla 'X'.
    *   L'intelligenza artificiale (PC) è sempre rappresentata dalla 'O'.
6. **Avvio Gioco:** Il gioco deve iniziare automaticamente o attivarsi alla pressione del primo pulsante della griglia.
7. **Intelligenza Artificiale (AI):** La logica di turno per il PC ('O') deve essere implementata in modo casuale (random).
8. **Architettura:** L'implementazione deve seguire rigorosamente lo schema MVVM (Model-View-ViewModel).
9. **Ambito di Lavoro:** Lo sviluppo deve coprire l'intero progetto, inclusi i file Solution e CSPROJ necessari per la compilazione WPF.
10. **Vincolo Operativo:** Tutte le modifiche devono avvenire all'interno della cartella assegnata: `C:\Users\Antonio Esposito\Desktop\toctactoe2`.

## 🧠 Requisiti Impliciti (Senior Developer Best Practices)
1. **Qualità del Codice:** Il codice deve essere estremamente pulito, ben commentato e aderire alle best practice standard di C#/.NET.
2. **Logica Core:** La logica fondamentale di gioco (verifica di vittoria o pareggio) deve risiedere nel Model o ViewModel per mantenere la separazione delle responsabilità.
3. **Interoperabilità View-ViewModel:** L'interazione tra la View e il ViewModel deve avvenire esclusivamente tramite meccanismi di Data Binding WPF, evitando manipolazioni dirette del DOM/UI dal codice logico.

---
**Priorità Immediata:** Implementare l'architettura MVVM e creare i componenti base (Model, ViewModel, View) per gestire lo stato del gioco e la griglia.