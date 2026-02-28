# AI-Proof Job Scanner — Architecture

## Stack

| Layer | Technologie |
|-------|-------------|
| Framework | Next.js 15 (App Router) |
| UI | Tailwind CSS v3 + Shadcn/ui |
| Animations | Framer Motion |
| LLM | OpenAI GPT-4o-mini |
| Base de données | Firebase Firestore (tier gratuit) |
| Déploiement | Vercel |

## Fonctionnement

### Étape 1 — Analyse rapide
1. L'utilisateur entre un titre de poste (+ secteur optionnel)
2. `POST /api/analyze` vérifie d'abord le cache Firestore
3. Si cache hit (< 30 jours) → réponse instantanée (~100ms)
4. Si cache miss → appel GPT-4o-mini → stockage cache → réponse (~3s)
5. Les analytics sont trackées dans Firestore (fire-and-forget)

### Étape 2 — Affinage personnel
1. L'utilisateur décrit ses tâches quotidiennes spécifiques
2. `POST /api/analyze` avec `tasks_description` rempli
3. Pas de cache (l'analyse est personnelle)
4. GPT affine le score avec les données contextuelles

## Collections Firestore

### `analyses`
Chaque analyse déclenchée (quick ou detailed) :
```
job_title, sector, lang, step, resilience_score,
risk_level, years_to_impact, automation_percentage,
tasks_at_risk_count, created_at
```

### `cache`
Résultats GPT pour les analyses rapides (déduplication) :
```
result (JSON complet), created_at, hit_count
```
Clé = `normalize(job_title)_normalize(sector)` — expire après 30 jours.

## Variables d'environnement

```env
OPENAI_API_KEY=...
FIREBASE_PROJECT_ID=...
FIREBASE_CLIENT_EMAIL=...
FIREBASE_PRIVATE_KEY=...
NEXT_PUBLIC_BASE_URL=https://your-domain.vercel.app
```

## Format de réponse GPT

```json
{
  "resilience_score": 0-100,
  "risk_level": "low|moderate|high|critical",
  "timeline": {
    "years_to_impact": 5,
    "automation_percentage": 45,
    "message_fr": "...",
    "message_en": "..."
  },
  "tasks_at_risk": [{ "task": "...", "risk_pct": 75, "why": "..." }],
  "tasks_resilient": [{ "task": "...", "why": "..." }],
  "take_your_way": [{ "action": "...", "why": "...", "resource": null, "urgency": "now|soon|later" }],
  "pivot_roles": ["Rôle A", "Rôle B"],
  "summary_fr": "...",
  "summary_en": "..."
}
```
