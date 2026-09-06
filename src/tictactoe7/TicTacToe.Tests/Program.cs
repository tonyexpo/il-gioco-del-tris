using TicTacToe.Models;
using TicTacToe.ViewModels;

UpgradeTests.Run();
var passed = 0;
void Check(bool condition, string message)
{
    if (!condition) throw new InvalidOperationException(message);
    passed++;
}

var game = new Game(new ScriptedRandom(3, 5));
Check(game.State == GameState.Ready && game.Board.All(m => m == Mark.Empty), "Initial state");
Check(!game.PlayHuman(-1) && !game.PlayHuman(9), "Invalid indices");
Check(game.PlayHuman(0) && game.Board[0] == Mark.X && game.Board[4] == Mark.O, "First click and PC response");
var snapshot = game.Board.ToArray();
Check(!game.PlayHuman(0) && !game.PlayHuman(4) && snapshot.SequenceEqual(game.Board), "Occupied cells");
game.PlayHuman(1);
game.PlayHuman(2);
Check(game.State == GameState.HumanWon && game.WinningCells.SequenceEqual(new[] { 0, 1, 2 }), "Human victory");
Check(game.Board.Count(m => m == Mark.O) == 2 && !game.PlayHuman(3), "No moves after victory");
game.Reset();
Check(game.State == GameState.Ready && game.WinningCells.Count == 0 && game.Board.All(m => m == Mark.Empty), "Reset after victory");

game = new Game(new ScriptedRandom(2, 1, 1));
foreach (var i in new[] { 0, 1, 8 }) game.PlayHuman(i);
Check(game.State == GameState.ComputerWon && game.WinningCells.SequenceEqual(new[] { 3, 4, 5 }), "PC victory");

game = new Game(new ScriptedRandom(0, 1, 0, 0));
foreach (var i in new[] { 0, 2, 3, 7, 8 }) game.PlayHuman(i);
Check(game.State == GameState.Draw && game.WinningCells.Count == 0, "Draw on last cell");
Check(!game.PlayHuman(8), "No moves after draw");
game.Reset();
Check(game.CanPlay(8), "Reset after draw");

var vm = new MainViewModel(new Game(new ScriptedRandom(3, 5)));
var notifications = 0;
var commandNotifications = 0;
vm.PropertyChanged += (_, _) => notifications++;
vm.PlayCommand.CanExecuteChanged += (_, _) => commandNotifications++;
Check(vm.Cells.Count == 9 && !vm.PlayCommand.CanExecute(null), "ViewModel initial state");
vm.PlayCommand.Execute(0);
Check(vm.Cells[0].Symbol == "X" && vm.Cells[4].Symbol == "O" && !vm.PlayCommand.CanExecute(0), "ViewModel bindings");
Check(notifications > 0 && commandNotifications > 0, "Binding and command notifications");
vm.PlayCommand.Execute(1);
vm.PlayCommand.Execute(2);
Check(vm.Cells.Count(c => c.IsWinning) == 3 && Enumerable.Range(0, 9).All(i => !vm.PlayCommand.CanExecute(i)), "ViewModel end game");
vm.ResetCommand.Execute(null);
Check(vm.Cells.All(c => c.Symbol == "" && !c.IsWinning) && vm.PlayCommand.CanExecute(0), "ViewModel reset");
vm.ResetCommand.Execute(null);
Check(vm.PlayCommand.CanExecute(0), "Repeated reset");

// Seeded simulations verify legal moves, terminal states and every winning line.
var seenLines = new HashSet<string>();
var outcomes = new HashSet<GameState>();
for (var seed = 0; seed < 5000; seed++)
{
    var human = new Random(seed);
    game = new Game(new Random(seed + 5000));
    var turns = 0;
    while (!game.IsOver)
    {
        var free = Enumerable.Range(0, 9).Where(game.CanPlay).ToArray();
        var before = game.Board.ToArray();
        Check(game.PlayHuman(free[human.Next(free.Length)]), "Legal move accepted");
        Check(Enumerable.Range(0, 9).All(i => before[i] == Mark.Empty || before[i] == game.Board[i]), "No overwritten cells");
        var xs = game.Board.Count(m => m == Mark.X);
        var os = game.Board.Count(m => m == Mark.O);
        Check(xs == os || xs == os + 1, "Turn counts");
        Check(++turns <= 5, "Bounded game");
    }
    outcomes.Add(game.State);
    if (game.WinningCells.Count > 0)
    {
        seenLines.Add(string.Join(",", game.WinningCells));
        var expected = game.State == GameState.HumanWon ? Mark.X : Mark.O;
        Check(game.WinningCells.All(i => game.Board[i] == expected), "Winning marks");
    }
    else Check(game.Board.All(m => m != Mark.Empty), "Draw has full board");
}
Check(seenLines.Count == 8 && outcomes.Count == 3, "All eight lines and three outcomes exercised");
Console.WriteLine($"PASS: {passed} assertions, 5000 simulated games, all winning lines.");

sealed class ScriptedRandom(params int[] values) : Random
{
    private readonly Queue<int> _values = new(values);
    public override int Next(int maxValue)
    {
        var value = _values.Dequeue();
        if (value < 0 || value >= maxValue) throw new InvalidOperationException("Invalid scripted random value");
        return value;
    }
}

