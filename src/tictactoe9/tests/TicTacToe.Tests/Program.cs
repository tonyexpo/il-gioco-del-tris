using TicTacToe.Services;
using TicTacToe.ViewModels;

var tests = new (string Name, Action Body)[]
{
    ("Stato iniziale", InitialState),
    ("Mossa umana seguita dalla mossa PC", HumanThenComputerMove),
    ("Cella occupata non genera una seconda mossa PC", OccupiedCellIsRejected),
    ("Vittoria X interrompe il turno prima del PC", HumanVictoryStopsComputer),
    ("Vittoria O blocca ulteriori mosse", ComputerVictoryStopsGame),
    ("Pareggio rilevato correttamente", DrawIsDetected),
    ("Reset ripristina la partita", ResetRestoresGame),
    ("ICommand usa il parametro della cella", CommandUsesCellParameter)
};

var failures = 0;
foreach (var (name, body) in tests)
{
    try
    {
        body();
        Console.WriteLine($"PASS  {name}");
    }
    catch (Exception exception)
    {
        failures++;
        Console.WriteLine($"FAIL  {name}: {exception.Message}");
    }
}

Console.WriteLine();
Console.WriteLine($"Risultato: {tests.Length - failures}/{tests.Length} test superati.");
Environment.ExitCode = failures == 0 ? 0 : 1;

static void InitialState()
{
    var vm = NewGame();
    Equal(9, vm.Cells.Count, "numero celle");
    True(vm.Cells.All(c => c.IsEmpty), "la griglia deve essere vuota");
    Equal(GameOutcome.InProgress, vm.Outcome, "esito");
    True(!vm.IsGameOver, "la partita non deve essere terminata");
    Contains("X", vm.Status, "stato");
}

static void HumanThenComputerMove()
{
    var random = new FakeRandom(0);
    var vm = NewGame(random);
    True(vm.TryPlayCell(4), "mossa X valida");
    Equal("X", vm.Cells[4].Mark, "segno umano");
    Equal("O", vm.Cells[0].Mark, "segno PC scelto fra le celle libere");
    Equal(1, vm.Cells.Count(c => c.Mark == "X"), "numero X");
    Equal(1, vm.Cells.Count(c => c.Mark == "O"), "numero O");
    SequenceEqual([8], random.MaxExclusiveCalls, "dimensione passata al random");
}

static void OccupiedCellIsRejected()
{
    var random = new FakeRandom(0, 0);
    var vm = NewGame(random);
    True(vm.TryPlayCell(4), "prima mossa");
    True(!vm.TryPlayCell(4), "una cella occupata deve essere rifiutata");
    Equal(1, vm.Cells.Count(c => c.Mark == "O"), "non deve comparire un'altra O");
    Equal(1, random.MaxExclusiveCalls.Count, "il random non deve essere richiamato");
}

static void HumanVictoryStopsComputer()
{
    var random = new FakeRandom(2, 1, 0);
    var vm = NewGame(random);
    vm.TryPlayCell(0); // O -> 3
    vm.TryPlayCell(1); // O -> 4
    True(vm.TryPlayCell(2), "mossa vincente X");
    Equal(GameOutcome.HumanWon, vm.Outcome, "esito vittoria umana");
    Equal(2, vm.Cells.Count(c => c.Mark == "O"), "il PC non deve muovere dopo la vittoria X");
    Equal(2, random.MaxExclusiveCalls.Count, "nessuna estrazione dopo la vittoria");
    True(!vm.TryPlayCell(8), "mosse post-partita bloccate");
}

static void ComputerVictoryStopsGame()
{
    var random = new FakeRandom(2, 1, 1);
    var vm = NewGame(random);
    vm.TryPlayCell(0); // O -> 3
    vm.TryPlayCell(1); // O -> 4
    vm.TryPlayCell(8); // O -> 5, vittoria
    Equal(GameOutcome.ComputerWon, vm.Outcome, "esito vittoria PC");
    Contains("PC", vm.Status, "stato vittoria PC");
    True(!vm.TryPlayCell(2), "mosse post-partita bloccate");
    SequenceEqual([8, 6, 4], random.MaxExclusiveCalls, "celle libere passate al random");
}

static void DrawIsDetected()
{
    var random = new FakeRandom(0, 1, 0, 0);
    var vm = NewGame(random);
    vm.TryPlayCell(0); // O -> 1
    vm.TryPlayCell(2); // O -> 4
    vm.TryPlayCell(3); // O -> 5
    vm.TryPlayCell(7); // O -> 6
    vm.TryPlayCell(8); // ultima X
    Equal(GameOutcome.Draw, vm.Outcome, "esito pareggio");
    True(vm.IsGameOver, "partita terminata");
    SequenceEqual([8, 6, 4, 2], random.MaxExclusiveCalls, "range casuali decrescenti");
}

static void ResetRestoresGame()
{
    var vm = NewGame(new FakeRandom(0));
    vm.TryPlayCell(4);
    vm.Reset();
    Equal(GameOutcome.InProgress, vm.Outcome, "esito dopo reset");
    True(vm.Cells.All(c => c.IsEmpty), "celle pulite");
    True(!vm.IsGameOver, "partita riaperta");
}

static void CommandUsesCellParameter()
{
    var vm = NewGame(new FakeRandom(0));
    True(vm.PlayCellCommand.CanExecute("4"), "comando abilitato");
    vm.PlayCellCommand.Execute("4");
    Equal("X", vm.Cells[4].Mark, "parametro comando");
    True(!vm.PlayCellCommand.CanExecute("4"), "comando disabilitato sulla cella occupata");
}

static GameViewModel NewGame(FakeRandom? random = null) => new(random ?? new FakeRandom());

static void True(bool condition, string message)
{
    if (!condition) throw new InvalidOperationException(message);
}

static void Equal<T>(T expected, T actual, string message)
{
    if (!EqualityComparer<T>.Default.Equals(expected, actual))
        throw new InvalidOperationException($"{message}: atteso '{expected}', ottenuto '{actual}'");
}

static void Contains(string expected, string actual, string message)
{
    if (!actual.Contains(expected, StringComparison.OrdinalIgnoreCase))
        throw new InvalidOperationException($"{message}: '{actual}' non contiene '{expected}'");
}

static void SequenceEqual(IEnumerable<int> expected, IEnumerable<int> actual, string message)
{
    if (!expected.SequenceEqual(actual))
        throw new InvalidOperationException($"{message}: atteso [{string.Join(",", expected)}], ottenuto [{string.Join(",", actual)}]");
}

sealed class FakeRandom(params int[] values) : IRandomProvider
{
    private readonly Queue<int> _values = new(values);
    public List<int> MaxExclusiveCalls { get; } = [];

    public int Next(int maxExclusive)
    {
        MaxExclusiveCalls.Add(maxExclusive);
        if (_values.Count == 0) throw new InvalidOperationException("Sequenza casuale esaurita.");
        var value = _values.Dequeue();
        if (value < 0 || value >= maxExclusive) throw new InvalidOperationException("Valore fake fuori range.");
        return value;
    }
}
