namespace TicTacToe.ViewModels;

/// <summary>Stato di una singola casella della griglia.</summary>
public sealed class CellViewModel : ViewModelBase
{
    private string _content = string.Empty;
    private bool _isEnabled = true;
    private bool _isWinning;

    public int Index { get; }

    /// <summary>Marcatore visualizzato: "X", "O" o vuoto.</summary>
    public string Content
    {
        get => _content;
        set => SetProperty(ref _content, value);
    }

    public bool IsEnabled
    {
        get => _isEnabled;
        set => SetProperty(ref _isEnabled, value);
    }

    /// <summary>True se la casella fa parte della linea vincente (evidenziata in verde).</summary>
    public bool IsWinning
    {
        get => _isWinning;
        set => SetProperty(ref _isWinning, value);
    }

    public CellViewModel(int index) => Index = index;
}
