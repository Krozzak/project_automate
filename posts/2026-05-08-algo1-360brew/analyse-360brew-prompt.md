# Analyse ta catégorie 360Brew

> Prompt à utiliser avec Claude (Claude.ai, Claude Code, ou n'importe quel LLM).
> Temps estimé : 5 minutes.

---

## Pourquoi faire ça

360Brew — le système de ranking LinkedIn depuis début 2026 — ne juge pas tes posts un par un.
Il catégorise ton compte sur les 90 derniers jours : profil, vocabulaire, historique complet.

Si ta thématique est claire → il te distribue à la bonne audience.
Si ton historique est mixte → il ne sait pas qui tu es, et il ne te distribue pas.

Depuis son déploiement, le reach organique moyen a chuté de 50% en vues et 25% en engagement.
Ce n'est pas une coïncidence — c'est le filtre qui s'applique.

Ce prompt te donne la réponse en 5 minutes.

---

## Comment fonctionne 360Brew (version technique)

**Architecture réelle :**
LinkedIn utilise deux systèmes qui coexistent :
- **Causal LLM** — système de récupération, décide quels posts sont candidats à la distribution
- **360Brew** — système de ranking, décide l'ordre et l'audience finale

360Brew n'a pas remplacé tout l'algo d'un coup. Les deux tournent en parallèle. Ce qui a changé : le poids du ranking sémantique (cohérence thématique) est devenu dominant.

**Ce que 360Brew lit sur ton compte :**
- Ton profil : titre, headline, expériences, compétences
- Ton vocabulaire récurrent sur les 90 derniers jours
- La cohérence entre ce que dit ton profil et ce que disent tes posts
- Le type d'engagement que tes posts génèrent (saves > partages > commentaires > likes)

**Ce qu'il pénalise :**
- Les pods d'engagement (groupes qui s'engagent en grappe dans les premières minutes) — détectés à 97%, shadow ban 60-90 jours
- Les hashtags excessifs (plus de 5) — signal de spam sémantique
- Le contenu IA générique — patterns structurels identifiés (phrases uniformes, transitions prévisibles, vocabulaire type "holistic", "leverage", "game-changer")
- La dissonance profil/posts — si ton titre dit une chose et tes posts en disent une autre

**Profil personnel vs Page Entreprise :**
Les deux sont traités différemment. Sur un profil personnel, 360Brew pondère plus fortement l'authenticité et la voix individuelle. Sur une Page Entreprise, il pondère plus la cohérence de marque et le volume. Ce guide s'applique aux profils personnels.

---

## Étape 1 — Prépare tes posts

**Option A — Tu as tes posts dans un dossier ou un repo**

Ouvre Claude Code dans le dossier qui contient tes posts.
Le prompt ci-dessous les lira directement.

**Option B — Tu n'as pas de repo**

Crée un fichier `mes-posts.txt` sur ton bureau.
Colle-y chaque post avec ce format :

```
--- POST 1 ---
Titre : [titre ou date]
Texte : [texte complet du post]

--- POST 2 ---
Titre : [titre ou date]
Texte : [texte complet du post]
```

Minimum recommandé : 10 posts. Idéalement tous les posts des 90 derniers jours.

---

## Étape 2 — Colle ce prompt dans Claude

```
Analyse tous les posts LinkedIn disponibles (dans ce dossier, ou dans le fichier mes-posts.txt fourni).

Pour chaque post :
- Identifie le thème principal en 3-5 mots
- Note s'il est centré sur quelque chose de concret (outil, build, résultat, expérience vécue)
  ou sur une réflexion abstraite (concept, opinion générale, actualité sans ancrage personnel)

Ensuite synthétise :

1. Ma catégorie 360Brew en 5 mots max
   → La thématique dominante sur l'ensemble de mes posts

2. Les posts qui rentrent clairement dans cette catégorie
   → Liste avec le thème identifié

3. Les posts qui en sortent
   → Liste avec le thème identifié et une phrase expliquant pourquoi ils dévient

4. Le % de posts hors territoire

5. Un verdict direct :
   → Mon signal thématique est-il clair, mixte, ou flou ?
   → Si quelqu'un voit mes 10 derniers posts d'affilée, est-ce qu'il comprend immédiatement ce que je fais ?

Sois direct. Si le signal est flou, dis-le clairement.
```

---

## Étape 3 — Lis le résultat

**La catégorie en 5 mots** = ce que 360Brew utilise probablement pour te distribuer.
Demande-toi : est-ce que c'est ce que je veux être pour mon audience ?

**Les posts hors territoire** = ceux qui diluent ton signal.
Ce ne sont pas forcément de mauvais posts — mais ils coûtent de la distribution.

**Le % hors territoire** :
- Moins de 15% → signal solide, tu peux continuer
- 15-30% → signal mixte, quelques ajustements suffisent
- Plus de 30% → signal flou, 360Brew a du mal à te catégoriser

---

## Ce que tu fais ensuite

**Tes posts hors territoire ont deux destinations possibles :**

- **Les pivoter** : trouver l'angle concret qui les ramène dans ta thématique (une ligne suffit souvent)
- **Les déplacer** : si le sujet est bon mais pas pour LinkedIn, il a sa place dans une newsletter ou un article long

**Vérifie aussi ton profil LinkedIn.**
360Brew ne lit pas que tes posts — il lit aussi ton titre, tes expériences, tes compétences.
Si ton profil dit "Chef de projet" et tes posts parlent de builder IA, il y a une dissonance sémantique.
Aligne les deux : titre, headline, compétences doivent refléter la même thématique que tes posts.

**Sur les métriques.**
360Brew valorise les saves, le watch-time et les partages plus que les likes.
Un post sauvegardé = signal fort que le contenu a de la valeur.
Si tu optimises quelque chose, optimise pour "est-ce que quelqu'un va sauvegarder ça ?"

L'objectif n'est pas de supprimer ce que tu as fait.
C'est de savoir ce que l'algo a retenu de toi jusqu'ici — et de décider si c'est ce que tu veux.

---

*Prompt créé par Thomas Silliard — ekenor.com*
*Si tu veux voir comment j'ai construit le workflow complet de publication : ekenor.com/workflow*
