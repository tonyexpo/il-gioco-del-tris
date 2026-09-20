namespace TicTacToe.ViewModels
{
    /// <summary>Stato di una singola casella della griglia.</summary>
    public class CellViewModel : ViewModelBase
    {
        private string _content = "";
        private bool _isLocked;

        public int Index { get; }

        /// <summary>Simbolo mostrato nella casella ("", "X" o "O").</summary>
        public string Content
        {
            get => _content;
            internal set => SetProperty(ref _content, value);
        }

        /// <summary>True se il pulsante della casella deve essere disabilitato.</summary>
        public bool IsLocked
        {
            get => _isLocked;
            internal set => SetProperty(ref _isLocked, value);
        }

        public CellViewModel(int index) => Index = index;

        /// <summary>Pone un simbolo nella casella e la blocca.</summary>
        public void SetContent(string content)
        {
            Content = content;
            IsLocked = true;
        }

        /// <summary>Blocca la casella senza modificarne il contenuto (turno del PC o fine partita).</summary>
        public void Lock() => IsLocked = true;

        /// <summary>Sblocca la casella.</summary>
        public void Unlock() => IsLocked = false;

        /// <summary>Svuota e sblocca la casella.</summary>
        public void Clear()
        {
            Content = "";
            IsLocked = false;
        }
    }
}
