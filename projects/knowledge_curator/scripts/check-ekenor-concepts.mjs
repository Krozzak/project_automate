// Vérification des fiches Ekenor (règles de /sync-concepts). Usage : node check-ekenor-concepts.mjs [slugs créés…]
// À lancer depuis d:/Projet_Newsletter_Hub. Code de sortie 1 si une erreur.
import fs from 'node:fs';
import path from 'node:path';

const DIR = 'src/content/concepts';
const MOTION = 'src/components/concepts-v2/motion';
const REF_FIELDS = ['relatedConcepts', 'relatedProjects', 'relatedArticles', 'citedBy'];
const PHOTO_FIELDS = ['photo', 'photoCredit', 'photoSource', 'photoLicenseUrl'];
const created = process.argv.slice(2);
const errors = [];

// Frontmatter minimal : scalaires, listes inline ["a", "b"] et listes en bloc "- a".
function frontmatter(file) {
  const m = fs.readFileSync(file, 'utf8').match(/^---\r?\n([\s\S]*?)\r?\n---/);
  const data = {};
  let key = null;
  for (const line of (m ? m[1] : '').split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z]+):\s*(.*)$/);
    const item = line.match(/^\s+-\s*(.+)$/);
    if (kv) {
      key = kv[1];
      const v = kv[2].trim();
      if (v.startsWith('[')) data[key] = [...v.matchAll(/"([^"]*)"|'([^']*)'|([^,\[\]\s][^,\[\]]*)/g)].map((x) => (x[1] ?? x[2] ?? x[3]).trim());
      else data[key] = v === '' ? [] : v.replace(/^["']|["']$/g, '');
    } else if (item && Array.isArray(data[key])) data[key].push(item[1].trim().replace(/^["']|["']$/g, ''));
  }
  return data;
}

const files = fs.readdirSync(DIR).filter((f) => f.endsWith('.md'));
const fiches = files.map((f) => ({ file: f, fm: frontmatter(path.join(DIR, f)) }));
const bySlug = new Map();
for (const f of fiches) if (f.fm.lang !== 'en') bySlug.set(f.fm.sharedSlug, f.fm);

// 1. Références croisées : toujours le sharedSlug, jamais de suffixe -en (concepts + articles).
const articleDir = 'src/content/newsletter';
const articles = fs.existsSync(articleDir)
  ? fs.readdirSync(articleDir).filter((f) => f.endsWith('.md')).map((f) => ({ file: `newsletter/${f}`, fm: frontmatter(path.join(articleDir, f)) }))
  : [];
let badRefs = 0;
for (const { file, fm } of [...fiches, ...articles])
  for (const field of REF_FIELDS)
    for (const ref of [].concat(fm[field] ?? []))
      if (/-en$/.test(ref)) {
        badRefs++;
        if (badRefs <= 20) errors.push(`${file} · ${field} : "${ref}" finit par -en (écrire "${ref.replace(/-en$/, '')}")`);
      }
if (badRefs > 20) errors.push(`… ${badRefs} références en -en au total`);

// 5. Graphe : sharedSlug sans -en, type présent, cohérent avec knowledgeType.
const graph = JSON.parse(fs.readFileSync(path.join(DIR, '_graph.json'), 'utf8'));
for (const n of graph.concepts) {
  if (/-en$/.test(n.slug)) errors.push(`_graph.json : slug "${n.slug}" finit par -en`);
  for (const r of n.relatedConcepts ?? []) if (/-en$/.test(r)) errors.push(`_graph.json · ${n.slug} : lien "${r}" finit par -en`);
  if (!n.type) errors.push(`_graph.json : "${n.slug}" n'a pas de type`);
  if (['concept', 'author', 'book'].includes(n.type)) {
    const fm = bySlug.get(n.slug);
    if (!fm) errors.push(`_graph.json : "${n.slug}" ne correspond à aucune fiche FR`);
    else if ((fm.knowledgeType || 'concept') !== n.type) errors.push(`_graph.json : "${n.slug}" type ${n.type} ≠ knowledgeType ${fm.knowledgeType || 'concept'}`);
  }
}
const graphSlugs = new Set(graph.concepts.map((n) => n.slug));
for (const s of created) if (!graphSlugs.has(s)) errors.push(`${s} : absent de _graph.json`);

// 2-4. Fiches créées dans cette session.
for (const slug of created) {
  const pair = fiches.filter((f) => f.fm.sharedSlug === slug);
  const fr = pair.find((f) => f.fm.lang !== 'en');
  const en = pair.find((f) => f.fm.lang === 'en');
  if (!fr || !en) { errors.push(`${slug} : il faut une fiche FR et une fiche EN (trouvé ${pair.map((f) => f.file).join(', ') || 'rien'})`); continue; }
  const type = fr.fm.knowledgeType || 'concept';

  if (type === 'concept') {
    const motion = path.join(MOTION, `${slug}.astro`);
    if (!fs.existsSync(motion)) errors.push(`${slug} : motion design manquant (${motion})`);
    else {
      const src = fs.readFileSync(motion, 'utf8');
      if (/#[0-9a-f]{3,8}\b/i.test(src.replace(/<!--[\s\S]*?-->/g, ''))) errors.push(`${slug} : couleur en hex dans le motion (utiliser les classes du kit)`);
      if (/gradient/i.test(src)) errors.push(`${slug} : dégradé dans le motion`);
      if (/\p{Extended_Pictographic}/u.test(src)) errors.push(`${slug} : émoji dans le motion`);
      if (!/aria:\s*\{[^}]*fr:[^}]*en:/s.test(src)) errors.push(`${slug} : TEXT.aria { fr, en } manquant`);
      for (const k of src.matchAll(/@keyframes\s+([\w-]+)/g)) if (!k[1].startsWith('fxs-')) errors.push(`${slug} : keyframes "${k[1]}" sans préfixe fxs-<abréviation>-`);
      const dur = src.match(/--fxs-dur:\s*([\d.]+)s/);
      if (!dur || +dur[1] < 8 || +dur[1] > 12) errors.push(`${slug} : boucle --fxs-dur hors 8–12 s (${dur ? dur[1] + ' s' : 'absente'})`);
    }
  }

  for (const f of [fr, en]) {
    const present = PHOTO_FIELDS.filter((k) => f.fm[k]);
    if (type !== 'author' && present.length) errors.push(`${f.file} : champs photo sur une fiche ${type}`);
    if (type === 'author' && present.length && present.length < 4) errors.push(`${f.file} : photo incomplète, il manque ${PHOTO_FIELDS.filter((k) => !f.fm[k]).join(', ')}`);
    if (type === 'book' && (f.fm.cover || f.fm.coverImage)) errors.push(`${f.file} : couverture sur une fiche livre (le site affiche une tuile typographique)`);
  }
  if (type === 'author' && fr.fm.photo) {
    for (const ext of ['jpg', 'webp']) if (!fs.existsSync(`public/concepts/${slug}/photo.${ext}`)) errors.push(`${slug} : public/concepts/${slug}/photo.${ext} manquant`);
    if (fr.fm.photo !== en.fm.photo || fr.fm.photoSource !== en.fm.photoSource) errors.push(`${slug} : photo / photoSource différents entre FR et EN`);
    if (/\b(NC|ND)\b|non-commercial|noderiv|fair use/i.test(`${fr.fm.photoCredit} ${fr.fm.photoLicenseUrl}`)) errors.push(`${slug} : licence photo refusée (NC, ND ou fair use)`);
  }
}

if (errors.length) { console.log(`✗ ${errors.length} problème(s)\n- ` + errors.join('\n- ')); process.exit(1); }
console.log(`✓ Fiches OK (${fiches.length} fichiers, ${graph.concepts.length} nœuds${created.length ? `, créées : ${created.join(', ')}` : ''})`);
