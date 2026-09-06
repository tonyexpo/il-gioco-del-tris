namespace TicTacToe.Models;

public enum Mark { Empty, X, O }
public enum GameState { Ready, Playing, HumanWon, ComputerWon, Draw }

/// <summary>Regole del tris, indipendenti dalla UI. Ogni turno include la risposta del PC.</summary>
public sealed class Game
{
    private static readonly int[][] Lines =
    [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];
    private readonly Mark[] _board = new Mark[9];
    private readonly Random _random;

    public Game(Random? random = null, Difficulty difficulty = Difficulty.Easy)
    {
        _random = random ?? Random.Shared;
        if (!Enum.IsDefined(difficulty)) throw new ArgumentOutOfRangeException(nameof(difficulty));
        Difficulty = difficulty;
        Board = Array.AsReadOnly(_board);
    }

    public IReadOnlyList<Mark> Board { get; }
    public Difficulty Difficulty { get; private set; }
    public void ChangeDifficulty(Difficulty difficulty)
    {
        if (State == GameState.Playing) throw new InvalidOperationException("Termina o azzera la partita prima di cambiare livello.");
        if (!Enum.IsDefined(difficulty)) throw new ArgumentOutOfRangeException(nameof(difficulty));
        Difficulty = difficulty;
    }
    public GameState State { get; private set; } = GameState.Ready;
    public IReadOnlyList<int> WinningCells { get; private set; } = Array.Empty<int>();
    public bool IsOver => State is GameState.HumanWon or GameState.ComputerWon or GameState.Draw;
    public bool CanPlay(int index) => index >= 0 && index < 9 && !IsOver && _board[index] == Mark.Empty;

    public bool PlayHuman(int index)
    {
        if (!CanPlay(index)) return false;
        State = GameState.Playing;
        _board[index] = Mark.X;
        Evaluate();
        if (IsOver) return true;

        _board[ComputerPlayer.ChooseMove(Board, Difficulty, _random)] = Mark.O;
        Evaluate();
        return true;
    }

    public void Reset()
    {
        Array.Clear(_board);
        WinningCells = Array.Empty<int>();
        State = GameState.Ready;
    }

    private void Evaluate()
    {
        foreach (var line in Lines)
        {
            var mark = _board[line[0]];
            if (mark == Mark.Empty || _board[line[1]] != mark || _board[line[2]] != mark) continue;
            WinningCells = Array.AsReadOnly(line);
            State = mark == Mark.X ? GameState.HumanWon : GameState.ComputerWon;
            return;
        }
        if (_board.All(mark => mark != Mark.Empty)) State = GameState.Draw;
    }
}

