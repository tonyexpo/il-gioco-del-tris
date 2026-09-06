namespace TicTacToe.Models;

public record DifficultyLevel(string Name, string Description, IOpponent Opponent)
{
    public static readonly IReadOnlyList<DifficultyLevel> All =
    [
        new("Facile", "Il PC gioca a caso", new RandomOpponent()),
        new("Medio", "Il PC vince e blocca quando può", new HeuristicOpponent()),
        new("Difficile", "Il PC non perde mai", new MinimaxOpponent())
    ];
}
