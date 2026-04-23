---
title: "Claude Design — Before/After ProofsLab"
slug: "2026-04-22-claude-design-proofslab"
type: ACTUALITÉ
projet: "Claude Design / ProofsLab"
status: Brouillon V2
planned_date: "2026-04-22"
slot: Mercredi (actualité — à publier dans la journée)
concept: ""
concept_level: Simple
tags: ["claude-design", "proofslab", "ia", "design"]
linkedin_url: ""
lesson: ""
rules_applied: ["accroche-3-lignes", "récit-personnel-spécifique", "max-2-takeaways", "solution-en-narration-pas-en-liste", "phrase-punch-finale"]
rule_added: ""
rule_hypothesis: ""
---

# POST — ACTUALITÉ — 22 AVRIL 2026

**Type** : ACTUALITÉ
**Sous-thème** : Outil IA / Design / Build in public
**Projet** : Claude Design + ProofsLab
**Visuels** : Carousel recommandé — voir section Notes visuels

---

## Key takeaways

1. Claude Design ne génère pas — il comprend le brief, propose 3 directions différentes, et t'aide à choisir. C'est ça la rupture avec tous les outils avant.
2. Pour un builder non-designer, ça efface le blocage entre "j'ai une idée visuelle" et "j'ai quelque chose d'utilisable". Quelques heures au lieu de semaines.

---

## Post LinkedIn — V2

J'ai testé Claude Design sur ProofsLab en tant que non-designer,
Et j'ai trouvé ça incroyable.
En quelques heures, j'ai pu rebrander entièrement un site fonctionnel en site professionnel.

Ce qui m'a surpris : il ne génère pas d'abord.
Il pose des questions. Il veut comprendre l'ambiance, l'audience, ce que le produit doit faire ressentir.
Ensuite il propose 3 directions — vraiment différentes, avec des noms et une intention claire :

Studio (safe, éditorial), Spectrum (coloré, audacieux), Lab (technique, dark-first).

Pas une seule réponse. Un vrai choix.

J'ai pris Spectrum.
En quelques heures, j'avais un prototype complet — landing, workspace, dashboard, pricing — avec une charte que j'ai pu implémenter directement dans mon code.

Ce qui le distingue vraiment des alternatives : les autres outils supposent que tu sais déjà ce que tu veux.
Canva : tu dois avoir le goût. Bolt ou Lovable : tu dois savoir ce que tu codes. Un designer humain : tu dois savoir briefer.

Claude Design part du principe que tu ne sais pas — et il t'aide à découvrir.
Zéro expérience en design requise. Output 4 étoiles.
Pas 5 — un bon designer reste meilleur. Mais avec un investissement en temps et en argent sans commune mesure.

La limite honnête : une session aussi complète m'a bouffé tous mes crédits hebdomadaires en abonnement Pro.
C'est puissant. Pas illimité.

Before/after, process complet et comparatif détaillé → dans le carousel ci-dessous.

---

## Commentaire épinglé

_(optionnel — si tu veux pointer vers ProofsLab)_

```
ProofsLab : proofslab.com — l'outil de vérification de documents que j'ai construit.
```

---

## Reconstruction du process — extrait de la session Claude Design

> Ce que tu as vécu, étape par étape. À utiliser pour enrichir le carousel ou intégrer dans le post si tu veux montrer le mechanic.

**Étape 1 — Brief**
Tu décris le projet : ProofsLab, outil de vérification de documents. Claude lit le repo, comprend les composants, le périmètre.

**Étape 2 — Plan annoncé à voix haute**
Claude détaille ce qu'il va faire avant de générer : design tokens + logo, 3 directions, 6 pages (landing, workspace, compare, dashboard, historique, tarifs), toggle dark mode, switcher de direction flottant. Pas de boîte noire — tu sais exactement ce qui arrive.

**Étape 3 — Les 3 directions, avec intention**
Claude ne te sort pas 3 variantes de la même chose. Il te propose 3 philosophies différentes :

- **Studio** — crème chaleureux + indigo profond + serif. Éditorial, rassurant, un peu chic.
- **Spectrum** — palette multicolore Figma-like (cyan, magenta, lime, violet). Grands chiffres display. Audacieux, mémorable.
- **Lab** — dark navy + acid green, monospace, esthétique "capteur/laboratoire". Très créatif, technique assumé.

**Étape 4 — Implémentation**
Tu choisis Spectrum. Claude livre un fichier HTML complet avec les 3 directions, un sélecteur flottant, la navigation entre pages, le toggle dark mode, l'état persisté en localStorage. Tu implémentes directement dans ton code depuis la charte générée.

**La limite que tu as vécue :**
Une session aussi complète (6 pages, 3 directions, dark mode, logo redesigné) sur Claude Opus 4.7 = tous les crédits hebdomadaires d'un abonnement Pro consommés.

---

## Notes pour les visuels — Carousel 5 slides

| Slide | Description | Ce qu'on montre |
|-------|-------------|-----------------|
| 1 | Before / After | Ancien ProofsLab à gauche, Spectrum à droite — côte à côte |
| 2 | Le process Claude Design | 4 étapes : brief → questions → 3 directions → implémentation dans le code |
| 3 | Bonus — les 2 autres directions | Studio + Lab : montrer que c'était un vrai choix, pas une génération unique |
| 4 | Pour / Contre Claude Design | Avantages : rapidité, non-designer, pipeline code, collaboration view/comment/edit, input depuis lien ou inspiration. Limites : crédits hebdo, research preview, gros repos = lag |
| 5 | Comparatif | Claude Design vs Canva vs Bolt vs Lovable vs Designer humain — axes : temps, coût, courbe d'apprentissage, barrière à l'entrée, output |

---

## Charte graphique — à appliquer sur toutes les slides

> Source : BRAND.md + tailwind.config.mjs du site Ekenor. Palette "Forge & Nord" adaptée en thème light pour LinkedIn.

**Format** : 1080 × 1440 px (portrait 3:4) — taille personnalisée dans Canva

**Police** : **Inter** (ou Manrope si Inter indisponible) — les deux sont dans Canva

| Rôle | Style | Taille | Couleur |
|------|-------|--------|---------|
| Titre slide | Inter Bold | 52–60px | `#0f1117` |
| Label / sous-titre | Inter SemiBold | 28–34px | `#1A1F2E` |
| Corps / tableau | Inter Regular | 22–26px | `#3A3A4A` |

**Couleurs — thème light LinkedIn**

| Rôle | Couleur | Usage |
|------|---------|-------|
| Fond slide | `#F8F8F6` | Blanc cassé — propre, pas agressif |
| Cards / blocs | `#FFFFFF` | Sur le fond F8F8F6, les cards ressortent |
| Bordures | `#E0E4EA` | Séparateurs discrets |
| **Bleu glacier** (accent principal) | `#4A9EBB` | Highlights, cellule Claude Design dans le comparatif, liens |
| **Cuivre** (accent chaud) | `#C97B3A` | Titre principal de chaque slide — fond cuivre + texte blanc |
| Texte principal | `#0f1117` | Corps |
| Texte secondaire | `#6B6B7B` | Labels, notes |
| Pour / avantages | `#E8F5F0` fond + `#1A6B4A` texte | Colonne verte slide 4 |
| Contre / limites | `#FDF0EC` fond + `#C0440E` texte | Colonne orange-rouge slide 4 |

**Élément signature — titre de chaque slide :**
Rectangle fond `#C97B3A` (cuivre) — texte Inter Bold `#FFFFFF` — coins arrondis 8px — padding 12px 24px. Même traitement sur toutes les slides pour la cohérence.

**Logo** : `ekenor.com` — bas gauche, marge 40px, largeur ~200px — version dark (texte `#0f1117` ou logo SVG)

**Formes & éléments graphiques**

| Élément | Forme | Fond | Bordure | Coins |
|---------|-------|------|---------|-------|
| Titre slide | Rectangle | `#C97B3A` cuivre | Aucune | 8px |
| Card / bloc contenu | Rectangle | `#FFFFFF` | `#E0E4EA` 1px | 12px |
| Flèche de transition (ex: Before→After) | Flèche pleine | `#C97B3A` cuivre | `#0f1117` noir 1.5px | — |
| Flèche de process (étape→étape) | Flèche fine / chevron | `#4A9EBB` bleu glacier | Aucune | — |
| Badge / label | Pill | `#4A9EBB` bleu glacier | Aucune | 999px (full round) |
| Séparateur horizontal | Ligne | — | `#E0E4EA` 1px | — |
| Highlight cellule tableau | Rectangle | `#EAF5FA` (bleu glacier très clair) | `#4A9EBB` 1px | 6px |

**Règle générale formes :**
- Coins arrondis partout — jamais d'angle droit sec (sauf les séparateurs)
- Cuivre `#C97B3A` = action, transition, titre → réservé aux éléments qui guident l'œil
- Bleu `#4A9EBB` = information, highlight, label → réservé aux éléments qui qualifient
- Bordure noire `#0f1117` uniquement sur les flèches cuivre — crée le contraste sans alourdir

**Règles visuelles**
- Cards blanches `#FFFFFF` sur fond `#F8F8F6`, bordure `#E0E4EA`, coins arrondis 12px
- Drop shadow légère : `0 2px 8px rgba(0,0,0,0.06)`
- Padding interne 48–60px sur les bords de slide
- Pas de texte superposé sur les screenshots

---

## Guide slide par slide — Canva

**Slide 1 — Before / After**
- Titre haut : "Before → After" (Inter Bold, 56px)
- Moitié haute : screenshot ancien ProofsLab — label "Avant" en Inter SemiBold gris
- Ligne séparatrice fine `#E0E0E0`
- Moitié basse : screenshot Spectrum — label "Après" en Inter SemiBold bleu `#4A90D9`
- Logo Ekenor bas gauche

**Slide 2 — Le process**
- Titre : "Comment ça marche" (Inter Bold)
- 4 blocs verticaux avec flèches entre eux :
  1. 📋 Brief — "Tu décris ton projet ou tu colles un lien"
  2. ❓ Questions — "Claude comprend l'ambiance, l'audience, le style"
  3. 🎨 3 directions — "Studio / Spectrum / Lab — tu choisis"
  4. ⚡ Implémentation — "Design system exporté, intégré dans ton code"
- Fond de chaque bloc : blanc, coins arrondis, drop shadow légère

**Slide 3 — Bonus : les 2 autres directions**
- Titre : "Les directions que je n'ai pas choisies"
- 2 blocs côte à côte : screenshot Studio à gauche, screenshot Lab à droite
- Label sous chaque screenshot : nom + 3 mots clés (ex: "Studio — éditorial, crème, indigo")
- Note bas de page : "J'ai choisi Spectrum — voir slide 1"

**Slide 4 — Pour / Contre**
- Titre : "Claude Design — Pour / Contre"
- 2 colonnes : colonne verte (Pour) + colonne rouge douce (Contre)
- Fond colonne Pour : `#D4EDDA` — Fond colonne Contre : `#F8D7DA`
- 5 points max par colonne, Inter Regular 24px

**Slide 5 — Comparatif**
- Titre : "Claude Design vs les alternatives"
- Tableau complet : 5 outils en colonnes, 6 axes en lignes
- Colonne Claude Design surlignée en `#C7DCFF`
- Cellules avec ★ pour qualité, texte court pour les autres axes
- Note bas : "Données avril 2026"

---

## Données comparatif — Slide 5

> Source : recherches web avril 2026.

### Matrice résumée — Slide 5

> **Contexte de comparaison : redesign complet d'un site web (landing + pages internes, 5–10 pages)**
> Sources vérifiées : support.claude.com, WebFX, Cybernews, NxCode, BoostWithAiTools — avril 2026.
> Note coût freelance : $1 000–$15 000 = freelance indépendant. Agences établies : $15 000–$50 000+.

| | Claude Design + Claude Code | Canva AI | Bolt / Lovable | Designer + Dev freelance |
|--|--|--|--|--|
| **Temps résultat** | ~1–2h (design) + implémentation | Quelques heures (maquette) | Quelques heures | 2–4 mois (design + dev) |
| **Coût total** | Inclus abo ($20+/mois) | $13/mois | Gratuit–$25/mois | $5 000–$50 000+ (design + dev) |
| **Niveau requis pour démarrer** | Aucun — prompting naturel | Goût design utile | Aucun | Savoir briefer |
| **Courbe d'apprentissage** | Faible | Très faible | Faible | Nulle (tu délègues) |
| **Qualité redesign site** | ★★★★ | ★★★ (maquette statique) | ★★★ | ★★★★★ |
| **Design → Code** | ★★★★★ (pipeline natif) | ★ (export à recoder) | ★★★★★ (code direct) | ★★★ (handoff manuel) |
| **Site en production** | ✅ | ❌ | ✅ | ✅ |

---

### Pour / Contre Claude Design — Slide 4

**Pour :**

- Résultat en heures, pas en semaines
- Pas besoin de compétences design — prompting en langage naturel
- 3 directions visuelles distinctes proposées, pas une seule réponse
- Peut partir d'un lien de site existant ou d'images d'inspiration
- Collaboration intégrée : view-only, commentaire, édition au sein de l'organisation
- Pipeline direct vers Claude Code pour implémenter
- Compris dans l'abonnement existant (Pro, Max, Team, Enterprise)
- Rythme de développement Anthropic = les gaps comblés très vite

**Contre :**

- Limites de crédits hebdomadaires strictes (non publiées, mais réelles — une session complète = quota Pro consommé)
- Research preview — encore instable, pas de timeline GA
- Gros repositories peuvent causer du lag
- Plus tu es précis dans le brief, meilleur le résultat — courbe d'apprentissage légère
- Pas un remplacement Figma pour une équipe design pro à l'échelle

**Différences clés vs les alternatives :**

- **vs Bolt / Lovable** : ils livrent du code en production directement, sans vrai process de design. Claude Design fait le design proprement → Claude Code implémente. Meilleure qualité visuelle, en deux étapes.
- **vs Canva** : maquettes statiques à recoder manuellement après. Pas de pipeline code, pas de design system automatique.
- **vs Designer + Dev freelance** : qualité supérieure, mais $5 000–$50 000+ et 2–4 mois. Claude Design donne 80% du résultat en 2h pour le prix de l'abonnement.

### Points incertains — ne pas affirmer dans le post

- Les limites exactes hebdomadaires par plan ne sont pas publiées par Anthropic
- La durée du "research preview" n'est pas communiquée

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | phrase-punch-finale | — |
