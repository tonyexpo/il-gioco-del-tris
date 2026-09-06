# Tris — WPF / MVVM

Applicazione desktop Windows con .NET 10, senza pacchetti NuGet esterni.

## Avvio

Prerequisiti: Windows e SDK .NET 10 (oppure Visual Studio con supporto .NET 10 e sviluppo desktop .NET).

```powershell
dotnet build TicTacToe.slnx
dotnet run --project TicTacToe
```

Aprire in alternativa `TicTacToe.slnx` in Visual Studio e impostare TicTacToe come progetto di avvio.

## Uso

- Clicca una delle nove caselle per iniziare: sei sempre **X** e giochi per primo.
- Il PC è **O** e risponde immediatamente scegliendo uniformemente tra le caselle libere: nessuna strategia.
- Le caselle occupate non sono selezionabili. Alla vittoria o al pareggio la griglia viene bloccata.
- Una linea vincente viene evidenziata in verde; il messaggio indica il risultato.
- **Reset**, in basso, azzera la partita in qualsiasi momento senza avviarne automaticamente una nuova.
- Supporto tastiera: Tab per navigare, Spazio/Invio per attivare i pulsanti, Alt+R per il reset.

## Struttura

- **Models/Game**: stato, validazione mosse, scelta casuale del PC, vittoria/pareggio e reset; nessuna dipendenza dalla UI.
- **ViewModels**: celle e stato osservabili tramite INotifyPropertyChanged; comandi di gioco e reset.
- **Commands/RelayCommand**: ICommand con CanExecute e notifiche esplicite.
- **Views/MainWindow**: layout e binding XAML. Il code-behind contiene solo InitializeComponent.

Il turno umano e la risposta PC sono sincroni e atomici rispetto alla UI: nessun timer o operazione pendente da annullare al reset. Random è iniettabile per test riproducibili.

## Verifica automatica

```powershell
dotnet run --project TicTacToe.Tests
```

Runner console senza dipendenze esterne (non un progetto per `dotnet test`): verifica avvio, mosse illegali, vittorie, pareggio, reset, binding/comandi e 5.000 partite riproducibili coprendo tutte le otto linee vincenti. Un errore termina con codice diverso da zero.

## Miglioramenti UX e AI

- Selettore difficoltÃ  disponibile prima della partita e dopo il risultato. Durante il gioco premi Reset per cambiare livello; cambiare livello dopo il risultato prepara una griglia vuota.
- Punteggi di sessione (tutti i livelli): vittorie umane, pareggi e vittorie PC. Reset conserva i punteggi; Azzera punteggi non modifica la partita. Nessuna persistenza alla chiusura.
- Messaggi contestuali, legenda X/O, layout ridimensionabile e navigazione da tastiera.
- ComputerPlayer separa la strategia dalle regole; la ricerca opera su una copia della griglia.
- Test aggiuntivi: vittoria immediata, blocco, immutabilitÃ , esplorazione di tutte le risposte umane contro minimax con due criteri di spareggio (primo/ultimo), selezione difficoltÃ  e contatori. Non Ã¨ un'esplorazione di ogni possibile spareggio casuale del PC.
