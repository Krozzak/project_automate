# Architecture — LinkedIn Auto

> Documentation technique pour le Mois 4 du Projet Automate
> Automatisation de la publication LinkedIn + récupération des statistiques

## Vue d'ensemble

Deux workflows n8n indépendants :

1. **LinkedIn Stats Collector** — Récupère les stats de performance des posts LinkedIn via l'API
2. **LinkedIn Auto Publisher** — Publie automatiquement le post du lundi matin

## Workflow 1 — LinkedIn Stats Collector

### Déclenchement
- Message Telegram contenant "stats" ou "/stats"
- Déclenché manuellement (pas de cron automatique)

### Flow simplifié

```
Telegram "stats"
      ↓
Query Notion (PostStats) — Status = "Publié"
      ↓
Filter (garde seulement les posts avec LinkedInPostURN)
      ↓
Get LinkedIn Stats (API call par post)
      ↓
Update Notion (stats + engagement rate)
      ↓
Aggregate Results (ranking, moyennes)
      ↓
GPT Analysis (patterns, recommandations)
      ↓
Format Report (Telegram-ready)
      ↓
Send Report via Telegram
```

### Noeuds clés

| Noeud | Type | Description |
|-------|------|-------------|
| Telegram Trigger | telegramTrigger | Filtre messages contenant "stats" |
| Query Published Posts | notion | Récupère tous les posts Status="Publié" |
| Filter & Prepare | code | Filtre les posts avec URN LinkedIn |
| Get LinkedIn Stats | httpRequest | API LinkedIn (socialMetadata endpoint) |
| Format Stats | code | Parse la réponse API, calcule l'engagement rate |
| Update Notion Stats | notion | Met à jour Impressions, Likes, Comments, Shares, Clicks |
| Aggregate Results | code | Ranking par engagement, moyennes |
| GPT Analysis | openAi | Analyse patterns, recommandations actionnables |
| Send Report | telegram | Envoie le résumé avec ranking |

### API LinkedIn utilisée

```http
GET https://api.linkedin.com/rest/socialMetadata/{postURN}
Headers:
  Authorization: Bearer {access_token}
  LinkedIn-Version: 202401
  X-Restli-Protocol-Version: 2.0.0
```

**Réponse** : `impressionCount`, `likeCount`, `commentCount`, `shareCount`, `clickCount`

### Engagement Rate

Formule : `(likes + comments×3 + shares×5) / impressions × 100`

Pondération :
- Like = 1 pt (action passive)
- Comment = 3 pts (engagement actif)
- Share = 5 pts (amplification maximale)

## Workflow 2 — LinkedIn Auto Publisher

### Déclenchement
- Cron trigger : chaque lundi à 08:25 (5 min avant l'heure de publication)

### Flow simplifié

```
Cron Lundi 08:25
      ↓
Query Notion (PostStats) — Status = "Prêt", PlannedDate ≤ aujourd'hui
      ↓
Has Post?
 ↓        ↓
Yes       No
 ↓        ↓
Publish   Alert Telegram
via API   "Rien à publier"
 ↓
Update Notion — Status → "Publié", PublishedAt, LinkedInPostURN
 ↓
Send Confirmation Telegram
```

### Noeuds clés

| Noeud | Type | Description |
|-------|------|-------------|
| Cron Monday 08:25 | scheduleTrigger | `25 8 * * 1` |
| Query Next Post | notion | Status="Prêt", PlannedDate ≤ now, limit 1 |
| Prepare Post | code | Extrait le contenu, vérifie qu'il n'est pas vide |
| Has Post? | if | Vérifie si un post est disponible |
| Publish to LinkedIn | httpRequest | POST /rest/posts via API LinkedIn |
| Extract Post URN | code | Parse la réponse API pour récupérer l'URN |
| Update Notion | notion | Status → "Publié", date + URN |
| Send Confirmation | telegram | "Post publié avec succès" + lien |

### API LinkedIn utilisée

```http
POST https://api.linkedin.com/rest/posts
Headers:
  Authorization: Bearer {access_token}
  LinkedIn-Version: 202401
  X-Restli-Protocol-Version: 2.0.0
  Content-Type: application/json

Body:
{
  "author": "urn:li:person:{personId}",
  "commentary": "Le texte du post...",
  "visibility": "PUBLIC",
  "distribution": {
    "feedDistribution": "MAIN_FEED",
    "targetEntities": [],
    "thirdPartyDistributionChannels": []
  },
  "lifecycleState": "PUBLISHED"
}
```

**Réponse** : header `x-restli-id` contient le post URN

## Base Notion — PostStats

### Propriétés

| Propriété | Type | Usage |
|-----------|------|-------|
| Title | title | Titre du post |
| Mois | select | Mois_1, Mois_2, Mois_3... |
| Semaine | select | S1, S2, S3, S4 |
| Type | select | AUTOMATISATION, RÉFLEXION, RETOUR_EXP, MÉTA |
| Status | status | Brouillon, Prêt, Publié, Archivé |
| PlannedDate | date | Date prévue de publication |
| PublishedAt | date | Date réelle de publication |
| Content | rich_text | Texte complet du post |
| LinkedInPostURN | rich_text | URN du post LinkedIn |
| Impressions | number | Nombre de vues |
| Likes | number | Nombre de likes |
| Comments | number | Nombre de commentaires |
| Shares | number | Nombre de partages |
| Clicks | number | Nombre de clics |
| EngagementRate | number | (likes + comments×3 + shares×5) / impressions × 100 |
| Concept | rich_text | Concept utilisé dans le post |
| ConceptLevel | select | Simple, Intermédiaire, Avancé |
| GPTAnalysis | rich_text | Analyse GPT des performances |
| StatsUpdatedAt | date | Dernière mise à jour des stats |
| Tags | multi_select | Sous-thèmes |

### Vues

1. **Calendrier** : Triée par PlannedDate, groupée par Mois
2. **Performance** : Triée par EngagementRate desc
3. **À publier** : Filtrée Status="Prêt", triée par PlannedDate

## Setup requis

### 1. LinkedIn Developer App

1. Créer une app sur https://www.linkedin.com/developers/apps
2. Demander accès aux produits :
   - Share on LinkedIn
   - Sign In with LinkedIn using OpenID Connect
   - Marketing Developer Platform (pour les stats détaillées)
3. Configurer Redirect URLs : `https://<ton-n8n>/rest/oauth2-credential/callback`
4. Récupérer Client ID + Client Secret

### 2. Scopes OAuth2

- `openid` : Authentification
- `profile` : Récupérer l'URN du profil
- `w_member_social` : Publier des posts
- `r_organization_social` : Lire les stats (nécessite Marketing Developer Platform)

### 3. Credentials n8n

1. Ajouter credential type "LinkedIn OAuth2 API"
2. Renseigner Client ID + Client Secret
3. Scopes : `openid,profile,w_member_social`
4. Connecter via OAuth2 flow
5. Récupérer l'URN personnel (`urn:li:person:{id}`)

### 4. Configuration workflows

Remplacer dans les JSON :
- `TODO_POSTSTATS_DATABASE_ID` → ID de la base Notion PostStats
- `TODO_LINKEDIN_CREDENTIAL_ID` → ID du credential LinkedIn dans n8n
- `TODO_LINKEDIN_PERSON_URN` → Ton URN LinkedIn personnel

## Limites et restrictions

### LinkedIn API Rate Limits

- **Posts API** : 100 requêtes/jour par membre
- **Stats API** : Varie selon l'accès (Marketing Developer Platform requis pour stats détaillées)

### Workarounds

- Stats Collector déclenché **manuellement** → pas de risque de rate limiting
- Publisher déclenché **1x/semaine** → très en dessous des limites

### Cas non couverts (V1)

- **Images/Carousels** : Publication texte seul. Les images nécessitent un upload séparé → V2
- **Hashtags** : Pas de champ dédié dans Notion pour les hashtags → V2
- **Programmation fine** : Publication fixée à 08:30 lundi. Pas de gestion d'heures variables → V2

## Philosophie du système

**Automatiser l'exécution, pas la décision.**

- L'écriture reste manuelle (seule partie créative qu'on garde)
- La publication est automatique (éliminer la friction mentale)
- Les stats sont accessibles sur demande (éviter la gamification, cf. Goodhart's Law)

**Build in public ≠ Marketing**

Ce système n'est PAS conçu pour :
- Maximiser les impressions
- Optimiser pour l'algo LinkedIn
- Publier plus souvent

Il EST conçu pour :
- Éliminer la friction du process de publication
- Avoir un filet de sécurité (alerte si rien n'est prêt)
- Mesurer sans devenir prisonnier des métriques
