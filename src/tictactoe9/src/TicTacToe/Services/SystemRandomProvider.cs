namespace TicTacToe.Services;

public sealed class SystemRandomProvider : IRandomProvider
{
    public int Next(int maxExclusive) => Random.Shared.Next(maxExclusive);
}
