// Chiamate a OpenRouter: Decisions API (Jev, GPT-6 Luna Decisions) e Chat Completions (GPT-6 Luna).
import { readFile } from 'node:fs/promises';
import {
  API_KEY_ENV_NAMES, OPENROUTER_BASE, CLEANLINESS, INTEGRITY, CONTEXT,
  IMAGE_MIME, REQUEST_TIMEOUT_MS, MAX_RETRIES,
} from './config.mjs';

export function findApiKey(env = process.env) {
  for (const name of API_KEY_ENV_NAMES) if (env[name]) return { name, value: env[name] };
  return null;
}

export async function toDataUrl(path) {
  return `data:${IMAGE_MIME};base64,${(await readFile(path)).toString('base64')}`;
}

export class ApiError extends Error {
  constructor(message, status) { super(message); this.status = status; }
}

async function post(path, body, apiKey, fetchImpl = fetch) {
  let lastErr;
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      const res = await fetchImpl(`${OPENROUTER_BASE}${path}`, {
        method: 'POST',
        headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
      });
      const text = await res.text();
      let json; try { json = JSON.parse(text); } catch { /* corpo non JSON */ }
      if (res.ok) return json;
      const msg = json?.error?.message ?? text.slice(0, 300);
      const retryable = res.status === 429 || res.status >= 500;
      lastErr = new ApiError(`HTTP ${res.status}: ${msg}`, res.status);
      if (!retryable) throw lastErr;
    } catch (e) {
      if (e instanceof ApiError && !(e.status === 429 || e.status >= 500)) throw e;
      lastErr = e instanceof ApiError ? e : new ApiError(`${e.name}: ${e.message}`, 0);
    }
    if (attempt < MAX_RETRIES) await new Promise(r => setTimeout(r, 1000 * 2 ** (attempt - 1)));
  }
  throw lastErr;
}

// ---------------------------------------------------------------- Decisions API

const describe = (map) => Object.fromEntries(Object.entries(map).map(([k, v]) => [k, v]));

export function decisionsBody(model, imageUrl) {
  return {
    model: model.id,
    state: [CONTEXT, { type: 'image_url', image_url: { url: imageUrl } }],
    questions: {
      egg_visible: {
        type: 'noul',
        instructions: "L'immagine mostra almeno un uovo di gallina intero?",
        criteria: {
          true: 'Nella foto si vede almeno un uovo di gallina intero.',
          false: 'Nella foto non ci sono uova di gallina (altro oggetto, immagine vuota o illeggibile).',
        },
      },
      cleanliness: { type: 'choice', instructions: 'Qual è il grado di pulizia del guscio?', criteria: describe(CLEANLINESS) },
      integrity: { type: 'choice', instructions: "Qual è l'integrità del guscio?", criteria: describe(INTEGRITY) },
    },
  };
}

export function parseDecisions(json) {
  const a = json?.answers;
  if (!a?.cleanliness?.choice || !a?.integrity?.choice) throw new ApiError('Risposta Decisions senza le risposte attese', 0);
  const pick = (x) => ({ label: x.choice, probs: x.probabilities ?? null, confidence: x.confidence ?? null });
  return {
    served_model: json.model ?? null,
    egg_visible: a.egg_visible?.noul ?? null,
    cleanliness: pick(a.cleanliness),
    integrity: pick(a.integrity),
    reason: null,
    usage: { input_tokens: json.usage?.input_tokens ?? null, output_tokens: json.usage?.output_tokens ?? null, cost: json.usage?.cost ?? null },
  };
}

export async function inspectWithDecisions(model, imageUrl, apiKey, fetchImpl) {
  return parseDecisions(await post('/alpha/decisions', decisionsBody(model, imageUrl), apiKey, fetchImpl));
}

// ---------------------------------------------------------------- Chat Completions (LLM)

const CHAT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['egg_visible', 'cleanliness', 'integrity', 'reason'],
  properties: {
    egg_visible: { type: 'boolean', description: 'Almeno un uovo di gallina intero è visibile' },
    cleanliness: { type: 'string', enum: Object.keys(CLEANLINESS) },
    integrity: { type: 'string', enum: Object.keys(INTEGRITY) },
    reason: { type: 'string', description: 'Motivazione in massimo 20 parole, in italiano' },
  },
};

const legend = (map) => Object.entries(map).map(([k, v]) => `- ${k}: ${v}`).join('\n');

export function chatBody(model, imageUrl) {
  return {
    model: model.id,
    messages: [
      {
        role: 'system',
        content: 'Sei un ispettore di qualità delle uova. Rispondi solo con il JSON richiesto.',
      },
      {
        role: 'user',
        content: [
          {
            type: 'text',
            text:
              `${CONTEXT}\n\nPulizia (cleanliness):\n${legend(CLEANLINESS)}\n\n` +
              `Integrità (integrity):\n${legend(INTEGRITY)}\n\n` +
              'Imposta egg_visible a false se non c\'è nessun uovo di gallina intero nella foto.',
          },
          { type: 'image_url', image_url: { url: imageUrl } },
        ],
      },
    ],
    response_format: { type: 'json_schema', json_schema: { name: 'egg_inspection', strict: true, schema: CHAT_SCHEMA } },
    max_completion_tokens: 2000,
    usage: { include: true },
  };
}

export function parseChat(json) {
  const content = json?.choices?.[0]?.message?.content;
  if (!content) throw new ApiError(`Risposta chat vuota (finish_reason=${json?.choices?.[0]?.finish_reason ?? '?'})`, 0);
  let o;
  try { o = JSON.parse(content); } catch { throw new ApiError(`Risposta chat non JSON: ${String(content).slice(0, 120)}`, 0); }
  if (!(o.cleanliness in CLEANLINESS) || !(o.integrity in INTEGRITY)) throw new ApiError('Risposta chat con etichette non valide', 0);
  return {
    served_model: json.model ?? null,
    egg_visible: o.egg_visible ? 1 : 0,
    cleanliness: { label: o.cleanliness, probs: null, confidence: null },
    integrity: { label: o.integrity, probs: null, confidence: null },
    reason: o.reason ?? null,
    usage: { input_tokens: json.usage?.prompt_tokens ?? null, output_tokens: json.usage?.completion_tokens ?? null, cost: json.usage?.cost ?? null },
  };
}

export async function inspectWithChat(model, imageUrl, apiKey, fetchImpl) {
  return parseChat(await post('/v1/chat/completions', chatBody(model, imageUrl), apiKey, fetchImpl));
}

export function inspect(model, imageUrl, apiKey, fetchImpl) {
  return model.kind === 'decisions'
    ? inspectWithDecisions(model, imageUrl, apiKey, fetchImpl)
    : inspectWithChat(model, imageUrl, apiKey, fetchImpl);
}
