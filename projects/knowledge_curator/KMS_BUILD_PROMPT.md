# Prompt de build — Knowledge Management System (KMS)

> À lancer via `/new-automation — lis projects/knowledge_curator/KMS_BUILD_PROMPT.md`
> Généré le 2026-05-08. Projet #8b — extension standalone de #8 Knowledge Management.

---

## Vision

Un pipeline KM complet publiable en open source sous le nom **KMS —
Knowledge Management System**.

Quelqu'un clone le repo, lance 5 commandes, et a un système de knowledge
management opérationnel avec graphe 3D interactif dans son navigateur :
nœuds cliquables qui ouvrent les fiches dans un nouvel onglet, clusters
colorés, backlinks automatiques à chaque commit.

Le pipeline couvre le cycle complet : capturer → structurer → lier →
visualiser → brainstormer → contribuer.

Repo GitHub : `kms` (Knowledge Management System)

---

## Modèle privé / public — comment ça fonctionne

C'est la distinction centrale du système. Bien expliquer dans le README.

### Vault personnel (local)

Chaque utilisateur travaille sur sa propre copie locale du repo.
Ses fiches sont privées par défaut — il choisit ce qu'il publie.

```
Flux local :
  clone kms → ajoute ses fiches → git commit
  → post-commit hook → backlinks recalculés + _graph.json regénéré
  → npm run dev → graphe personnel visible dans le navigateur
```

Le vault local peut contenir des fiches personnelles, des notes brutes,
des drafts — rien de ça n'est publié sauf si l'utilisateur ouvre une PR.

### Contribution au graphe public

Quand l'utilisateur veut partager une ou plusieurs fiches :

```
Flux contribution :
  git checkout -b contribution/[slug]
  → push sa branche sur le fork
  → ouvre une PR vers le repo principal
  → GitHub Actions vérifie automatiquement
  → review humaine (maintainer)
  → merge → _graph.json public regénéré automatiquement
```

**Règle** : on ne publie que ce qu'on choisit explicitement.
Le graphe public = agrégation des contributions validées de tous.

---

## Architecture des types de fiches

### Structure par dossier — le dossier détermine le type

```
notes/
├── concepts/     → type: concept
├── books/        → type: book
├── authors/      → type: author
├── projects/     → type: project
└── articles/     → type: article
```

Le script Python détermine le type depuis `parent_folder_name`.
Règle : `type = Path(file).parent.name` (singularisé).
Zéro ambiguïté, zéro IA nécessaire.

### Frontmatter canonique unifié

Tous les types partagent le même schéma. Le champ `related` utilise
des préfixes pour identifier le type de la cible.

```yaml
---
title: "Nom du concept / livre / auteur / projet / article"
type: concept          # dérivable du dossier — optionnel mais utile
cluster: Systèmes      # V1 : clusters sur concepts uniquement
                       # Vision : clusters sur tous les types à terme
related:
  - concept:small-world-network
  - concept:permissionless-leverage
  - book:naval-almanack
  - author:naval-ravikant
  - project:knowledge-management
  - article:nl-01-poiesis-praxis
citedBy:               # calculé automatiquement — ne pas éditer à la main
  - concept:ego-depletion
aliases:
  fr: []
  en: []
tags: []
status: draft          # draft | ready | published
dateCreated: "2026-01-01"
sources: []
---
```

Parser : `type, slug = entry.split(":", 1)`
Avantage : nouveau type = nouveau dossier + nouveau préfixe, zéro
modification des scripts.

### Migration depuis le schéma actuel (Projet_Automate)

`backlinks_updater.py --migrate` doit fusionner :

- `relatedConcepts[]` → `related: [concept:slug, ...]`
- `relatedProjects[]` → `related: [project:slug, ...]`
- `relatedArticles[]` → `related: [article:slug, ...]`

En une passe, sans perte de données.

### Clusters (V1 : concepts uniquement)

Liste évolutive — nouveaux clusters créés librement dans le frontmatter.
Clusters de départ :
Productivité, Cognition, Systèmes, IA & Outils, Philosophie,
Finance & Marchés, Travail & IA, Stratégie & Levier, Psychologie Sociale

Vision : clusters sur tous les types → graphe global où concepts,
livres, auteurs, projets et articles apparaissent comme nœuds liés.

---

## Stack

- **Fiches** : `.md` avec frontmatter YAML
- **Backlinks** : `scripts/backlinks_updater.py` (Python, depuis Projet_Automate)
- **Git hook local** : `post-commit` générique (`python3`)
- **Graphe** : Vite + React + `3d-force-graph` (même lib qu'ekenor.com)
- **Génération graph.json** : `scripts/generate_graph.js` (Node, à créer)
- **CI/CD** : GitHub Actions pour validation PR + regénération graphe public
- **Deps** : `requirements.txt` (pyyaml) + `package.json`

---

## Base de code à réutiliser depuis Ekenor

Repo Ekenor : `d:/Projet_Newsletter_Hub`

| Ekenor | KMS | Adaptation nécessaire |
|--------|-----|-----------------------|
| `src/components/ConceptMap.tsx` | `src/ConceptMap.tsx` | Retirer lang/enSlugsMap, click → nouvel onglet |
| `src/layouts/BaseLayout.astro` | Base HTML | Simplifier : retirer i18n, nav Ekenor, Resend |
| `src/layouts/ConceptLayout.astro` | Page fiche | Adapter pour lecture locale |
| `src/pages/[lang]/concepts/map.astro` | `src/pages/graph.astro` | Retirer routing bilingue |

**Option à trancher au démarrage** : Vite + React pur (sans Astro) pour
simplifier le setup standalone. Pas de `output: 'server'`, pas de content
collections, pas de routing bilingue. Probablement le bon choix pour V1.

---

## Structure du repo

```
kms/
├── notes/
│   ├── concepts/               ← fiches concept (.md)
│   ├── books/                  ← fiches livre
│   ├── authors/                ← fiches auteur
│   ├── projects/               ← fiches projet
│   └── articles/               ← fiches article / newsletter
├── scripts/
│   ├── backlinks_updater.py    ← recalcule citedBy[]
│   ├── generate_graph.js       ← lit les .md → produit _graph.json
│   ├── check_duplicates.py     ← détection doublons (voir section CI)
│   └── install_hooks.sh        ← installe le git hook post-commit
├── .githooks/
│   └── post-commit             ← python3 backlinks_updater.py
│                                  + node generate_graph.js
├── .github/
│   ├── workflows/
│   │   ├── validate-pr.yml     ← validation automatique des PRs
│   │   └── generate-graph.yml  ← regénère _graph.json après merge
│   └── ISSUE_TEMPLATE/
│       ├── new-concept.md
│       └── broken-link.md
├── src/
│   ├── ConceptMap.tsx          ← depuis Ekenor, adapté standalone
│   ├── ConceptPage.tsx         ← page fiche (rendu Markdown)
│   └── main.tsx                ← routing /graph + /concept/:slug
├── .claude/
│   └── commands/
│       ├── new-concept.md
│       ├── new-book.md
│       ├── new-author.md
│       ├── link-concepts.md
│       ├── sync-graph.md
│       ├── brainstorm-km.md
│       └── review-pr.md        ← review PR GitHub depuis Claude Code
├── _graph.json                 ← graphe public (racine, servi statiquement)
├── INDEX.md                    ← liste de tous les nœuds par type
├── TEMPLATE_CONCEPT.md
├── TEMPLATE_BOOK.md
├── TEMPLATE_AUTHOR.md
├── CONTRIBUTING.md
├── requirements.txt
├── package.json
└── README.md
```

---

## Graphe public — ConceptMap.tsx

Copier depuis `d:/Projet_Newsletter_Hub/src/components/ConceptMap.tsx`.

**Différences avec la version Ekenor :**

- `onNodeClick` : `window.open('/concept/${node.id}', '_blank')`
- Pas de `lang` ni `enSlugsMap` — mono-langue V1
- `graphData` chargé depuis `fetch('/_graph.json')`
- Hauteur : `100vh - 120px` au lieu de `600px` fixe

**Format `_graph.json`** (identique à Ekenor) :

```json
{
  "clusters": {
    "Systèmes": { "color": "#4a90d9", "emoji": "⚙️" },
    "Cognition": { "color": "#e67e22", "emoji": "🧠" }
  },
  "concepts": [
    {
      "slug": "small-world-network",
      "title": "Small World Network",
      "summary": "Réseau où tout nœud est accessible depuis tout autre en ≤5 liens.",
      "cluster": "Systèmes",
      "relatedConcepts": ["permissionless-leverage", "shelling-point"]
    }
  ]
}
```

`generate_graph.js` lit tous les `.md` de `notes/`, extrait title +
type + cluster + summary (1ère phrase du body) + slugs `related`.

---

## Système de contribution — GitHub Actions

### validate-pr.yml

Déclenché sur chaque PR vers `main`. Vérifie :

**1. Frontmatter valide**
- Champs obligatoires présents : `title`, `cluster`, `related`, `status`, `dateCreated`
- Format `related` correct : préfixe valide + slug kebab-case
- `status` dans `[draft, ready, published]`

**2. Liens non cassés**
- Chaque slug dans `related` doit exister dans le repo OU dans la PR elle-même
- Sinon : commentaire automatique listant les slugs manquants

**3. Détection de doublons — `check_duplicates.py`**

Algorithme :
- Pour chaque nouvelle fiche dans la PR, comparer avec toutes les fiches existantes
- Comparaison sur **titre normalisé** : minuscules + retrait accents + retrait stopwords
  (`le`, `la`, `les`, `de`, `du`, `des`, `et`, `the`, `of`, `a`)
- Seuil similarité : score Jaccard sur les tokens > 0.6 → doublon probable
- Comparaison aussi sur les **aliases** déclarés dans le frontmatter

Si doublon détecté → commentaire automatique sur la PR :
```
⚠️ Doublon potentiel détecté

La fiche `ego-depletion-baumeister.md` (PR) ressemble à `ego-depletion.md` (repo).
Score de similarité : 0.78

Options :
- Fusionner dans la fiche existante et fermer cette PR
- Garder les deux si les angles sont vraiment différents (expliquer dans la PR)
- Agréger : ajouter tes sources/contenu à la fiche existante via une PR de mise à jour
```

La PR n'est pas bloquée automatiquement — c'est une alerte. Le maintainer décide.

**4. Résumé de la PR**

Le bot commente automatiquement :
```
✅ Validation KMS

Fiches ajoutées : 3 (2 concepts, 1 book)
Liens vérifiés : 12 / 12 valides
Doublons détectés : 1 (voir commentaire ci-dessus)
Nouveaux clusters : aucun
```

### generate-graph.yml

Déclenché sur chaque merge sur `main`.
Lance `node scripts/generate_graph.js` → commit `_graph.json` mis à jour.
Le graphe public est toujours à jour sans action manuelle.

---

## Commandes Claude Code

### `/new-concept [titre optionnel]`

1. Demande : titre, cluster (liste les clusters depuis `_graph.json`),
   résumé en 1 phrase, sources connues
2. Crée `notes/concepts/[slug].md` avec frontmatter canonique
3. Lance `backlinks_updater.py --scan` → affiche liens suggérés,
   confirmation un par un
4. Affiche le template pré-rempli pour rédaction du body

### `/new-book [titre optionnel]`

1. Demande : titre, auteur, année, concepts extraits, citation clé
2. Crée `notes/books/[slug].md`
3. Crée ou met à jour `notes/authors/[auteur-slug].md` — demande confirmation
4. Lie automatiquement le livre aux concepts mentionnés

### `/new-author [nom optionnel]`

1. Demande : nom, domaine, livres connus, concepts associés
2. Crée `notes/authors/[slug].md`
3. Lie aux livres déjà présents dans `notes/books/`

### `/link-concepts`

Wrapper de `backlinks_updater.py --scan`.
Affiche les mentions non liées avec confirmation une par une.
Écrit dans le frontmatter à confirmation.

### `/sync-graph`

1. `node scripts/generate_graph.js` → régénère `_graph.json`
2. `python3 scripts/backlinks_updater.py` → recalcule `citedBy[]`
3. Régénère `INDEX.md`
4. Résumé : N concepts, N livres, N auteurs, N liens, N clusters

### `/brainstorm-km [source]`

Source = URL, texte collé, transcript, podcast, livre.

Outputs par type selon ce qui est mentionné dans la source :

- Concepts → `notes/concepts/[slug].md` (draft)
- Livres cités → `notes/books/[slug].md` (draft)
- Auteurs cités → `notes/authors/[slug].md` (draft)
- Projets mentionnés → `notes/projects/[slug].md` (draft)

Pour chaque fiche : frontmatter pré-rempli + sections body à remplir.
Liens entre nouvelles fiches et existantes : proposés, non créés auto.
Résumé : X fiches créées, Y liens proposés.

Flag `--pr` : au lieu de committer sur la branche courante, crée une
branche `contribution/brainstorm-YYYY-MM-DD` et ouvre une PR GitHub.

### `/review-pr [numéro optionnel]`

Commande de review PR depuis Claude Code — pour le maintainer (toi).

Sans numéro : liste les PRs ouvertes avec leur statut de validation CI.
Avec numéro : charge les fiches ajoutées dans la PR et affiche :

- Résumé des fiches (titre, cluster, liens)
- Doublons potentiels détectés par le CI avec score de similarité
- Liens cassés éventuels
- Recommandation : merger / demander modifications / rejeter

Propose des commentaires de review à poster sur GitHub.
Ne merge jamais automatiquement — toujours confirmation explicite.

---

## Fiches d'exemple à inclure

Depuis `.private/notes/concepts/` de Projet_Automate.
Copier et migrer au nouveau schéma `related` unifié.

| Fichier source | Slug cible | Cluster |
|---|---|---|
| `Small_World_Network.md` | `small-world-network` | Systèmes |
| `Ego_depletion_volonte_limitee.md` | `ego-depletion` | Cognition |
| `Planning_Fallacy.md` | `planning-fallacy` | Productivité |
| `Loi_de_Gall_systemes_simples.md` | `loi-de-gall` | Systèmes |
| `Permissionless_Leverage.md` | `permissionless-leverage` | Stratégie & Levier |
| `Specific_Knowledge.md` | `specific-knowledge` | Stratégie & Levier |
| `Feynman_Technique.md` | `feynman-technique` | Cognition |
| `Retrieval_Practice.md` | `retrieval-practice` | Cognition |

Ces 8 fiches couvrent 4 clusters et ont déjà des liens entre elles —
le graphe est non-trivial dès le lancement.

---

## README — ce qui doit être expliqué

### Section "Vault personnel vs graphe public"

Expliquer clairement :

> Ton vault est local. Tu décides ce que tu publies.
>
> Par défaut, tout reste sur ta machine. Le graphe que tu vois dans
> ton navigateur (`npm run dev`) est le tien — personnel, privé.
>
> Si tu veux contribuer une fiche au graphe public :
> 1. Crée une branche : `git checkout -b contribution/[slug]`
> 2. Ajoute ta fiche, lance `/sync-graph`
> 3. Push et ouvre une PR
> 4. Le CI vérifie automatiquement (liens, doublons, format)
> 5. Review humaine → merge → ta fiche rejoint le graphe public

### Setup en 5 commandes

```bash
git clone https://github.com/[user]/kms
cd kms
pip install -r requirements.txt
npm install
bash scripts/install_hooks.sh
npm run dev    # → localhost:5173/graph
```

---

## Contraintes

- Zéro credential, zéro API externe — tout tourne en local
- Graphe visuellement identique à ekenor.com/fr/concepts/map
- Click nœud → `window.open('/concept/:slug', '_blank')`
- V1 FR only, pas de multi-langue
- V1 lecture + navigation — édition dans l'éditeur de code
- Pas de génération LLM sans supervision humaine
- Le CI ne bloque jamais automatiquement — il alerte, le maintainer décide

---

## Output attendu de la session de build

1. `projects/knowledge_curator/KMS_SPEC.md` — spec complète
2. Structure de dossiers `projects/knowledge_curator/kms/` créée
3. Les 7 commandes `.claude/commands/` rédigées avec contenu complet
4. `scripts/backlinks_updater.py` mis à jour :
   - `NOTES_DIR` configurable (remplace `CONCEPTS_DIR`)
   - Support schéma `related` unifié
   - `--migrate` fusionne les anciens champs séparés
5. `scripts/generate_graph.js` créé
6. `scripts/check_duplicates.py` créé
7. `scripts/install_hooks.sh` créé
8. `.github/workflows/validate-pr.yml` créé
9. `.github/workflows/generate-graph.yml` créé
10. `src/ConceptMap.tsx` adapté depuis Ekenor
11. `src/ConceptPage.tsx` créé
12. `src/main.tsx` créé avec routing `/graph` + `/concept/:slug`
13. `CONTRIBUTING.md` rédigé
14. `README.md` rédigé avec section privé/public
15. Les 8 fiches d'exemple copiées et migrées
16. Entrée `#8b KMS` ajoutée dans `.private/IDEES_PROJETS.md`
