// Regole di decisione e ordinamento delle foto (logica pura, senza rete).
import { RULES } from './config.mjs';

export const LABELS_IT = {
  cleanliness: { clean: 'pulito', slightly_dirty: 'lievemente sporco', dirty: 'sporco' },
  integrity: { intact: 'integro', cracked: 'crepato', broken: 'rotto' },
};

// result: output normalizzato di api.mjs. Ritorna { action, grade, reasons, low_confidence }.
export function decide(result, rules = RULES) {
  if (result.egg_visible != null && result.egg_visible < rules.minEggVisible) {
    return { action: 'UNREADABLE', grade: '-', reasons: ['uovo non rilevato'], low_confidence: false };
  }
  const reasons = [];
  if (result.integrity.label !== 'intact') reasons.push(LABELS_IT.integrity[result.integrity.label]);
  if (result.cleanliness.label === 'dirty') reasons.push('sporco');
  if (result.cleanliness.label === 'slightly_dirty' && !rules.acceptSlightlyDirty) reasons.push('lievemente sporco');

  const confs = [result.cleanliness.confidence, result.integrity.confidence].filter(c => c != null);
  const low_confidence = confs.length > 0 && Math.min(...confs) < rules.lowConfidence;

  if (reasons.length) return { action: 'DISCARD', grade: '-', reasons, low_confidence };
  return { action: 'ACCEPT', grade: result.cleanliness.label === 'clean' ? 'A' : 'B', reasons: [], low_confidence };
}

// Probabilità dell'etichetta scelta (Decisions) oppure null (LLM).
export function labelProb(answer) {
  return answer.probs?.[answer.label] ?? answer.confidence ?? null;
}

// PRNG deterministico (mulberry32) per un mescolamento riproducibile.
function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6D2B79F5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function shuffle(arr, seed) {
  const r = rng(seed), a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

// Alterna uova bianche e uova di altre tonalità (marroni, cartoni misti), ciascun gruppo mescolato.
export function interleaveByTone(images, seed = 14) {
  const white = shuffle(images.filter(i => i.tone === 'white'), seed);
  const other = shuffle(images.filter(i => i.tone !== 'white'), seed + 1);
  const out = [];
  for (let i = 0; i < Math.max(white.length, other.length); i++) {
    if (i < white.length) out.push(white[i]);
    if (i < other.length) out.push(other[i]);
  }
  return out;
}
