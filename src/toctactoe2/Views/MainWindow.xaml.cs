using System.Windows;
using System.Windows.Controls;
using TicTacToeWPF.ViewModels;

namespace TicTacToeWPF.Views
{
    /// <summary>
    /// View principale per il gioco Tic Tac Toe. Implementa la logica di Data Binding MVVM.
    /// </summary>
    public partial class MainWindow : Window
    {
        private MainViewModel ViewModel { get; set; }

        public MainWindow()
        {
            InitializeComponent();
            // Inizializza il ViewModel e lo imposta come DataContext
            ViewModel = new MainViewModel();
            this.DataContext = ViewModel;
        }
    }
}