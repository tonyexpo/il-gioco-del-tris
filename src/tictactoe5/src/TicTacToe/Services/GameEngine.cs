using TicTacToe.Models;

namespace TicTacToe.Services;

/// <summary>
/// Logica pura del tris (niente dipendenze UI): tabellone, mosse, vittoria e pareggio.
/// </summary>
public sealed class GameEngine
{
    private static readonly int[][] WinningLines =
    {
        new[] { 0, 1, 2 }, new[] { 3, 4, 5 }, new[] { 6, 7, 8 }, // righe
        new[] { 0, 3, 6 }, new[] { 1, 4, 7 }, new[] { 2, 5, 8 }, // colonne
        new[] { 0, 4, 8 }, new[] { 2, 4, 6 }                     // diagonali
    };

    private readonly char[] _board = new char[9];
    private Player _currentPlayer = Player.X;

    public int MoveCount { get; private set; }
    public Player CurrentPlayer => _currentPlayer;
    public Player? Winner { get; private set; }
    public IReadOnlyList<int> WinningLine { get; private set; } = Array.Empty<int>();
    public bool IsDraw => MoveCount == 9 && Winner is null;

    /// <summary>Esegue una mossa. Restituisce false se la casella è occupata o la partita è finita.</summary>
    public bool TryMove(int index, Player player)
    {
        if (index < 0 || index >= _board.Length) return false;
        if (_board[index] != ' ') return false;
        if (Winner is not null || IsDraw) return false;

        _board[index] = player == Player.X ? 'X' : 'O';
        MoveCount++;

        var line = FindWinningLine(index);
        if (line is not null)
        {
            Winner = player;
            WinningLine = line;
        }

        _currentPlayer = player == Player.X ? Player.O : Player.X;
        return true;
    }

    public void Reset()
    {
        Array.Clear(_board, 0, _board.Length);
        MoveCount = 0;
        Winner = null;
        WinningLine = Array.Empty<int>();
        _currentPlayer = Player.X;
    }

    private int[]? FindWinningLine(int lastMove)
    {
        foreach (var line in WinningLines.Where(line => line.Contains(lastMove)))
        {
            char mark = _board[line[0]];
            if (mark != ' ' && line.All(i => _board[i] == mark))
                return line;
        }

        return null;
    }
}
