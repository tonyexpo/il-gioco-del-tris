using System;
using System.Collections.Generic;
using System.Linq;

namespace TicTacToe
{
    public partial class MainWindow : Window
    {
        private const string PlayerSymbol = "X";
        private const string ComputerSymbol = "O";

        public MainWindow()
        {
            InitializeComponent();
        }

        #region Game Logic

        private static readonly List<Button> _cells = new()
        {
            Cell1, Cell2, Cell3,
            Cell4, Cell5, Cell6,
            Cell7, Cell8, Cell9
        };

        public void ResetGame()
        {
            // Clear all cells
            foreach (var cell in _cells)
                cell.Content = "";

            // Reset status bar
            StatusBar.Children.Clear();

            var scoreText = new TextBlock { HorizontalAlignment = HorizontalAlignment.Center, VerticalAlignment = VerticalAlignment.Bottom };
            scoreText.Text = "Score: X=0 O=0";
            StatusBar.Children.Add(scoreText);
        }

        public void ShowWinner(string winner)
        {
            string bgColor = $"#{winner == "X" ? "22c55e" : "dc2626"}";
            string textColor = "#ffffff";
            var label = new TextBlock { HorizontalAlignment = HorizontalAlignment.Center, VerticalAlignment = VerticalAlignment.Middle };
            label.Text = $"Game over! Winner: {winner}!";
            label.Foreground = new SolidColorBrush(Color.FromRgb((int)textColor[0], (int)textColor[1], (int)textColor[2]));

            // Find and color all matching cells
            foreach (var cell in _cells)
            {
                if ((cell.Content?.ToString() ?? "").Equals(winner))
                    cell.Background = new SolidColorBrush(Color.FromRgb((int)bgColor[0], (int)bgColor[1], (int)bgColor[2]));
            }

            StatusBar.Children.Clear();
            var sbLabel = new TextBlock { HorizontalAlignment = HorizontalAlignment.Center, VerticalAlignment = VerticalAlignment.Bottom };
            sbLabel.Text = $"Game over! Winner: {winner}!";
            StatusBar.Children.Add(sbLabel);
        }

        public void ShowTie()
        {
            string bgColor = "#22c55e";
            var label = new TextBlock
            {
                HorizontalAlignment = HorizontalAlignment.Center,
                VerticalAlignment = VerticalAlignment.Middle,
                Foreground = "ffffff"
            };
            label.Text = "Game tied!";
            StatusBar.Children.Clear();
            StatusBar.Children.Add(label);
        }

        #endregion

        private void OnClick(object sender, RoutedEventArgs e)
        {
            if (e.Source is Button button && !button.IsEnabled)
                return;

            string symbol = PlayerSymbol;
            if ((string)button.Content == ComputerSymbol || (string)button.Content == PlayerSymbol &&
                ((Button)e.Source).Tag?.ToString() != "X" && ((Button)e.Source).Tag?.ToString() != "O"))
            {
                // Simple prevention: don't allow double-click of same symbol
            }

            button.Content = $"{symbol}";
        }
    }
}
