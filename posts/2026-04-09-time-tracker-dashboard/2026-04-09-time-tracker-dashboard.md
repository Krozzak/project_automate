---
title: "J'ai utilisé mon Time Tracker toute la semaine. Voilà ce que les données disent."
slug: "2026-04-10-time-tracker-dashboard"
type: AUTOMATISATION
projet: "Time Tracker"
status: Publié
planned_date: "2026-04-09"
slot: Vendredi (exception semaine 1 — screenshots nécessitent une semaine complète de données)
concept: ""
concept_level: ""
tags: [time-tracker, dashboard, stats, semaine, heatmap]
linkedin_url: "https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_dapr%C3%A8s-mon-time-tracker-je-sous-estime-ugcPost-7447625403311095808-HXhZ"
lesson: ""
rules_applied: [structure-3-actes, récit-personnel-spécifique, accroche-3-lignes, phrase-punch-finale]
rule_added: ""
rule_hypothesis: ""
---

# POST TT.2b — AVRIL 2026, SEMAINE 1 (vendredi)

**Type** : AUTOMATISATION (suite features)
**Sous-thème** : Dashboard précision, WeekView, heatmap, patterns de travail
**Projet** : Time Tracker adaptatif (#47)
**Visuels** : 3 slides — slide 1 image concept, slide 2 screenshot StatsDashboard, slide 3 screenshot WeekView + heatmap

> ⚠️ **À faire vendredi matin 10/04** : screenshots StatsDashboard + WeekView après une semaine complète d'utilisation (lundi→vendredi). Mettre à jour le post avec les vrais chiffres de la slide 1 si pertinent.

---

## Key takeaways

1. Le StatsDashboard révèle le coef réel par catégorie — voir son propre chiffre c'est différent de savoir que le biais existe
2. Insight découvert par l'usage : une tâche de 3h étalée sur 4 jours = 4 jours pour le manager. Temps brut ≠ temps calendaire — c'est ça la vraie source du problème d'estimation

---

## Post LinkedIn

D'après mon Time Tracker, je sous-estime le temps de x2.
Et pire, je n'avais pas la bonne vision du temps.
Une tâche de 4h étalée sur 4 jours, c'est une tâche de 4 jours.

Pour ceux qui attendent le résultat, peu importe les heures que t'as mises — ce qui compte c'est quand c'est livré.
C'est pour ça que mon manager et moi, on n'avait pas la même réalité.

Mon outil Time Tracker m'a permis de visualiser cela car je capture en un seul clic play/stop :

- le temps passé sur une tâche
- le temps d'interruption
- le nombre de jours
- le temps calendaire

Puis, il affiche :

Le StatsDashboard qui me montre ma précision par catégorie.
Mon coef dev : ×[CHIFFRE RÉEL VENDREDI].
Admin : j'estime bien.
Réunions : à l'heure près — normal, c'est la seule que je ne contrôle pas.

Le WeekView qui montre le temps calendaire qu'a pris la tâche.
Ce n'est plus le temps brut par catégorie — c'est la tâche vue en jours.

Résultat :

Avant, j'étais optimiste, maintenant, je suis réaliste.

Et vous — c'est quoi votre coef ?

---

## Commentaire épinglé

L'outil est sur ekenor.com/tools/time-tracker — gratuit, sans compte.

---

## Notes pour les visuels

| Slide | Fichier | Ce qu'on montre |
| ----- | ------- | --------------- |
| 1 | `time-tracker-time-span.png` | L'insight conceptuel — "Une tâche de 4h étalée sur 4 jours, c'est une tâche de 4 jours." Visuel généré Nano Banana. À corriger couleur copper si gradient visible. |
| 2 | `time-tracker-stats-page.png` | StatsDashboard — Estimé 6h05 vs Réel 10h58, coef ×1.8 en rouge, tableau par catégorie. La preuve chiffrée. |
| 3 | `time-tracker-calendar-empiled-page.png` | WeekView empilé — semaine lundi→vendredi, barres par catégorie, charge journalière visible. |

**Non retenu** : `time-tracker-calendar-timeline-page.png` — plus technique, moins immédiat. Garder en réserve pour un post futur retour d'expérience.

**Slide 1 — Prompt Nano Banana :**

```
Create a clean infographic for LinkedIn (1080×1080px).
Background: #f5f5f5. Font: Inter or similar sans-serif.
TOP — Bold title: "Ce que tu crois faire" / "vs ce que tu fais vraiment"
CENTER — Two columns side by side:
Left column (muted, gray): label "Le plan" — 3 small icons: 💻 Dev (large block), 📝 Production (medium block), 📋 Admin (small block)
Right column — deep blue background (#2563EB), rounded card, white text:
  Label white muted: "Ce qu'ils voient"
  Large bold number, white: "4 jours"
  Small label below, white: "temps calendaire réel"

A bold arrow → between the two columns, color #2563EB.

BOTTOM — Leave a clean margin of ~80px for a logo badge to be added manually.
No gradients. No decorative elements. High contrast between the two cards.
```

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | lien-site-dans-post (suite) | — |
