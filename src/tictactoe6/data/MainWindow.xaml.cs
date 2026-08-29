using System;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace TicTacToe
{
    public partial class MainWindow : Window
    {
        private Button[] _cells = null!;
        private readonly char[] _board = new char[9]; // ' ', 'X', 'O'
        private bool _gameOver;
        private bool _pcThinking;

        private static readonly int[][] Lines =
        {
            new[] { 0, 1, 2 }, new[] { 3, 4, 5 }, new[] { 6, 7, 8 }, // righe
            new[] { 0, 3, 6 }, new[] { 1, 4, 7 }, new[] { 2, 5, 8 }, // colonne
            new[] { 0, 4, 8 }, new[] { 2, 4, 6 }                     // diagonali
        };

        public MainWindow()
        {
            InitializeComponent();
            _cells = new[] { Cell0, Cell1, Cell2, Cell3, Cell4, Cell5, Cell6, Cell7, Cell8 };
            ResetBoard();
        }

        private async void OnCellClick(object sender, RoutedEventArgs e)
        {
            if (_gameOver || _pcThinking) return;
            int idx = int.Parse((string)((Button)sender).Tag);
            if (_board[idx] != ' ') return;

            // Il primo click su una casella avvia la partita: il giocatore mette X
            Place(idx, 'X');
            string? result = GetResult();
            if (result != null) { Finish(result); return; }

            // Tocca al PC: sceglie a caso una casella libera e mette O
            _pcThinking = true;
            StatusText.Text = "Il PC sta giocando...";
            await Task.Delay(350);

            int[] empties = Enumerable.Range(0, 9).Where(i => _board[i] == ' ').ToArray();
            if (empties.Length > 0)
                Place(empties[Random.Shared.Next(empties.Length)], 'O');

            result = GetResult();
            if (result != null) Finish(result);
            else StatusText.Text = "Tocca a te (X).";
            _pcThinking = false;
        }

        private void Place(int idx, char mark)
        {
            _board[idx] = mark;
            var b = _cells[idx];
            b.Content = mark.ToString();
            b.Foreground = mark == 'X' ? Brushes.DodgerBlue : Brushes.Crimson;
        }

        private string? GetResult()
        {
            foreach (var line in Lines)
            {
                char a = _board[line[0]];
                if (a != ' ' && a == _board[line[1]] && a == _board[line[2]])
                    return a.ToString();
            }
            if (_board.All(c => c != ' ')) return "draw";
            return null;
        }

        private void Finish(string result)
        {
            _gameOver = true;
            StatusText.Text = result == "X" ? "Hai vinto! Ottimo lavoro."
                              : result == "O" ? "Ha vinto il PC (O). Ricomincia!"
                                              : "Pareggio. Nessun vincitore.";
            foreach (var b in _cells) b.IsEnabled = false;
        }

        private void OnResetClick(object sender, RoutedEventArgs e) => ResetBoard();

        private void ResetBoard()
        {
            for (int i = 0; i < 9; i++) _board[i] = ' ';
            foreach (var b in _cells)
            {
                b.Content = string.Empty;
                b.Foreground = Brushes.Black;
                b.IsEnabled = true;
            }
            _gameOver = false;
            _pcThinking = false;
            StatusText.Text = "Sei sempre X. Tocca una casella per iniziare.";
        }
    }
}