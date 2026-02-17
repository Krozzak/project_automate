# Ligne éditoriale LinkedIn — Projet Automate

## Philosophie

Partager le parcours de construction d'un écosystème d'automatisations personnelles. Ton authentique, retours d'expérience réels, pas de "guru". On montre ce qui marche ET ce qui ne marche pas.

## Rythme de publication

- **1 post par semaine**, le lundi à 08:30
- **4 posts par mois** = 1 mois = 1 projet
- Alternance des types de posts (voir ci-dessous)

## Types de posts (rotation)

| Type | Description | Visuel |
|------|-------------|--------|
| AUTOMATISATION | Présentation d'un outil/workflow construit | Carousel screenshots (3+ images) |
| MÉTA / BUILD IN PUBLIC | Réflexion sur le process de construction | Texte seul ou 1 image |
| RETOUR D'EXPÉRIENCE | Ce qui a marché / échoué + leçon tirée | Carousel avant/après ou iconographie |
| RÉFLEXION | Concept ou principe appliqué au projet | Texte seul |

## Règles pour les images

### Structure carousel
- **Toujours suivre un arc narratif** : chaque carousel raconte une histoire en images
- Exemples d'arcs : input → traitement → output | principe → problème → solution | avant → après
- La première image est l'**accroche** : elle doit donner envie de swiper, pas faire fuir
- Ne pas mettre une image chaotique/complexe en slide 1

### Bonnes pratiques
- Screenshots dark mode (cohérent avec n8n)
- Annotations si nécessaire (cercles, numéros) pour guider l'oeil
- Iconographies générées (DALL-E) pour illustrer des concepts/principes
- Pas besoin que chaque détail soit lisible — l'impression générale compte

### Génération d'images — Charte graphique et prompt type

Chaque iconographie générée doit respecter la même charte pour créer une identité visuelle reconnaissable à travers les posts.

**Charte graphique :**
- **Fond selon le contexte :**
  - **Dark mode** (`#1a1a2e` ou `#0d1117`) : quand le carousel contient des screenshots de workflows n8n (cohérence visuelle)
  - **Light mode** (`#f5f5f5` ou blanc) : quand l'iconographie est seule (pas de screenshots), pour un rendu plus aéré
- Couleurs d'accent : cyan `#00b4d8`, vert `#2ecc71`, orange `#e67e22`, blanc/noir selon le fond
- Typographie : sans-serif élégante (Inter, Montserrat)
- Style : flat design, infographique, minimaliste
- Interdit : 3D, photoréalisme, dégradés, stock photos

**Prompt type (base à adapter) :**

```
Crée une image infographique épurée et moderne avec un fond sombre (type #1a1a2e).

FORMAT : Paysage (ratio 1200x628px, optimal LinkedIn)

CONTENU :
- [TITRE DU CONCEPT en haut, texte blanc]
- [VISUEL CENTRAL : schéma/progression/formule selon le concept]
- [SOUS-TEXTE en bas si nécessaire]

STYLE :
- Esthétique dark mode
- Couleurs d'accent : cyan (#00b4d8), vert (#2ecc71), blanc
- Pas de dégradés, pas d'effets 3D, design plat
- Professionnel et tech, adapté à LinkedIn
- AUCUN élément photoréaliste
```

## Concepts présentés (historique)

| Post | Concept | Auteur | Niveau |
|------|---------|--------|--------|
| 1.1 | Aucun (démonstration pure) | — | Simple |
| 1.2 | Score ICE | Sean Ellis | Simple |
| 1.3 | Loi de Gall | John Gall, 1975 | Simple |
| 1.4 | Ego Depletion | Roy Baumeister, 1998 | Intermédiaire |

## Tracking de performance

Chaque post inclut une section "Tracking publication" avec :
- Date et heure de publication
- Métriques à J+7 : impressions, likes, commentaires, partages, clics
- Notes / observations qualitatives

## Calendrier des mois

| Mois | Projet | Thème |
|------|--------|-------|
| 1 | Ideas Logger | Capture d'idées vocale + IA |
| 2 | Todo Manager | Transformer les idées en actions |
| 3 | Smart Focus | Interface de focus + overlay |
| 4 | Publish or Shame | Publication LinkedIn automatisée + récupération stats |

## Structure des fichiers

```
Projet_Automate/
├── EDITORIAL.md                  ← ce fichier (charte publique)
├── README.md
├── Mois_1_IdeasLogger/
│   ├── posts/
│   │   ├── post1/
│   │   │   ├── Post1-xxx.md     ← texte + images + tracking
│   │   │   └── *.png            ← images du post
│   │   ├── post2/
│   │   ├── post3/
│   │   └── post4/
│   ├── workflow/
│   │   ├── Ideas_Logger_v3.json ← workflow n8n importable
│   │   └── README.md
│   └── docs/
│       ├── ARCHITECTURE.md
│       └── NOTION_SETUP.md
├── Mois_2_TodoManager/
│   └── (même structure)
├── Mois_3_SmartFocus/
└── Mois_4_PublishOrShame/
```
