# Setup Notion — Base PostStats

> Guide de configuration de la base Notion pour le système LinkedIn Auto

## Créer la base de données

1. Ouvrir Notion
2. Créer une nouvelle page
3. Taper `/database` → choisir "Table - Full page"
4. Nommer la page : **PostStats**

## Propriétés à créer

### 1. Title (par défaut)
- **Type** : Title
- Titre du post LinkedIn

### 2. Mois
- **Type** : Select
- **Options** : Mois_1, Mois_2, Mois_3, Mois_4, Mois_5, Mois_6...
- Identifie le mois du projet

### 3. Semaine
- **Type** : Select
- **Options** : S1, S2, S3, S4
- Position du post dans le mois

### 4. Type
- **Type** : Select
- **Options** :
  - AUTOMATISATION
  - RÉFLEXION
  - RETOUR_EXP
  - MÉTA
  - VISION

### 5. Status
- **Type** : Status
- **Options** :
  - Brouillon (gris)
  - Prêt (vert)
  - Publié (bleu)
  - Archivé (rouge)

### 6. PlannedDate
- **Type** : Date
- Date prévue de publication (sans heure)

### 7. PublishedAt
- **Type** : Date
- Date réelle de publication (avec heure)
- Rempli automatiquement par le workflow Publisher

### 8. Content
- **Type** : Text (rich text)
- Texte complet du post à publier
- **Important** : Copier le texte du post depuis les fichiers .md

### 9. LinkedInPostURN
- **Type** : Text (rich text)
- URN du post LinkedIn (format : `urn:li:share:...`)
- Rempli automatiquement par le workflow Publisher

### 10. Impressions
- **Type** : Number
- Nombre de vues du post
- Rempli automatiquement par le workflow Stats Collector

### 11. Likes
- **Type** : Number
- Nombre de likes
- Rempli automatiquement par le workflow Stats Collector

### 12. Comments
- **Type** : Number
- Nombre de commentaires
- Rempli automatiquement par le workflow Stats Collector

### 13. Shares
- **Type** : Number
- Nombre de partages
- Rempli automatiquement par le workflow Stats Collector

### 14. Clicks
- **Type** : Number
- Nombre de clics sur le post
- Rempli automatiquement par le workflow Stats Collector

### 15. EngagementRate
- **Type** : Number (formaté en pourcentage)
- **Formule** : `(Likes + Comments×3 + Shares×5) / Impressions × 100`
- Rempli automatiquement par le workflow Stats Collector

### 16. Concept
- **Type** : Text (rich text)
- Nom du concept utilisé dans le post
- Exemple : "Goodhart's Law", "Curse of Knowledge", "Feynman Technique"

### 17. ConceptLevel
- **Type** : Select
- **Options** : Simple, Intermédiaire, Avancé
- Niveau de complexité du concept

### 18. GPTAnalysis
- **Type** : Text (rich text)
- Analyse GPT des performances du post
- Rempli automatiquement par le workflow Stats Collector

### 19. StatsUpdatedAt
- **Type** : Date (avec heure)
- Dernière mise à jour des stats
- Rempli automatiquement par le workflow Stats Collector

### 20. Tags
- **Type** : Multi-select
- **Options** : Focus, Charge mentale, IA pragmatique, Simplicité, Discipline, Friction, Éthique IA
- Sous-thèmes du post

## Créer les vues

### Vue 1 — Calendrier (par défaut)

1. Cliquer sur "..." en haut à droite → "New view"
2. Type : Table
3. Nom : **Calendrier**
4. **Grouper par** : Mois
5. **Trier par** : PlannedDate (croissant)
6. **Filtrer** : Status is not Archivé

### Vue 2 — Performance

1. Nouvelle vue → Table
2. Nom : **Performance**
3. **Trier par** : EngagementRate (décroissant)
4. **Filtrer** : Status is Publié
5. **Afficher** : Titre, Mois, Semaine, Type, Impressions, Likes, Comments, Shares, EngagementRate

### Vue 3 — À publier

1. Nouvelle vue → Table
2. Nom : **À publier**
3. **Filtrer** :
   - Status is Prêt
4. **Trier par** : PlannedDate (croissant)
5. **Afficher** : Titre, PlannedDate, Content (pour vérifier le texte)

## Remplir les posts du Mois 4

### Post 4.1 — AUTOMATISATION

| Propriété | Valeur |
|-----------|--------|
| Title | J'ai automatisé la publication (pas l'écriture) |
| Mois | Mois_4 |
| Semaine | S1 |
| Type | AUTOMATISATION |
| Status | Brouillon |
| PlannedDate | [À définir — premier lundi du mois] |
| Content | [Copier depuis `Mois_4_LinkedInAPI/posts/post1/Post1-automatisation-LinkedIn-Auto.md`] |
| Concept | Aucun |
| ConceptLevel | Simple |
| Tags | Friction, Discipline |

### Post 4.2 — RÉFLEXION

| Propriété | Valeur |
|-----------|--------|
| Title | Pourquoi je ne cherche pas la viralité |
| Mois | Mois_4 |
| Semaine | S2 |
| Type | RÉFLEXION |
| Status | Brouillon |
| PlannedDate | [À définir — 2ème lundi] |
| Content | [Copier depuis `Mois_4_LinkedInAPI/posts/post2/Post2-reflexion-pas-de-viralite.md`] |
| Concept | Goodhart's Law |
| ConceptLevel | Simple |
| Tags | Discipline, Simplicité |

### Post 4.3 — RETOUR D'EXPÉRIENCE

| Propriété | Valeur |
|-----------|--------|
| Title | Ce que les non-tech pensent impossible |
| Mois | Mois_4 |
| Semaine | S3 |
| Type | RETOUR_EXP |
| Status | Brouillon |
| PlannedDate | [À définir — 3ème lundi] |
| Content | [Copier depuis `Mois_4_LinkedInAPI/posts/post3/Post3-retour-experience-non-tech.md`] |
| Concept | Curse of Knowledge |
| ConceptLevel | Simple |
| Tags | IA pragmatique, Simplicité |

### Post 4.4 — MÉTA

| Propriété | Valeur |
|-----------|--------|
| Title | Publier pour apprendre : chaque post me force à sourcer ce que je crois savoir |
| Mois | Mois_4 |
| Semaine | S4 |
| Type | MÉTA |
| Status | Brouillon |
| PlannedDate | [À définir — 4ème lundi] |
| Content | [Copier depuis `Mois_4_LinkedInAPI/posts/post4/Post4-meta-publier-pour-apprendre.md`] |
| Concept | Feynman Technique |
| ConceptLevel | Simple |
| Tags | Discipline, IA pragmatique |

## Récupérer l'ID de la base

1. Ouvrir la page PostStats dans Notion
2. Cliquer sur "Share" en haut à droite
3. Copier le lien de la page
4. L'ID est dans l'URL :
   - Format : `https://www.notion.so/workspace/{DATABASE_ID}?v=...`
   - Exemple : `2fa5ee6f-1580-803d-b7f5-fd812c9215ad`

5. Remplacer dans les workflows :
   - `LinkedIn_Stats_v1.json` → ligne "databaseId"
   - `LinkedIn_Publisher_v1.json` → ligne "databaseId"

## Connecter à n8n

1. Dans n8n, créer un credential "Notion API"
2. Suivre le flow OAuth2 pour autoriser l'accès
3. Vérifier que la base PostStats est accessible dans le sélecteur de base de données n8n

## Workflow de mise à jour

### Workflow manuel (recommandé)

1. Rédiger les posts dans les fichiers `.md`
2. Copier le texte final dans Notion (champ Content)
3. Passer le Status à "Prêt" quand le post est finalisé
4. Le workflow Publisher se déclenche automatiquement le lundi

### Workflow automatisé (futur)

Possibilité d'ajouter un workflow qui :
- Lit les fichiers `.md` dans le dossier `Mois_X/posts/`
- Crée ou met à jour automatiquement les entrées Notion
- Synchronise le contenu entre les fichiers et Notion

→ V2, pas prioritaire pour l'instant
