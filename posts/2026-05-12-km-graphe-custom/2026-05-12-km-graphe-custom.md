---
title: "J'ai reconstruit ma mémoire"
slug: "2026-05-12-km-graphe-custom"
type: AUTOMATISATION
projet: "KM #8"
status: Brouillon
planned_date: "2026-05-12"
slot: Mardi
concept: ""
concept_level: Simple
tags: [knowledge-management, graphe, obsidian, github, claude-code]
linkedin_url: ""
lesson: ""
rules_applied: [accroche-3-lignes, récit-personnel-spécifique, voix-vecue-pas-pattern, max-2-takeaways, solution-en-narration-pas-en-liste]
rule_added: ""
rule_hypothesis: ""
---

## POST 8.1 — MAI 2026, SEMAINE 2

**Type** : AUTOMATISATION
**Sous-thème** : Knowledge Management, graphe de concepts, Obsidian, Claude Code
**Projet** : KM #8
**Visuels** : Screenshot du graphe 3D ekenor.com/fr/concepts/map

---

## Key takeaways

1. Un graphe de connaissance connecté génère des angles éditoriaux qu'on ne produit pas seul — c'est un outil de génération, pas de stockage.
2. Versionné sur GitHub, intégré à l'écosystème, scannable par Claude Code — adapté à l'usage exact, pas à la hype Obsidian.

---

## Post LinkedIn

J'ai reconstruit ma mémoire. En créant un graphe de connaissance.
C'est comme Obsidian mais directement sur Github.
Claude Code peut ensuite parcourir cette connaissance et faire des liens inattendus entre des concepts de thématiques différentes.

85 fiches — chaque podcast, chaque article, chaque idée formalisée depuis deux ans.
Toutes liées entre elles. Navigables sur ekenor.com.

En écrivant un article sur l'IA et le travail, j'avais une intuition sur les compétences menacées.
Claude a remonté un concept d'économie dans le graphe : l'élasticité des prix.
Ça a produit une phrase que j'aurais pas écrite seul :
"Les compétences obéissent aux mêmes lois que les prix : ce qui est substituable finit par être substitué."

Ce lien venait de deux clusters complètement différents.

C'est ça que le graphe fait — pas stocker, connecter des domaines que le cerveau n'associe pas naturellement.
Et formaliser des liens qu'on avait faits intuitivement sans le savoir.

---

## Commentaire épinglé

Le graphe est navigable ici : ekenor.com/fr/concepts/map

---

## Notes pour les visuels

| Slide | Description | Ce qu'on montre |
|-------|-------------|-----------------|
| 1 | Screenshot graphe 3D ekenor.com/fr/concepts/map | Les clusters de concepts et les liens entre eux — la mémoire visualisée |

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | — | — |

---

## Notes de session — 2026-05-08

### Statut
Post en brouillon — accroche validée par Thomas (dictée textos), corps à finaliser
ce weekend. Ne pas réécrire l'accroche, elle est fixée :

> "J'ai reconstruit ma mémoire. En créant un graphe de connaissance.
> C'est comme Obsidian mais directement sur Github.
> Claude Code peut ensuite parcourir cette connaissance et faire des liens
> inattendus entre des concepts de thématiques différentes."

### Ce qui a été décidé pendant la session

Le post a déclenché une réflexion sur la publication du système en open source.
Résultat : le projet **KMS (Knowledge Management System)** a été spécifié.

- Repo GitHub créé pendant la session (dans une discussion parallèle)
- Prompt de build complet : `projects/knowledge_curator/KMS_BUILD_PROMPT.md`
- `/new-automation` réécrite en générique (supporte web-app, site-astro,
  extension, script, plugin, api — plus seulement n8n)

### Pour finaliser le post ce weekend

1. Lire le repo KMS créé (URL à récupérer depuis l'autre discussion)
2. Vérifier combien de fiches sont publiques dans le repo au moment de la rédaction
   → mettre à jour "85 fiches" si le chiffre a changé
3. Décider si on mentionne le repo GitHub dans le post ou juste ekenor.com
   → si le repo est public et propre : ajouter en commentaire épinglé
4. Le corps du post est à retravailler — Thomas n'était pas inspiré ce jour-là,
   les formulations sonnent encore génériques après l'accroche
5. Angle à garder : l'exemple concret Price Inelasticity → compétences est le
   point fort — ne pas le diluer

### Décisions d'architecture KMS (contexte pour le prochain post)

- Structure par dossier : `notes/concepts/`, `notes/books/`, `notes/authors/`...
- Schéma `related` unifié avec préfixes (`concept:`, `book:`, `author:`...)
- Deux graphes : vault local privé + graphe public GitHub
- GitHub Actions : validation PR + détection doublons (similarité Jaccard)
- Dual licence : MIT (code) + CC BY-SA 4.0 (contenu notes/)
- `.gitignore` : `notes/private/` pour sandbox local non commitable
