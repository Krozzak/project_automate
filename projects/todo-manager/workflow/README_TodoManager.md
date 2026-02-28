# Todo Manager

Workflow n8n standalone qui transforme vos idées Notion en listes de tâches actionnables.

## Ce que ça fait

1. Vous envoyez un message vocal ou texte mentionnant une idée existante
2. Le workflow cherche l'idée dans votre base Notion
3. GPT analyse l'idée et génère/enrichit les todos avec des métadonnées complètes
4. Chaque todo reçoit : durée estimée, contexte, niveau d'énergie, priorité, critère de validation
5. Les todos sont créés/mis à jour dans Notion
6. Confirmation envoyée sur Telegram

## Import

1. Copier le contenu de `Todo_Manager_Standalone.json`
2. Dans n8n : Workflows > Import
3. Remplacer les placeholders `YOUR_*` par vos credentials

## Credentials nécessaires

| Placeholder | Service | Comment l'obtenir |
|-------------|---------|-------------------|
| `YOUR_TELEGRAM_CREDENTIAL_ID` | Telegram Bot | Créer un bot via @BotFather, ajouter dans n8n |
| `YOUR_OPENAI_CREDENTIAL_ID` | OpenAI API | Clé API depuis platform.openai.com |
| `YOUR_NOTION_CREDENTIAL_ID` | Notion | Integration depuis notion.so/my-integrations |
| `YOUR_IDEAS_DATABASE_ID` | Notion DB | ID de votre base "Ideas" |
| `YOUR_TODOS_DATABASE_ID` | Notion DB | ID de votre base "Todos" |
| `YOUR_LOGS_DATABASE_ID` | Notion DB | ID de votre base "Logs" |
| `YOUR_TELEGRAM_USER_ID` | Telegram | Votre user ID (via @userinfobot) |

## Structure Notion requise

Voir [NOTION_SETUP.md](../../docs/NOTION_SETUP.md) pour la configuration complète des bases.

### Propriétés Todos requises

| Propriété | Type | Valeurs |
|-----------|------|---------|
| Title | title | Nom de la tâche |
| Ideas Logger | relation | Lien vers l'idée parente |
| Status | status | À faire, En cours, Terminé |
| Priority | select | P1, P2, P3 |
| EstimatedMinutes | number | 15, 30, 45, 60, 90, 120, 180, 240 |
| Context | select | Bureau, Maison, Mobile, Partout |
| EnergyLevel | select | Haute, Moyenne, Basse |
| Order | number | Ordre d'exécution |
| ValidationCriteria | rich_text | Critère de validation simple |

## Exemples de messages

### Générer les todos d'une idée

```
les todos pour l'idée du dashboard analytics
```

```
décompose l'idée du logger en tâches
```

### Ajouter des tâches à une idée

```
pour le dashboard, il faut aussi ajouter un export CSV et un filtre par date
```

### Message vocal

Envoyez une note vocale décrivant les tâches à créer pour une idée existante.
