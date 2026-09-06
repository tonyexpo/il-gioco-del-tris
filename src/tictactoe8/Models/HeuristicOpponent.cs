namespace TicTacToe.Models;

// Wins if possible, blocks if needed, otherwise prefers centre, then corners, then anything.
public class HeuristicOpponent : IOpponent
{
    private static readonly int[] Corners = [0, 2, 6, 8];
    private readonly Random _random = new();

    public int ChooseMove(GameBoard board, Player self)
    {
        var human = self == Player.X ? Player.O : Player.X;

        return FindWinningMove(board, self)
            ?? FindWinningMove(board, human)
            ?? (board.IsEmpty(4) ? 4 : (int?)null)
            ?? PickRandom(Corners.Where(board.IsEmpty))
            ?? PickRandom(board.EmptyIndices)
            ?? throw new InvalidOperationException("Board is full.");
    }

    private static int? FindWinningMove(GameBoard board, Player player)
    {
        foreach (var i in board.EmptyIndices)
        {
            board.Place(i, player);
            var wins = board.GetWinner() == player;
            board.Clear(i);
            if (wins)
                return i;
        }
        return null;
    }

    private int? PickRandom(IEnumerable<int> candidates)
    {
        var list = candidates.ToArray();
        return list.Length == 0 ? null : list[_random.Next(list.Length)];
    }
}
