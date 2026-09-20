using System;
using System.Collections.Generic;

using TicTacToe.Models;
using TicTacToe.Services;

namespace TicTacToe.ViewModels
{
    /// <summary>
    /// ViewModel principale del gioco.
    /// L'umano è sempre X e muove per primo (il primo clic sulla griglia avvia la partita);
    /// il PC è sempre O e risponde con una mossa casuale tra le caselle libere.
    /// </summary>
    public class GameViewModel : ViewModelBase
    {
        private const string IdleStatus = "Clicca una casella per iniziare (X)";
        private const string HumanTurnStatus = "Tocca a te — clicca una casella (X)";
        private const string PcThinkingStatus = "Il PC sta pensando...";

        private readonly GameModel _model = new();
        private readonly IRandomProvider _random;
        private readonly IUiDelayScheduler _delay;
        private readonly List<CellViewModel> _cellItems = new();

        private bool _isHumanTurn = true; // true in stato Idle e HumanTurn
        private bool _gameOver;
        private string _statusText = IdleStatus;
        private int _generation; // token per invalidare le callback PC stale dopo reset

        /// <summary>Le 9 caselle della griglia (in ordine di lettura). Sola lettura per i consumer.</summary>
        public IReadOnlyList<CellViewModel> Cells { get; }

        public RelayCommand ResetCommand { get; }
        public RelayCommand CellClickCommand { get; }

        /// <summary>Messaggio di stato mostrato sopra la griglia.</summary>
        public string StatusText
        {
            get => _statusText;
            private set => SetProperty(ref _statusText, value);
        }

        /// <summary>Costruttore di produzione: random reale e breve delay UI (DispatcherTimer).</summary>
        public GameViewModel()
            : this(new SystemRandomProvider(), new DispatcherDelayScheduler())
        {
        }

        /// <summary>Costruttore testabile: sorgente random e scheduler iniettabili.</summary>
        public GameViewModel(IRandomProvider random, IUiDelayScheduler delay)
        {
            _random = random ?? throw new ArgumentNullException(nameof(random));
            _delay = delay ?? throw new ArgumentNullException(nameof(delay));

            for (int i = 0; i < 9; i++)
                _cellItems.Add(new CellViewModel(i));
            Cells = _cellItems.AsReadOnly();

            ResetCommand = new RelayCommand(ResetGame);
            CellClickCommand = new RelayCommand(OnCellClicked, CanHumanMove);
        }

        private bool CanHumanMove() => _isHumanTurn && !_gameOver;

        private void OnCellClicked(object? parameter)
        {
            if (parameter is not CellViewModel cell || !CanHumanMove())
                return;

            // La casella deve appartenere alla griglia di questo ViewModel:
            // indice valido e stessa istanza presente in _cellItems[index].
            int index = cell.Index;
            if (index < 0 || index >= _cellItems.Count)
                return;
            if (!ReferenceEquals(_cellItems[index], cell))
                return;

            // Mossa dell'umano (X): rifiutata se indice invalido o casella occupata.
            if (!_model.TryPlaceMark(index, Player.X))
                return;

            cell.SetContent("X");

            if (!CheckEnd())
                EnterPcThinking();
        }

        private void EnterPcThinking()
        {
            _isHumanTurn = false;
            StatusText = PcThinkingStatus;
            LockFreeCells();
            int generation = ++_generation; // token univoco della callback in schedulazione
            _delay.Schedule(() => PcMove(generation), TimeSpan.FromMilliseconds(400));
            CellClickCommand.RaiseCanExecuteChanged();
        }

        private void PcMove(int generation)
        {
            // Callback stale (es. reset durante il turno del PC): non agire mai.
            if (generation != _generation || _gameOver || _isHumanTurn)
                return;

            var free = new List<int>();
            for (int i = 0; i < Cells.Count; i++)
                if (_model.IsEmpty(i))
                    free.Add(i);

            if (free.Count == 0)
                return; // impossibile: dopo una mossa umana senza vittoria c'è sempre una casella libera

            int pick = free[_random.Next(free.Count)];
            if (!_model.TryPlaceMark(pick, Player.O))
                return; // casella già occupata: non aggiornare la UI

            Cells[pick].SetContent("O");

            if (!CheckEnd())
                EnterHumanTurn();
        }

        private void EnterHumanTurn()
        {
            _isHumanTurn = true;
            StatusText = HumanTurnStatus;
            UnlockFreeCells();
            CellClickCommand.RaiseCanExecuteChanged();
        }

        /// <summary>Verifica vittoria/pareggio. Se la partita continua, lo stato è già corretto: nessuna transizione ridondante.</summary>
        private bool CheckEnd()
        {
            char? winner = _model.GetWinner();
            if (winner.HasValue)
            {
                EndGame(winner.Value == 'X' ? "Hai vinto!" : "Il PC ha vinto. Riprova!");
                return true;
            }

            if (_model.IsFull())
            {
                EndGame("Pareggio!");
                return true;
            }

            return false;
        }

        private void EndGame(string message)
        {
            _gameOver = true;
            _isHumanTurn = false; // a game-over non c'è turno umano
            StatusText = message;
            LockAllCells();
            CellClickCommand.RaiseCanExecuteChanged();
        }

        private void ResetGame()
        {
            _generation++; // invalida eventuali callback PC pendenti/stale
            _delay.Cancel(); // annulla una eventuale mossa PC pendente
            _model.Reset();
            _isHumanTurn = true;
            _gameOver = false;
            foreach (var cell in Cells)
                cell.Clear();
            StatusText = IdleStatus;
            CellClickCommand.RaiseCanExecuteChanged();
        }

        private void LockFreeCells()
        {
            foreach (var cell in Cells)
                if (_model.IsEmpty(cell.Index))
                    cell.Lock();
        }

        private void UnlockFreeCells()
        {
            foreach (var cell in Cells)
                if (_model.IsEmpty(cell.Index))
                    cell.Unlock();
        }

        private void LockAllCells()
        {
            foreach (var cell in Cells)
                cell.Lock();
        }
    }
}
