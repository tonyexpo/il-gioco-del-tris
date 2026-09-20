using System;
using System.Windows.Input;

namespace TicTacToe.ViewModels
{
    /// <summary>Implementazione minimale di ICommand che delega l'esecuzione a una Action.</summary>
    public class RelayCommand : ICommand
    {
        private readonly Action<object?> _execute;
        private readonly Func<bool>? _canExecute;

        /// <summary>Crea un comando senza parametri (es. Reset).</summary>
        public RelayCommand(Action execute, Func<bool>? canExecute = null)
            : this(_ => execute(), canExecute)
        {
        }

        /// <summary>Crea un comando che riceve il parametro passato dal binding.</summary>
        public RelayCommand(Action<object?> execute, Func<bool>? canExecute = null)
        {
            _execute = execute;
            _canExecute = canExecute;
        }

        public bool CanExecute(object? parameter)
            => _canExecute?.Invoke() ?? true;

        public void Execute(object? parameter)
            => _execute(parameter);

        /// <summary>Notifica ai binding che lo stato di abilitazione potrebbe essere cambiato.</summary>
        public void RaiseCanExecuteChanged()
            => CanExecuteChanged?.Invoke(this, EventArgs.Empty);

        /// <summary>Evento richiesto da ICommand per notificare i cambiamenti di abilitazione.</summary>
        public event EventHandler? CanExecuteChanged;
    }
}
