# Convention de commits — Projet Automate

Référence rapide avant chaque `git commit`.
Objectif : capturer les données de travail pour le Work Profile Analyzer.

Utilise `/commit` dans Claude Code pour générer le message automatiquement.

---

## Format

```
type(projet): description courte

[mode HHhMM] [temps: ~Xh] [énergie: N/10]
Décision: pourquoi ce choix
```

- `mode` : `exploration` ou `focus`
- `HHhMM` : heure locale du commit (ex: `08h45`, `14h30`)
- `temps` : optionnel en exploration, utile en focus sans Smart Focus
- `énergie` : optionnel, mais précieux pour les corrélations
- `Décision` : obligatoire — 1 ligne suffit

---

## Les deux modes

### `exploration`
Travail libre, multi-projets, réflexion, brainstorm, rédaction de posts.
Chaque commit porte son heure. Le Work Profile Analyzer calcule la plage
min→max et la densité (combien de commits, combien de projets, sur quelle durée).

```
post(smart-focus): rédiger post S1 démo workflow

[exploration 09h15] [énergie: 8/10]
Décision: angle "gain de temps" plutôt que "technique" — plus accessible.
```

### `focus`
Tâche unique, timer actif, Smart Focus ouvert.
Le temps réel est capturé automatiquement par Smart Focus dans Notion.
Note quand même `[temps: ~Xh]` si tu n'as pas utilisé Smart Focus.

```
feat(smart-focus): fixer bug overlay multi-écran

[focus 14h30] [temps: ~45min] [énergie: 6/10]
Décision: message loop Win32 sur thread dédié — bridge Tauri trop lent.
```

---

## Types de commits

| Type     | Quand                                          |
|----------|------------------------------------------------|
| feat     | Nouvelle fonctionnalité ou feature             |
| fix      | Correction de bug ou d'erreur                  |
| refactor | Restructuration sans nouvelle feature          |
| spec     | Ajout ou modification d'une spec / brainstorm  |
| post     | Rédaction ou publication d'un post LinkedIn    |
| docs     | Documentation technique (README, SPEC, notes)  |
| chore    | Setup, config, dépendances, ménage             |

---

## Projets (slugs normalisés)

| Slug             | Projet                      |
|------------------|-----------------------------|
| ideas-logger     | Ideas Logger                |
| todo-manager     | Todo Manager                |
| smart-focus      | Smart Focus (Tauri)         |
| linkedin-auto    | LinkedIn Auto               |
| ai-proof-scanner | AI-Proof Job Scanner        |
| should-i-buy-it  | Should I Buy It             |
| memory-logger    | Memory Logger               |
| work-profiler    | Work Profile Analyzer       |
| finance          | Finance Automation Suite    |
| polymarket       | Polymarket Bot              |
| comfort-zone     | Comfort Zone Coach          |
| habit-tracker    | Habit Tracker               |
| editorial        | Stratégie éditoriale / docs |

---

## Ce que le Work Profile Analyzer fera avec ces données

- **Plage exploration** : min/max des heures du jour → durée de la session, projets touchés
- **Densité** : commits par heure en exploration → rythme de production
- **Mode focus** : durée réelle (Smart Focus Notion) + énergie avant/après
- **Énergie** : corrélation état → volume et qualité livrés
- **Décisions** : patterns d'architecture et de contenu par domaine tech
