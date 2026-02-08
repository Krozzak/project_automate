# Ideas Logger v3

Workflow n8n standalone pour capturer et gérer des idées via Telegram.

## Ce que ça fait

1. Vous envoyez un message vocal ou texte à votre bot Telegram
2. Si vocal : transcription automatique (Whisper)
3. GPT analyse le message et détecte s'il s'agit d'une **nouvelle idée** ou d'un **update** d'une idée existante
4. L'idée est créée ou mise à jour dans Notion avec toutes les métadonnées
5. Les todos sont générés automatiquement
6. Confirmation envoyée sur Telegram

## Import

1. Copier le contenu de `Ideas_Logger_v3.json`
2. Dans n8n : Workflows → Import
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

## Exemples de messages à envoyer

### Nouvelle idée

```
nouvelle idée: un dashboard analytics pour suivre mes habitudes
```

```
j'ai une idée de système de notification intelligent
```

### Update d'une idée existante

```
pour l'idée du dashboard, je veux ajouter un filtre par date
```

```
l'idée du logger est terminée
```

### Message ambigu (le bot demande de préciser)

```
mise à jour de l'analytics
```

Le bot répond avec des options numérotées. Répondre en reply avec `01`, `02`, ou `nouveau`.
