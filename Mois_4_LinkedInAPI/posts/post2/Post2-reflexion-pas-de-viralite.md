# Post 4.2 — Pourquoi je ne cherche pas la viralité

## Metadata

- **Type** : RÉFLEXION
- **Sous-thème** : Discipline, Simplicité
- **Projet** : Publication LinkedIn automatisée
- **Concept** : Goodhart's Law (Charles Goodhart, 1975)
- **Niveau** : Simple
- **Mois** : 4
- **Semaine** : S2

## Concept

**Loi de Goodhart** — "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure."

- **Origine** : Charles Goodhart, économiste à la Banque d'Angleterre, 1975. Formulée dans le contexte de la politique monétaire.
- **Vulgarisation** : Marilyn Strathern (1997) a reformulé : "When a measure becomes a target, it ceases to be a good measure."
- **Exemples classiques** : Les KPI d'entreprise qui dérivent (nombre de lignes de code comme mesure de productivité → code inutilement verbeux), les indicateurs scolaires (enseigner le test au lieu du sujet).
- **Mon usage** : Quand je construis un système de stats LinkedIn, le piège serait de transformer les métriques en objectifs. Les impressions servent à comprendre, pas à optimiser.

## Key Takeaways

1. Mesurer la performance de ses posts est utile — mais transformer la mesure en objectif change ce qu'on écrit
2. La loi de Goodhart explique pourquoi les créateurs qui optimisent pour l'algo finissent par tous dire la même chose
3. Les stats servent à éliminer ce qui ne fonctionne pas, pas à reproduire ce qui buzze

## Texte du post

La semaine dernière, j'ai automatisé la récupération de mes stats LinkedIn.

Impressions, likes, commentaires, partages — tout est stocké, classé, analysé.

Et la première chose que je me suis dit, c'est : faut que je fasse attention à ne pas me faire piéger par mes propres chiffres.

Parce qu'il y a un truc contre-intuitif avec les métriques.

Plus tu les regardes, plus tu optimises pour elles.
Et plus tu optimises pour elles, moins elles mesurent ce qu'elles étaient censées mesurer.

Ça s'appelle la loi de Goodhart. Un économiste britannique l'a formulée en 1975 : "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure."

Appliqué à LinkedIn, ça donne : si tu écris pour maximiser les impressions, tu finis par écrire ce que l'algo veut entendre. Des accroches choc. Du storytelling formaté. Des posts qui ressemblent à tous les autres.

Le contenu devient un produit de la mesure au lieu de l'inverse.

Moi, ce que je veux, c'est simple :
- Savoir quels sujets résonnent avec les gens
- Identifier les formats qui ne marchent pas du tout
- Avoir un historique pour ne pas me répéter

Pas optimiser pour l'algo. Comprendre ce qui connecte.

Du coup, dans mon système, les stats ne sont pas un dashboard que je consulte tous les jours. C'est un outil que j'active quand j'en ai besoin. Pas de notification quotidienne, pas de comparaison post par post en temps réel.

Un rapport, quand je le demande. Avec un classement et des patterns.

C'est la différence entre un outil qui t'informe et un outil qui te contrôle.

T'as déjà changé ta façon de faire un truc à cause d'une métrique ?

## Images

| # | Fichier | Description | Rôle |
|---|---------|-------------|------|
| 1 | slide1-goodhart.png | Iconographie de la loi de Goodhart | Illustration du concept |

### Prompt DALL-E (slide 1)

```
Crée une image infographique épurée et moderne avec un fond clair (#f5f5f5).

FORMAT : Carré (1080x1080px, optimal LinkedIn)

CONTENU :
- En haut : "LOI DE GOODHART" en texte noir, sous-titre "Charles Goodhart, 1975"
- Au centre : deux scénarios visuels séparés par une ligne verticale
  - À gauche : un thermomètre qui mesure la température (label "Mesurer") — le thermomètre reflète la réalité
  - À droite : une main qui force le thermomètre vers le haut (label "Optimiser") — le thermomètre ne reflète plus rien
- En bas : citation "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure."

STYLE :
- Light mode, fond clair
- Couleurs d'accent : cyan (#00b4d8), orange (#e67e22) pour le côté "optimiser"
- Pas de dégradés, design plat, minimaliste
- Typographie sans-serif
```

## Tracking publication

- **Date prévue** : Lundi [à définir]
- **Heure** : 08:30
- **Statut** : Brouillon

### Métriques J+7

| Métrique | Valeur |
|----------|--------|
| Impressions | — |
| Likes | — |
| Commentaires | — |
| Partages | — |
| Clics | — |

### Notes
- Post ancré dans le mois : le concept vient directement de la construction du stats collector
- Pas de visuel de workflow — iconographie seule → fond light mode
- Créer la fiche concept `.private/notes/Goodharts_Law.md`
