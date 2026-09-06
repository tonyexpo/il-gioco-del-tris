using TicTacToe.Models;

namespace TicTacToe.ViewModels;

public class CellViewModel(int index) : ViewModelBase
{
    private Player _mark;
    private bool _isWinning;

    public int Index { get; } = index;

    public Player Mark
    {
        get => _mark;
        set => SetProperty(ref _mark, value);
    }

    public bool IsWinning
    {
        get => _isWinning;
        set => SetProperty(ref _isWinning, value);
    }
}
