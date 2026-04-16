---
title: "25 heures d'approbation. Maintenant 4 heures."
slug: "2026-04-13-proofslab-approbation-visuels"
type: AUTOMATISATION
projet: "ProofsLab"
status: Publié
planned_date: "2026-04-13"
slot: Lundi
concept: ""
concept_level: ""
tags: [proofreading, visuel, retail, automatisation, cosmétiques, impression]
linkedin_url: ""
lesson: "Le vrai pain point n'était pas la comparaison — c'était tout ce qu'il faut faire autour. La V1 décrivait le problème côté comparaison, la version finale l'attaque côté manipulation de fichiers. C'est ce détail qui rend le post identifiable pour les gens du secteur."
rules_applied: [accroche-3-lignes, récit-personnel-spécifique, chiffres-contrastés, voix-vecue-pas-pattern, max-2-takeaways, phrase-punch-finale]
rule_added: "chiffres-côte-à-côte"
rule_hypothesis: "Si on met les deux chiffres contrastés (avant/après) dans des phrases consécutives plutôt que séparées, le lecteur saisit le gain sans effort de calcul."
---

# POST W.15 — AVRIL 2026, SEMAINE 2

**Type** : AUTOMATISATION
**Sous-thème** : Proofreading visuel, approbation, retail cosmétique
**Projet** : ProofsLab
**Visuels** : Carousel 3 slides — slide 1 contraste chiffré (25h → 4h), slide 2 workflow solution, slide 3 interface mockup (avec PDFs neutres)

---

## Key takeaways

1. Le vrai coût de l'approbation ce n'est pas la comparaison — c'est toutes les manipulations autour. C'est là que le temps se perd.
2. 25h → 4h sur 500 fichiers. Le gain est concret, chiffré, immédiat.

---

## Post LinkedIn

En tant que spécialiste retail design, chaque saison j'approuvais des centaines de visuels avant impression.
Sur 500, il y en a peut-être 5 avec une erreur. Mais si tu en rates une — c'est une réimpression pour tout le Canada.
Ce qui est long, c'est pas de comparer. C'est tout ce qu'il faut faire autour.

Dans le retail cosmétique, le process c'est ça : le designer envoie le fichier validé, l'imprimeur renvoie sa version haute résolution prête pour production. Et toi tu vérifies que rien n'a changé entre les deux.

C'est le jeu des 7 différences.

Le problème : la plupart du temps il n'y a pas d'erreur. Donc tu passes des heures à manipuler des fichiers parfaits, pour rien.

Le process réel :
→ Ouvrir ma liste d'approbations
→ Identifier les deux bons fichiers dans les deux bons dossiers
→ Les ouvrir côte à côte
→ Comparer
→ Cocher
→ Recommencer 499 fois

3 minutes par fichier. Sur 500, c'est 25 heures — étalées sur un mois, en parallèle de tout le reste.
Maintenant : 30 secondes. Sur 500, c'est 4 heures.

Pour passer de 25h à 4h, j'ai construit ProofsLab.
Je dépose les deux dossiers. L'outil fait le matching automatiquement — chaque fichier porte un code dans son nom, il associe les paires. Il calcule un score de similarité visuelle pixel par pixel (SSIM). Tout ce qui est conforme : validé. Les outliers remontent.

En face de chaque paire : un bouton approuver, un champ commentaire. À la fin j'exporte ma liste et je la renvoie.

C'est en R&D — ça couvre 90% des cas — mais sur les vrais écarts (texte modifié, couleur décalée), ça les sort systématiquement.

Si tu travailles dans le retail, le luxe, ou n'importe quel domaine où tu valides des visuels avant impression — dis-moi si tu vis la même chose.

Les robots peuvent perdre leur temps à jouer au jeu des 7 différences.
Nous on peut continuer à faire la vraie différence — le design.

Le lien est en commentaire — si tu l'as testé, dis-moi ce qui marche ou pas. Je développe en fonction des retours.

---

## Commentaire épinglé

ProofsLab : proofslab.com — gratuit, drag & drop, aucune installation.

---

## Notes pour les visuels

| Slide | Description | Ce qu'on montre |
|-------|-------------|-----------------|
| 1 | Contraste chiffré vertical | Titre : "Temps d'approbation — 500 fichiers" / Bloc haut (manuel) : 3 min/fichier → 25 heures / Bloc bas (ProofsLab) : 30 sec/fichier → 4 heures / Flèche vers le bas entre les deux blocs |
| 2 | Workflow flux vertical | PDF designer + dossier imprimeur → Matching automatique (code fichier) → Score similarité SSIM → Outliers remontés → Validation humaine ciblée |
| 3 | Interface mockup | Liste de paires de fichiers avec score vert (✅ 97%) ou rouge (⚠️ 63%) — à faire avec PDFs neutres (pas L'Oréal) |

**Prompt Nano Banana — Slide 1 :**

```
Create a clean infographic for LinkedIn (1080×1080px).
Background: #f5f5f5. Font: Inter or similar sans-serif.

TOP CENTER — Hero branding:
  Blue square icon with white checkmark (~60px) centered above text
  Title bold large centered: "ProofsLab"
  Subtitle muted centered: "PDF Comparison Laboratory"

BELOW — Section label centered, smaller: "Temps d'approbation"
Caption muted centered: "500 fichiers PDF à valider par saison, avant impression"

CENTER — Two horizontal rows, stacked vertically with spacing:

Row 1 (muted gray background, rounded corners, full width):
  Left: "Sans ProofsLab"
  Center: "3 min / fichier"
  Right bold large dark: "→ 25 heures"

Row 2 (soft blue background, rounded corners, full width, slightly larger, subtle drop shadow):
  Left: "Avec ProofsLab"
  Center: "30 sec / fichier"
  Right bold large blue: "→ 4 heures"

BOTTOM RIGHT — Empty rounded square placeholder (~80px) for ekenor.com badge to be added manually in Canva.
```

**Prompt Nano Banana — Slide 2 :**

```
Create a clean workflow diagram for LinkedIn (1080×1080px).
Background: #f5f5f5. Font: Inter or similar sans-serif.
TOP — Bold title: "Comment l'outil trie" / Subtitle: "Matching automatique + score de similarité"
CENTER — Vertical flow:
📁 PDF designer + dossier imprimeur
↓
🔗 Matching automatique (même code dans le nom)
↓
📊 Score similarité SSIM calculé pour chaque paire
↓
✅ Visuels conformes → validés automatiquement
↓
⚠️ Outliers → remontés pour inspection humaine
Rounded rectangles, thin arrows, soft pastel blue on boxes, subtle drop shadows. Last box slightly larger.
BOTTOM — Leave a clean margin of ~80px for logo badges to be added manually.
```

---

## Historique des versions et leçons de session

### V1 — Version initiale (session précédente)

**Accroche :** "500 visuels à approuver. 490 sont parfaits."
**Angle central :** le paradoxe du volume (490 parfaits mais 500 à regarder)
**Ce qui manquait :**

- Le vrai pain point était absent : la friction n'est pas dans la comparaison, elle est dans tout ce qu'il faut faire *autour* (ouvrir les bons fichiers, les mettre côte à côte, cocher, recommencer)
- Pas de chiffres sur le gain de temps concret
- Liste numérotée 1-5 → format tuto, interdit par les règles éditoriales
- "À terme j'ajoute une couche IA" → décrédibilise (suggère que c'est pas fini)

### V2 — Réécriture courte (tentative intermédiaire)

**Ce qui a été retiré à tort :**

- Le contexte du process (designer → imprimeur → validation) — sans ça le lecteur ne comprend pas d'où viennent les deux dossiers
- "C'est le jeu des 7 différences" — image forte, mémorable, à garder
- La transition problème → solution

**Leçon :** en cherchant à alléger, j'ai retiré des éléments qui portaient la compréhension et l'identification du lecteur.

### V3 — Version finale validée

**Ce qui a changé par rapport à la V1 :**

| Élément | V1 | V3 |
|---------|----|----|
| Accroche | "500 visuels à approuver. 490 sont parfaits." | "Ce qui est long, c'est pas de comparer. C'est tout ce qu'il faut faire autour." |
| Pain point central | La comparaison (jeu des 7 différences) | Les manipulations de fichiers autour de la comparaison |
| Chiffres | Aucun gain de temps chiffré | 3 min → 30 sec / 25h → 4h côte à côte |
| Format solution | Liste numérotée 1-5 (tuto) | Narration fluide avec les étapes intégrées |
| Fin | "Un robot peut faire le jeu des 7 différences. Moi je peux faire la différence." | "Les robots peuvent perdre leur temps à jouer au jeu des 7 différences. Nous on peut continuer à faire la vraie différence — le design." |
| Cible | Implicite | Explicite : retail, luxe, impression physique |
| Slide 1 | Contraste 500/490/10 | Contraste temporel 25h/4h (plus parlant) |

**Règles éditoriales appliquées ou confirmées :**

- **Accroche 3 lignes** : la contrainte "3 lignes visibles avant voir plus" a forcé à choisir le message central. C'est là que le vrai angle est apparu.
- **Récit personnel spécifique** : nommer le process exact (les deux dossiers, les codes fichiers, le bouton approuver) rend le post identifiable pour les gens du secteur
- **Chiffres contrastés côte à côte** : "3 min / 25h → 30 sec / 4h" dans des phrases consécutives — le lecteur saisit le gain sans calcul
- **Pas de tuto** : la liste 1-5 de la V1 a été remplacée par une narration
- **Phrase punch finale inclusive** : "nous" plutôt que "moi" — inclut le lecteur dans la valeur ajoutée

---

## Tracking

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| Impressions | — | — |
| Likes | — | — |
| Commentaires | — | — |
| EngagementRate | — | — |
| Règle testée | chiffres-côte-à-côte | — |
