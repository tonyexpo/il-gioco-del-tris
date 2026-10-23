// fetch finto per provare la demo senza chiave né rete (--mock).
// Restituisce risposte con la stessa forma di OpenRouter, quindi passa dal parsing reale.
// I risultati finiscono in results/mock e reports/mock: non sono analisi vere.
import { createHash } from 'node:crypto';

function pick(seed, salt, weights) {
  const h = createHash('sha256').update(seed + salt).digest();
  const x = h.readUInt32BE(0) / 2 ** 32;
  let acc = 0;
  for (const [k, w] of Object.entries(weights)) { acc += w; if (x < acc) return k; }
  return Object.keys(weights).at(-1);
}

export function mockFetch() {
  return async (url, opts) => {
    const body = JSON.parse(opts.body);
    const seed = createHash('sha256').update(opts.body).digest('hex');
    const cleanliness = pick(seed, 'c', { clean: 0.6, slightly_dirty: 0.25, dirty: 0.15 });
    const integrity = pick(seed, 'i', { intact: 0.5, cracked: 0.35, broken: 0.15 });
    await new Promise(r => setTimeout(r, 20 + (seed.charCodeAt(0) % 40)));
    const json = (o) => ({ ok: true, status: 200, text: async () => JSON.stringify(o) });
    if (url.endsWith('/alpha/decisions')) {
      const p = (label, labels) => Object.fromEntries(labels.map(l => [l, l === label ? 0.9 : 0.05]));
      return json({
        id: 'gen-dec-mock', model: `${body.model}-mock`, provider: 'mock',
        answers: {
          egg_visible: { type: 'noul', noul: 0.97 },
          cleanliness: { type: 'choice', choice: cleanliness, probabilities: p(cleanliness, ['clean', 'slightly_dirty', 'dirty']), confidence: 0.85 },
          integrity: { type: 'choice', choice: integrity, probabilities: p(integrity, ['intact', 'cracked', 'broken']), confidence: 0.85 },
        },
        usage: { input_tokens: 1500, output_tokens: 0, cost: 0.00006 },
      });
    }
    return json({
      id: 'gen-mock', model: `${body.model}-mock`,
      choices: [{ finish_reason: 'stop', message: { content: JSON.stringify({ egg_visible: true, cleanliness, integrity, reason: 'risposta simulata' }) } }],
      usage: { prompt_tokens: 1500, completion_tokens: 40, cost: 0.0002 },
    });
  };
}
