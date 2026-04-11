---
title: "Mon manager me dit que je suis trop optimiste"
slug: "2026-04-06-time-tracker-estimation"
type: AUTOMATISATION
projet: "Time Tracker"
status: Publié
planned_date: "2026-04-06"
slot: Lundi
concept: "Planning Fallacy"
concept_level: Simple
tags: [time-tracker, estimation, planning-fallacy, productivité]
linkedin_url: ""
lesson: ""
rules_applied: [structure-3-actes, récit-personnel-spécifique, accroche-3-lignes, concept-seulement-si-il-colle, phrase-punch-finale, lien-site-dans-post]
rule_added: "lien-site-dans-post"
rule_hypothesis: "Si le lien vers l'outil est dans le corps du post, alors plus de personnes cliquent (conversion > reach)"
---

# POST TT.1 — AVRIL 2026, SEMAINE 1

**Type** : AUTOMATISATION
**Sous-thème** : Estimation du temps, biais cognitif, outil correcteur
**Projet** : Time Tracker adaptatif (#47)
**Visuels** : Carousel 3 slides — slide 1 visuelle/concept, slide 2 workflow outil, slide 3 screen StatsDashboard

---

## Key takeaways

1. On estime en temps brut idéal, pas en temps réel — c'est structurel (Planning Fallacy, Kahneman 1979)
2. L'outil corrige l'estimation naturelle avec un coef historique par catégorie — l'objectif est de converger vers ×1

---

## Post LinkedIn

Mon manager m'a dit que j'estimais toujours trop court.
Il avait raison.
Quand j'estime 2h, en réalité ça m'en prend 3 ou 4.

Pendant longtemps j'ai cru que c'était un problème de rigueur.
Que si j'essayais vraiment, je pourrais estimer correctement.

Sauf que non — ma tendance naturelle reprend toujours le dessus.

Le vrai problème : j'estime la tâche en temps brut, dans l'idéal.
2h de dev, c'est 2h si je suis dans un tunnel, sans interruption, sans blocage, sans rien d'autre.
Mais dans un contexte de travail réel, ces 2h s'étalent sur 3h, 4h, parfois plusieurs jours.

Daniel Kahneman a documenté ça en 1979.
Il appelle ça la Planning Fallacy : on sous-estime systématiquement les durées parce qu'on raisonne sur comment les choses devraient se passer, pas comment elles se passent en vrai.

Alors j'ai construit un outil qui utilise mon historique réel.

Concrètement :

1. Je log une tâche avec mon estimation naturelle
2. Je chronomètre le temps réel
3. L'outil calcule un coefficient par catégorie de travail — dev, recherche, rédaction, admin

Quand j'estime la tâche suivante, je donne mon chiffre instinctif.
L'outil applique le coefficient et sort l'estimation corrigée.

Le coefficient, c'est le rapport entre ce que j'estime et ce que je mets réellement.
Si mon coef dev est à ×2 : j'estime systématiquement deux fois trop court.
Si je converge vers ×1 : j'estime juste.

C'est ça l'objectif — pas de corriger mes estimations à la main, mais de les voir évoluer naturellement au fil des tâches loggées.

L'outil est sur ekenor.com/tools/time-tracker — gratuit, sans compte.

---

## Commentaire épinglé

_(pas de lien supplémentaire — le lien est dans le post)_

---

## Notes pour les visuels

| Slide | Description | Ce qu'on montre |
|-------|-------------|-----------------|
| 1 | Image conceptuelle — contraste 3 colonnes | Titre : "Pourquoi on surestime toujours" / 3 blocs : Estimation → Réalité → Écart (Planning Fallacy chiffrée — ex: tâches sous-estimées en moyenne de 40%) |
| 2 | Workflow de l'outil | Flux vertical : Tu estimes une durée → Tu chronométres → L'outil calcule ton coef par catégorie → Il corrige ta prochaine estimation |
| 3 | Screenshot direct de l'outil | Vue principale avec une tâche en cours + estimation corrigée visible |

**Prompts Nano Banana — Slide 1 :**

```
Create a clean infographic for LinkedIn (1080×1080px).
Background: #f5f5f5. Font: Inter or similar sans-serif.
TOP — Bold title, large: "Pourquoi on surestime toujours"
Subtitle below, smaller and muted: "Planning Fallacy — Kahneman & Tversky, 1979"
CENTER — Three blocks side by side showing a progression:
Block 1 (muted): ⏱ Estimation "2h" (large bold gray)
Block 2 (medium): ⚡ Réalité "3h45" (medium tone)
Block 3 (highlighted, soft blue accent background): 📊 Écart moyen "+40%" (dark — visual anchor)
Thin progression arrow connecting blocks left to right. Rounded corners. Subtle drop shadow on block 3 only.
BOTTOM — Leave a clean margin of ~80px for a logo badge to be added manually.
```

**Prompts Nano Banana — Slide 2 :**

```
Create a clean workflow diagram for LinkedIn (1080×1080px).
Background: #f5f5f5. Font: Inter or similar sans-serif.
TOP — Bold title: "Comment l'outil apprend" / Subtitle: "Auto-correction basée sur l'historique réel"
CENTER — Vertical flow: ✍️ Tu estimes une durée ↓ ⏱ Tu chronométres ↓ 📊 L'outil calcule ton coef par catégorie ↓ ✅ Il corrige ta prochaine estimation
Rounded rectangles, thin arrows, soft pastel blue on boxes, subtle drop shadows. Last box slightly larger.
BOTTOM — Leave a clean margin of ~80px for a logo badge to be added manually.
```

---

## Historique des versions

| Version | Ce qui a changé | Pourquoi |
|---------|-----------------|----------|
| V1 | Structure pattern standard : problème → concept Kahneman → solution → phrase punch | Dérivée uniquement des features du projet et de la structure narrative type. Résultat : générique, "post IA" reconnaissable — mêmes tournures que tous les posts LinkedIn sur la productivité. |
| V2 | Ajout du chiffre concret (2h → 3 ou 4), explication mécanique mentale (temps brut idéal vs contexte réel) | Thomas a fourni son vécu exact. Ces infos ne sont pas dans les docs du projet. Le post est passé de générique à personnel. |
| V3 | Ajout mini-liste 1-2-3 pour décrire l'outil, explication du coef ×1 et de la convergence | Thomas a signalé que la description de l'outil n'était pas claire — un lecteur ne comprenait pas ce que le coef signifiait ni pourquoi converger vers ×1 est l'objectif. |

**Leçon principale** : Pour les posts AUTOMATISATION sur un projet personnel, les docs donnent les features mais pas le vécu. Ce qui rend le post fort : le chiffre concret du problème, la mécanique mentale expliquée par l'auteur, la logique de l'outil avec ses mots. Ces 3 éléments doivent être demandés ou pré-écrits depuis le user profile si les informations y sont.

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | lien-site-dans-post | — |
