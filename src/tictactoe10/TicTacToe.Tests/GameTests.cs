using System;

using System.Collections.Generic;
using TicTacToe.Models;

using TicTacToe.Services;
using TicTacToe.ViewModels;
using Xunit;

namespace TicTacToe.Tests
{
    /// <summary>Random deterministico: restituisce i valori scriptati in ordine. Fallisce su valore fuori range o chiamata inattesa.</summary>
    internal sealed class ScriptedRandom : IRandomProvider
    {
        private readonly Queue<int> _values = new();

        public ScriptedRandom(params int[] values)
        {
            foreach (var v in values)
                _values.Enqueue(v);
        }

        public int Next(int exclusiveMax)
        {
            if (_values.Count == 0)
                throw new InvalidOperationException("ScriptedRandom: chiamata inattesa, script esaurito.");

            int value = _values.Dequeue();
            if (value < 0 || value >= exclusiveMax)
                throw new ArgumentOutOfRangeException(nameof(exclusiveMax), $"Valore {value} fuori range [0, {exclusiveMax}).");
            return value;
        }
    }

    /// <summary>Scheduler manuale: la mossa PC resta pendente finché il test non la "spara" o viene annullata.</summary>
    internal sealed class ManualDelayScheduler : IUiDelayScheduler
    {
        private Action? _pending;
        private Action? _lastScheduled; // conservata per simulare un tick "stale" dopo Cancel

        public bool HasPending => _pending != null;

        public void Schedule(Action action, TimeSpan delay)
        {
            _pending = action;
            _lastScheduled = action;
        }

        public void Cancel() => _pending = null;

        /// <summary>Esegue l'azione pendente (simula il tick del timer).</summary>
        public void FirePending()
        {
            var a = _pending;
            _pending = null;
            a?.Invoke();
        }

        /// <summary>Simula un tick "stale": esegue l'ultima action schedulata anche se è stata annullata.</summary>
        public void FireCancelled() => _lastScheduled?.Invoke();
    }

    internal static class VmHelpers
    {
        public static (GameViewModel vm, ManualDelayScheduler sched) Create(int[] randomScript)
        {
            var sched = new ManualDelayScheduler();
            var vm = new GameViewModel(new ScriptedRandom(randomScript), sched);
            return (vm, sched);
        }

        public static void Click(GameViewModel vm, int index) => vm.CellClickCommand.Execute(vm.Cells[index]);

        public static int CountSymbols(GameViewModel vm, char symbol)
        {
            var n = 0;
            foreach (var c in vm.Cells)
                if (c.Content == symbol.ToString())
                    n++;
            return n;
        }
    }

    public class GameModelTests
    {
        [Fact]
        public void TryPlaceMark_RejectsInvalidIndex()
        {
            var m = new GameModel();
            Assert.False(m.TryPlaceMark(-1, Player.X));
            Assert.False(m.TryPlaceMark(9, Player.O));
            for (int i = 0; i < 9; i++)
                Assert.True(m.IsEmpty(i));

            Assert.Throws<ArgumentOutOfRangeException>(() => m.PlaceMark(-1, Player.X));
            Assert.Throws<ArgumentOutOfRangeException>(() => m.PlaceMark(9, Player.O));
        }

        [Fact]
        public void TryPlaceMark_RejectsInvalidPlayer()
        {
            var m = new GameModel();
            Assert.False(m.TryPlaceMark(0, (Player)5));
            Assert.True(m.IsEmpty(0));
            Assert.Throws<ArgumentException>(() => m.PlaceMark(0, (Player)5));
        }

        [Fact]
        public void TryPlaceMark_RejectsOccupiedCell()
        {
            var m = new GameModel();
            Assert.True(m.TryPlaceMark(4, Player.X));
            Assert.False(m.TryPlaceMark(4, Player.O));
            Assert.Equal('X', m.SymbolAt(4));
            Assert.Throws<InvalidOperationException>(() => m.PlaceMark(4, Player.O));
        }

        [Theory]
        [InlineData(0, 1, 2)] // riga 1
        [InlineData(3, 4, 5)] // riga 2
        [InlineData(6, 7, 8)] // riga 3
        [InlineData(0, 3, 6)] // colonna 1
        [InlineData(1, 4, 7)] // colonna 2
        [InlineData(2, 5, 8)] // colonna 3
        [InlineData(0, 4, 8)] // diagonale principale
        [InlineData(2, 4, 6)] // diagonale secondaria
        public void Win_AllEightLines(int a, int b, int c)
        {
            var m = new GameModel();
            m.TryPlaceMark(a, Player.X);
            m.TryPlaceMark(b, Player.X);
            Assert.Null(m.GetWinner()); // con due soli X nessuna linea è completa
            m.TryPlaceMark(c, Player.X);
            Assert.Equal('X', m.GetWinner());
        }

        [Fact]
        public void Draw_FullBoardNoWinner()
        {
            var m = new GameModel();
            char[] board = { 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X' };
            for (int i = 0; i < 9; i++)
                m.TryPlaceMark(i, board[i] == 'X' ? Player.X : Player.O);

            Assert.True(m.IsFull());
            Assert.Null(m.GetWinner()); // pareggio: nessun vincitore
        }

        [Fact]
        public void Reset_ClearsBoard()
        {
            var m = new GameModel();
            m.TryPlaceMark(0, Player.X);
            m.TryPlaceMark(1, Player.O);
            m.Reset();
            for (int i = 0; i < 9; i++)
                Assert.True(m.IsEmpty(i));
            Assert.Null(m.GetWinner());
        }
    }

    public class GameViewModelTests
    {
        [Fact]
        public void HumanClick_PlacesX_AndPcRespondsOnlyOnFreeCell()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 }); // PC sceglie la prima casella libera

            VmHelpers.Click(vm, 4);
            Assert.Equal("X", vm.Cells[4].Content);
            Assert.False(vm.CellClickCommand.CanExecute(null)); // turno del PC: clic disabilitato
            Assert.True(sched.HasPending);

            sched.FirePending();
            // O deve comparire solo su una casella che era libera (non la 4)
            Assert.Equal(1, VmHelpers.CountSymbols(vm, 'O'));
            Assert.NotEqual("O", vm.Cells[4].Content);
            Assert.True(vm.CellClickCommand.CanExecute(null)); // torna il turno umano
        }

        [Fact]
        public void PcMove_PlacesO_OnExactlyScriptedCell()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 2 }); // dopo X@4 le libere sono [0,1,2,3,5,6,7,8]: indice 2 => cella 2

            VmHelpers.Click(vm, 4);
            sched.FirePending();

            Assert.Equal("O", vm.Cells[2].Content); // esatta cella scelta dal random
            Assert.Equal(1, VmHelpers.CountSymbols(vm, 'O'));
        }

        [Fact]
        public void IllegalMove_OccupiedCell_IsIgnored()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            VmHelpers.Click(vm, 0);   // X@0, PC in attesa
            Assert.False(vm.CellClickCommand.CanExecute(null));
            VmHelpers.Click(vm, 3);   // clic durante il turno del PC: ignorato
            sched.FirePending();      // O@1 (prima casella libera dopo lo 0)

            string statusBefore = vm.StatusText;
            VmHelpers.Click(vm, 1);   // casella già occupata da O: mossa rifiutata
            Assert.Equal(statusBefore, vm.StatusText);
            Assert.Equal(1, VmHelpers.CountSymbols(vm, 'X'));
            Assert.Equal(1, VmHelpers.CountSymbols(vm, 'O'));
        }

        [Fact]
        public void ForeignCell_WithValidIndex_IsIgnored()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            vm.CellClickCommand.Execute(new CellViewModel(4)); // stessa indice, istanza estranea alla griglia

            Assert.Equal("", vm.Cells[4].Content);
            Assert.False(sched.HasPending);
        }

        [Fact]
        public void ForeignCell_WithInvalidIndex_IsIgnored()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            vm.CellClickCommand.Execute(new CellViewModel(-1));
            vm.CellClickCommand.Execute(new CellViewModel(9));

            for (int i = 0; i < 9; i++)
                Assert.Equal("", vm.Cells[i].Content);
            Assert.False(sched.HasPending);
        }

        [Fact]
        public void NullOrWrongType_Parameter_IsIgnored()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            vm.CellClickCommand.Execute(null);
            vm.CellClickCommand.Execute("X");

            for (int i = 0; i < 9; i++)
                Assert.Equal("", vm.Cells[i].Content);
            Assert.False(sched.HasPending);
        }

        [Fact]
        public void XWins_ByClicks_GameOver_NoHumanTurn_NoScheduling()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 6, 0 }); // PC: prima mossa -> cella 7, seconda -> cella 1

            VmHelpers.Click(vm, 0);   // X@0 ; PC O@7
            sched.FirePending();
            VmHelpers.Click(vm, 4);   // X@4 ; PC O@1
            sched.FirePending();
            VmHelpers.Click(vm, 8);   // X@8 -> diagonale: vittoria

            Assert.Equal("Hai vinto!", vm.StatusText);
            Assert.False(vm.CellClickCommand.CanExecute(null)); // game-over: niente turno umano
            Assert.False(sched.HasPending);                     // nessuna schedulazione dopo la vittoria
            foreach (var c in vm.Cells)
                Assert.True(c.IsLocked);

            VmHelpers.Click(vm, 2);   // clic post-vittoria ignorato
            Assert.Equal(3, VmHelpers.CountSymbols(vm, 'X'));
            Assert.False(sched.HasPending);
        }

        [Fact]
        public void OWins_ByDiagonal_PcWin()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0, 3, 3 }); // PC: O@0, poi O@4, poi O@8 -> diagonale

            VmHelpers.Click(vm, 6);   // X@6 ; libere [0,1,2,3,4,5,7,8] -> O@0
            sched.FirePending();
            VmHelpers.Click(vm, 7);   // X@7 ; libere [1,2,3,4,5,8]    -> O@4
            sched.FirePending();
            VmHelpers.Click(vm, 2);   // X@2 ; libere [1,3,5,8]         -> O@8: diagonale del PC
            sched.FirePending();      // spara la callback PC: O@8 completa la diagonale

            Assert.Equal("Il PC ha vinto. Riprova!", vm.StatusText);
            Assert.False(vm.CellClickCommand.CanExecute(null));
            Assert.False(sched.HasPending); // game-over: nessuna schedulazione
            Assert.Equal(3, VmHelpers.CountSymbols(vm, 'O'));
            Assert.Equal(3, VmHelpers.CountSymbols(vm, 'X'));
            foreach (var c in vm.Cells)
                Assert.True(c.IsLocked);
        }

        [Fact]
        public void Draw_WhenBoardFull()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 1, 0, 0, 0 });

            VmHelpers.Click(vm, 0); sched.FirePending(); // O@2
            VmHelpers.Click(vm, 1); sched.FirePending(); // O@3
            VmHelpers.Click(vm, 5); sched.FirePending(); // O@4
            VmHelpers.Click(vm, 6); sched.FirePending(); // O@7
            VmHelpers.Click(vm, 8);                      // scacchiera piena: pareggio

            Assert.Equal("Pareggio!", vm.StatusText);
            Assert.False(vm.CellClickCommand.CanExecute(null));
            foreach (var c in vm.Cells)
                Assert.True(c.IsLocked);
        }

        [Fact]
        public void StatusText_ReflectsGameStates()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            Assert.Equal("Clicca una casella per iniziare (X)", vm.StatusText); // idle iniziale

            VmHelpers.Click(vm, 4);
            Assert.Equal("Il PC sta pensando...", vm.StatusText); // turno del PC

            sched.FirePending();
            Assert.Equal("Tocca a te — clicca una casella (X)", vm.StatusText); // torna il turno umano

            vm.ResetCommand.Execute(null);
            Assert.Equal("Clicca una casella per iniziare (X)", vm.StatusText); // reset -> idle
        }

        [Fact]
        public void Reset_DuringPcWait_CancelsPendingMove()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            VmHelpers.Click(vm, 4);      // X@4, mossa PC pendente
            Assert.True(sched.HasPending);

            vm.ResetCommand.Execute(null);

            Assert.False(sched.HasPending);          // mossa PC annullata dal reset
            sched.FirePending();                    // no-op: nessun O piazzato
            for (int i = 0; i < 9; i++)
                Assert.Equal("", vm.Cells[i].Content);
            Assert.True(vm.CellClickCommand.CanExecute(null));

            VmHelpers.Click(vm, 2);      // dopo il reset si può giocare di nuovo
            Assert.Equal("X", vm.Cells[2].Content);
        }

        [Fact]
        public void StalePcCallback_AfterReset_DoesNotPlaceO()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 0 });

            VmHelpers.Click(vm, 4);      // X@4, callback PC schedulata
            vm.ResetCommand.Execute(null); // reset: generazione incrementata + cancel
            Assert.False(sched.HasPending);

            sched.FireCancelled();        // tick "stale": esegue la callback annullata dopo il reset
            for (int i = 0; i < 9; i++)
                Assert.Equal("", vm.Cells[i].Content); // nessun O appare
            Assert.True(vm.CellClickCommand.CanExecute(null));
        }

        [Fact]
        public void Reset_AfterGameOver_RestartsGame()
        {
            var (vm, sched) = VmHelpers.Create(new[] { 6, 0 });
            VmHelpers.Click(vm, 0); sched.FirePending();
            VmHelpers.Click(vm, 4); sched.FirePending();
            VmHelpers.Click(vm, 8);   // vittoria X

            vm.ResetCommand.Execute(null);

            for (int i = 0; i < 9; i++)
                Assert.Equal("", vm.Cells[i].Content);
            Assert.True(vm.CellClickCommand.CanExecute(null));

            VmHelpers.Click(vm, 3);
            Assert.Equal("X", vm.Cells[3].Content);
        }

        [Fact]
        public void Cells_IsReadOnlyList_WithNineCells()
        {
            var (vm, _) = VmHelpers.Create(Array.Empty<int>());
            IReadOnlyList<CellViewModel> cells = vm.Cells; // contratto di sola lettura per i consumer
            Assert.Equal(9, cells.Count);
        }
    }
}
