# Projet Automate

Un écosystème d'automatisations personnelles construit en public. Chaque projet = une automatisation réelle, utilisée au quotidien. Tout est documenté : les workflows, les décisions, les échecs.

Pas de tuto. Pas de gourou. Juste un builder qui montre ce qu'il construit et ce que ça change.

## Structure

```
projects/           ← Les automatisations (workflows, code, docs)
posts/              ← L'archive LinkedIn chronologique (texte + stats)
```

### Projects

Chaque projet contient ce qui est disponible publiquement :

```
projects/ideas-logger/
├── workflow/       ← Workflow n8n importable
├── docs/           ← Architecture, setup Notion
└── concepts/       ← Concepts théoriques liés au projet

projects/todo-manager/
├── workflow/       ← Workflows n8n importables (Smart Router + Todo Manager)
└── docs/

projects/smart-focus/   ← App desktop (code privé, docs à venir)
projects/linkedin-auto/ ← Workflow de publication automatique
projects/ai-proof-job-scanner/ ← Site web d'analyse de résilience IA
projects/no-confort-zone/      ← À venir
projects/should-i-buy-it/      ← À venir
projects/memory-logger/        ← À venir
```

### Posts

Archive chronologique des publications LinkedIn. Format : `YYYY-MM-DD-slug.md`

Chaque fichier contient : texte publié + images utilisées + stats de performance.

```
posts/
├── images/                         ← Images classées par projet
│   └── ideas-logger/
├── 2026-02-03-ideas-logger-demo.md
├── 2026-02-10-score-ice.md
├── 2026-02-17-loi-de-gall.md
├── 2026-02-23-ego-depletion.md
└── ...
```

## Automatisations disponibles

| Projet | Description | Type | Statut |
|--------|-------------|------|--------|
| [Ideas Logger](projects/ideas-logger/) | Capture vocale/texte → Notion, détection update vs nouvelle idée | n8n workflow | Launched ✅ |
| [Todo Manager](projects/todo-manager/) | Transforme une idée en tâches actionnables avec métadonnées | n8n workflow | Launched ✅ |
| [Smart Focus](projects/smart-focus/) | App desktop : une seule tâche visible, overlay focus | Tauri (Windows) | Beta 🔄 |
| [LinkedIn Auto](projects/linkedin-auto/) | Automatise la publication LinkedIn | n8n workflow | Build 🔧 |
| [AI-Proof Job Scanner](projects/ai-proof-job-scanner/) | Analyse la résilience IA d'un métier | Site web | MVP 🧪 |

## Utiliser un workflow n8n

1. **Importer** : Dans n8n → Workflows → Import → coller le contenu du fichier `.json`
2. **Configurer les credentials** : Remplacer les placeholders `YOUR_*` par vos propres IDs
   - `YOUR_TELEGRAM_CREDENTIAL_ID` → credential Telegram Bot dans n8n
   - `YOUR_OPENAI_CREDENTIAL_ID` → credential OpenAI dans n8n
   - `YOUR_NOTION_CREDENTIAL_ID` → credential Notion dans n8n
   - `YOUR_IDEAS_DATABASE_ID` → ID de votre base Notion "Ideas"
   - `YOUR_TODOS_DATABASE_ID` → ID de votre base Notion "Todos"
   - `YOUR_LOGS_DATABASE_ID` → ID de votre base Notion "Logs"
   - `YOUR_TELEGRAM_USER_ID` → votre Telegram user ID
3. **Configurer Notion** : Voir le dossier `docs/` du projet correspondant
4. **Activer** le workflow et envoyer un message à votre bot Telegram

## Ligne éditoriale

Voir [EDITORIAL.md](EDITORIAL.md) pour la charte graphique, les types de posts et le rythme de publication.

## Licence

[CC BY-NC 4.0](LICENSE) — Vous pouvez copier, adapter et partager. Pas d'usage commercial.
