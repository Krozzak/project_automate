# Smart Router

Workflow n8n qui analyse vos messages Telegram et les décompose en actions multiples.

## Ce que ça fait

1. Vous envoyez un message vocal ou texte contenant une ou plusieurs intentions
2. GPT décompose le message en actions distinctes : nouvelle idée, update, todo
3. Chaque action est dispatchée vers le workflow approprié (Ideas Logger ou Todo Manager)
4. Les actions sont ordonnées intelligemment (update avant todo pour la même idée)
5. Un log de chaque décision est enregistré dans Notion

## Architecture

Le Smart Router est un **orchestrateur**. Il nécessite les 2 autres workflows pour fonctionner :

```
Smart Router (ce workflow)
    ├── Ideas Logger (pour new_idea et update_idea)
    └── Todo Manager (pour les todos)
```

Après import, vous devez configurer les IDs des sous-workflows dans les noeuds `Execute Workflow`.

## Import

1. Importer d'abord [Ideas Logger](../ideas-logger/) et [Todo Manager](../todo-manager/)
2. Noter leurs workflow IDs dans n8n
3. Importer `Smart_Router_Standalone.json`
4. Dans les noeuds "Execute Ideas Logger (New)", "Execute Ideas Logger (Update)" et "Execute Todo Manager" : remplacer le workflow ID par les vrais IDs
5. Remplacer les placeholders `YOUR_*` par vos credentials

## Credentials nécessaires

| Placeholder | Service | Comment l'obtenir |
|-------------|---------|-------------------|
| `YOUR_TELEGRAM_CREDENTIAL_ID` | Telegram Bot | Créer un bot via @BotFather, ajouter dans n8n |
| `YOUR_OPENAI_CREDENTIAL_ID` | OpenAI API | Clé API depuis platform.openai.com |
| `YOUR_NOTION_CREDENTIAL_ID` | Notion | Integration depuis notion.so/my-integrations |
| `YOUR_LOGS_DATABASE_ID` | Notion DB | ID de votre base "Logs" |
| `YOUR_TELEGRAM_USER_ID` | Telegram | Votre user ID (via @userinfobot) |

## Exemples de messages

### Message simple (1 action)

```
nouvelle idée: un dashboard analytics pour suivre mes habitudes
```

### Message multi-actions (2+ actions)

```
l'idée du blocker est en cours, et pour le logger il faut ajouter un système de cache
```
→ Décomposé en : 1 update (blocker → en cours) + 1 update (logger → cache)

```
pour l'idée du dashboard, je veux ajouter les exports CSV et il faut créer un endpoint d'export
```
→ Décomposé en : 1 update (dashboard → exports CSV) + 1 todo (endpoint d'export)

### Réponse à une sélection

Quand le bot demande de préciser quelle idée, répondez en reply avec `01`, `02`, ou `nouveau`.
