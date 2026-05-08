# KMS — Knowledge Management System — Spec V1

## Objectif

Pipeline KM complet publiable en open source. Quelqu'un clone le repo, lance 5 commandes, et a un système de knowledge management opérationnel avec graphe 3D interactif dans son navigateur : nœuds cliquables, clusters colorés, backlinks automatiques à chaque commit.

## Problème résolu

Les outils KM existants (Obsidian, Roam, Notion) sont soit fermés, soit sans graphe interactif publishable, soit sans pipeline de contribution communautaire validé. KMS est un vault local + graphe public open source, avec CI/CD intégré.

## Stack

- **Fiches** : `.md` avec frontmatter YAML
- **Backlinks** : `scripts/backlinks_updater.py` (Python + pyyaml)
- **Git hook local** : `.githooks/post-commit`
- **Graphe** : Vite + React + `3d-force-graph`
- **Génération graph.json** : `scripts/generate_graph.js` (Node)
- **CI/CD** : GitHub Actions (validate-pr + generate-graph)
- **Deps** : `requirements.txt` (pyyaml) + `package.json`

## Architecture

```
Flux local :
  clone kms → ajoute fiches → git commit
  → post-commit hook → backlinks recalculés + _graph.json regénéré
  → npm run dev → graphe visible sur localhost:5173/graph

Flux contribution :
  git checkout -b contribution/[slug]
  → push fork → PR → GitHub Actions vérifie
  → review humaine → merge → _graph.json public regénéré auto
```

## Schéma frontmatter canonique

```yaml
---
title: "Nom du concept"
type: concept          # dérivé du dossier parent
cluster: Systèmes
related:
  - concept:small-world-network
  - book:naval-almanack
  - author:naval-ravikant
  - project:knowledge-management
  - article:nl-01-poiesis-praxis
citedBy: []            # calculé auto — ne pas éditer à la main
aliases:
  fr: []
  en: []
tags: []
status: draft          # draft | ready | published
dateCreated: "2026-01-01"
sources: []
---
```

## Types de fiches

| Dossier | Type | Préfixe related |
|---------|------|----------------|
| notes/concepts/ | concept | `concept:` |
| notes/books/ | book | `book:` |
| notes/authors/ | author | `author:` |
| notes/projects/ | project | `project:` |
| notes/articles/ | article | `article:` |

## Clusters de départ

Productivité, Cognition, Systèmes, IA & Outils, Philosophie,
Finance & Marchés, Travail & IA, Stratégie & Levier, Psychologie Sociale

## Phases

- [x] V1 : Structure + scripts + graphe + 8 fiches d'exemple + CI/CD + commandes Claude
- [ ] V2 : Clusters sur tous les types (books/authors dans le graphe) + **contributeurs dérivés du git log**
- [ ] V3 : Mode contribution UI (pas seulement CLI)

## Contributeurs (V2) — modèle Wikipedia

Pas de champ `author` dans le frontmatter — git est la source de vérité.

**Sur la page fiche** : "Contribué par @pseudo1, @pseudo2" — dérivé de `git log --follow --format="%an" notes/[type]/[slug].md`.

**Page `/contributors`** générée automatiquement par `generate_graph.js` :

- Liste des contributeurs par nombre de fiches créées/modifiées
- Dérivée de `git log --format="%an" -- notes/` à la génération

Avantages vs champ manuel :

- Infalsifiable — l'historique git ne ment pas
- Automatique — aucune maintenance
- Complet — capture toutes les modifications, pas seulement la création
- Modèle Wikipedia : chaque fiche a son historique de révisions traçable

## Repo GitHub

`kms` (Knowledge Management System)

## Contraintes

- Zéro credential, zéro API externe — tout tourne en local
- Graphe visuellement identique à ekenor.com/fr/concepts/map
- Click nœud → `window.open('/concept/:slug', '_blank')`
- V1 FR only
- V1 lecture + navigation uniquement (édition dans l'éditeur)
- Pas de génération LLM sans supervision humaine
- Le CI ne bloque jamais automatiquement — il alerte, le maintainer décide
