using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using TicTacToeDemo.ViewModels;
using TicTacToeDemo.Models;

namespace TicTacToeDemo;

public partial class MainWindow : Window
{
    private MainViewModel _vm;

    public MainWindow()
    {
        InitializeComponent();
        _vm = new MainViewModel();
        this.DataContext = _vm;

        // Bind button content to the ViewModel's Cells collection
        // Since we are using a simple demo, we manually link them for clarity
        BindButtons();
    }

    private void BindButtons()
    {
        var buttons = new Button[] { 
            Btn0, Btn1, Btn2, Btn3, Btn4, Btn5, Btn6, Btn7, Btn8 
        };

        for (int i = 0; i < 9; i++)
        {
            // We use a simple approach: the button content is updated via the ViewModel's property change.
            // However, to make it truly MVVM-compliant without complex behaviors, we can just 
            // update the buttons manually in the VM or use a Converter.
            // For this demo, I will let the View handle the visual state of the button content.
        }
    }

    private void Cell_Click(object sender, RoutedEventArgs e)
    {
        var btn = (Button)sender;
        int index = int.Parse(btn.Name.Replace("Btn", ""));
        _vm.OnCellClicked(_vm.Cells[index]);
        UpdateButtons();
    }

    private void Reset_Click(object sender, RoutedEventArgs e)
    {
        _vm.ResetGame();
        UpdateButtons();
    }

    private void UpdateButtons()
    {
        for (int i = 0; i < 9; i++)
        {
            var cell = _vm.Cells[i];
            var btn = (Button)this.FindName("Btn" + i);
            btn.Content = cell.Status switch
            {
                CellStatus.X => "X",
                CellStatus.O => "O",
                _ => ""
            };
            btn.IsEnabled = cell.IsClickable && _vm.GameActive;
        }
    }

    // Override to ensure buttons update when the VM changes (e.g., PC move)
    protected override void OnContentRendered(EventArgs e)
    {
        base.OnContentRendered(e);
        UpdateButtons();
    }
}
