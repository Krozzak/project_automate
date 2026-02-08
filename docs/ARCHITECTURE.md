# Architecture technique

## Vue d'ensemble

Système d'automatisation de productivité basé sur n8n. L'utilisateur interagit via Telegram (voix ou texte), le système analyse, structure et stocke dans Notion.

## Écosystème

```
┌─────────────────────────────────────────────────────────────────┐
│                    ÉCOSYSTÈME PRODUCTIVITÉ                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐  │
│  │   IDEAS      │      │    TODOS     │      │   TODO LIST  │  │
│  │   LOGGER     │ ───▶ │   (Steps)    │ ◀─── │   DYNAMIQUE  │  │
│  │  (Base 1)    │      │   (Base 2)   │      │  (Future)    │  │
│  └──────────────┘      └──────────────┘      └──────────────┘  │
│        │                      ▲                                │
│        ▼                      │                                │
│  ┌──────────────┐             │                                │
│  │    LOGS      │─────────────┘                                │
│  │  (Base 3)    │                                              │
│  └──────────────┘                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow (v3)

```
Telegram Message
       ↓
Voice/Text Switch
       ↓
    ┌──┴──┐
  Voice  Text
    ↓      ↓
Transcribe  Is Reply?
(Whisper)  ↓    ↓
    ↓    Yes   No
    │     ↓     ↓
    │  Parse  Edit Fields
    │  Selection   ↓
    └──────► Query All Ideas
                 ↓
          Format Ideas for GPT (shortId mapping: 01, 02...)
                 ↓
          ┌──────────────────────────────────────┐
          │  Unified GPT (UN SEUL APPEL)         │
          │  Input: transcript + idées existantes│
          │  Output: action + data               │
          └──────────────────────────────────────┘
                 ↓
          Parse GPT Response (resolve shortId → fullNotionId)
                 ↓
          Action Switch
          ↓      ↓      ↓      ↓
        NEW  UPDATE   ASK   REJECT
```

## Principe clé

**Query Notion AVANT ChatGPT** : GPT reçoit les idées existantes ET le transcript, et fait l'association en une seule passe. Pas de matching JS fragile.

## GPT Response Format

```json
{
  "action": "new | update | ask | reject",

  "idea": { "title", "summary", "pillar", "domain", "tags", "difficulty_1to5", "impact_1to5", "..." },

  "matched_idea_id": "01",
  "update": { "status", "new_info", "new_todos" },

  "options": [{"id": "01", "title": "...", "why": "..."}],

  "confirmation_message": "..."
}
```

## Tech Stack

| Composant | Technologie |
|-----------|------------|
| Workflow Automation | n8n (cloud ou local) |
| Messaging | Telegram Bot API |
| Speech-to-Text | OpenAI Whisper |
| LLM Analysis | OpenAI GPT-4o-mini |
| Database | Notion API |
| Data Transformation | JavaScript (n8n nodes) |

## Notion Database Schema

### Ideas Logger (Main)

| Propriété | Type | Description |
|----------|------|-------------|
| Title | title | Nom de l'idée |
| Summary | rich_text | Description |
| Pilar | rich_text | Pilier stratégique |
| Domain | multi_select | Domaines |
| Tags | multi_select | Catégories |
| TimeBucket | select | 5-15min, 15-60min, 1-3h, 3-10h, 10h+ |
| Difficulty | number | 1-5 |
| Impact | number | 1-5 |
| Urgency | number | 1-5 |
| Clarity | number | 1-5 |
| ICE | number | Impact x Clarity x (6-Difficulty) |
| NextAction | rich_text | Prochaine étape |
| Dependencies | rich_text | Bloqueurs |
| Status | status | Pas commencé, En cours, Terminé, Abandonné |
| CapturedAt | date | Date de création |
| Source | rich_text | Telegram |
| UpdateCount | number | Nombre d'updates |
| LastUpdated | date | Dernière mise à jour |
| RawText | rich_text | Transcript original |

### Todos

| Propriété | Type |
|----------|------|
| Title | title |
| Ideas Logger | relation |
| Status | status |
| Priority | select (P1, P2, P3) |
| EstimatedMinutes | number |
| Context | select (Bureau, Maison, Mobile, Partout) |
| EnergyLevel | select (Haute, Moyenne, Basse) |
| Order | number |
| ValidationCriteria | rich_text |
| BlockedBy | relation (self) |

### Logs

| Propriété | Type |
|----------|------|
| Ideas Logger | relation |
| Timestamp | date |
| UpdateType | select |
| Content | rich_text |
| RawTranscript | rich_text |

## Déploiement local

```bash
# Install n8n
npm install n8n -g

# Start
n8n start --port 5678

# Pour les webhooks Telegram
ngrok http 5678
```
