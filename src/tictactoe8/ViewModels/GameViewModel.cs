using System.Collections.ObjectModel;
using System.Windows.Input;
using TicTacToe.Commands;
using TicTacToe.Models;

namespace TicTacToe.ViewModels;

public class GameViewModel : ViewModelBase
{
    private const Player Human = Player.X;
    private const Player Computer = Player.O;
    private static readonly TimeSpan ComputerThinkTime = TimeSpan.FromMilliseconds(450);

    private readonly GameBoard _board = new();

    private DifficultyLevel _difficulty = DifficultyLevel.All[1];
    private string _statusMessage = "";
    private GameOutcome _outcome;
    private bool _isComputerThinking;
    private int _humanWins;
    private int _computerWins;
    private int _draws;
    private int _gameId;

    public GameViewModel()
    {
        Cells = new ObservableCollection<CellViewModel>(
            Enumerable.Range(0, 9).Select(i => new CellViewModel(i)));

        PlayCommand = new RelayCommand(
            p => Play((CellViewModel)p!),
            p => p is CellViewModel cell && CanPlay(cell));

        ResetCommand = new RelayCommand(_ => Reset());
        ResetScoreCommand = new RelayCommand(_ => ResetScore());

        Reset();
    }

    public ObservableCollection<CellViewModel> Cells { get; }

    public IReadOnlyList<DifficultyLevel> Difficulties => DifficultyLevel.All;

    public ICommand PlayCommand { get; }

    public ICommand ResetCommand { get; }

    public ICommand ResetScoreCommand { get; }

    public DifficultyLevel Difficulty
    {
        get => _difficulty;
        set => SetProperty(ref _difficulty, value);
    }

    public string StatusMessage
    {
        get => _statusMessage;
        private set => SetProperty(ref _statusMessage, value);
    }

    public GameOutcome Outcome
    {
        get => _outcome;
        private set
        {
            if (SetProperty(ref _outcome, value))
                OnPropertyChanged(nameof(IsGameOver));
        }
    }

    public bool IsGameOver => Outcome != GameOutcome.InProgress;

    public bool IsComputerThinking
    {
        get => _isComputerThinking;
        private set => SetProperty(ref _isComputerThinking, value);
    }

    public int HumanWins
    {
        get => _humanWins;
        private set => SetProperty(ref _humanWins, value);
    }

    public int ComputerWins
    {
        get => _computerWins;
        private set => SetProperty(ref _computerWins, value);
    }

    public int Draws
    {
        get => _draws;
        private set => SetProperty(ref _draws, value);
    }

    private bool CanPlay(CellViewModel cell) =>
        !IsGameOver && !IsComputerThinking && _board.IsEmpty(cell.Index);

    private async void Play(CellViewModel cell)
    {
        Mark(cell.Index, Human);
        if (UpdateOutcome())
            return;

        var gameId = _gameId;
        IsComputerThinking = true;
        StatusMessage = "Il PC sta pensando…";

        await Task.Delay(ComputerThinkTime);

        // A reset during the delay abandons this game.
        if (gameId != _gameId)
            return;

        IsComputerThinking = false;
        Mark(Difficulty.Opponent.ChooseMove(_board, Computer), Computer);
        UpdateOutcome();
    }

    private void Mark(int index, Player player)
    {
        _board.Place(index, player);
        Cells[index].Mark = player;
    }

    private bool UpdateOutcome()
    {
        var line = _board.GetWinningLine();
        if (line is not null)
        {
            foreach (var i in line)
                Cells[i].IsWinning = true;

            if (_board.GetWinner() == Human)
            {
                Outcome = GameOutcome.HumanWon;
                HumanWins++;
                StatusMessage = "Hai vinto!";
            }
            else
            {
                Outcome = GameOutcome.ComputerWon;
                ComputerWins++;
                StatusMessage = "Ha vinto il PC";
            }
            return true;
        }

        if (_board.IsFull)
        {
            Outcome = GameOutcome.Draw;
            Draws++;
            StatusMessage = "Pareggio";
            return true;
        }

        StatusMessage = "Tocca a te";
        return false;
    }

    private void Reset()
    {
        _gameId++;
        _board.Reset();
        foreach (var cell in Cells)
        {
            cell.Mark = Player.None;
            cell.IsWinning = false;
        }

        IsComputerThinking = false;
        Outcome = GameOutcome.InProgress;
        StatusMessage = "Tocca a te";
    }

    private void ResetScore()
    {
        HumanWins = 0;
        ComputerWins = 0;
        Draws = 0;
    }
}
