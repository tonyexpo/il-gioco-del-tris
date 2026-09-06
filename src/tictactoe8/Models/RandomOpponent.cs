namespace TicTacToe.Models;

public class RandomOpponent : IOpponent
{
    private readonly Random _random = new();

    public int ChooseMove(GameBoard board, Player self)
    {
        var empty = board.EmptyIndices.ToArray();
        return empty[_random.Next(empty.Length)];
    }
}
