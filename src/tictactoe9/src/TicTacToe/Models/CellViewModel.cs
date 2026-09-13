using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace TicTacToe.Models;

public sealed class CellViewModel : INotifyPropertyChanged
{
    private string _mark = string.Empty;

    public string Mark
    {
        get => _mark;
        private set
        {
            if (_mark == value) return;
            _mark = value;
            OnPropertyChanged();
            OnPropertyChanged(nameof(IsEmpty));
        }
    }

    public bool IsEmpty => Mark.Length == 0;

    internal void SetMark(string mark) => Mark = mark;
    internal void Clear() => Mark = string.Empty;

    public event PropertyChangedEventHandler? PropertyChanged;

    private void OnPropertyChanged([CallerMemberName] string? propertyName = null) =>
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
}
