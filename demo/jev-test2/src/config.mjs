// Configurazione della demo: modelli, domande poste a ogni foto e regole di decisione.

export const MODELS = [
  { key: 'jev', label: 'Jev 1.14', id: 'typesafe/jev-1.14', kind: 'decisions' },
  { key: 'luna-decisions', label: 'GPT-6 Luna Decisions', id: 'openai/gpt-6-luna-decisions', kind: 'decisions' },
  { key: 'luna', label: 'GPT-6 Luna (LLM, raffronto)', id: 'openai/gpt-6-luna', kind: 'chat' },
  { key: 'sol', label: 'GPT-6.1 Sol (LLM, raffronto)', id: 'openai/gpt-6.1-sol', kind: 'chat' },
];

export const OPENROUTER_BASE = 'https://openrouter.ai/api';

// Nomi di variabile d'ambiente accettati per la chiave, in ordine di priorità.
// La chiave resta in process.env: non viene mai stampata né scritta su file.
export const API_KEY_ENV_NAMES = ['OPENROUTER_API_KEY', 'OPEN_ROUTER_KEY', 'OPEN_ROUTER'];

// Scale di valutazione. Gli id sono quelli che i modelli restituiscono.
export const CLEANLINESS = {
  clean: 'Guscio pulito: nessuna sporcizia, feci, sangue o macchie visibili (minuscoli puntini o timbri di stampa sono ammessi).',
  slightly_dirty: 'Guscio lievemente sporco: poche macchie, residui o aloni che coprono una piccola parte della superficie.',
  dirty: 'Guscio sporco: feci, sangue, fango, tuorlo o macchie evidenti su una parte significativa della superficie.',
};
export const INTEGRITY = {
  intact: 'Guscio integro: nessuna crepa, frattura, ammaccatura o perdita di contenuto visibile.',
  cracked: 'Guscio crepato: è visibile una crepa o una frattura (anche sottile) ma il guscio è ancora in un pezzo.',
  broken: 'Guscio rotto: pezzi mancanti, guscio sfondato o contenuto che fuoriesce.',
};

// Contesto comune: i dataset contengono sia uova singole sia confezioni con più uova.
export const CONTEXT =
  "Foto di controllo qualità di uova di gallina. Se nella foto ci sono più uova, valuta l'uovo in condizioni peggiori. " +
  'Valuta solo quello che vedi nel guscio.';

// Regole di decisione (uguali per tutti i modelli, così il raffronto è equo).
export const RULES = {
  // Sotto questa probabilità di "uovo visibile" la foto è marcata come non valutabile.
  minEggVisible: 0.5,
  // Le uova lievemente sporche restano utilizzabili (grado B); metti false per scartarle.
  acceptSlightlyDirty: true,
  // Sotto questa confidenza (solo modelli Decisions) l'etichetta è segnalata "da verificare".
  lowConfidence: 0.6,
};

export const IMAGE_MIME = 'image/jpeg';
export const REQUEST_TIMEOUT_MS = 120_000;
export const MAX_RETRIES = 3;
