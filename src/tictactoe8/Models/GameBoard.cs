namespace TicTacToe.Models;

public class GameBoard
{
    private static readonly int[][] WinningLines =
    [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];

    private readonly Player[] _cells = new Player[9];

    public Player this[int index] => _cells[index];

    public bool IsEmpty(int index) => _cells[index] == Player.None;

    public bool IsFull => _cells.All(c => c != Player.None);

    public IEnumerable<int> EmptyIndices =>
        Enumerable.Range(0, _cells.Length).Where(IsEmpty);

    public void Place(int index, Player player)
    {
        if (!IsEmpty(index))
            throw new InvalidOperationException($"Cell {index} is already taken.");
        _cells[index] = player;
    }

    public void Clear(int index) => _cells[index] = Player.None;

    public int[]? GetWinningLine() =>
        WinningLines.FirstOrDefault(line =>
            _cells[line[0]] != Player.None &&
            _cells[line[0]] == _cells[line[1]] &&
            _cells[line[1]] == _cells[line[2]]);

    public Player GetWinner()
    {
        var line = GetWinningLine();
        return line is null ? Player.None : _cells[line[0]];
    }

    public void Reset() => Array.Fill(_cells, Player.None);
}
