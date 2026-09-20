using System.Windows;
using TicTacToe.ViewModels;

namespace TicTacToe.Views
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DataContext = new GameViewModel();
        }
    }
}
