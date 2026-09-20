using System;
using System.Windows.Threading;

namespace TicTacToe.Services
{
    /// <summary>Sorgente di casualità per la mossa del PC (iniettabile per test deterministici).</summary>
    public interface IRandomProvider
    {
        /// <summary>Ritorna un intero in [0, exclusiveMax).</summary>
        int Next(int exclusiveMax);
    }

    /// <summary>Schedula un'azione ritardata (delay UI) e permette di annullarla.</summary>
    public interface IUiDelayScheduler
    {
        /// <summary>Pianifica l'esecuzione di action dopo delay, annullando eventuali azioni pendenti.</summary>
        void Schedule(Action action, TimeSpan delay);

        /// <summary>Annulla l'azione pendente (es. reset durante il turno del PC).</summary>
        void Cancel();
    }

    /// <summary>Implementazione di produzione: casualità reale.</summary>
    public sealed class SystemRandomProvider : IRandomProvider
    {
        private readonly Random _random;

        public SystemRandomProvider() : this(Random.Shared)
        {
        }

        public SystemRandomProvider(Random random) => _random = random ?? throw new ArgumentNullException(nameof(random));

        public int Next(int exclusiveMax) => _random.Next(exclusiveMax);
    }

    /// <summary>Implementazione di produzione: breve delay UI tramite DispatcherTimer.</summary>
    public sealed class DispatcherDelayScheduler : IUiDelayScheduler
    {
        private readonly DispatcherTimer _timer;
        private Action? _pending;

        public DispatcherDelayScheduler()
        {
            _timer = new DispatcherTimer();
            _timer.Tick += (_, _) =>
            {
                var action = _pending;
                _pending = null;
                _timer.Stop();
                action?.Invoke();
            };
        }

        public void Schedule(Action action, TimeSpan delay)
        {
            if (action is null) throw new ArgumentNullException(nameof(action));
            Cancel();
            _pending = action;
            _timer.Interval = delay;
            _timer.Start();
        }

        public void Cancel()
        {
            _pending = null;
            _timer.Stop();
        }
    }
}
