// Demo: ispezione di 200 foto di uova con Jev 1.14, GPT-6 Luna Decisions e GPT-6 Luna.
//
//   node src/demo.mjs                       tutti i modelli, tutte le foto
//   node src/demo.mjs --limit 10            prova rapida (le prime 10 foto alternando bianche e marroni)
//   node src/demo.mjs --models jev,luna     solo alcuni modelli (jev, luna-decisions, luna)
//   node src/demo.mjs --mock                prova senza chiave né rete (risultati in results/mock)
//   node src/demo.mjs --fresh               ignora i risultati già salvati
import { readFile, writeFile, mkdir, appendFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';
import { MODELS } from './config.mjs';
import { findApiKey, inspect, toDataUrl } from './api.mjs';
import { decide, interleaveByTone, LABELS_IT, labelProb } from './decision.mjs';
import { buildModelReport, buildComparison } from './report.mjs';
import { mockFetch } from './mock.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

const { values: opt } = parseArgs({
  options: {
    models: { type: 'string', default: MODELS.map(m => m.key).join(',') },
    limit: { type: 'string' },
    concurrency: { type: 'string', default: '4' },
    mock: { type: 'boolean', default: false },
    fresh: { type: 'boolean', default: false },
  },
});

const models = opt.models.split(',').map(k => {
  const m = MODELS.find(x => x.key === k.trim());
  if (!m) { console.error(`Modello sconosciuto: ${k}. Disponibili: ${MODELS.map(x => x.key).join(', ')}`); process.exit(2); }
  return m;
});
const limit = opt.limit ? Number(opt.limit) : null;
const concurrency = Math.max(1, Number(opt.concurrency));

// Chiave: solo da variabile d'ambiente, mai stampata né scritta su file.
let apiKey = 'mock', fetchImpl;
if (opt.mock) {
  fetchImpl = mockFetch();
  console.log('MODALITÀ SIMULATA: nessuna chiamata a OpenRouter, i risultati non sono veri.\n');
} else {
  const found = findApiKey();
  if (!found) {
    console.error('Chiave OpenRouter non trovata. Imposta OPENROUTER_API_KEY (oppure OPEN_ROUTER_KEY / OPEN_ROUTER) nel terminale da cui lanci la demo.');
    process.exit(2);
  }
  apiKey = found.value;
  console.log(`Chiave letta dalla variabile ${found.name}.\n`);
}

const picsDir = join(ROOT, '_pics');
const manifest = JSON.parse((await readFile(join(picsDir, 'manifest.json'), 'utf8')).replace(/^﻿/, ''));
let images = interleaveByTone(manifest.images);
if (limit) images = images.slice(0, limit);
const order = images.map(i => i.file);

const sub = opt.mock ? 'mock' : '';
const resultsDir = join(ROOT, 'results', sub);
// Report veri in docs/reports; quelli simulati restano fuori da docs.
const reportsDir = opt.mock ? join(ROOT, 'results', 'mock', 'reports') : join(ROOT, 'docs', 'reports');
const picsRel = relative(reportsDir, picsDir).replaceAll('\\', '/');
const reportsLabel = relative(ROOT, reportsDir).replaceAll('\\', '/');
await mkdir(resultsDir, { recursive: true });
await mkdir(reportsDir, { recursive: true });

const started = new Date().toLocaleString('it-IT', { dateStyle: 'long', timeStyle: 'short' });
const reportFiles = {};
const resultsByModel = {};

async function loadCache(model) {
  const path = join(resultsDir, `${model.key}.jsonl`);
  const map = new Map();
  if (!opt.fresh && existsSync(path)) {
    for (const line of (await readFile(path, 'utf8')).split('\n')) {
      if (!line.trim()) continue;
      const r = JSON.parse(line);
      if (r.ok) map.set(r.file, r); // gli errori vengono ritentati
    }
  }
  if (opt.fresh) await writeFile(path, '');
  return { path, map };
}

async function runModel(model) {
  const { path, map: cache } = await loadCache(model);
  const todo = images.filter(i => !cache.has(i.file));
  console.log(`== ${model.label} (${model.id}): ${images.length} foto, ${cache.size} già in cache, ${todo.length} da analizzare`);
  const results = new Map(images.filter(i => cache.has(i.file)).map(i => [i.file, cache.get(i.file)]));

  let done = 0, consecutiveFails = 0, abort = null;
  const queue = [...todo];
  async function worker() {
    while (queue.length && !abort) {
      const img = queue.shift();
      const t0 = performance.now();
      let rec;
      try {
        const out = await inspect(model, await toDataUrl(join(picsDir, img.file)), apiKey, fetchImpl);
        rec = { file: img.file, model: model.id, ok: true, latency_ms: Math.round(performance.now() - t0), ...out, decision: decide(out) };
        consecutiveFails = 0;
      } catch (e) {
        rec = { file: img.file, model: model.id, ok: false, latency_ms: Math.round(performance.now() - t0), error: e.message };
        consecutiveFails++;
        if ([401, 402, 403].includes(e.status) || consecutiveFails >= 5) abort = e.message;
      }
      results.set(img.file, rec);
      await appendFile(path, JSON.stringify(rec) + '\n');
      done++;
      const n = `[${String(done).padStart(3)}/${todo.length}]`;
      if (rec.ok) {
        const d = rec.decision, c = rec.cleanliness, g = rec.integrity;
        const verdict = d.action === 'ACCEPT' ? `accetta ${d.grade}` : d.action === 'DISCARD' ? `SCARTA (${d.reasons.join(', ')})` : 'non valutabile';
        const p = (a) => (labelProb(a) != null ? ` ${labelProb(a).toFixed(2)}` : '');
        console.log(`${n} ${img.file.padEnd(34)} ${LABELS_IT.cleanliness[c.label]}${p(c)} | ${LABELS_IT.integrity[g.label]}${p(g)} -> ${verdict}  ${(rec.latency_ms / 1000).toFixed(2)}s`);
      } else {
        console.log(`${n} ${img.file.padEnd(34)} ERRORE: ${rec.error}`);
      }
    }
  }
  await Promise.all(Array.from({ length: Math.min(concurrency, todo.length) }, worker));
  if (abort) console.error(`\nInterrotto: ${abort}`);

  const list = images.map(i => results.get(i.file)).filter(Boolean);
  resultsByModel[model.key] = list;
  const file = `report-${model.id.replace('/', '_')}.md`;
  reportFiles[model.key] = file;
  await writeFile(join(reportsDir, file), buildModelReport({ model, manifest, results: list, run: { started, order, mock: opt.mock, limit, picsRel } }));
  const ok = list.filter(r => r.ok);
  console.log(`   ${ok.filter(r => r.decision.action === 'ACCEPT').length} accettate, ${ok.filter(r => r.decision.action === 'DISCARD').length} scartate, ${list.length - ok.length} errori -> ${reportsLabel}/${file}\n`);
  return !abort;
}

let allOk = true;
for (const model of models) allOk = (await runModel(model)) && allOk;

if (models.length > 1) {
  await writeFile(join(reportsDir, 'report-comparison.md'),
    buildComparison({ models, manifest, resultsByModel, run: { started, mock: opt.mock, reportFiles, picsRel } }));
  console.log(`Confronto: ${reportsLabel}/report-comparison.md`);
}
process.exit(allOk ? 0 : 1);
