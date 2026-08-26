using System;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Windows.Input;
using TicTacToeWPF.Models;

namespace TicTacToeWPF.ViewModels
{
    /// <summary>
    /// ViewModel principale che gestisce la logica di gioco, l'interazione con il Model e l'AI del PC.
    /// </summary>
    public class MainViewModel : INotifyPropertyChanged
    {
        private readonly GameModel _gameModel;
        private Random _random = new Random();

        // Proprietà per la notifica di cambiamenti UI (MVVM)
        public event PropertyChangedEventHandler? PropertyChanged;

        protected void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        private string _statusMessage = "Premi il primo pulsante per iniziare.";
        public string StatusMessage
        {
            get => _statusMessage;
            set { _statusMessage = value; OnPropertyChanged(nameof(StatusMessage)); }
        }

        private bool _isGameOver = true;
        public bool IsGameOver
        {
            get => _isGameOver;
            set { _isGameOver = value; OnPropertyChanged(nameof(IsGameOver)); }
        }

        private char _currentPlayer = 'X'; // Giocatore umano
        public char CurrentPlayer
        {
            get => _currentPlayer;
            set { _currentPlayer = value; OnPropertyChanged(nameof(CurrentPlayer)); }
        }

        // Collezione di comandi per i 9 pulsanti (per Data Binding)
        public ObservableCollection<ICommand> GridCommands { get; set; }

        public MainViewModel()
        {
            _gameModel = new GameModel();
            // Iscrizione all'evento del Model: ogni volta che il board cambia, aggiorniamo lo stato.
            _gameModel.BoardChanged += OnBoardChanged;

            GridCommands = new ObservableCollection<ICommand>();
            InitializeGame();
        }

        private void InitializeGame()
        {
            // Popola la collezione di comandi per i 9 pulsanti (indice 0 a 8)
            for (int i = 0; i < 9; i++)
            {
                GridCommands.Add(new RelayCommand<int>(HandleMove, CanExecuteMove));
            }
        }

        /// <summary>
        /// Gestisce la mossa del giocatore (X).
        /// </summary>
        private void HandleMove(int index)
        {
            if (!CanExecuteMove(index)) return;

            // 1. Esegui la mossa per il Giocatore ('X')
            if (_gameModel.MakeMove(index, 'X'))
            {
                CheckGameStatus('X');
            }
        }

        /// <summary>
        /// Logica di controllo del gioco dopo ogni mossa (vittoria/pareggio).
        /// </summary>
        private void CheckGameStatus(char lastPlayer)
        {
            if (_gameModel.CheckWin(lastPlayer))
            {
                StatusMessage = $"🎉 Hai vinto! 🎉";
                IsGameOver = true;
            }
            else if (_gameModel.CheckDraw())
            {
                StatusMessage = "🤝 Pareggio! 🤝";
                IsGameOver = true;
            }
            else
            {
                // Passa il turno al PC ('O')
                CurrentPlayer = 'O';
                Task.Run(async () => await Task.Delay(500)).Wait(); // Breve pausa per UX
                RunAICall();
            }
        }

        /// <summary>
        /// Logica di AI del PC ('O') - Mossa casuale.
        /// </summary>
        private async void RunAICall()
        {
            // 1. Trova tutte le mosse disponibili (caselle vuote)
            var availableMoves = new List<int>();
            for (int i = 0; i < 9; i++)
            {
                if (_gameModel.GetBoardState()[i] == ' ')
                {
                    availableMoves.Add(i);
                }
            }

            // 2. Scegli una mossa casuale tra quelle disponibili
            int randomIndex = _random.Next(availableMoves.Count);
            int moveIndex = availableMoves[randomIndex];

            // 3. Esegui la mossa del PC ('O')
            if (_gameModel.MakeMove(moveIndex, 'O'))
            {
                CheckGameStatus('O');
            }
        }


        /// <summary>
        /// Determina se il comando può essere eseguito (se non è finita la partita e l'indice è vuoto).
        /// </summary>
        private bool CanExecuteMove(int index)
        {
            return !IsGameOver && _gameModel.GetBoardState()[index] == ' ';
        }

        /// <summary>
        /// Gestisce il reset del gioco (richiesto dal pulsante dedicato).
        /// </summary>
        public void ResetGameCommand()
        {
            _gameModel.ResetGame();
            StatusMessage = "Partita resettata. Inizia a giocare!";
            IsGameOver = false;
            CurrentPlayer = 'X'; // Il giocatore inizia sempre
        }

        // Gestore di eventi del Model (sincronizza lo stato UI)
        private void OnBoardChanged(char[] newBoardState)
        {
            // In un'implementazione completa, si dovrebbe notificare un'altra proprietà che contiene l'array board.
            // Per ora, ci basiamo sullo stato di IsGameOver/StatusMessage e il binding XAML deve leggere lo stato dal Model.
        }

        /// <summary>
        /// Comando che viene chiamato quando l'utente clicca sul pulsante Reset.
        /// </summary>
        public ICommand ResetCommand => new RelayCommand(ResetGameCommand);
    }

    // --- Implementazioni di supporto per MVVM ---

    /// <summary>
    /// Classe generica per implementare un comando che accetta parametri (per i pulsanti della griglia).
    /// </summary>
    public class RelayCommand<T> : ICommand
    {
        private readonly Action<T> _execute;
        private readonly Func<T, bool> _canExecute;

        public event EventHandler? CanExecuteChanged
        {
            add { CommandManager.RequerySuggested += value; }
            remove { CommandManager.RequerySuggested -= value; }
        }

        public RelayCommand(Action<T> execute, Func<T, bool>? canExecute = null)
        {
            _execute = execute ?? throw new ArgumentNullException(nameof(execute));
            _canExecute = canExecute;
        }

        public bool CanExecute(object? parameter) => _canExecute == null || _canExecute((T)parameter);
        public void Execute(object? parameter) => _execute((T)parameter);
    }