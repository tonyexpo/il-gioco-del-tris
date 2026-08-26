using System.Collections.ObjectModel;
using System.Windows.Input;
using TicTacToe.Models;
using TicTacToe.Services;

namespace TicTacToe.ViewModels;

/// <summary>
/// ViewModel principale: stato della partita, punteggio e comandi.
/// Il giocatore è sempre X, il PC è sempre O (strategia casuale).
/// </summary>
public sealed class MainViewModel : ViewModelBase
{
    private const string InitialStatus = "Premi una casella per iniziare — giochi sempre con X";
    private const int AiThinkingDelayMs = 500;

    private readonly GameEngine _engine = new();
    private readonly IAiStrategy _ai;
    private bool _isBusy; // true mentre il PC gioca: blocca nuovi input

    public ObservableCollection<CellViewModel> Cells { get; }

    private string _statusText = InitialStatus;
    public string StatusText
    {
        get => _statusText;
        private set => SetProperty(ref _statusText, value);
    }

    private int _scoreX;
    public int ScoreX
    {
        get => _scoreX;
        private set => SetProperty(ref _scoreX, value);
    }

    private int _scoreDraws;
    public int ScoreDraws
    {
        get => _scoreDraws;
        private set => SetProperty(ref _scoreDraws, value);
    }

    private int _scoreO;
    public int ScoreO
    {
        get => _scoreO;
        private set => SetProperty(ref _scoreO, value);
    }

    public ICommand CellClickCommand { get; }
    public ICommand ResetCommand { get; }

    public MainViewModel(IAiStrategy? ai = null)
    {
        _ai = ai ?? new RandomAiStrategy();
        Cells = new ObservableCollection<CellViewModel>(
            Enumerable.Range(0, 9).Select(i => new CellViewModel(i)));

        CellClickCommand = new RelayCommand(OnCellClicked);
        ResetCommand = new RelayCommand(_ => ResetGame());
    }

    /// <summary>Click su una casella: la prima mossa avvia la partita.</summary>
    private async void OnCellClicked(object? parameter)
    {
        if (_isBusy || parameter is not int index) return;

        var cell = Cells[index];
        if (!cell.IsEnabled || !string.IsNullOrEmpty(cell.Content)) return;
        if (_engine.Winner is not null || _engine.IsDraw) return; // partita finita: serve Reset

        // 1) Mossa del giocatore (X).
        _engine.TryMove(index, Player.X);
        cell.Content = "X";

        if (_engine.Winner is not null || _engine.IsDraw)
        {
            FinishGame();
            return;
        }

        // 2) Mossa del PC (O), con breve pausa per UX.
        _isBusy = true;
        SetCellsEnabled(false);
        StatusText = "Il PC sta pensando…";

        await Task.Delay(AiThinkingDelayMs);

        var emptyIndices = Enumerable.Range(0, 9)
            .Where(i => string.IsNullOrEmpty(Cells[i].Content))
            .ToList();

        if (emptyIndices.Count > 0)
        {
            int aiIndex = _ai.ChooseMove(emptyIndices, Player.O);
            _engine.TryMove(aiIndex, Player.O);
            Cells[aiIndex].Content = "O";
        }

        _isBusy = false;

        if (_engine.Winner is not null || _engine.IsDraw)
        {
            FinishGame();
        }
        else
        {
            StatusText = "Tocca a te (X)";
            SetCellsEnabled(true);
        }
    }

    private void FinishGame()
    {
        if (_engine.Winner == Player.X)
        {
            ScoreX++;
            StatusText = "Hai vinto!";
        }
        else if (_engine.Winner == Player.O)
        {
            ScoreO++;
            StatusText = "Ha vinto il PC (O)";
        }
        else
        {
            ScoreDraws++;
            StatusText = "Pareggio!";
        }

        foreach (int i in _engine.WinningLine)
            Cells[i].IsWinning = true;

        SetCellsEnabled(false);
    }

    private void ResetGame()
    {
        if (_isBusy) return; // non resettare mentre il PC "pensa"

        _engine.Reset();

        foreach (var cell in Cells)
        {
            cell.Content = string.Empty;
            cell.IsWinning = false;
            cell.IsEnabled = true;
        }

        StatusText = InitialStatus;
    }

    private void SetCellsEnabled(bool enabled)
    {
        foreach (var cell in Cells)
            cell.IsEnabled = enabled;
    }
}
