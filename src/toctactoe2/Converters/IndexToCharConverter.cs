// Questo è un Converter necessario perché i pulsanti devono mostrare lo stato del gioco (X, O o vuoto), 
// ma il DataContext li sta vedendo come ICommand (che non ha una rappresentazione visiva diretta).
using System;
using System.Globalization;
using System.Windows.Data;

namespace TicTacToeWPF.Converters
{
    public class IndexToCharConverter : IValueConverter
    {
        // NOTA SENIOR: Questo converter è un placeholder concettuale. 
        // In WPF, per mostrare lo stato del gioco (X/O) in tempo reale, il ViewModel dovrebbe esporre 
        // una proprietà ObservableCollection<char> che viene legata direttamente ai pulsanti, non i comandi ICommand.
        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (parameter is string charValue && !string.IsNullOrEmpty(charValue))
            {
                return charValue[0]; // Restituisce il carattere desiderato dal CommandParameter
            }
            // Se non è specificato un parametro o se lo stato è vuoto, restituisci uno spazio.
            return ' '; 
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}