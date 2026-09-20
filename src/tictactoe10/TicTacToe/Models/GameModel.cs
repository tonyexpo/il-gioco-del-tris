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

        /// <summary>True se l'indice identifica una casella della scacchiera (0..8).</summary>
        public bool IsValidIndex(int index) => index >= 0 && index < _board.Length;

        /// <summary>True se il giocatore è uno dei due validi (X o O).</summary>
        public static bool IsValidPlayer(Player player) => player == Player.X || player == Player.O;

        /// <summary>Simbolo nella casella ('X', 'O') oppure '\0' se libera.</summary>
        public char SymbolAt(int index)
        {
            if (!IsValidIndex(index))
                throw new ArgumentOutOfRangeException(nameof(index));
            return _board[index];
        }

        /// <summary>True se la casella esiste ed è libera.</summary>
        public bool IsEmpty(int index) => IsValidIndex(index) && _board[index] == '\0';

        /// <summary>
        /// Contratto: tenta di piazzare il simbolo del giocatore nella casella.
        /// Ritorna false (mossa rifiutata, scacchiera invariata) se:
        ///  - l'indice è fuori range;
        ///  - il player non è valido (diverso da X/O);
        ///  - la casella è già occupata.
        /// Ritorna true e aggiorna la scacchiera solo su successo.
        /// </summary>
        public bool TryPlaceMark(int index, Player player)
        {
            if (!IsValidIndex(index)) return false;
            if (!IsValidPlayer(player)) return false;
            if (_board[index] != '\0') return false;

            _board[index] = player == Player.X ? 'X' : 'O';
            return true;
        }

        /// <summary>
        /// Piazzamento con contratto forte: lancia un'eccezione se la mossa è illegale.
        ///  - indice fuori range   -> ArgumentOutOfRangeException
        ///  - player non valido    -> ArgumentException
        ///  - casella già occupata -> InvalidOperationException
        /// </summary>
        public void PlaceMark(int index, Player player)
        {
            if (TryPlaceMark(index, player))
                return;

            if (!IsValidIndex(index))
                throw new ArgumentOutOfRangeException(nameof(index), "Indice casella fuori range.");
            if (!IsValidPlayer(player))
                throw new ArgumentException("Giocatore non valido.", nameof(player));
            throw new InvalidOperationException($"La casella {index} è già occupata.");
        }

        /// <summary>Ritorna il simbolo del vincitore ('X' o 'O'), oppure null se non c'è vincitore (partita in corso o pareggio).</summary>
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
