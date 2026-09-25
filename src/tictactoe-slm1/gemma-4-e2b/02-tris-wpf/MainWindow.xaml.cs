using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace TicTacToeWpf
{
    public partial class MainWindow : Window
    {
        private string[] board = new string[9]; // Represents the 3x3 board
        private string currentPlayer = "X"; // Human starts as X
        private bool isGameActive = true;

        public MainWindow()
        {
            InitializeComponent();
            InitializeGame();
        }

        private void InitializeGame()
        {
            // Initialize the board state (all cells are empty)
            for (int i = 0; i < 9; i++)
            {
                board[i] = "";
                // Set initial border colors to a default block color if needed, though XAML sets them initially.
            }
            currentPlayer = "X"; // Human starts
            isGameActive = true;
            UpdateStatus();
        }

        private void Cell_Click(object sender, RoutedEventArgs e)
        {
            if (!isGameActive || board[this.GetCellIndex(sender)] != "")
                return;

            int index = this.GetCellIndex(sender);

            // Place the current player's mark (X or O)
            board[index] = currentPlayer;

            // Update the visual appearance of the clicked block (Minecraft style)
            UpdateCellVisual(index, currentPlayer);

            // Check for game end conditions
            if (CheckForWinner())
            {
                EndGame();
            }
            else if (CheckForDraw())
            {
                EndGame();
            }
            else
            {
                // Switch player if the game continues
                currentPlayer = (currentPlayer == "X") ? "O" : "X";
                UpdateStatus();
            }
        }

        private int GetCellIndex(object sender)
        {
            // This method needs to map the clicked Border element back to its index (0-8).
            // Since we are using named elements in XAML, we need a way to map the click event source.
            // In a real WPF scenario, this is often done by setting DataContext or using a custom control.
            // For simplicity here, we rely on the names defined in XAML (Cell00, Cell01, etc.)
            if (sender is Border cell)
            {
                string name = cell.Name;
                if (name.StartsWith("Cell"))
                {
                    // Extract the last two digits as the index
                    return int.Parse(name.Substring(4));
                }
            }
            return -1; // Should not happen
        }

        private void UpdateCellVisual(int index, string player)
        {
            string cellName = $"Cell{index / 3}{index % 3}";
            var cell = this.FindName(cellName) as Border;

            if (cell != null)
            {
                // Set the background color based on the player
                if (player == "X")
                {
                    cell.Background = new SolidColorBrush(Colors.LightGreen); // Green for X
                }
                else if (player == "O")
                {
                    cell.Background = new SolidColorBrush(Colors.LightBlue); // Blue for O
                }
            }
        }

        private bool CheckForWinner()
        {
            // Check rows, columns, and diagonals
            for (int i = 0; i < 3; i++)
            {
                // Check row i
                if (board[i] == board[0] && board[i] == board[1] && board[i] == board[2]) return true;
                // Check column i
                if (board[0][i] == board[1][i] && board[0][i] == board[2][i]) return true;
            }

            // Check diagonals
            if (board[0][0] == board[1][1] && board[0][0] == board[2][2]) return true;
            if (board[0][2] == board[1][1] && board[0][2] == board[2][0]) return true;

            return false;
        }

        private bool CheckForDraw()
        {
            for (int i = 0; i < 9; i++)
            {
                if (board[i] == "") return false;
            }
            return true;
        }

        private void EndGame()
        {
            isGameActive = false;
            string message = "";

            // Determine winner or draw
            for (int i = 0; i < 9; i++)
            {
                if (board[i] == "X")
                {
                    message = "Human (X) Wins!";
                    break;
                }
                if (board[i] == "O")
                {
                    message = "PC (O) Wins!";
                    break;
                }
            }

            if (message == "")
            {
                message = "It's a Draw!";
            }

            UpdateStatus(message);
        }

        private void UpdateStatus(string message = "")
        {
            if (string.IsNullOrEmpty(message))
            {
                if (isGameActive)
                {
                    UpdateStatus("Status: Waiting for X to move...");
                }
                else
                {
                    UpdateStatus("Game Over!");
                }
            }
            else
            {
                UpdateStatus(message);
            }
        }

        private void ResetButton_Click(object sender, RoutedEventArgs e)
        {
            InitializeGame();
            UpdateStatus("Game has been reset. X starts.");
        }
    }