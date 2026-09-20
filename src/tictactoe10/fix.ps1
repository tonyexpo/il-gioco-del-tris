$ErrorActionPreference = 'Stop'
function GetNL([string]$path) {
    if ([IO.File]::ReadAllText($path).Contains("`r`n")) { return "`r`n" } else { return "`n" }
}
function Apply([string]$path, [string[]]$beforeLines, [string[]]$afterLines) {
    $nl = GetNL $path
    $t  = [IO.File]::ReadAllText($path)
    $before = ($beforeLines -join $nl)
    $after  = ($afterLines -join $nl)
    if (-not $t.Contains($before)) { Write-Output "MISS: $path"; return }
    $n = ([regex]::Matches($t, [regex]::Escape($before))).Count
    if ($n -ne 1) { Write-Output "AMBIGUOUS($n): $path"; return }
    [IO.File]::WriteAllText($path, $t.Replace($before, $after), (New-Object Text.UTF8Encoding $false))
    Write-Output "OK: $path"
}

$base = 'C:\Users\Antonio Esposito\Desktop\tictactoe10\TicTacToe'
$vm = "$base\ViewModels\GameViewModel.cs"
$rc = "$base\ViewModels\RelayCommand.cs"

Apply $rc `
  @('        public event EventHandler? CanExecuteChanged;') `
  @(
    '        /// <summary>Notifica ai binding che lo stato di abilitazione potrebbe essere cambiato.</summary>',
    '        public void RaiseCanExecuteChanged()',
    '            => CanExecuteChanged?.Invoke(this, EventArgs.Empty);',
    '',
    '        public event EventHandler? CanExecuteChanged;'
  )

Apply $vm @('private void OnCellClicked(object parameter)') @('private void OnCellClicked(object? parameter)')

Apply $vm `
  @('            LockFreeCells();','            _pcMoveDelay.Start();','        }') `
  @('            LockFreeCells();','            _pcMoveDelay.Start();','            CellClickCommand.RaiseCanExecuteChanged();','        }')

Apply $vm `
  @('            _isHumanTurn = true;','            CheckEnd();','        }') `
  @('            _isHumanTurn = true;','            CheckEnd();','            CellClickCommand.RaiseCanExecuteChanged();','        }')

Apply $vm `
  @('            _gameOver = true;','            StatusText = message;','            LockAllCells();','        }') `
  @('            _gameOver = true;','            StatusText = message;','            LockAllCells();','            CellClickCommand.RaiseCanExecuteChanged();','        }')

Apply $vm `
  @('            StatusText = HumanTurnStatus;','        }','','        private void LockFreeCells()') `
  @('            StatusText = HumanTurnStatus;','            CellClickCommand.RaiseCanExecuteChanged();','        }','','        private void LockFreeCells()')
