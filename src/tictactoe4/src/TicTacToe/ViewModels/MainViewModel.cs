using System.Collections.ObjectModel;
using System.Windows.Input;
using TicTacToe.Models;

namespace TicTacToe.ViewModels;

public sealed class MainViewModel : ObservableObject
{
    private readonly Random _random = new();
    private string _status = "Scegli una casella per iniziare";
    private bool _gameStarted;
    private bool _gameOver;
    private string _difficulty = "Casuale";

    public ObservableCollection<CellViewModel> Cells { get; } = new(Enumerable.Range(0, 9).Select(i => new CellViewModel(i)));
    public IReadOnlyList<string> Difficulties { get; } = ["Casuale", "Bilanciata"];
    public string Difficulty { get => _difficulty; set => SetProperty(ref _difficulty, value); }
    public string Status { get => _status; private set => SetProperty(ref _status, value); }
    public ICommand PlayCommand { get; }
    public ICommand ResetCommand { get; }

    public MainViewModel()
    {
        PlayCommand = new RelayCommand(p => Play(Convert.ToInt32(p)), p => !_gameOver);
        ResetCommand = new RelayCommand(_ => Reset());
    }

    private void Play(int index)
    {
        if (index is < 0 or > 8 || Cells[index].Value != Cell.Empty || _gameOver) return;
        _gameStarted = true;
        Cells[index].Value = Cell.X;
        if (FinishIfNeeded()) return;
        Status = "Il PC sta scegliendo...";
        PcMove();
        FinishIfNeeded();
    }

    private void PcMove()
    {
        var empty = Cells.Where(c => c.Value == Cell.Empty).Select(c => c.Index).ToList();
        if (empty.Count == 0) return;
        var winning = FindTacticalMove(Cell.O);
        var blocking = FindTacticalMove(Cell.X);
        var selected = Difficulty == "Bilanciata" ? winning ?? blocking ?? empty[_random.Next(empty.Count)] : empty[_random.Next(empty.Count)];
        Cells[selected].Value = Cell.O;
    }

    private int? FindTacticalMove(Cell mark)
    {
        foreach (var cell in Cells.Where(c => c.Value == Cell.Empty))
        {
            cell.Value = mark;
            var won = HasWon(mark);
            cell.Value = Cell.Empty;
            if (won) return cell.Index;
        }
        return null;
    }

    private bool FinishIfNeeded()
    {
        if (HasWon(Cell.X)) { Status = "Hai vinto! 🎉"; _gameOver = true; return true; }
        if (HasWon(Cell.O)) { Status = "Il PC ha vinto. Riprova!"; _gameOver = true; return true; }
        if (Cells.All(c => c.Value != Cell.Empty)) { Status = "Pareggio!"; _gameOver = true; return true; }
        Status = _gameStarted ? "Tocca a te — sei X" : Status;
        return false;
    }

    private bool HasWon(Cell mark)
    {
        int[][] lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
        return lines.Any(line => line.All(i => Cells[i].Value == mark));
    }

    private void Reset()
    {
        foreach (var cell in Cells) cell.Value = Cell.Empty;
        _gameStarted = false; _gameOver = false;
        Status = "Scegli una casella per iniziare";
        (PlayCommand as RelayCommand)?.RaiseCanExecuteChanged();
    }
}
