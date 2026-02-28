# Workflows LinkedIn Auto — Import Guide

> Workflows n8n pour automatiser la publication LinkedIn et la récupération des statistiques

## Fichiers

| Fichier | Description | Noeuds | Déclenchement |
|---------|-------------|--------|---------------|
| `LinkedIn_Stats_v1.json` | Récupère les stats des posts LinkedIn et analyse les performances | 16 | Message Telegram "stats" |
| `LinkedIn_Publisher_v1.json` | Publie automatiquement le post du lundi depuis Notion | 8 | Cron lundi 08:25 |

## Prérequis

### 1. LinkedIn Developer App

Vous devez créer une application LinkedIn Developer pour obtenir un accès API.

**Étapes** :
1. Aller sur https://www.linkedin.com/developers/apps
2. Créer une nouvelle app
3. Demander l'accès aux produits :
   - **Share on LinkedIn** (pour publier)
   - **Sign In with LinkedIn using OpenID Connect** (pour l'authentification)
   - **Marketing Developer Platform** (optionnel, pour stats détaillées)
4. Configurer les Redirect URLs :
   - `https://<votre-instance-n8n>/rest/oauth2-credential/callback`
5. Noter le **Client ID** et **Client Secret**

### 2. Scopes OAuth2 requis

- `openid` — Authentification
- `profile` — Récupérer l'URN du profil
- `w_member_social` — Publier des posts
- `r_organization_social` — Lire les stats (nécessite Marketing Developer Platform)

### 3. Récupérer votre URN LinkedIn

Après avoir configuré l'OAuth2 dans n8n :

```bash
curl -X GET https://api.linkedin.com/v2/userinfo \
  -H "Authorization: Bearer {access_token}"
```

Réponse : `{"sub": "abc123..."}` → votre URN sera `urn:li:person:abc123`

### 4. Base Notion PostStats

Créer une base Notion avec les propriétés listées dans [`docs/NOTION_SETUP.md`](../docs/NOTION_SETUP.md).

Récupérer l'ID de la base (dans l'URL de la page).

## Import dans n8n

### Étape 1 — Créer les credentials

#### Credential LinkedIn OAuth2

1. Dans n8n : **Credentials** → **New**
2. Type : **LinkedIn OAuth2 API**
3. Renseigner :
   - Client ID
   - Client Secret
   - Scopes : `openid,profile,w_member_social`
4. Cliquer sur **Connect** → suivre le flow OAuth2
5. Noter le **Credential ID** (visible dans l'URL après sauvegarde)

#### Credential Telegram (si pas déjà configuré)

1. Type : **Telegram API**
2. Access Token : obtenu via [@BotFather](https://t.me/BotFather)

#### Credential Notion (si pas déjà configuré)

1. Type : **Notion API**
2. Suivre le flow OAuth2 pour autoriser n8n

#### Credential OpenAI (si pas déjà configuré)

1. Type : **OpenAI API**
2. API Key : depuis https://platform.openai.com/api-keys

### Étape 2 — Importer les workflows

#### LinkedIn_Stats_v1.json

1. Dans n8n : **Workflows** → **Add workflow** → **Import from File**
2. Sélectionner `LinkedIn_Stats_v1.json`
3. **Modifier les noeuds suivants** :

| Noeud | Paramètre | Valeur à remplacer |
|-------|-----------|-------------------|
| Query Published Posts | databaseId | `TODO_POSTSTATS_DATABASE_ID` → ID de votre base Notion |
| Get LinkedIn Stats | credentials | `TODO_LINKEDIN_CREDENTIAL_ID` → ID du credential LinkedIn |
| Telegram Trigger | userIds | Votre Telegram User ID (optionnel, pour sécuriser) |

4. **Sauvegarder** et **Activer**

#### LinkedIn_Publisher_v1.json

1. Import depuis `LinkedIn_Publisher_v1.json`
2. **Modifier les noeuds suivants** :

| Noeud | Paramètre | Valeur à remplacer |
|-------|-----------|-------------------|
| Query Next Post | databaseId | `TODO_POSTSTATS_DATABASE_ID` → ID de votre base Notion |
| Publish to LinkedIn | credentials | `TODO_LINKEDIN_CREDENTIAL_ID` → ID du credential LinkedIn |
| Publish to LinkedIn | jsonBody | `TODO_LINKEDIN_PERSON_URN` → Votre URN LinkedIn |
| Send Confirmation | chatId | Votre Telegram User ID |
| Send No Post Alert | chatId | Votre Telegram User ID |

3. **Sauvegarder** et **Activer**

### Étape 3 — Tester

#### Test Stats Collector

1. Ajouter un post test dans Notion :
   - Status : "Publié"
   - LinkedInPostURN : (URN d'un vrai post LinkedIn existant)
2. Envoyer "stats" sur Telegram à votre bot
3. Vérifier que vous recevez un rapport avec les stats

#### Test Publisher

**Option 1 — Test manuel** :
1. Créer un post test dans Notion :
   - Status : "Prêt"
   - PlannedDate : aujourd'hui
   - Content : "Test de publication automatique"
2. Dans n8n, ouvrir le workflow Publisher
3. Cliquer sur **Execute Workflow** (bouton Play en haut à droite)
4. Vérifier que le post est publié sur LinkedIn

**Option 2 — Attendre le lundi** :
- Le workflow se déclenche automatiquement chaque lundi à 08:25

## Configuration avancée

### Changer l'heure de publication

Par défaut : lundi 08:25

Pour modifier :
1. Ouvrir `LinkedIn_Publisher_v1.json` dans n8n
2. Aller au noeud "Cron Monday 08:25"
3. Modifier l'expression cron :
   - Format : `{minute} {hour} * * {day}`
   - Exemple : `30 9 * * 1` = lundi 09:30

### Changer le format du rapport stats

1. Ouvrir `LinkedIn_Stats_v1.json`
2. Aller au noeud "GPT Analysis"
3. Modifier le prompt système pour ajuster le format du rapport

### Ajouter des filtres sur les stats

Exemple : ne récupérer que les posts du Mois 4

1. Ouvrir `LinkedIn_Stats_v1.json`
2. Aller au noeud "Query Published Posts"
3. Ajouter un filtre JSON :
```json
{
  "and": [
    {"property": "Status", "status": {"equals": "Publié"}},
    {"property": "Mois", "select": {"equals": "Mois_4"}}
  ]
}
```

## Sécurité

### Credentials

- Les credentials LinkedIn, Telegram, Notion et OpenAI sont stockés dans n8n de manière sécurisée
- Ne jamais commiter les fichiers JSON avec les vrais credential IDs

### Token LinkedIn

- Les tokens OAuth2 expirent après 60 jours
- n8n gère automatiquement le refresh via le refresh token
- Si le token expire, reconnecter manuellement le credential

### Rate Limiting

**LinkedIn API** :
- **Posts API** : 100 requêtes/jour par membre
- **Stats API** : Limites variables selon l'accès (Marketing Developer Platform)

**Protection** :
- Stats Collector déclenché manuellement (pas de cron)
- Publisher déclenché 1×/semaine → bien en dessous des limites

## Troubleshooting

### "No posts found with LinkedIn URN"

**Cause** : Aucun post dans Notion avec Status="Publié" ET un LinkedInPostURN rempli

**Solution** :
1. Vérifier qu'au moins un post a été publié manuellement sur LinkedIn
2. Copier l'URN du post dans Notion (champ LinkedInPostURN)
3. Relancer le workflow

### "LinkedIn API error 401 Unauthorized"

**Cause** : Token expiré ou scopes insuffisants

**Solution** :
1. Aller dans n8n Credentials → LinkedIn OAuth2
2. Cliquer sur "Reconnect"
3. Vérifier que les scopes incluent bien `w_member_social`

### "Post published but no URN returned"

**Cause** : La réponse API LinkedIn ne contient pas l'URN dans le header attendu

**Solution** :
1. Vérifier le noeud "Extract Post URN"
2. Modifier le code pour parser `response.body.id` au lieu de `response.headers['x-restli-id']`

### "Nothing to publish this week" alors qu'un post est prêt

**Cause** : Le post a Status="Prêt" mais PlannedDate est dans le futur

**Solution** :
1. Vérifier que PlannedDate ≤ aujourd'hui
2. Ou modifier le filtre dans "Query Next Post" pour ignorer PlannedDate

## Évolutions futures (V2)

- [ ] Support des images/carousels dans les posts
- [ ] Hashtags automatiques depuis Notion
- [ ] Meilleur parsing des stats (clickCount peut ne pas être disponible)
- [ ] Synchronisation automatique fichiers .md → Notion
- [ ] Multi-plateformes (Twitter, Threads...)

## Support

Pour toute question ou bug :
- Ouvrir une issue sur GitHub
- Contacter via LinkedIn

---

**Built with** : n8n, LinkedIn API v2, Notion API, OpenAI GPT-4o-mini, Telegram Bot API
