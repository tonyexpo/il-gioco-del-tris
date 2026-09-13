using System.Collections.ObjectModel;
using System.Globalization;
using System.Windows.Input;
using TicTacToe.Commands;
using TicTacToe.Models;
using TicTacToe.Services;

namespace TicTacToe.ViewModels;

public enum GameOutcome
{
    InProgress,
    HumanWon,
    ComputerWon,
    Draw
}

public sealed class GameViewModel : System.ComponentModel.INotifyPropertyChanged
{
    private static readonly int[][] WinningLines =
    [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];

    private readonly IRandomProvider _random;
    private readonly RelayCommand _playCellCommand;
    private string _status = string.Empty;
    private GameOutcome _outcome;

    public GameViewModel(IRandomProvider random)
    {
        _random = random ?? throw new ArgumentNullException(nameof(random));
        Cells = new ObservableCollection<CellViewModel>(Enumerable.Range(0, 9).Select(_ => new CellViewModel()));
        _playCellCommand = new RelayCommand(ExecuteCell, CanExecuteCell);
        ResetCommand = new RelayCommand(_ => Reset());
        Reset();
    }

    public ObservableCollection<CellViewModel> Cells { get; }
    public ICommand PlayCellCommand => _playCellCommand;
    public ICommand ResetCommand { get; }

    public string Status
    {
        get => _status;
        private set
        {
            if (_status == value) return;
            _status = value;
            OnPropertyChanged();
        }
    }

    public GameOutcome Outcome
    {
        get => _outcome;
        private set
        {
            if (_outcome == value) return;
            _outcome = value;
            OnPropertyChanged();
            OnPropertyChanged(nameof(IsGameOver));
        }
    }

    public bool IsGameOver => Outcome != GameOutcome.InProgress;

    public bool TryPlayCell(int index)
    {
        if (!CanPlay(index)) return false;

        Cells[index].SetMark("X");
        if (CompleteGameIfNeeded())
        {
            RefreshCommands();
            return true;
        }

        Status = "Il PC sta giocando…";
        PlayComputerMove();

        if (!CompleteGameIfNeeded())
            Status = "Tocca a te — sei X";

        RefreshCommands();
        return true;
    }

    public void Reset()
    {
        foreach (var cell in Cells)
            cell.Clear();

        Outcome = GameOutcome.InProgress;
        Status = "Tocca a te — sei X";
        RefreshCommands();
    }

    private void PlayComputerMove()
    {
        var freeIndexes = Enumerable.Range(0, Cells.Count).Where(i => Cells[i].IsEmpty).ToArray();
        if (freeIndexes.Length == 0) return;

        var randomIndex = _random.Next(freeIndexes.Length);
        if (randomIndex < 0 || randomIndex >= freeIndexes.Length)
            throw new InvalidOperationException("Il generatore casuale ha restituito un indice non valido.");

        Cells[freeIndexes[randomIndex]].SetMark("O");
    }

    private bool CompleteGameIfNeeded()
    {
        var winner = FindWinner();
        if (winner == "X")
        {
            Outcome = GameOutcome.HumanWon;
            Status = "Hai vinto!";
            return true;
        }

        if (winner == "O")
        {
            Outcome = GameOutcome.ComputerWon;
            Status = "Ha vinto il PC.";
            return true;
        }

        if (Cells.All(cell => !cell.IsEmpty))
        {
            Outcome = GameOutcome.Draw;
            Status = "Pareggio!";
            return true;
        }

        return false;
    }

    private string? FindWinner()
    {
        foreach (var line in WinningLines)
        {
            var mark = Cells[line[0]].Mark;
            if (mark.Length > 0 && Cells[line[1]].Mark == mark && Cells[line[2]].Mark == mark)
                return mark;
        }

        return null;
    }

    private bool CanPlay(int index) =>
        !IsGameOver && index >= 0 && index < Cells.Count && Cells[index].IsEmpty;

    private bool CanExecuteCell(object? parameter) => TryGetIndex(parameter, out var index) && CanPlay(index);

    private void ExecuteCell(object? parameter)
    {
        if (TryGetIndex(parameter, out var index))
            TryPlayCell(index);
    }

    private static bool TryGetIndex(object? parameter, out int index) =>
        int.TryParse(Convert.ToString(parameter, CultureInfo.InvariantCulture), NumberStyles.Integer,
            CultureInfo.InvariantCulture, out index);

    private void RefreshCommands() => _playCellCommand.RaiseCanExecuteChanged();

    public event System.ComponentModel.PropertyChangedEventHandler? PropertyChanged;

    private void OnPropertyChanged([System.Runtime.CompilerServices.CallerMemberName] string? propertyName = null) =>
        PropertyChanged?.Invoke(this, new System.ComponentModel.PropertyChangedEventArgs(propertyName));
}
