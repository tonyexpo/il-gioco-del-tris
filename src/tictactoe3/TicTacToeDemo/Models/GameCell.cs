using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace TicTacToeDemo.Models;

public enum CellStatus { Empty, X, O }

public class GameCell : INotifyPropertyChanged
{
    private CellStatus _status;
    public int Index { get; set; }

    public CellStatus Status
    {
        get => _status;
        set
        {
            _status = value;
            OnPropertyChanged();
            OnPropertyChanged(nameof(IsClickable));
        }
    }

    public bool IsClickable => Status == CellStatus.Empty;

    public event PropertyChangedEventHandler? PropertyChanged;
    protected void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
