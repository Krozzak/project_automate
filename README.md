# Projet Automate

Un écosystème d'automatisations personnelles construit en public. Chaque mois, une nouvelle automatisation, un post LinkedIn, et un retour d'expérience honnête.

## Pourquoi ce projet

Je perds du temps sur des tâches que je pourrais automatiser. Plutôt que de construire en silence, je documente tout : les workflows, les décisions, les échecs.

Pas de tuto. Pas de gourou. Juste un builder qui montre ce qu'il construit et ce que ça change.

## Structure

Chaque mois = un projet d'automatisation. Tout est regroupé par mois : les posts LinkedIn, le workflow n8n, et la documentation technique.

```
Mois_1_IdeasLogger/
├── posts/          ← 4 posts LinkedIn (texte + images)
├── workflow/       ← Workflow n8n importable
└── docs/           ← Architecture, setup Notion

Mois_2_TodoManager/
├── posts/
├── workflow/
└── docs/
```

## Automatisations disponibles

| Mois | Projet | Description |
|------|--------|-------------|
| 1 | [Ideas Logger](Mois_1_IdeasLogger/) | Capture vocale/texte d'idées → Notion, détection update vs nouvelle idée |
| 2 | [Todo Manager](Mois_2_TodoManager/) | Transforme une idée en tâches actionnables avec métadonnées |

Chaque workflow est **importable directement dans n8n**. Il suffit de configurer vos propres credentials.

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
3. **Configurer Notion** : Voir le dossier `docs/` du mois correspondant pour la structure des bases
4. **Activer** le workflow et envoyer un message à votre bot Telegram

## Ligne éditoriale

Voir [EDITORIAL.md](EDITORIAL.md) pour la charte graphique, les types de posts et le rythme de publication.

## Licence

[CC BY-NC 4.0](LICENSE) — Vous pouvez copier, adapter et partager. Pas d'usage commercial.
