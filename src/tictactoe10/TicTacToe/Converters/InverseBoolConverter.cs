using System;
using System.Globalization;
using System.Windows.Data;

namespace TicTacToe.Converters
{
    /// <summary>Inverte un valore booleano (usato per IsEnabled = !IsLocked).</summary>
    public class InverseBoolConverter : IValueConverter
    {
        /// <summary>Inverte un bool; per valori non booleani ritorna false (non abilita).</summary>
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
            => value is bool b ? !b : false;

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
            => throw new NotSupportedException();
    }
}
