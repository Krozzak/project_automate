---
title: "J'oublie 80% de mon voyage en une semaine. Alors j'ai construit un bot."
slug: "2026-03-30-memory-logger"
type: AUTOMATISATION
projet: Memory Logger
status: Brouillon — à finaliser avant publication
planned_date: "2026-03-30"
slot: Lundi
concept: "Courbe de l'oubli (Ebbinghaus, 1885) + Retrieval Practice (Roediger, 2006)"
concept_level: Simple
tags: [mémoire, voyage, capture, Telegram, Notion, Ebbinghaus]
linkedin_url: ""
lesson: ""
rules_applied: [structure-3-actes, max-2-takeaways, sourcing-naturalisé, récit-personnel-spécifique, accroche-3-lignes, concept-seulement-si-il-colle, pas-de-teasing, angle-personnel-narratif, accroche-chiffre-contraste]
rule_added: ""
rule_hypothesis: ""
---

# POST ML.1 — MEMORY LOGGER — Lundi 30/03

**Type** : AUTOMATISATION
**Sous-thème** : Capture mémorielle + Retrieval Practice passif
**Projet** : Memory Logger V1
**Visuels** : Screenshot Telegram (note vocale → confirmation structurée) + Screenshot Notion (entrée journal avec lieu, mood, type, highlight)

---

## Key takeaways

1. On oublie 80% de son voyage en une semaine — les détails d'abord, puis les histoires
2. Raconter au bot chaque soir = zéro friction + ancrage mémoriel double (noter ET rappeler active le souvenir)

---

## Post LinkedIn

Il y a deux ans, j'ai essayé de me rappeler d'un voyage sans notes. 80% oublié.
L'année dernière, j'avais pris quelques lignes par jour. 60% oublié.
Cette année, j'ai raconté chaque soir à un bot comme je l'aurais fait à un pote.

La différence entre les trois, c'est pas la mémoire — c'est comment tu captures.

Ebbinghaus l'a mesuré en 1885 : sans rappel actif, la mémoire se dégrade exponentiellement. Roediger a précisé en 2006 — ce n'est pas relire qui aide, c'est raconter. L'acte de rappeler un souvenir le renforce plus que de le revoir. Le Testing Effect.

Écrire quelques lignes, c'est déjà mieux que rien. Mais raconter à voix haute comme si tu t'adressais à quelqu'un — c'est un autre niveau. Tu reconstruis l'histoire, pas juste les faits. Les Grecs le savaient déjà : la tradition orale ne transmettait pas des faits, elle racontait des histoires. Raconter, c'est ancrer.

Chaque soir, je sortais mon téléphone et je racontais ma journée. Un repas, une rencontre, un truc qui avait mal tourné. Trois minutes, parfois moins. Derrière la note vocale, un workflow Telegram → Whisper → GPT → Notion. Chaque entrée ressort structurée automatiquement : lieu, mood, type d'activité, si c'était un moment fort.

Je n'ai rien écrit. Je n'ai rien tapé. J'ai juste raconté.

Au lieu de retrouver des bribes, j'ai retrouvé les histoires complètes.

---

## Commentaire épinglé

Le workflow complet est sur GitHub : [lien — à ajouter après `/publish-workflow`]
La page projet : ekenor.com/fr/projects/memory-logger

---

## Notes pour les visuels

| Slide | Description | Ce qu'on montre |
|-------|-------------|-----------------|
| 1 | Screenshot Telegram | Note vocale envoyée → confirmation bot : "Jour 3 · Médina · Culture · ⭐ Highlight" |
| 2 | Screenshot Notion | Vue de la base Journal : colonnes Lieu, Jour, Type, Mood, Highlights — quelques entrées visibles |

**Règle visuels** : sans texte ajouté, sans annotations, sans flèches. Screenshots bruts.
**Dark mode** recommandé pour Telegram. Light ou dark pour Notion selon rendu.

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | accroche-chiffre-contraste (3/3) + angle-personnel-narratif (1/3) | à mesurer |

---

## Todo avant publication

- [ ] Ajouter screenshots dans ce dossier (Telegram entrée vocale + Notion journal)
- [ ] Lancer `/publish-workflow` sur Memory Logger → récupérer lien GitHub
- [ ] Mettre à jour le commentaire épinglé avec le vrai lien GitHub
- [ ] Mettre à jour `linkedinPosts` dans `d:/Projet_Newsletter_Hub/src/content/projects/memory-logger.md` après publication

---

## Notes de session

- `accroche-chiffre-contraste` : 3ème et dernier post de test — "80% d'un voyage oublié en une semaine" est le chiffre de contraste. À valider dès que stats disponibles.
- `angle-personnel-narratif` : 1er post isolé de ce test (E.2 Ekenor était simultané avec autre chose). Ce post part d'une tension vécue ("chaque soir, avant de dormir") sans présenter le projet en premier.
- Transactive Memory non mentionnée dans le post — lien trop conceptuel pour ce post. Réservée pour ML.2 ou post jeudi.
- Retrieval Practice sourcé naturellement dans le flux, pas comme cours.
- Post se termine sur "tout était là" — phrase punch sobre, pas de question forcée.
