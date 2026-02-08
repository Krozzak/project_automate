# Projet Automate

Un écosystème d'automatisations personnelles construit en public. Chaque mois, une nouvelle automatisation, un post LinkedIn, et un retour d'expérience honnête.

## Pourquoi ce projet

Je perds du temps sur des tâches que je pourrais automatiser. Plutôt que de construire en silence, je documente tout : les workflows, les décisions, les échecs.

Pas de tuto. Pas de gourou. Juste un builder qui montre ce qu'il construit et ce que ça change.

## Architecture

```
Telegram (voix ou texte)
       ↓
  Transcription (Whisper, si vocal)
       ↓
  Analyse GPT (classification, extraction)
       ↓
  Notion (stockage structuré)
       ↓
  Confirmation Telegram
```

## Workflows disponibles

| Workflow | Description | Standalone |
|----------|-------------|:----------:|
| [Ideas Logger](workflows/ideas-logger/) | Capture vocale/texte d'idées → Notion, détection update vs nouvelle idée, todos, logs | oui |
| [Todo Manager](workflows/todo-manager/) | Transforme une idée en tâches actionnables avec métadonnées (durée, énergie, contexte) | oui |
| [Smart Router](workflows/smart-router/) | Orchestrateur : décompose un message en actions et dispatch vers les autres workflows | requiert les 2 autres |

Chaque workflow est **importable directement dans n8n**. Il suffit de configurer vos propres credentials.

D'autres automatisations arrivent chaque mois — chaque dossier dans [`workflows/`](workflows/) correspond à une automatisation avec son README et ses exemples.

## Posts LinkedIn

Les posts sont dans [`posts_linkedin/`](posts_linkedin/). Organisés par mois, chaque mois correspond à un projet d'automatisation.

| Mois | Projet | Posts |
|------|--------|-------|
| 1 | Logger d'idées vocal | 4 posts (automatisation, réflexion, retour d'expérience, méta) |
| 2 | Todo Manager + Router | 4 posts (en cours) |

## Comment utiliser un workflow

1. **Importer** : Dans n8n, aller dans Workflows > Import > coller le contenu du fichier `.json`
2. **Configurer les credentials** : Remplacer les placeholders `YOUR_*` par vos propres IDs
   - `YOUR_TELEGRAM_CREDENTIAL_ID` → votre credential Telegram Bot dans n8n
   - `YOUR_OPENAI_CREDENTIAL_ID` → votre credential OpenAI dans n8n
   - `YOUR_NOTION_CREDENTIAL_ID` → votre credential Notion dans n8n
   - `YOUR_IDEAS_DATABASE_ID` → l'ID de votre base Notion "Ideas"
   - `YOUR_TODOS_DATABASE_ID` → l'ID de votre base Notion "Todos"
   - `YOUR_LOGS_DATABASE_ID` → l'ID de votre base Notion "Logs"
   - `YOUR_TELEGRAM_USER_ID` → votre Telegram user ID
3. **Configurer Notion** : Voir [docs/NOTION_SETUP.md](docs/NOTION_SETUP.md) pour la structure des bases
4. **Activer** le workflow et envoyer un message à votre bot Telegram

## Documentation

- [Architecture technique](docs/ARCHITECTURE.md) — schémas, data flow, tech stack
- [Configuration Notion](docs/NOTION_SETUP.md) — structure des bases de données

## Licence

[CC BY-NC 4.0](LICENSE) — Vous pouvez copier, adapter et partager. Pas d'usage commercial.
