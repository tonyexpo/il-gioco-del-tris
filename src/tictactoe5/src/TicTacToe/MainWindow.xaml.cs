using System.Windows;
using TicTacToe.ViewModels;

namespace TicTacToe;

/// <summary>
/// Composition root: crea il ViewModel principale e lo assegna come DataContext.
/// </summary>
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        DataContext = new MainViewModel();
    }
}
