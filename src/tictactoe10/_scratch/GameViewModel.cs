using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Windows.Threading;
using TicTacToe.Models;

namespace TicTacToe.ViewModels
{
    /// <summary>
    /// ViewModel principale del gioco.
    /// L'umano è sempre X e muove per primo (il primo clic sulla griglia avvia la partita);
    /// il PC è sempre O e risponde con una mossa casuale tra le caselle libere.
    /// </summary>
    public class GameViewModel : ViewModelBase
    {
        private const string HumanTurnStatus = "Tocca a te — clicca una casella (X)";
        private const string PcThinkingStatus = "Il PC sta pensando...";

        private readonly GameModel _model = new();
        private readonly DispatcherTimer _pcMoveDelay;
        private bool _isHumanTurn = true;
        private bool _gameOver;

        /// <summary>Le 9 caselle della griglia (in ordine di lettura, da sinistra a destra).</summary>
        public ObservableCollection<CellViewModel> Cells { get; }

        public RelayCommand ResetCommand { get; }
        public RelayCommand CellClickCommand { get; }

        private string _statusText = HumanTurnStatus;

        /// <summary>Messaggio di stato mostrato sopra la griglia.</summary>
        public string StatusText
        {
            get => _statusText;
            private set => SetProperty(ref _statusText, value);
        }

        public GameViewModel()
        {
            Cells = new ObservableCollection<CellViewModel>();
            for (int i = 0; i < 9; i++)
                Cells.Add(new CellViewModel(i));

            ResetCommand = new RelayCommand(ResetGame);
            CellClickCommand = new RelayCommand(OnCellClicked, () => _isHumanTurn && !_gameOver);

            // Breve pausa prima della mossa del PC: rende il gioco più naturale.
            _pcMoveDelay = new DispatcherTimer { Interval = TimeSpan.FromMilliseconds(400) };
            _pcMoveDelay.Tick += (_, _) =>
            {
                _pcMoveDelay.Stop();
                PcMove();
            };
        }

        private void OnCellClicked(object parameter)
        {
            if (parameter is not CellViewModel cell || _gameOver || !_isHumanTurn)
                return;
            if (!_model.IsEmpty(cell.Index))
                return;

            // 1) Mossa dell'umano (X).
            _model.PlaceMark(cell.Index, Player.X);
            cell.SetContent("X");

            if (CheckEnd())
                return;

            // 2) Turno del PC: si bloccano le caselle libere in attesa della mossa.
            _isHumanTurn = false;
            StatusText = PcThinkingStatus;
            LockFreeCells();
            _pcMoveDelay.Start();
        }

        private void PcMove()
        {
            var free = new List<int>();
            for (int i = 0; i < Cells.Count; i++)
                if (_model.IsEmpty(i))
                    free.Add(i);

            if (free.Count == 0)
                return;

            // Logica randomica del PC: sceglie una casella libera a caso.
            int pick = free[Random.Shared.Next(free.Count)];
            _model.PlaceMark(pick, Player.O);
            Cells[pick].SetContent("O");

            _isHumanTurn = true;
            CheckEnd();
        }

        /// <summary>Verifica vittoria/pareggio e aggiorna stato e lock delle caselle.</summary>
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

            UnlockFreeCells();
            StatusText = HumanTurnStatus;
            return false;
        }

        private void EndGame(string message)
        {
            _gameOver = true;
            StatusText = message;
            LockAllCells();
        }

        private void ResetGame()
        {
            _pcMoveDelay.Stop();
            _model.Reset();
            _isHumanTurn = true;
            _gameOver = false;
            foreach (var cell in Cells)
                cell.Clear();
            StatusText = HumanTurnStatus;
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
