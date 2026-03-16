# AI-Proof Job Scanner — Architecture

**Site live** : https://ekenor.com/tools/ai-proof

## Stack

| Layer | Technologie |
|-------|-------------|
| Framework | Astro 5 (intégré à Ekenor) + React island |
| UI | Tailwind CSS |
| LLM | OpenAI GPT-4o-mini (temperature 0.3) |
| Cache | Upstash Redis (30 jours, clé normalisée) |
| Analytics | Firebase Firestore (fire-and-forget) |
| Déploiement | Vercel (repo Krozzak/ekenor) |

## Fonctionnement

### Étape 1 — Analyse rapide
1. L'utilisateur entre un titre de poste (+ secteur optionnel)
2. `POST /api/analyze` vérifie d'abord le cache Redis
3. Si cache hit (< 30 jours) → réponse instantanée (~100ms)
4. Si cache miss → appel GPT-4o-mini → stockage cache → réponse (~3s)
5. Les analytics sont trackées dans Firestore (fire-and-forget)

### Étape 2 — Affinage personnel
1. L'utilisateur décrit ses tâches quotidiennes spécifiques
2. `POST /api/analyze` avec `tasks_description` rempli
3. Pas de cache (l'analyse est personnelle)
4. GPT affine le score avec les données contextuelles

## Collections Firestore

### `ai_proof_analytics`
Chaque analyse déclenchée (quick ou detailed) :
```
job_title, sector, lang, step, resilience_score,
risk_level, years_to_impact, automation_percentage,
tasks_at_risk_count, created_at
```

### Cache Redis
Résultats GPT pour les analyses rapides (déduplication) :
```
result (JSON complet), created_at, hit_count
```
Clé = `normalize(job_title)_normalize(sector)` — expire après 30 jours.

## Variables d'environnement

```env
OPENAI_API_KEY=...
KV_REST_API_URL=...
KV_REST_API_TOKEN=...
FIREBASE_PROJECT_ID=...
FIREBASE_CLIENT_EMAIL=...
FIREBASE_PRIVATE_KEY=...
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
  "takeaway": [{ "action": "...", "why": "...", "resource": null, "urgency": "now|soon|later" }],
  "pivot_roles": ["Rôle A", "Rôle B"],
  "summary_fr": "...",
  "summary_en": "..."
}
```

## Roadmap V2

- Toggle FR/EN (langue de l'interface et de l'analyse)
- URLs partageables avec paramètres (job + secteur pré-remplis)
- Dynamic OG images (carte de score partageable sur LinkedIn/Stories)
- "Top jobs this week" — stats publiques des métiers les plus analysés
- Rate limiting basique par IP

## Publication

- Post LinkedIn de lancement : 2026-03-16
- Post "behind the build" (stats réelles) : 2026-03-26
