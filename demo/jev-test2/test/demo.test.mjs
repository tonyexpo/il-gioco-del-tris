import test from 'node:test';
import assert from 'node:assert/strict';
import { decide, interleaveByTone } from '../src/decision.mjs';
import { parseDecisions, parseChat, decisionsBody, chatBody, findApiKey } from '../src/api.mjs';
import { mockFetch } from '../src/mock.mjs';
import { inspect } from '../src/api.mjs';
import { MODELS } from '../src/config.mjs';

const ans = (c, i, ev = 1) => ({ egg_visible: ev, cleanliness: { label: c, confidence: 0.9 }, integrity: { label: i, confidence: 0.9 } });

test('decide: scarta rotte, crepate e sporche; accetta A e B', () => {
  assert.deepEqual(decide(ans('clean', 'intact')).grade, 'A');
  assert.equal(decide(ans('slightly_dirty', 'intact')).grade, 'B');
  assert.equal(decide(ans('clean', 'cracked')).action, 'DISCARD');
  assert.equal(decide(ans('clean', 'broken')).action, 'DISCARD');
  assert.equal(decide(ans('dirty', 'intact')).action, 'DISCARD');
  assert.deepEqual(decide(ans('dirty', 'broken')).reasons, ['rotto', 'sporco']);
});

test('decide: uovo non rilevato e bassa confidenza', () => {
  assert.equal(decide(ans('clean', 'intact', 0.1)).action, 'UNREADABLE');
  const low = { egg_visible: 1, cleanliness: { label: 'clean', confidence: 0.4 }, integrity: { label: 'intact', confidence: 0.9 } };
  assert.equal(decide(low).low_confidence, true);
});

test('interleaveByTone alterna bianche e le altre ed è deterministico', () => {
  const imgs = [...Array(6)].map((_, i) => ({ file: `w${i}`, tone: 'white' })).concat([...Array(6)].map((_, i) => ({ file: `b${i}`, tone: i % 2 ? 'brown' : 'mixed' })));
  const a = interleaveByTone(imgs), b = interleaveByTone(imgs);
  assert.deepEqual(a, b);
  a.forEach((x, i) => assert.equal(x.tone === 'white', i % 2 === 0));
});

test('parseDecisions e parseChat normalizzano la risposta', () => {
  const d = parseDecisions({ model: 'm', answers: { egg_visible: { noul: 0.9 }, cleanliness: { choice: 'clean', probabilities: { clean: 0.8 }, confidence: 0.7 }, integrity: { choice: 'intact', probabilities: { intact: 0.95 }, confidence: 0.9 } }, usage: { input_tokens: 5, output_tokens: 0, cost: 0.1 } });
  assert.equal(d.integrity.label, 'intact'); assert.equal(d.usage.cost, 0.1);
  const c = parseChat({ model: 'm', choices: [{ message: { content: '{"egg_visible":true,"cleanliness":"dirty","integrity":"cracked","reason":"x"}' } }], usage: { prompt_tokens: 3, completion_tokens: 2 } });
  assert.equal(c.cleanliness.label, 'dirty'); assert.equal(c.egg_visible, 1);
  assert.throws(() => parseChat({ choices: [{ message: { content: '{"cleanliness":"boh","integrity":"intact"}' } }] }));
});

test('le richieste hanno la forma attesa da OpenRouter', () => {
  const url = 'data:image/jpeg;base64,AAAA';
  const d = decisionsBody(MODELS[0], url);
  assert.equal(d.model, 'typesafe/jev-1.14');
  assert.deepEqual(d.state[1], { type: 'image_url', image_url: { url } });
  assert.deepEqual(Object.keys(d.questions), ['egg_visible', 'cleanliness', 'integrity']);
  assert.equal(d.questions.egg_visible.type, 'noul');
  assert.deepEqual(Object.keys(d.questions.integrity.criteria), ['intact', 'cracked', 'broken']);
  const c = chatBody(MODELS[2], url);
  assert.equal(c.response_format.type, 'json_schema');
  assert.equal(c.messages[1].content[1].image_url.url, url);
  assert.equal(JSON.stringify(d).includes('sk-'), false);
});

test('findApiKey legge OPENROUTER_API_KEY per prima e non inventa nulla', () => {
  assert.equal(findApiKey({}), null);
  assert.equal(findApiKey({ OPEN_ROUTER: 'b', OPENROUTER_API_KEY: 'a' }).name, 'OPENROUTER_API_KEY');
});

test('percorso completo con fetch finto, per tutti e tre i modelli', async () => {
  for (const m of MODELS) {
    const out = await inspect(m, 'data:image/jpeg;base64,AAAA', 'mock', mockFetch());
    assert.ok(['clean', 'slightly_dirty', 'dirty'].includes(out.cleanliness.label));
    assert.ok(decide(out).action);
  }
});

test('tabella foto per foto: stesso numero di colonne anche per le righe in errore, confidenza solo per i modelli Decisions', async () => {
  const { buildModelReport } = await import('../src/report.mjs');
  const manifest = { sources: [], images: [
    { file: 'a.jpg', scene: 'single_egg', tone: 'white', ground_truth: null },
    { file: 'b.jpg', scene: 'carton', tone: 'mixed', ground_truth: null },
  ] };
  for (const m of [MODELS[0], MODELS[2]]) {
    const ok = await inspect(m, 'data:image/jpeg;base64,AAAA', 'mock', mockFetch());
    const results = [
      { file: 'a.jpg', ok: true, latency_ms: 100, ...ok, decision: decide(ok) },
      { file: 'b.jpg', ok: false, latency_ms: 5, error: 'HTTP 500: boom' },
    ];
    const md = buildModelReport({ model: m, manifest, results, run: { started: 'oggi', order: ['a.jpg', 'b.jpg'], picsRel: '../_pics' } });
    const lines = md.split('\n');
    const start = lines.findIndex(l => l.startsWith('| # | Foto'));
    const cols = (l) => l.split('|').length;
    const table = lines.slice(start).filter(l => l.startsWith('|')).slice(0, 4);
    assert.equal(table.length, 4);
    for (const l of table) assert.equal(cols(l), cols(table[0]), l);
    assert.equal(table[0].includes('Conf.'), m.kind === 'decisions');
  }
});
