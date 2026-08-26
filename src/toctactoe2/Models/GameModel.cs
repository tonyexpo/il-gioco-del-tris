using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace TicTacToeWPF.Models
{
    /// <summary>
    /// Rappresenta lo stato del gioco e la logica di verifica delle condizioni di vittoria/pareggio.
    /// </summary>
    public class GameModel
    {
        // Stato della griglia: ' ' = vuoto, 'X' = Giocatore, 'O' = PC
        private char[] _board;
        public event Action<char[]> BoardChanged;

        public GameModel()
        {
            _board = new char[9];
            Array.Fill(_board, ' '); // Inizializza con spazi vuoti
        }

        /// <summary>
        /// Ottiene una copia immutabile dello stato attuale della griglia.
        /// </summary>
        public char[] GetBoardState()
        {
            return (char[])_board.Clone();
        }

        /// <summary>
        /// Tenta di piazzare un segno in una posizione specifica, se disponibile e non già occupata.
        /// Restituisce true se la mossa è stata effettuata con successo.
        /// </summary>
        public bool MakeMove(int index, char player)
        {
            if (index < 0 || index >= 9 || _board[index] != ' ')
            {
                return false; // Indice non valido o posizione già occupata
            }

            _board[index] = player;
            BoardChanged?.Invoke(_board);
            return true;
        }

        /// <summary>
        /// Controlla se la mossa corrente ha portato a una vittoria.
        /// </summary>
        public bool CheckWin(char lastPlayer)
        {
            // Tutte le combinazioni vincenti possibili (righe, colonne, diagonali)
            var winningCombinations = new List<int[]>
            {
                new[] { 0, 1, 2 }, // Riga 1
                new[] { 3, 4, 5 }, // Riga 2
                new[] { 6, 7, 8 }, // Riga 3
                new[] { 0, 3, 6 }, // Colonna 1
                new[] { 1, 4, 7 }, // Colonna 2
                new[] { 2, 5, 8 }, // Colonna 3
                new[] { 0, 4, 8 }, // Diagonale principale
                new[] { 2, 4, 6 }  // Diagonale secondaria
            };

            foreach (var combo in winningCombinations)
            {
                if (_board[combo[0]] == lastPlayer && _board[combo[1]] == lastPlayer && _board[combo[2]] == lastPlayer)
                {
                    return true; // Vittoria trovata
                }
            }
            return false;
        }

        /// <summary>
        /// Controlla se il gioco è terminato in pareggio (tutte le caselle sono piene).
        /// </summary>
        public bool CheckDraw()
        {
            // Se non ci sono spazi vuoti (' ') e non c'è stato un vincitore, è pareggio.
            return !_board.Contains(' ');
        }

        /// <summary>
        /// Resetta lo stato del gioco a quello iniziale.
        /// </summary>
        public void ResetGame()
        {
            Array.Fill(_board, ' ');
            BoardChanged?.Invoke(_board);
        }
    }
}