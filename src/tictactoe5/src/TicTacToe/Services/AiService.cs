using TicTacToe.Models;

namespace TicTacToe.Services;

/// <summary>Strategia di gioco del PC.</summary>
public interface IAiStrategy
{
    /// <summary>Sceglie una casella tra quelle libere per il giocatore indicato.</summary>
    int ChooseMove(IReadOnlyList<int> emptyIndices, Player player);
}

/// <summary>Difficoltà "casuale": il PC sceglie a caso una casella libera.</summary>
public sealed class RandomAiStrategy : IAiStrategy
{
    public int ChooseMove(IReadOnlyList<int> emptyIndices, Player player)
        => emptyIndices[Random.Shared.Next(emptyIndices.Count)];
}
