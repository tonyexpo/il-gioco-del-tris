using System;

namespace TicTacToe.Models
{
    /// <summary>
    /// Logica pura del gioco: stato della scacchiera e rilevamento di vittoria/pareggio.
    /// Nessuna dipendenza da UI, quindi testabile in isolamento.
    /// </summary>
    public class GameModel
    {
        private static readonly int[][] Lines =
        {
            new[] { 0, 1, 2 }, new[] { 3, 4, 5 }, new[] { 6, 7, 8 }, // righe
            new[] { 0, 3, 6 }, new[] { 1, 4, 7 }, new[] { 2, 5, 8 }, // colonne
            new[] { 0, 4, 8 }, new[] { 2, 4, 6 }                      // diagonali
        };

        private readonly char[] _board = new char[9]; // 'X', 'O' o '\0' (vuota)

        public bool IsEmpty(int index) => _board[index] == '\0';

        public void PlaceMark(int index, Player player)
            => _board[index] = player == Player.X ? 'X' : 'O';

        /// <summary>Ritorna il simbolo del vincitore ('X'/'O') oppure null se la partita non è finita.</summary>
        public char? GetWinner()
        {
            foreach (var line in Lines)
            {
                char a = _board[line[0]];
                if (a != '\0' && a == _board[line[1]] && a == _board[line[2]])
                    return a;
            }

            return null;
        }

        public bool IsFull()
        {
            for (int i = 0; i < _board.Length; i++)
                if (_board[i] == '\0')
                    return false;

            return true;
        }

        public void Reset() => Array.Clear(_board, 0, _board.Length);
    }
}
