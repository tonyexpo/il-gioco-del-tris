using System;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using TicTacToeDemo.Models;

namespace TicTacToeDemo.ViewModels;

public class MainViewModel : INotifyPropertyChanged
{
    private bool _gameActive = true;
    private string _statusMessage = "Player X's Turn";

    public ObservableCollection<GameCell> Cells { get; } = new();

    public string StatusMessage
    {
        get => _statusMessage;
        set { _statusMessage = value; OnPropertyChanged(); }
    }

    public bool GameActive
    {
        get => _gameActive;
        set { _gameActive = value; OnPropertyChanged(); }
    }

    public MainViewModel()
    {
        for (int i = 0; i < 9; i++)
        {
            Cells.Add(new GameCell { Index = i, Status = CellStatus.Empty });
        }
        StatusMessage = "Player X's Turn";
    }

    public void OnCellClicked(GameCell cell)
    {
        if (!GameActive || cell.Status != CellStatus.Empty) return;

        // Player Move (X)
        cell.Status = CellStatus.X;
        CheckWin();

        if (GameActive)
        {
            // PC Move (O) - Simple Random Logic with a small delay for UX
            System.Threading.Tasks.Task.Delay(500).ContinueWith(_ =>
            {
                MakePcMove();
            }).Wait(); 
        }
    }

    private void MakePcMove()
    {
        var availableCells = Cells.Where(c => c.Status == CellStatus.Empty).ToList();
        if (availableCells.Any())
        {
            var randomCell = availableCells[new Random().Next(availableCells.Count)];
            randomCell.Status = CellStatus.O;
            CheckWin();
        }
    }

    private void CheckWin()
    {
        // Utilizzo di un array jagged per evitare errori di indicizzazione
        int[][] winPatterns = new int[][]
        {
            new int[] {0, 1, 2}, new int[] {3, 4, 5}, new int[] {6, 7, 8}, // Rows
            new int[] {0, 3, 6}, new int[] {1, 4, 7}, new int[] {2, 5, 8}, // Cols
            new int[] {0, 4, 8}, new int[] {2, 4, 6}                        // Diagonals
        };

        bool win = false;
        foreach (var pattern in winPatterns)
        {
            var c1 = Cells[pattern[0]].Status;
            var c2 = Cells[pattern[1]].Status;
            var c3 = Cells[pattern[2]].Status;

            if (c1 == c2 && c2 == c3 && c1 != CellStatus.Empty)
            {
                win = true;
                break;
            }
        }

        if (win)
        {
            GameActive = false;
            StatusMessage = "Game Over!";
        }
        else if (!Cells.Any(c => c.Status == CellStatus.Empty))
        {
            GameActive = false;
            StatusMessage = "Draw!";
        }
        else
        {
            StatusMessage = "Player O's Turn";
        }
    }

    public void ResetGame()
    {
        for (int i = 0; i < 9; i++)
        {
            Cells[i].Status = CellStatus.Empty;
        }
        GameActive = true;
        StatusMessage = "Player X's Turn";
    }

    public event PropertyChangedEventHandler? PropertyChanged;
    protected void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
