using TicTacToe.Commands;
using TicTacToe.Models;

namespace TicTacToe.ViewModels;

public sealed record DifficultyOption(Difficulty Value, string Label);

public sealed class MainViewModel : ObservableObject
{
    private readonly Game _game;
    private Difficulty _selectedDifficulty;
    private int _humanWins, _computerWins, _draws;

    public MainViewModel() : this(new Game(difficulty: Difficulty.Unbeatable)) { }
    public MainViewModel(Game game)
    {
        _game = game;
        _selectedDifficulty = game.Difficulty;
        Cells = Array.AsReadOnly(Enumerable.Range(0, 9).Select(i => new CellViewModel(i)).ToArray());
        PlayCommand = new RelayCommand(p =>
        {
            if (p is not int index || !_game.PlayHuman(index)) return;
            if (_game.State == GameState.HumanWon) _humanWins++;
            if (_game.State == GameState.ComputerWon) _computerWins++;
            if (_game.State == GameState.Draw) _draws++;
            Refresh();
        }, p => p is int index && _game.CanPlay(index));
        ResetCommand = new RelayCommand(_ => { _game.Reset(); Refresh(); });
        ClearScoresCommand = new RelayCommand(_ =>
        {
            _humanWins = _computerWins = _draws = 0;
            Refresh();
        });
        Refresh();
    }

    public IReadOnlyList<DifficultyOption> Difficulties { get; } = Array.AsReadOnly(new[]
    {
        new DifficultyOption(Difficulty.Easy, "Facile · casuale"),
        new DifficultyOption(Difficulty.Medium, "Medio · tattico"),
        new DifficultyOption(Difficulty.Unbeatable, "Imbattibile · minimax")
    });
    public Difficulty SelectedDifficulty
    {
        get => _selectedDifficulty;
        set
        {
            if (!CanChangeDifficulty || !Enum.IsDefined(value) || value == _selectedDifficulty) return;
            _game.ChangeDifficulty(value);
            SetProperty(ref _selectedDifficulty, value);
            // Cambiare livello dopo un risultato prepara una nuova partita, senza toccare i punteggi.
            _game.Reset();
            Refresh();
        }
    }
    public bool CanChangeDifficulty => _game.State != GameState.Playing;
    public int HumanWins => _humanWins;
    public int ComputerWins => _computerWins;
    public int Draws => _draws;
    public IReadOnlyList<CellViewModel> Cells { get; }
    public RelayCommand PlayCommand { get; }
    public RelayCommand ResetCommand { get; }
    public RelayCommand ClearScoresCommand { get; }
    public string Hint => _game.IsOver ? "Premi Reset per la rivincita." :
        _game.State == GameState.Playing ? "Il PC ha risposto. Ora gioca la tua X." :
        SelectedDifficulty == Difficulty.Unbeatable ? "Il PC non commette errori. Riesci a pareggiare?" :
        SelectedDifficulty == Difficulty.Medium ? "Il PC cerca il tris e blocca le tue minacce." : "Una partita rilassata: il PC gioca a caso.";
    public string Status => _game.State switch
    {
        GameState.Ready => "Scegli una casella per iniziare",
        GameState.Playing => "Tocca a te",
        GameState.HumanWon => "Hai vinto!",
        GameState.ComputerWon => "Vince il PC. Riproviamo?",
        GameState.Draw => "Pareggio: bella sfida!",
        _ => ""
    };

    private void Refresh()
    {
        foreach (var cell in Cells)
            cell.Update(_game.Board[cell.Index], _game.WinningCells.Contains(cell.Index));
        foreach (var property in new[] { nameof(Status), nameof(Hint), nameof(CanChangeDifficulty), nameof(HumanWins), nameof(ComputerWins), nameof(Draws) })
            OnPropertyChanged(property);
        PlayCommand.RaiseCanExecuteChanged();
    }
}
