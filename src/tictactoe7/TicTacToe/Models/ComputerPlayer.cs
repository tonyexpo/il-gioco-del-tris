namespace TicTacToe.Models;

public enum Difficulty { Easy, Medium, Unbeatable }

public static class ComputerPlayer
{
    private static readonly int[][] Lines =
    [
        [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]
    ];

    // Lavora su una copia: la ricerca non modifica mai la partita o i binding.
    public static int ChooseMove(IReadOnlyList<Mark> board, Difficulty difficulty, Random random)
    {
        if (board.Count != 9) throw new ArgumentException("La griglia deve avere nove celle.", nameof(board));
        var cells = board.ToArray();
        var free = Enumerable.Range(0, 9).Where(i => cells[i] == Mark.Empty).ToArray();
        if (free.Length == 0 || Winner(cells) != Mark.Empty)
            throw new InvalidOperationException("La partita è terminata.");
        if (difficulty == Difficulty.Easy) return free[random.Next(free.Length)];
        if (difficulty == Difficulty.Medium)
        {
            foreach (var mark in new[] { Mark.O, Mark.X })
                foreach (var index in free)
                {
                    cells[index] = mark;
                    var wins = Winner(cells) == mark;
                    cells[index] = Mark.Empty;
                    if (wins) return index;
                }
            if (cells[4] == Mark.Empty) return 4;
            return free[random.Next(free.Length)];
        }
        var best = int.MinValue;
        var candidates = new List<int>();
        foreach (var index in free)
        {
            cells[index] = Mark.O;
            var score = Minimax(cells, false, 0);
            cells[index] = Mark.Empty;
            if (score > best) { best = score; candidates.Clear(); }
            if (score == best) candidates.Add(index);
        }
        // Varietà soltanto tra mosse di pari valore ottimale.
        return candidates[random.Next(candidates.Count)];
    }

    private static int Minimax(Mark[] cells, bool computerTurn, int depth)
    {
        var winner = Winner(cells);
        if (winner == Mark.O) return 10 - depth;
        if (winner == Mark.X) return depth - 10;
        if (cells.All(m => m != Mark.Empty)) return 0;
        var best = computerTurn ? int.MinValue : int.MaxValue;
        for (var i = 0; i < cells.Length; i++)
        {
            if (cells[i] != Mark.Empty) continue;
            cells[i] = computerTurn ? Mark.O : Mark.X;
            var score = Minimax(cells, !computerTurn, depth + 1);
            cells[i] = Mark.Empty;
            best = computerTurn ? Math.Max(best, score) : Math.Min(best, score);
        }
        return best;
    }

    private static Mark Winner(Mark[] cells)
    {
        foreach (var line in Lines)
            if (cells[line[0]] != Mark.Empty && cells[line[0]] == cells[line[1]] && cells[line[1]] == cells[line[2]])
                return cells[line[0]];
        return Mark.Empty;
    }
}
