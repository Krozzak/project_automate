# Score ICE — Original vs Adapté

## ICE original (Sean Ellis)

- **Impact** (1-10) : Quel effet potentiel sur le business/la croissance ?
- **Confidence** (1-10) : À quel point tu es sûr que ça va marcher ? Basé sur des données, du feedback, de l'expérience passée.
- **Ease** (1-10) : À quel point c'est facile/rapide à implémenter ? Score haut = facile.

Formule : Impact × Confidence × Ease

Contexte : Créé pour des équipes growth qui lancent des expériences et qui ont de la data utilisateur.

## Mon adaptation pour le Logger d'idées

- **Impact** (1-5) : Identique.
- **Clarté** (1-5) : Remplace Confidence.
- **6 – Difficulté** (1-5) : Remplace Ease (inversé).

Formule : Impact × Clarté × (6 – Difficulté)

Échelle sur 5 au lieu de 10.

## Pourquoi Clarté au lieu de Confidence

**Confidence** dans le ICE original = "est-ce que j'ai des preuves que ça va marcher ?" — basé sur des données utilisateurs, des tests A/B, du feedback. Pensé pour des équipes growth avec de la data.

Dans un contexte solo (capture vocale, idées personnelles), il n'y a pas de data utilisateur. La question n'est pas "est-ce que ça va marcher ?" mais **"est-ce que je sais vraiment ce que je veux faire ?"**

- Clarté haute = l'idée est bien définie, on peut s'y mettre demain
- Clarté basse = c'est encore flou, il faut d'abord réfléchir à ce que ça veut dire concrètement

Confidence élimine les paris risqués. **Clarté élimine les idées pas mûres.**

## Pourquoi Difficulté au lieu de Ease

C'est le même concept, juste formulé à l'envers.

- **Ease** demande "à quel point c'est facile ?" → score haut = facile
- **Difficulté** demande "à quel point c'est dur ?" → score haut = dur

C'est plus naturel d'évaluer la difficulté. Quand on décrit une idée à l'oral, on dit "ça c'est dur" ou "ça c'est simple", pas "le ease de ce projet est de 7/10".

Le `6 – Difficulté` dans la formule fait l'inversion : difficulté 1 (facile) → 5, difficulté 5 (très dur) → 1. Même résultat que Ease.

## Pourquoi une échelle sur 5

Sur une échelle de 10, la différence entre un 6 et un 7 est floue et subjective. Sur 5, chaque point compte. Pour une IA qui évalue à partir d'une description vocale, 5 niveaux c'est largement suffisant pour discriminer.

Le `6` dans `(6 – Difficulté)` = 5+1, pour que le score ne tombe jamais à zéro (difficulté 5 → donne 1, pas 0, ce qui annulerait tout le score).

## Score max vs min

- **Meilleur score possible** : 5 × 5 × 5 = 125 (impact max, clarté max, difficulté min)
- **Pire score possible** : 1 × 1 × 1 = 1 (impact faible, idée floue, très difficile)

## Sources

- Sean Ellis — *Hacking Growth* (2017)
- [GrowthHackers — ICE Score](https://growthhackers.com/)
