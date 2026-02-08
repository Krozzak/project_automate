# Workflows n8n

Chaque dossier contient un workflow n8n importable. Les credentials sont remplacées par des placeholders `YOUR_*`.

## Workflows disponibles

| Dossier | Workflow | Description |
|---------|----------|-------------|
| [`ideas-logger/`](ideas-logger/) | Ideas Logger v3 | Capture vocale/texte d'idées → Notion, avec détection nouvelle idée vs update, todos, logs, sélection |
| [`todo-manager/`](todo-manager/) | Todo Manager | Transforme une idée Notion en liste de tâches actionnables avec métadonnées (durée, énergie, contexte, priorité) |
| [`smart-router/`](smart-router/) | Smart Router | Orchestrateur : décompose un message en actions multiples et dispatch vers Ideas Logger et Todo Manager |

## Comment choisir

- **Vous voulez capturer des idées** → [`ideas-logger/`](ideas-logger/) (standalone, complet)
- **Vous voulez décomposer vos idées en tâches** → [`todo-manager/`](todo-manager/) (standalone)
- **Vous voulez tout connecter** → [`smart-router/`](smart-router/) (nécessite les 2 autres)

## Import dans n8n

1. Copier le contenu du fichier `.json`
2. Dans n8n : Workflows > Import from File
3. Configurer vos credentials (voir les `YOUR_*` dans le JSON)
4. Activer le workflow

Chaque dossier a son propre README avec les instructions détaillées.

## Structure

D'autres automatisations arrivent chaque mois. Chaque dossier correspond à une automatisation indépendante avec son README, ses instructions d'import et ses exemples de test.

```
workflows/
├── ideas-logger/          ← Mois 1
│   ├── Ideas_Logger_v3.json
│   └── README.md
├── todo-manager/          ← Mois 2
│   ├── Todo_Manager_Standalone.json
│   └── README.md
├── smart-router/          ← Mois 2
│   ├── Smart_Router_Standalone.json
│   └── README.md
└── [prochaines automatisations...]
```
