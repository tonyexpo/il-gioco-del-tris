// Generazione dei report Markdown (uno per modello + un confronto).
import { CLEANLINESS, INTEGRITY, RULES, CONTEXT } from './config.mjs';
import { LABELS_IT, labelProb } from './decision.mjs';

const pct = (n, d) => (d ? `${((100 * n) / d).toFixed(1)}%` : 'n/d');
const fmtP = (p) => (p == null ? '' : ` (${p.toFixed(2)})`);
const sum = (a) => a.reduce((x, y) => x + y, 0);
const esc = (s) => String(s ?? '').replace(/\|/g, '\\|').replace(/\r?\n/g, ' ');

function quantile(sorted, q) {
  if (!sorted.length) return null;
  return sorted[Math.min(sorted.length - 1, Math.floor(q * sorted.length))];
}
const sec = (ms) => (ms == null ? 'n/d' : `${(ms / 1000).toFixed(2)} s`);
const usd = (x) => (x == null ? 'n/d' : `$${x.toFixed(4)}`);

export function summarize(results, manifest) {
  const byFile = new Map(manifest.images.map(i => [i.file, i]));
  const ok = results.filter(r => r.ok);
  const lat = ok.map(r => r.latency_ms).sort((a, b) => a - b);
  const costs = ok.map(r => r.usage?.cost).filter(c => c != null);
  const count = (f) => ok.filter(f).length;
  const reasons = {};
  for (const r of ok) for (const x of r.decision.reasons) reasons[x] = (reasons[x] ?? 0) + 1;

  const scenes = {};
  for (const r of ok) {
    const meta = byFile.get(r.file); const k = meta?.scene ?? '?';
    const s = (scenes[k] ??= { n: 0, ACCEPT: 0, DISCARD: 0, UNREADABLE: 0 });
    s.n++; s[r.decision.action]++;
  }

  // Confronto con la verità nota (solo Figshare: crepe annotate a mano).
  const gtCracked = ok.filter(r => byFile.get(r.file)?.ground_truth === 'cracked');
  const gtIntact = ok.filter(r => byFile.get(r.file)?.ground_truth === 'intact');
  const crackedFound = gtCracked.filter(r => r.integrity.label !== 'intact');
  const intactWrong = gtIntact.filter(r => r.integrity.label !== 'intact');

  return {
    total: results.length, ok: ok.length, errors: results.length - ok.length,
    accept: count(r => r.decision.action === 'ACCEPT'),
    discard: count(r => r.decision.action === 'DISCARD'),
    unreadable: count(r => r.decision.action === 'UNREADABLE'),
    gradeA: count(r => r.decision.grade === 'A'), gradeB: count(r => r.decision.grade === 'B'),
    lowConf: count(r => r.decision.low_confidence),
    cleanliness: Object.keys(CLEANLINESS).map(k => [k, count(r => r.cleanliness.label === k)]),
    integrity: Object.keys(INTEGRITY).map(k => [k, count(r => r.integrity.label === k)]),
    reasons, scenes,
    gt: { cracked: gtCracked.length, crackedFound: crackedFound.length, intact: gtIntact.length, intactWrong: intactWrong.length,
          missed: gtCracked.filter(r => r.integrity.label === 'intact').map(r => r.file) },
    latency: { mean: lat.length ? sum(lat) / lat.length : null, p50: quantile(lat, 0.5), p95: quantile(lat, 0.95) },
    cost: costs.length ? sum(costs) : null,
    tokens: { input: sum(ok.map(r => r.usage?.input_tokens ?? 0)), output: sum(ok.map(r => r.usage?.output_tokens ?? 0)) },
    served: [...new Set(ok.map(r => r.served_model).filter(Boolean))],
  };
}

const SCENE_IT = { single_egg: 'uovo singolo', few_eggs: 'poche uova', carton: 'cartone con più uova' };
const TONE_IT = { white: 'bianche', brown: 'marroni (varie tonalità)', mixed: 'bianche e marroni' };

function sourcesSection(manifest) {
  const counts = {};
  for (const i of manifest.images) counts[i.source] = (counts[i.source] ?? 0) + 1;
  const rows = manifest.sources.map(s =>
    `| ${esc(s.name)} | ${esc(s.authors)} | ${esc(s.license)} | ${counts[s.id] ?? 0} | [pagina](${s.page})${s.doi ? ` · [DOI](${s.doi})` : ''}${s.file ? ` · [file](${s.file})` : ''} |`);
  return [
    '## Dataset di origine delle foto',
    '',
    '| Dataset | Autori | Licenza | Foto nella demo | URL originali |',
    '| --- | --- | --- | ---: | --- |',
    ...rows,
    '',
    ...manifest.sources.map(s => `- **${s.id}**: ${s.note}`),
    '',
  ].join('\n');
}

export function buildModelReport({ model, manifest, results, run }) {
  const S = summarize(results, manifest);
  const byFile = new Map(manifest.images.map(i => [i.file, i]));
  const order = new Map(run.order.map((f, i) => [f, i]));
  const sorted = [...results].sort((a, b) => order.get(a.file) - order.get(b.file));
  const hasProbs = model.kind === 'decisions';
  const L = [];

  L.push(`# Rapporto di analisi uova: ${model.label}`, '');
  L.push(`- **Modello richiesto**: \`${model.id}\``);
  L.push(`- **Modello servito**: ${S.served.length ? S.served.map(s => `\`${s}\``).join(', ') : 'n/d'}`);
  L.push(`- **Interfaccia**: ${hasProbs ? 'OpenRouter Decisions API (`POST /api/alpha/decisions`), risposte tipizzate con probabilità' : 'OpenRouter Chat Completions con output JSON strutturato (modello generativo, senza probabilità)'}`);
  L.push(`- **Data analisi**: ${run.started}`);
  L.push(`- **Foto analizzate**: ${S.ok} su ${manifest.images.length}${S.errors ? ` (${S.errors} errori)` : ''}`);
  if (run.mock) L.push('', '> **ATTENZIONE: esecuzione simulata (`--mock`). I numeri non provengono da nessun modello.**');
  if (run.limit) L.push('', `> Esecuzione parziale: limite di ${run.limit} foto.`);
  L.push('');

  L.push('## Riepilogo', '');
  L.push('| Esito | Foto | Quota |', '| --- | ---: | ---: |');
  L.push(`| Accettate (grado A, pulite e integre) | ${S.gradeA} | ${pct(S.gradeA, S.ok)} |`);
  L.push(`| Accettate (grado B, lievemente sporche) | ${S.gradeB} | ${pct(S.gradeB, S.ok)} |`);
  L.push(`| **Scartate** (rotte, crepate o sporche) | ${S.discard} | ${pct(S.discard, S.ok)} |`);
  L.push(`| Non valutabili (uovo non rilevato) | ${S.unreadable} | ${pct(S.unreadable, S.ok)} |`, '');
  if (Object.keys(S.reasons).length) {
    L.push(`Motivi di scarto (una foto può averne più d'uno): ${Object.entries(S.reasons).map(([k, v]) => `${k} ${v}`).join(', ')}.`, '');
  }
  L.push('| Pulizia | Foto |  | Integrità | Foto |', '| --- | ---: | --- | --- | ---: |');
  for (let i = 0; i < 3; i++) {
    const [ck, cn] = S.cleanliness[i], [ik, inn] = S.integrity[i];
    L.push(`| ${LABELS_IT.cleanliness[ck]} | ${cn} |  | ${LABELS_IT.integrity[ik]} | ${inn} |`);
  }
  L.push('');
  if (hasProbs) L.push(`Etichette con confidenza sotto ${RULES.lowConfidence}, segnalate "da verificare": ${S.lowConf}.`, '');

  L.push('### Per tipo di scena', '');
  L.push('| Scena | Foto | Accettate | Scartate | Non valutabili |', '| --- | ---: | ---: | ---: | ---: |');
  for (const [k, s] of Object.entries(S.scenes)) L.push(`| ${SCENE_IT[k] ?? k} | ${s.n} | ${s.ACCEPT} | ${s.DISCARD} | ${s.UNREADABLE} |`);
  L.push('');

  L.push('### Confronto con la verità nota', '');
  if (S.gt.cracked + S.gt.intact === 0) {
    L.push('Nessuna foto con verità nota tra quelle analizzate.', '');
  } else {
    L.push(`Solo le foto Figshare hanno una verità annotata a mano (crepe). Le altre foto non hanno etichette, quindi per pulizia e per le foto Commons/Hugging Face non esiste una misura di accuratezza.`, '');
    L.push(`- Uova crepate note: **${S.gt.crackedFound} su ${S.gt.cracked}** riconosciute come crepate o rotte (${pct(S.gt.crackedFound, S.gt.cracked)}).`);
    if (S.gt.intact) L.push(`- Uova integre note: ${S.gt.intactWrong} su ${S.gt.intact} giudicate crepate o rotte.`);
    L.push('- Le crepe di questo dataset sono sottili e le foto sono ridotte a 1568 px: è una prova difficile, non rappresentativa delle rotture evidenti.', '');
  }

  L.push('### Tempi e costi', '');
  L.push('| Metrica | Valore |', '| --- | ---: |');
  L.push(`| Latenza media | ${sec(S.latency.mean)} |`, `| Latenza p50 | ${sec(S.latency.p50)} |`, `| Latenza p95 | ${sec(S.latency.p95)} |`);
  L.push(`| Token in ingresso | ${S.tokens.input} |`, `| Token in uscita | ${S.tokens.output} |`);
  L.push(`| Costo totale (da \`usage.cost\`) | ${usd(S.cost)} |`, `| Costo per 1000 foto | ${S.cost == null || !S.ok ? 'n/d' : usd((S.cost / S.ok) * 1000)} |`, '');

  L.push('## Come è stata fatta l\'analisi', '');
  L.push(`Contesto dato al modello: "${CONTEXT}"`, '');
  L.push('Pulizia del guscio:', '', ...Object.entries(CLEANLINESS).map(([k, v]) => `- \`${k}\` (${LABELS_IT.cleanliness[k]}): ${v}`), '');
  L.push('Integrità del guscio:', '', ...Object.entries(INTEGRITY).map(([k, v]) => `- \`${k}\` (${LABELS_IT.integrity[k]}): ${v}`), '');
  L.push('Regola di decisione, identica per tutti i modelli:', '',
    `- scartata se l'integrità non è \`intact\` oppure la pulizia è \`dirty\`${RULES.acceptSlightlyDirty ? '' : ' o \\`slightly_dirty\\`'};`,
    `- grado A se pulita e integra, grado B se lievemente sporca e integra${RULES.acceptSlightlyDirty ? '' : ' (qui scartata)'};`,
    `- non valutabile se la probabilità di "uovo visibile" è sotto ${RULES.minEggVisible}.`, '');
  L.push('Se la foto mostra un cartone, il modello valuta l\'uovo in condizioni peggiori: un solo uovo difettoso fa scartare l\'intera foto.', '');

  const comp = {};
  for (const x of results) { const t = byFile.get(x.file)?.tone; comp[t] = (comp[t] ?? 0) + 1; }
  L.push('## Composizione del campione analizzato', '',
    Object.entries(comp).map(([k, v]) => `${v} foto di uova ${TONE_IT[k] ?? k}`).join(', ') + '.',
    'Le foto sono state analizzate alternando uova bianche e uova di altre tonalità (ordine mescolato con seed fisso).', '');

  L.push(sourcesSection(manifest));

  L.push('## Dettaglio per foto', '');
  if (hasProbs) {
    L.push('Tra parentesi la probabilità dell\'etichetta scelta; "Conf." è la confidenza dichiarata dal modello (campo `confidence`), che può essere più bassa della probabilità. Sotto ' + RULES.lowConfidence + ' la riga è segnalata "da verificare".', '');
    L.push('| # | Foto | Scena | Pulizia | Conf. | Integrità | Conf. | Decisione | Latenza | Note |');
    L.push('| ---: | --- | --- | --- | ---: | --- | ---: | --- | ---: | --- |');
  } else {
    L.push('| # | Foto | Scena | Pulizia | Integrità | Decisione | Latenza | Motivazione del modello |');
    L.push('| ---: | --- | --- | --- | --- | --- | ---: | --- |');
  }
  const conf = (a) => (a.confidence == null ? 'n/d' : a.confidence.toFixed(2));
  sorted.forEach((r, n) => {
    const meta = byFile.get(r.file);
    const link = `[${r.file}](${run.picsRel}/${r.file})`;
    if (!r.ok) { L.push(`| ${n + 1} | ${link} | ${SCENE_IT[meta?.scene] ?? ''} |${hasProbs ? ' | | | |' : ' | |'} ERRORE | | ${esc(r.error)} |`); return; }
    const d = r.decision;
    const decision = d.action === 'ACCEPT' ? `accetta (${d.grade})` : d.action === 'DISCARD' ? `**scarta**: ${d.reasons.join(', ')}` : 'non valutabile';
    const note = hasProbs ? (d.low_confidence ? 'da verificare' : '') : esc(r.reason);
    const gt = meta?.ground_truth ? `${note ? note + '; ' : ''}verità: ${meta.ground_truth}` : note;
    const clean = `${LABELS_IT.cleanliness[r.cleanliness.label]}${fmtP(labelProb(r.cleanliness))}`;
    const integ = `${LABELS_IT.integrity[r.integrity.label]}${fmtP(labelProb(r.integrity))}`;
    const labels = hasProbs
      ? `${clean} | ${conf(r.cleanliness)} | ${integ} | ${conf(r.integrity)}`
      : `${clean} | ${integ}`;
    L.push(`| ${n + 1} | ${link} | ${SCENE_IT[meta?.scene] ?? ''} | ${labels} | ${decision} | ${sec(r.latency_ms)} | ${gt} |`);
  });
  L.push('');

  const errs = results.filter(r => !r.ok);
  if (errs.length) { L.push('## Errori', '', ...errs.map(r => `- ${r.file}: ${esc(r.error)}`), ''); }

  L.push(detailSection({ model, sorted, byFile, run, hasProbs }));
  return L.join('\n');
}

// Appendice con il dettaglio completo di ogni foto: pensata per chi legge il report su GitHub.
// Ogni foto è un blocco richiudibile con miniatura, origine e licenza, probabilità di tutte le opzioni,
// decisione, costi e motivazione del modello.
function detailSection({ model, sorted, byFile, run, hasProbs }) {
  const probs = (a, scale) => (a.probs
    ? Object.keys(scale).map(k => { const p = (a.probs[k] ?? 0).toFixed(2); return k === a.label ? `**${k} ${p}**` : `${k} ${p}`; }).join(' · ')
    : null);
  const L = ['## Dettaglio completo per foto', ''];
  L.push(`Un blocco per foto analizzata, nello stesso ordine della tabella sopra: clicca sul titolo per aprirlo. L'origine di tutte le 200 foto del campione è anche in \`_pics/manifest.json\`. ${hasProbs
    ? 'Per ogni domanda sono indicate le probabilità di tutte le opzioni (in grassetto quella scelta) e la confidenza dichiarata dal modello.'
    : 'Il modello è generativo: non fornisce probabilità, ma una breve motivazione.'}`, '');
  sorted.forEach((r, n) => {
    const m = byFile.get(r.file) ?? {};
    const [url, ...rest] = String(m.original ?? '').split(' ');
    const origin = /^https?:/.test(url) ? `[${url}](${url})${rest.length ? ' ' + rest.join(' ') : ''}` : esc(m.original);
    const d = r.decision;
    const verdict = !r.ok ? 'ERRORE'
      : d.action === 'ACCEPT' ? `accetta (${d.grade})`
        : d.action === 'DISCARD' ? `scarta: ${d.reasons.join(', ')}` : 'non valutabile';
    L.push('<details>', `<summary><b>${n + 1}. ${r.file}</b> · ${verdict}</summary>`, '');
    L.push(`<img src="${run.picsRel}/${r.file}" alt="${r.file}" width="260">`, '');
    L.push(`- **Origine**: ${origin}`);
    L.push(`- **Licenza**: ${esc(m.license)}${m.author ? ` · **Autore**: ${esc(m.author)}` : ''}`);
    L.push(`- **Scena**: ${SCENE_IT[m.scene] ?? m.scene} · **Uova**: ${TONE_IT[m.tone] ?? m.tone} · **Dimensioni analizzate**: ${m.size}`);
    L.push(`- **Verità nota**: ${m.ground_truth ?? 'nessuna'}${m.defect_hint ? ' (foto scelta perché mostra un difetto visibile, non annotata)' : ''}`);
    if (!r.ok) {
      L.push(`- **Errore**: ${esc(r.error)}`, '', '</details>', '');
      return;
    }
    L.push(`- **Uovo visibile**: ${r.egg_visible == null ? 'n/d' : r.egg_visible.toFixed(2)}`);
    for (const [name, key, scale] of [['Pulizia', 'cleanliness', CLEANLINESS], ['Integrità', 'integrity', INTEGRITY]]) {
      const a = r[key];
      const p = probs(a, scale);
      L.push(`- **${name}**: ${LABELS_IT[key][a.label]} (\`${a.label}\`)${p ? ` · probabilità: ${p}` : ''}${a.confidence != null ? ` · confidenza ${a.confidence.toFixed(2)}` : ''}`);
    }
    L.push(`- **Decisione**: ${verdict}${d.low_confidence ? ' · da verificare (confidenza bassa)' : ''}`);
    const u = r.usage ?? {};
    L.push(`- **Chiamata**: modello \`${r.served_model ?? model.id}\` · latenza ${sec(r.latency_ms)} · token ${u.input_tokens ?? 'n/d'} in / ${u.output_tokens ?? 'n/d'} out · costo ${u.cost == null ? 'n/d' : '$' + u.cost.toFixed(6)}`);
    if (r.reason) L.push(`- **Motivazione del modello**: ${esc(r.reason)}`);
    L.push('', '</details>', '');
  });
  return L.join('\n');
}

export function buildComparison({ models, manifest, resultsByModel, run }) {
  const S = Object.fromEntries(models.map(m => [m.key, summarize(resultsByModel[m.key], manifest)]));
  const byFile = new Map(manifest.images.map(i => [i.file, i]));
  const okMap = Object.fromEntries(models.map(m => [m.key, new Map(resultsByModel[m.key].filter(r => r.ok).map(r => [r.file, r]))]));
  const common = [...okMap[models[0].key].keys()].filter(f => models.every(m => okMap[m.key].has(f)));
  const nPhotos = common.length;
  const label = (m) => m.label;
  const L = [];

  L.push('# Confronto tra modelli: ispezione uova', '');
  L.push(`Data: ${run.started}. Stesse ${nPhotos} foto (su ${manifest.images.length} disponibili), stesse domande, stessa regola di decisione.`, '');
  if (run.mock) L.push('> **ATTENZIONE: esecuzione simulata (`--mock`).**', '');

  // ---- In breve: solo affermazioni ricavate dai numeri
  const pickBest = (f) => models.reduce((a, b) => ((f(S[b.key]) ?? Infinity) < (f(S[a.key]) ?? Infinity) ? b : a));
  const fastest = pickBest(s => s.latency.p50), cheapest = pickBest(s => s.cost);
  const withGt = models.filter(m => S[m.key].gt.cracked > 0);
  const unanimous = common.filter(f => new Set(models.map(m => okMap[m.key].get(f).decision.action)).size === 1).length;
  L.push('## In breve', '');
  L.push(`- **Più veloce**: ${label(fastest)}, latenza mediana ${sec(S[fastest.key].latency.p50)}. **Più economico**: ${label(cheapest)}, ${usd(S[cheapest.key].cost / S[cheapest.key].ok * 1000)} ogni 1000 foto.`);
  if (withGt.length) {
    L.push(`- **Crepe note riconosciute** (${S[withGt[0].key].gt.cracked} foto Figshare): ${models.map(m => `${label(m)} ${S[m.key].gt.crackedFound}`).join(', ')}.`);
  }
  L.push(`- **Decisione identica** (accetta o scarta) in ${unanimous} foto su ${nPhotos}; nelle altre ${nPhotos - unanimous} almeno un modello decide diversamente (elenco più sotto).`);
  const solM = models.find(m => m.key === 'sol');
  if (solM) L.push(`- **GPT-6.1 Sol** è il modello più costoso (${usd(S[solM.key].cost / S[solM.key].ok * 1000)} ogni 1000 foto) e scarta di più: ${S[solM.key].discard} foto su ${S[solM.key].ok}. È usato come secondo parere, non come verità: analisi in una sezione dedicata più sotto.`);
  L.push('- Una quota di scarti più alta non significa risultati migliori: solo le foto con crepa nota permettono di dire chi ha ragione, per le altre manca una verità di riferimento.', '');

  // ---- Tabella principale
  const row = (name, f) => `| ${name} | ${models.map(m => f(S[m.key], m)).join(' | ')} |`;
  L.push('## Risultati a confronto', '');
  L.push(`| Metrica | ${models.map(label).join(' | ')} |`, `| --- | ${models.map(() => '---:').join(' | ')} |`);
  L.push(row('Modello servito', s => '`' + (s.served[0] ?? 'n/d') + '`'));
  L.push(row('Foto analizzate', s => s.ok), row('Errori', s => s.errors));
  L.push(row('Accettate (A + B)', s => `${s.accept} (${pct(s.accept, s.ok)})`), row('di cui grado B (lievemente sporche)', s => s.gradeB));
  L.push(row('Scartate', s => `${s.discard} (${pct(s.discard, s.ok)})`), row('Non valutabili', s => s.unreadable));
  L.push(row('Pulite / lievemente sporche / sporche', s => s.cleanliness.map(x => x[1]).join(' / ')));
  L.push(row('Integre / crepate / rotte', s => s.integrity.map(x => x[1]).join(' / ')));
  L.push(row('Etichette "da verificare"', (s, m) => (m.kind === 'decisions' ? s.lowConf : 'n/d')));
  L.push(row("Probabilità media dell'etichetta scelta", (s, m) => {
    if (m.kind !== 'decisions') return 'n/d';
    const v = resultsByModel[m.key].filter(r => r.ok).flatMap(r => [labelProb(r.cleanliness), labelProb(r.integrity)]).filter(x => x != null);
    return v.length ? (sum(v) / v.length).toFixed(2) : 'n/d';
  }));
  L.push(row('Latenza media', s => sec(s.latency.mean)), row('Latenza p50', s => sec(s.latency.p50)), row('Latenza p95', s => sec(s.latency.p95)));
  L.push(row('Token in ingresso (totale)', s => s.tokens.input), row('Token in uscita (totale)', s => s.tokens.output));
  L.push(row('Costo totale', s => usd(s.cost)), row('Costo per 1000 foto', s => (s.cost == null || !s.ok ? 'n/d' : usd((s.cost / s.ok) * 1000))), '');
  L.push('Le latenze sono misurate dal client e includono la rete. Il costo è la somma di `usage.cost` restituito da OpenRouter.', '');

  // ---- Per scena
  L.push('## Per tipo di scena', '', 'Foto scartate su foto analizzate.', '');
  L.push(`| Scena | Foto | ${models.map(label).join(' | ')} |`, `| --- | ---: | ${models.map(() => '---:').join(' | ')} |`);
  for (const sc of Object.keys(SCENE_IT)) {
    const files = common.filter(f => byFile.get(f)?.scene === sc);
    if (!files.length) continue;
    L.push(`| ${SCENE_IT[sc]} | ${files.length} | ${models.map(m => files.filter(f => okMap[m.key].get(f).decision.action === 'DISCARD').length).join(' | ')} |`);
  }
  L.push('');

  // ---- Crepe note
  const gtFiles = common.filter(f => byFile.get(f)?.ground_truth === 'cracked');
  if (gtFiles.length) {
    const found = (m, f) => okMap[m.key].get(f).integrity.label !== 'intact';
    const nFound = gtFiles.map(f => models.filter(m => found(m, f)).length);
    L.push('## Crepe note (foto Figshare)', '');
    L.push(`Le ${gtFiles.length} foto Figshare analizzate hanno una crepa annotata a mano. Un modello "riconosce" la crepa se giudica l'integrità \`cracked\` o \`broken\`.`, '');
    L.push('| Modello | Riconosciute | Quota |', '| --- | ---: | ---: |');
    for (const m of models) { const n = gtFiles.filter(f => found(m, f)).length; L.push(`| ${label(m)} | ${n} su ${gtFiles.length} | ${pct(n, gtFiles.length)} |`); }
    L.push('');
    L.push(`- Riconosciute da **tutti** i modelli: ${nFound.filter(n => n === models.length).length}`);
    L.push(`- Riconosciute da **alcuni**: ${nFound.filter(n => n > 0 && n < models.length).length}`);
    L.push(`- Mancate da **tutti**: ${nFound.filter(n => n === 0).length}`, '');
    const missedAll = gtFiles.filter((f, i) => nFound[i] === 0);
    if (missedAll.length) L.push(`Mancate da tutti: ${missedAll.map(f => `[${f}](${run.picsRel}/${f})`).join(', ')}.`, '');
    L.push('Il set non contiene uova integre con etichetta certa, quindi i falsi allarmi (uova integre scartate) non si possono misurare. Le crepe sono sottili e le foto sono ridotte a 1568 px.', '');
  }

  // ---- Accordo
  L.push('## Accordo tra modelli', '', `Decisione identica (accetta, scarta o non valutabile) sulle ${nPhotos} foto in comune.`, '');
  L.push('| Coppia | Stessa decisione |', '| --- | ---: |');
  for (let i = 0; i < models.length; i++) for (let j = i + 1; j < models.length; j++) {
    const same = common.filter(f => okMap[models[i].key].get(f).decision.action === okMap[models[j].key].get(f).decision.action).length;
    L.push(`| ${label(models[i])} / ${label(models[j])} | ${same} su ${nPhotos} (${pct(same, nPhotos)}) |`);
  }
  L.push(`| Tutti e ${models.length} | ${unanimous} su ${nPhotos} (${pct(unanimous, nPhotos)}) |`, '');

  // ---- Discordanze
  const cell = (r) => `${r.decision.action === 'ACCEPT' ? 'accetta' : r.decision.action === 'DISCARD' ? '**scarta**' : 'non valutabile'}: ${LABELS_IT.cleanliness[r.cleanliness.label]}, ${LABELS_IT.integrity[r.integrity.label]}`;
  const disagree = common.filter(f => new Set(models.map(m => okMap[m.key].get(f).decision.action)).size > 1);
  L.push('## Foto con decisioni discordanti', '');
  if (!disagree.length) L.push('Nessuna: tutti i modelli hanno deciso allo stesso modo.', '');
  else {
    L.push(`| Foto | Scena | Verità nota | ${models.map(label).join(' | ')} |`, `| --- | --- | --- | ${models.map(() => '---').join(' | ')} |`);
    for (const f of disagree) {
      const meta = byFile.get(f);
      L.push(`| [${f}](${run.picsRel}/${f}) | ${SCENE_IT[meta?.scene] ?? ''} | ${meta?.ground_truth ?? 'n/d'} | ${models.map(m => cell(okMap[m.key].get(f))).join(' | ')} |`);
    }
    L.push('');
  }

  // ---- Modello di riferimento aggiuntivo (Sol): confronto e voto di maggioranza
  const sol = models.find(m => m.key === 'sol');
  const others = models.filter(m => m !== sol);
  if (sol && others.length >= 2) {
    const act = (m, f) => okMap[m.key].get(f).decision.action;
    const lab = (m, f, k) => okMap[m.key].get(f)[k].label;
    L.push('## GPT-6.1 Sol come ulteriore termine di confronto', '');
    L.push('Sol è un modello generativo più grande e più costoso degli altri. Qui è usato come **secondo parere**: le sue risposte non sono una verità certificata, quindi un accordo con Sol non dimostra che un modello abbia ragione, e un disaccordo non dimostra che abbia torto. Sull\'unica verità nota, la crepa delle foto Figshare, il confronto è nella sezione sopra.', '');

    L.push('| Modello | Stessa decisione di Sol | Stessa pulizia | Stessa integrità |', '| --- | ---: | ---: | ---: |');
    for (const m of others) {
      const d = common.filter(f => act(m, f) === act(sol, f)).length;
      const c = common.filter(f => lab(m, f, 'cleanliness') === lab(sol, f, 'cleanliness')).length;
      const i = common.filter(f => lab(m, f, 'integrity') === lab(sol, f, 'integrity')).length;
      L.push('| ' + label(m) + ' | ' + d + ' su ' + nPhotos + ' (' + pct(d, nPhotos) + ') | ' + c + ' (' + pct(c, nPhotos) + ') | ' + i + ' (' + pct(i, nPhotos) + ') |');
    }
    L.push('');

    // Foto in cui Sol è l'unico a decidere diversamente, e foto in cui gli altri sono divisi
    const solAlone = common.filter(f => { const a = others.map(m => act(m, f)); return new Set(a).size === 1 && a[0] !== act(sol, f); });
    const solAloneDiscard = solAlone.filter(f => act(sol, f) === 'DISCARD').length;
    const solAloneAccept = solAlone.filter(f => act(sol, f) === 'ACCEPT').length;
    const othersSplit = common.filter(f => new Set(others.map(m => act(m, f))).size > 1).length;
    L.push('- Gli altri ' + others.length + ' modelli concordano tra loro e **solo Sol decide diversamente** in ' + solAlone.length + ' foto su ' + nPhotos + ': in ' + solAloneDiscard + ' Sol scarta e gli altri accettano, in ' + solAloneAccept + ' Sol accetta e gli altri scartano.');
    L.push('- Gli altri ' + others.length + ' modelli non concordano tra loro in ' + othersSplit + ' foto.');

    // Voto di maggioranza su accetta/scarta (i non valutabili non votano)
    let maj = { ACCEPT: 0, DISCARD: 0, tie: 0, none: 0 };
    const majority = new Map();
    for (const f of common) {
      const v = models.map(m => act(m, f)).filter(a => a !== 'UNREADABLE');
      const a = v.filter(x => x === 'ACCEPT').length, d = v.filter(x => x === 'DISCARD').length;
      const res = !v.length ? 'none' : a > d ? 'ACCEPT' : d > a ? 'DISCARD' : 'tie';
      maj[res]++; majority.set(f, res);
    }
    L.push('- **Voto di maggioranza** dei ' + models.length + ' modelli (i "non valutabili" non votano): ' + maj.ACCEPT + ' foto da accettare, ' + maj.DISCARD + ' da scartare, ' + maj.tie + ' in parità, ' + maj.none + ' senza voti.');
    for (const m of models) {
      const dec = common.filter(f => majority.get(f) === 'ACCEPT' || majority.get(f) === 'DISCARD');
      const same = dec.filter(f => act(m, f) === majority.get(f)).length;
      L.push('  - ' + label(m) + ' coincide con la maggioranza in ' + same + ' foto su ' + dec.length + ' (' + pct(same, dec.length) + ').');
    }
    L.push('');

    // Crepe note: cosa aggiunge Sol
    if (gtFiles && gtFiles.length) {
      const foundBy = (m, f) => lab(m, f, 'integrity') !== 'intact';
      const onlySol = gtFiles.filter(f => foundBy(sol, f) && others.every(m => !foundBy(m, f)));
      const missedAll = gtFiles.filter(f => models.every(m => !foundBy(m, f)));
      const solMissedOthersFound = gtFiles.filter(f => !foundBy(sol, f) && others.some(m => foundBy(m, f)));
      L.push('Sulle ' + gtFiles.length + ' foto con crepa nota: **' + onlySol.length + '** crepe sono riconosciute solo da Sol, **' + solMissedOthersFound.length + '** sono mancate da Sol ma riconosciute da almeno un altro modello, **' + missedAll.length + '** sono mancate da tutti i ' + models.length + ' modelli.', '');
    }

    // Costo e tempo
    const perPhoto = (m) => (S[m.key].cost == null || !S[m.key].ok ? null : S[m.key].cost / S[m.key].ok);
    const cs = perPhoto(sol);
    if (cs != null) {
      L.push('Costo e tempo di Sol rispetto agli altri: ' + others.map(m => { const c = perPhoto(m); return c ? label(m) + ' costa ' + (cs / c).toFixed(1) + ' volte meno di Sol' : null; }).filter(Boolean).join('; ') + '. Latenza mediana di Sol ' + sec(S[sol.key].latency.p50) + ' contro ' + others.map(m => sec(S[m.key].latency.p50) + ' (' + label(m) + ')').join(', ') + '.', '');
    }

    // Elenco foto in cui Sol è l'unico a divergere
    if (solAlone.length) {
      L.push('### Foto in cui solo Sol decide diversamente', '');
      L.push('| Foto | Scena | Verità nota | Sol | Gli altri ' + others.length + ' (stessa decisione; etichette di ' + label(others[0]) + ') |', '| --- | --- | --- | --- | --- |');
      for (const f of solAlone) {
        const meta = byFile.get(f);
        L.push('| [' + f + '](' + run.picsRel + '/' + f + ') | ' + (SCENE_IT[meta?.scene] ?? '') + ' | ' + (meta?.ground_truth ?? 'n/d') + ' | ' + cell(okMap[sol.key].get(f)) + ' | ' + cell(okMap[others[0].key].get(f)) + ' |');
      }
      L.push('');
    }
  }

  L.push('## Come leggere questi numeri', '');
  L.push('- Le pipeline usano le stesse definizioni di pulizia e integrità, le stesse foto e la stessa regola di scarto; cambia solo il modello.');
  L.push('- Solo la crepa delle foto Figshare ha una verità annotata. Per la pulizia e per le altre foto i report mostrano cosa decide ogni modello, non chi ha ragione.');
  L.push('- Il modello LLM non dà probabilità e, senza `temperature`, può rispondere in modo diverso tra due esecuzioni.');
  L.push('- Il campione è piccolo: le differenze di pochi punti percentuali non sono significative.', '');

  L.push('## Report per modello', '', ...models.map(m => `- [${m.label}](${run.reportFiles[m.key]})`), '');
  L.push(sourcesSection(manifest));
  return L.join('\n');
}
