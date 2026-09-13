# TicTacToe WPF

Demo del gioco del tris realizzata in C# con WPF e pattern MVVM.

## Esecuzione

```powershell
dotnet run --project src/TicTacToe/TicTacToe.csproj
```

## Build e test offline

```powershell
dotnet build TicTacToe.sln --no-restore
dotnet run --project tests/TicTacToe.Tests/TicTacToe.Tests.csproj --no-build
```

Il giocatore usa sempre **X**; il PC usa **O** e sceglie casualmente fra le celle libere.
