using TicTacToe.Models;
using TicTacToe.ViewModels;

static class UpgradeTests
{
    public static void Run()
    {
        var nodes = 0;
        void Assert(bool value, string message) { if (!value) throw new Exception(message); }
        void Explore(List<int> moves, bool last)
        {
            var game = new Game(new TieRandom(last), Difficulty.Unbeatable);
            foreach (var move in moves) Assert(game.PlayHuman(move), "Replay legal");
            nodes++;
            Assert(game.State != GameState.HumanWon, "Unbeatable AI lost");
            if (game.IsOver) return;
            foreach (var next in Enumerable.Range(0, 9).Where(game.CanPlay))
                Explore([.. moves, next], last);
        }
        Explore([], false);
        Explore([], true);
        foreach (var level in new[] { Difficulty.Medium, Difficulty.Unbeatable })
        {
            Mark[] win = [Mark.O, Mark.O, Mark.Empty, Mark.X, Mark.X, Mark.Empty, Mark.X, Mark.Empty, Mark.Empty];
            var original = win.ToArray();
            Assert(ComputerPlayer.ChooseMove(win, level, new Random(1)) == 2, "Take immediate win");
            Assert(win.SequenceEqual(original), "AI must not mutate input");
            Mark[] block = [Mark.X, Mark.X, Mark.Empty, Mark.Empty, Mark.O, Mark.Empty, Mark.Empty, Mark.Empty, Mark.Empty];
            Assert(ComputerPlayer.ChooseMove(block, level, new Random(1)) == 2, "Block immediate loss");
        }
        var vm = new MainViewModel(new Game(new TieRandom(false), Difficulty.Easy));
        vm.PlayCommand.Execute(0);
        vm.SelectedDifficulty = Difficulty.Medium;
        Assert(vm.SelectedDifficulty == Difficulty.Easy && !vm.CanChangeDifficulty, "Level locked midgame");
        vm.ResetCommand.Execute(null);
        vm.SelectedDifficulty = Difficulty.Unbeatable;
        Assert(vm.SelectedDifficulty == Difficulty.Unbeatable && vm.Cells.All(c => c.Symbol == ""), "Level change after reset");
        while (vm.Cells.Any(c => vm.PlayCommand.CanExecute(c.Index)))
            vm.PlayCommand.Execute(vm.Cells.First(c => vm.PlayCommand.CanExecute(c.Index)).Index);
        Assert(vm.ComputerWins + vm.Draws == 1 && vm.HumanWins == 0, "One result counted");
        vm.PlayCommand.Execute(0);
        Assert(vm.ComputerWins + vm.Draws == 1, "No double counting");
        vm.ResetCommand.Execute(null);
        Assert(vm.ComputerWins + vm.Draws == 1, "Reset preserves scores");
        vm.ClearScoresCommand.Execute(null);
        Assert(vm.ComputerWins + vm.Draws + vm.HumanWins == 0, "Clear scores");
        Assert(new MainViewModel().SelectedDifficulty == Difficulty.Unbeatable, "UI default difficulty");
        Console.WriteLine($"PASS: AI exploration ({nodes} nodes, all human choices with first/last optimal tie-break), tactics and UX state.");
    }
    private sealed class TieRandom(bool last) : Random
    {
        public override int Next(int maxValue) => last ? maxValue - 1 : 0;
    }
}
