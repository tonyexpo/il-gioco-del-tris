namespace TicTacToe.Models;

public class MinimaxOpponent : IOpponent
{
    private readonly Random _random = new();

    public int ChooseMove(GameBoard board, Player self)
    {
        var human = self == Player.X ? Player.O : Player.X;
        var bestScore = int.MinValue;
        var bestMoves = new List<int>();

        foreach (var i in board.EmptyIndices)
        {
            board.Place(i, self);
            var score = Minimax(board, self, human, isSelfTurn: false, depth: 1);
            board.Clear(i);

            if (score > bestScore)
            {
                bestScore = score;
                bestMoves.Clear();
            }
            if (score == bestScore)
                bestMoves.Add(i);
        }

        // Random among equally good moves so the opponent doesn't feel scripted.
        return bestMoves[_random.Next(bestMoves.Count)];
    }

    private static int Minimax(GameBoard board, Player self, Player human, bool isSelfTurn, int depth)
    {
        var winner = board.GetWinner();
        if (winner == self) return 10 - depth;
        if (winner == human) return depth - 10;
        if (board.IsFull) return 0;

        var current = isSelfTurn ? self : human;
        var best = isSelfTurn ? int.MinValue : int.MaxValue;

        foreach (var i in board.EmptyIndices)
        {
            board.Place(i, current);
            var score = Minimax(board, self, human, !isSelfTurn, depth + 1);
            board.Clear(i);

            best = isSelfTurn ? Math.Max(best, score) : Math.Min(best, score);
        }

        return best;
    }
}
