---
title: "J'ai reconstruit ma mémoire"
slug: "2026-05-12-km-graphe-custom"
type: AUTOMATISATION
projet: "KM #8"
status: Prêt
planned_date: "2026-05-12"
slot: Mardi
concept: ""
concept_level: Simple
tags: [knowledge-management, atlas, obsidian, github, claude-code]
linkedin_url: ""
lesson: "Trois leçons dans cette session : (1) Quand la conclusion devient binaire ('pas X mais Y'), elle sonne LinkedIn-générique même si la structure est bonne — phrases qui s'enchaînent au lieu de phrases qui s'opposent. (2) Pour un post sur un système custom, l'audience builder attend l'argument bout-en-bout (input + traitement + output) — la description statique de l'objet (ce que c'est) compte moins que le pourquoi du choix d'architecture (ce qu'on contrôle). (3) Chaque paragraphe doit être lisible par quelqu'un qui n'a pas lu le reste du post — relire chaque section en se demandant 'est-ce que ça se comprend si on commence ici ?'. Si un terme est jargon (cluster, exemple), le remplacer. Si un concept est lâché sans contexte (élasticité des prix), embarquer une définition courte."
rules_applied: [accroche-3-lignes, récit-personnel-spécifique, voix-vecue-pas-pattern, max-2-takeaways, solution-en-narration-pas-en-liste, angle-personnel-narratif, coherence-thematique-builder, phrase-punch-finale]
rule_added: "emojis-marqueurs-de-section"
rule_hypothesis: "Si on place 1 emoji par section principale (5 emojis fonctionnels, pas décoratifs — 🕸️ 🗺️ 🛠️ 📖 ✍️), alors le post gagne en rythme visuel et lisibilité sans tomber dans le pattern LinkedIn-générique des emojis-décoration. Hypothèse opposée à la règle algo 'max 2 emojis' — test à mesurer."
---

## POST 8.1 — MAI 2026, SEMAINE 2

**Type** : AUTOMATISATION
**Sous-thème** : Knowledge Management, atlas de concepts, Obsidian, Claude Code
**Projet** : KM #8
**Visuels** : Vidéo de présentation — le graphe en rotation puis clic sur quelques notes pour montrer la construction (panneau latéral, voisins, clusters)

---

## Key takeaways

1. Un atlas de tout ce qu'on a lu, écouté, écrit — système local, contrôle bout-en-bout (input + visualisation + output), pas d'app tierce.
2. Deux usages réels : visualiser ce qui entoure un livre (brainstorm complet en une vue), ou co-créer un concept avec Claude en suivant les liens entre clusters (exemple : élasticité des prix → élasticité des compétences).

---

## Post LinkedIn

J'ai reconstruit ma mémoire. En créant un atlas de connaissance.
C'est comme Obsidian mais directement sur Github.
Tout ce que j'ai lu, écouté, écrit depuis le début de l'année → relié.

🕸️ Il y a eu toute une tendance cette année à connecter Obsidian à Claude Code, pour que l'assistant navigue les notes au lieu de tout charger en contexte d'un coup.

J'ai construit le mien à la place.

🗺️ J'ai créé un atlas qui visualise toutes mes notes — chaque podcast, chaque article, chaque livre, chaque idée formalisée est devenu une fiche, reliée aux autres.

🛠️ Tout est en local, dans un repo que je contrôle. Pas d'app tierce.
Je décide de la visualisation, je décide des types de fiches : concepts, auteurs, livres, articles.
Et je contrôle aussi l'input et l'output : mes workflows d'ingestion transforment podcasts et articles en fiches au bon format, et Claude Code les utilise directement quand j'écris.

📖 L'usage quotidien :
Je clique sur une fiche de livre : Thinking, Fast and Slow.
Je vois d'un coup les concepts que j'en ai extraits, les articles que j'ai écrits dessus, les autres auteurs cités dans les mêmes contextes.
Tout le brainstorm autour d'un livre, en une vue.

✍️ L'usage plus profond, c'est quand j'écris.
Sur un article sur l'IA et le marché du travail (disponible sur Ekenor), je cherchais comment expliquer pourquoi certains métiers vont disparaître.
Claude a remonté un concept d'un autre thème : l'élasticité des prix — en finance, c'est ce qui fait qu'un produit remplaçable voit son prix s'effondrer.
On a transposé l'idée aux compétences :
"Les compétences obéissent aux mêmes lois que les prix. Ce qui est substituable finit par être substitué."

Mes notes existaient dans ma tête, dans ma mémoire.
L'atlas leur donne enfin une forme qu'on peut regarder.
Et grâce à lui, je peux visualiser ce que je sais.

---

## Commentaire épinglé

L'atlas est navigable ici : ekenor.com/fr/concepts/map

---

## Notes pour les visuels

| Slide     | Description                                                | Ce qu'on montre                                                                                                                                            |
| --------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 (vidéo) | Vidéo de présentation graphe 3D ekenor.com/fr/concepts/map | Rotation du graphe (les 9 clusters apparaissent), puis clic sur 2-3 notes (livre, concept, auteur) pour montrer le panneau latéral et la construction des voisins |

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | angle-personnel-narratif | — |

---

## Notes de session — 2026-05-19 (rewrite pour publication 2026-05-20)

### Décisions de rewrite (validées en session)

- **Accroche inchangée sur les 3 premières lignes** (validée à l'oral) sauf le glissement de "graphe" → "atlas" pour cohérence avec la suite. "Graphe" garde sa place pour décrire l'objet technique ; "atlas" devient le mot porteur du sens (carte / image mentale).
- **Suppression du chiffre "85 fiches"** — le repo bouge, le visuel affiche désormais 138 nœuds / 560 liens / 9 clusters. Pas de chiffre dans le texte, le visuel les montre.
- **"Depuis deux ans" remplacé par "depuis le début de l'année"** — précision Thomas : le projet KM ne tourne que depuis cette année.
- **Fusion bloc atlas + bloc Obsidian** : la tendance Obsidian+Claude Code arrive immédiatement après l'accroche (c'est ce que les gens se demandent), puis pivot "j'ai construit le mien à la place" → description de l'atlas + arguments du choix custom (local, contrôle de la stack, input/output via workflows d'ingestion).
- **Acte usage quotidien** : tour autour d'un livre (Thinking, Fast and Slow). Montre la multi-typologie (livre → concepts → articles → auteurs).
- **Acte usage profond resserré** : 5 → 4 lignes initialement. Puis (relecture finale) repensé pour la lisibilité standalone — le paragraphe doit se comprendre par quelqu'un qui n'a pas lu le reste. Remplacement de "cluster" par "thème" (jargon → mot courant). Ajout de la quête initiale ("je cherchais comment expliquer pourquoi certains métiers vont disparaître") + définition embarquée de l'élasticité des prix ("en finance, c'est ce qui fait qu'un produit remplaçable voit son prix s'effondrer"). Mention discrète de la source de l'article entre parenthèses ("disponible sur Ekenor"). "On a tiré le fil" remplacé par "On a transposé l'idée aux compétences" — verbe précis.
- **Phrase finale** : dictée par Thomas, polie pour le rythme final :
  > "Mes notes existaient dans ma tête, dans ma mémoire.
  > L'atlas leur donne enfin une forme qu'on peut regarder.
  > Et c'est là que je commence à visualiser ce que je sais."
  Pas d'antithèse binaire. Enchaînement de trois phrases qui glissent de la mémoire intérieure vers la forme visible vers la visualisation. Cohérent avec le profil visuel de Thomas.

### Visuel

Vidéo de présentation préparée par Thomas — pas un screenshot statique. Cadrage validé : rotation du graphe (montre les clusters et la densité) puis clic sur quelques notes pour montrer la construction (panneau latéral, voisins, types). L'usage quotidien décrit dans le post devient visible dans la vidéo.

### Ce qu'on a sorti volontairement (pour un futur post)

- **Le "pourquoi pas Obsidian" développé** : reste dans le post sur une seule ligne ("calé sur mes types + repo construit avec Claude Code"). Si on veut développer (architecture, fichiers .md, GitHub Actions, dual licence), ça devient un post META à part — build in public sur le choix d'architecture KMS.
- **Le repo GitHub KMS** : pas mentionné. Réservé pour le post META.
- **Les chiffres précis du graphe (138/560/9)** : visibles dans la vidéo, pas répétés dans le texte.

### Règle EN TEST appliquée

`angle-personnel-narratif` (3/5 mesurés, signal AMBIGU à étendre à 5) — le post part d'une tension/d'une démarche personnelle ("j'ai reconstruit ma mémoire") plutôt que d'une présentation de features. 4e test de la règle.

### Nouvelle règle EN TEST introduite

`emojis-marqueurs-de-section` — 1 emoji par section principale du post (5 emojis fonctionnels : 🕸️ 🗺️ 🛠️ 📖 ✍️), placés en tête de paragraphe comme marqueurs visuels de navigation. Choix par section : 🕸️ pour la tendance (notion de connexion/réseau), 🗺️ pour l'atlas, 🛠️ pour l'architecture/stack, 📖 pour l'usage quotidien autour d'un livre, ✍️ pour l'usage en écriture. Hypothèse : le rythme visuel améliore la lisibilité LinkedIn sans tomber dans le pattern emoji-décoration. **Opposé à la règle algo "max 2 emojis"** — c'est un choix éditorial assumé par Thomas, à mesurer sur 3 posts.
