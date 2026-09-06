using TicTacToe.Models;

namespace TicTacToe.ViewModels;

public sealed class CellViewModel(int index) : ObservableObject
{
    private string _symbol = "";
    private bool _isWinning;
    public int Index { get; } = index;
    public string Symbol { get => _symbol; private set => SetProperty(ref _symbol, value); }
    public bool IsWinning { get => _isWinning; private set => SetProperty(ref _isWinning, value); }
    public string AccessibleName => $"Riga {Index / 3 + 1}, colonna {Index % 3 + 1}: {(Symbol.Length == 0 ? "vuota" : Symbol)}";

    internal void Update(Mark mark, bool winning)
    {
        Symbol = mark == Mark.Empty ? "" : mark.ToString();
        IsWinning = winning;
        OnPropertyChanged(nameof(AccessibleName));
    }
}
