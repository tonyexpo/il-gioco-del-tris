namespace TicTacToe.Services;

public interface IRandomProvider
{
    int Next(int maxExclusive);
}
