# Hypothesis-Variable Tracker (HVT) — Spec

> **Statut** : Idée — spec validée 2026-05-14
> **Projet** : #52 dans `IDEES_PROJETS.md`
> **Origine** : Tugan Labossière — podcast Mass Extract (2026-05-14)
> **Concept lié** : `.private/notes/concepts/Hypothesis_Variable_Framework.md`

---

## Vision

Moteur d'analyse autonome de thèses. Tu énonces une thèse centrale, tu fournis des sources brutes — le HVT décompose, collecte dans 4 piliers, itère hypothèse × variable, et sort une analyse convergée et sourcée.

**Ce que le HVT n'est pas** : un outil de KM. Le KM (#8) ingère et structure la connaissance (crée la base). Le HVT raisonne par-dessus (analyse la thèse). Les deux peuvent vivre indépendamment.

**Cas d'usage principaux** :
- Vérifier la véracité d'une thèse complexe (médicale, fiscale, business, géopolitique)
- Préparer un article de l'Actualité Analysée avec rigueur sourcée
- Dépasser les avis d'experts contradictoires sans se noyer dedans

---

## Pipeline complet

### Étape 1 — Thèse centrale

Tu énonces : "Voici ma thèse."

Le HVT :
1. Reformule la thèse de façon précise et testable
2. Te la soumet pour confirmation

**Validation humaine requise avant de continuer.**

---

### Étape 2 — Génération des hypothèses (A, B, C…)

Le moteur décompose la thèse en hypothèses distinctes et testables.

Règles :
- Chaque hypothèse est indépendante (on peut l'infirmer sans infirmer les autres)
- Maximum 5-7 hypothèses par thèse (au-delà = thèse trop large, à découper)
- Libellé format : "Si [condition], alors [conséquence observable]"

**Validation humaine** : tu valides, retires ou reformules avant de passer à l'étape 3.

---

### Étape 3 — Variables par hypothèse (1, 2, 3…)

Pour chaque hypothèse validée, le moteur identifie les variables observables et testables individuellement.

Règles :
- Une variable = un élément qu'on peut modifier ou mesurer isolément
- On modifiera **une seule variable à la fois** lors de l'itération (étape 5)
- Numérotation continue sur toutes les hypothèses (variable 1, 2, 3… sans recommencer à 1 pour chaque hypothèse)

**Validation humaine** avant collecte.

---

### Étape 4 — Collecte automatisée par pilier

Pour chaque variable, collecte parallèle dans 4 piliers :

#### Pilier 1 — Crowd sourcing
- Sources : Reddit (PRAW), YouTube transcripts (youtube-transcript-api), forums spécialisés, blogs
- Consigne IA critique : extraire uniquement les **spécificités** — chiffres réels, protocoles précis, timelines concrètes. Jamais les résumés généraux. L'IA tend à simplifier → lui demander explicitement de lister les données précises.
- Format output : liste de données spécifiques avec source URL

#### Pilier 2 — Data perso
- Sources : vault KM (#8), notes Notion, historique de recherche personnelle
- Optionnel si HVT utilisé standalone (sans KM connecté)
- Format output : extraits des fiches pertinentes avec lien

#### Pilier 3 — Experts (mode chasse au trésor)
- **Principe fondamental** : on ne cherche pas la confirmation — on cherche la **question inédite**.
- Un expert qui pose la même question que les précédents = perdu (information redondante).
- Un expert qui ouvre une dimension non explorée = jackpot (nouvelle hypothèse ou variable).
- Mécanique : le moteur identifie des experts variés (profils différents, écoles de pensée différentes) → génère des questions ciblées pour maximiser la diversité des angles → agrège les réponses en cherchant les divergences, pas les consensus.
- À chaque expert consulté : noter s'il a posé une question ou proposé un diagnostic qu'aucun autre n'avait formulé. Si oui → nouvelle hypothèse ou variable potentielle.
- Format output : tableau [Expert | Question inédite apportée | Hypothèse/variable déclenchée]

#### Pilier 4 — Science
- Sources : Semantic Scholar API (gratuit), arXiv, PubMed (médical), SSRN (économie/finance)
- Chercher les papers qui testent directement les variables identifiées
- Format output : liste [Titre | Auteurs | Résultat clé | Lien]

---

### Étape 5 — Itération hypothèse × variable

Le moteur teste chaque variable **une par une**, en gardant toutes les autres constantes.

Mécanique :
1. Pour chaque hypothèse (A, B, C…) : tester variable 1, puis variable 2, etc.
2. À chaque test : croiser avec les 4 piliers collectés
3. Scorer : Confirmé ✅ / Infirmé ❌ / Partiel ⚠️ / Insuffisant (données manquantes) 🔲
4. Si une variable révèle une nouvelle hypothèse → l'ajouter et relancer

Convergence : quand toutes les variables d'une hypothèse sont testées, scorer l'hypothèse globale.

---

### Étape 6 — Synthèse

Output structuré :

```markdown
## Thèse : [énoncé]
## Verdict global : [Confirmée / Infirmée / Partielle / Incertaine]

### Hypothèse A — [libellé]
**Verdict** : ✅ Confirmée
**Variables testées** : 1 (✅), 2 (✅), 3 (⚠️)
**Sources principales** : [Pilier 1 : X, Pilier 4 : Y]
**Nuance** : [ce qui reste incertain]

### Hypothèse B — [libellé]
...

## Claims à sourcer (pour article)
- [Claim 1] → Source : [Pilier X, URL]
- [Claim 2] → Source : [Pilier Y, URL]

## Hypothèses non résolues (à approfondir)
- [Hypothèse C] : données insuffisantes sur variable 4
```

---

## Architecture technique

### Moteur
- **Orchestration** : Claude Code (raisonnement principal + coordination des agents)
- **Agents spécialisés par pilier** : chaque pilier = un agent avec son propre contexte et ses outils

### APIs et outils par pilier

| Pilier | Outil | Coût |
|--------|-------|------|
| Crowd — Reddit | PRAW (Python Reddit API Wrapper) | Gratuit (OAuth) |
| Crowd — YouTube | youtube-transcript-api | Gratuit |
| Data perso — KM | Lecture directe vault `.private/notes/` | Interne |
| Science | Semantic Scholar API | Gratuit |
| Science | arXiv API | Gratuit |
| Science | PubMed E-utilities | Gratuit |

### Interface
Conversationnelle — tu énonces la thèse dans une conversation Claude Code. Les validations (étapes 1-3) sont des retours courts. La collecte et l'itération sont automatisées. Output final en Markdown.

### Storage
Un dossier par thèse : `projects/hypothesis_variable_tracker/theses/YYYY-MM-DD-slug/`
- `thesis.md` : thèse + hypothèses + variables
- `pilier_crowd.md` : données collectées
- `pilier_data_perso.md`
- `pilier_experts.md`
- `pilier_science.md`
- `synthesis.md` : output final

---

## Connexions écosystème

| Projet | Type de connexion |
|--------|------------------|
| #8 KM | Pilier "data perso" branché sur le vault — optionnel |
| Actualité Analysée | HVT = template de travail systématique pour chaque article |
| #15 Context Engineer | Contexte initial enrichi avant lancement du pipeline |

---

## Roadmap

### V1 — Manuel assisté
- Interface : conversation Claude Code
- Étapes 1-3 : semi-automatiques (Claude propose, tu valides)
- Étape 4 : collecte manuelle (tu fournis les sources, Claude structure)
- Étapes 5-6 : Claude itère et synthétise
- Livrable : Markdown par thèse

### V2 — Automatisation piliers
- Pilier 1 automatisé : scraping Reddit + YouTube transcripts
- Pilier 4 automatisé : requêtes Semantic Scholar
- Pilier 3 semi-auto : Claude génère les questions experts, tu les envoies

### V3 — Pipeline complet
- Tous les piliers automatisés
- Interface web légère (Astro)
- Connexion KM native
- Potentiel : freemium (3 thèses gratuites, illimité payant)
