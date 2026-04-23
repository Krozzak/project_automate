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

Le before/after, le process complet, et un comparatif avec Canva, Bolt et un designer humain → dans le carousel ci-dessous.

La limite honnête : une session aussi complète m'a bouffé tous mes crédits hebdomadaires en abonnement Pro.
C'est puissant. Pas illimité.

Mais pour débloquer un non-designer sur un vrai projet en production — rien de comparable pour l'instant.

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

**Règle visuelle :**
Screenshots bruts pour slides 1-3, infographie minimaliste (fond `#f5f5f5`) pour slides 4-5. Pas de texte superposé sur les screenshots.

---

## Données comparatif — Slide 5

> Source : recherches web avril 2026.

### Matrice résumée — Slide 5

> Source : support.claude.com + recherches web avril 2026. Lovable ajouté ($25/mois, génère du code fonctionnel d'emblée).

| | Claude Design | Canva AI | Bolt.new | Lovable | Designer freelance |
|--|--|--|--|--|--|
| **Temps résultat** | Quelques heures | Quelques minutes | Heures à jours | Heures | 2–4 semaines |
| **Coût** | Inclus abo ($20+/mois) | $13/mois | Gratuit (limité) | $25/mois | $1 000–$75 000 |
| **Courbe d'apprentissage** | Faible (prompting naturel) | Très faible | Faible | Faible | Aucune (tu délègues) |
| **Barrière à l'entrée** | Abo Claude Pro requis | Gratuit possible | Gratuit possible | Payant | Budget + brief |
| **Output** | Prototype visuel + design system | Assets marketing | Site/app fonctionnel | Site/app fonctionnel | Design production |
| **Design → Code** | ★★★★★ (Claude Code) | ★ | ★★★★★ | ★★★★★ | ★★★ |
| **Collaboration** | ✅ view/comment/edit (org) | ✅ | ✅ | ✅ | ✅ |
| **Input depuis lien/inspiration** | ✅ | ✅ | ✅ | ✅ | ✅ (brief) |

**Différence clé Bolt/Lovable vs Claude Design :** Bolt et Lovable génèrent du code fonctionnel directement. Claude Design génère un prototype visuel + design system qu'on implémente ensuite (ou via Claude Code). Pas le même usage — complémentaires plutôt que concurrents directs.

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
