# Tris (Tic-Tac-Toe) — WPF / MVVM

Gioco del tris in WPF (.NET 8, `net8.0-windows`) con architettura **MVVM**.

## Regole implementate
- L'umano è sempre **X** e muove per primo: il primo clic su una casella avvia la partita.
- Il PC è sempre **O** e risponde con una mossa **casuale** tra le caselle libere (con breve pausa di 400 ms).
- Vittoria, pareggio e fine partita bloccano la griglia; il messaggio di stato viene aggiornato in tempo reale.
- Pulsante **Reset** in basso per ripartire da zero.

## Struttura del progetto
```
tictactoe10/
├── TicTacToe.sln
└── TicTacToe/
    ├── TicTacToe.csproj
    ├── App.xaml / App.xaml.cs          # bootstrap + risorse globali (converter)
    ├── Models/                        # M — logica pura, nessuna dipendenza da UI
    │   ├── Player.cs                  # enum X/O
    │   └── GameModel.cs               # scacchiera, vittoria, pareggio, reset
    ├── ViewModels/                    # V — stato e comandi per la vista
    │   ├── ViewModelBase.cs           # INotifyPropertyChanged + SetProperty
    │   ├── RelayCommand.cs            # ICommand minimale
    │   ├── CellViewModel.cs           # una casella (Content, IsLocked)
    │   └── GameViewModel.cs           # flusso di gioco, turni, reset
    ├── Converters/
    │   └── InverseBoolConverter.cs    # IsEnabled = !IsLocked
    └── Views/                         # V — XAML
        ├── MainWindow.xaml            # griglia 3x3 (ItemsControl + UniformGrid), status, Reset
        └── MainWindow.xaml.cs         # solo DataContext = new GameViewModel()
```

## Build & run
```bash
dotnet build TicTacToe.sln
dotnet run --project TicTacToe
```
