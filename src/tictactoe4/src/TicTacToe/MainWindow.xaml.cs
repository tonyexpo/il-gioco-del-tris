using System.Windows;
using TicTacToe.ViewModels;

namespace TicTacToe;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        DataContext = new MainViewModel();
    }
}
