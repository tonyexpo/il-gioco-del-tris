using TicTacToe.Models;

namespace TicTacToe.ViewModels;

public sealed class CellViewModel(int index) : ObservableObject
{
    private Cell _value;
    public int Index { get; } = index;
    public Cell Value { get => _value; set { if (SetProperty(ref _value, value)) OnPropertyChanged(nameof(Display)); } }
    public string Display => Value == Cell.Empty ? string.Empty : Value.ToString();
}
