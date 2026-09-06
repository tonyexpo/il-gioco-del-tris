namespace TicTacToe.Models;

public interface IOpponent
{
    int ChooseMove(GameBoard board, Player self);
}
