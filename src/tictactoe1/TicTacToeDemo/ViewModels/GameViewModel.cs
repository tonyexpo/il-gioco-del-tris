using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;

namespace TicTacToeDemo.ViewModels
{
    public class GameViewModel : INotifyPropertyChanged
    {
        private string _statusText = "Turno di X (Giocatore)";
        private string _message = "Inizia a giocare!";
        private bool _isGameActive = false;
        private int _currentPlayer = 1; // 1 per X, 2 per O
        private Random _random = new Random();

        public event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, propertyName == nameof(StatusText) ? _statusText : propertyName == nameof(Message) ? _message : null);
        }

        public string StatusText
        {
            get => _statusText;
            set { _statusText = value; OnPropertyChanged(); }
        }

        public string Message
        {
            get => _message;
            set { _message = value; OnPropertyChanged(); }
        }

        public bool IsGameActive
        {
            get => _isGameActive;
            set { _isGameActive = value; OnPropertyChanged(); }
        }

        public int CurrentPlayer
        {
            get => _currentPlayer;
            set { _currentPlayer = value; OnPropertyChanged(); }
        }

        public bool ResetGame()
        {
            // Logica di reset: riavvia il gioco con X come primo giocatore
            _isGameActive = true;
            _currentPlayer = 1; // X inizia sempre
            _statusText = "Turno di X (Giocatore)";
            _message = "Gioco riavviato. Turno di X.";
            return true;
        }

        // Logica per la logica casuale (se richiesta) - qui implementiamo una semplice scelta casuale del primo movimento
        public void StartNewGameRandomly()
        {
            if (_isGameActive) return;

            // In un gioco reale, si genererebbe una posizione casuale. Per semplicità demo, gestiamo solo il reset per ora.
            // La logica di gioco vera e propria sarà gestita dal codice del View/Code-Behind o da eventi.
            ResetGame(); // Per ora, usiamo il reset come punto di partenza per la logica casuale richiesta.
        }
    }
}