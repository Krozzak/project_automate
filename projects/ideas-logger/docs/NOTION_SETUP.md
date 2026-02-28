# Configuration Notion pour Ideas Logger v2

Ce document explique comment configurer les bases de données Notion pour le workflow Ideas Logger v2.

## 1. Modifier la base "Ideas Logger" existante

Ajouter ces propriétés à votre base existante :

| Propriété | Type | Description |
|-----------|------|-------------|
| UpdateCount | Number | Nombre de mises à jour (défaut: 0) |
| LastUpdated | Date | Date de dernière mise à jour |
| Todos | Relation | Lien vers la base Todos |
| Logs | Relation | Lien vers la base Logs |

### Étapes dans Notion

1. Ouvrir la base "Ideas Logger"
2. Cliquer sur "+" pour ajouter une propriété
3. Ajouter "UpdateCount" → Type: Number → Défaut: 0
4. Ajouter "LastUpdated" → Type: Date
5. Les relations seront créées automatiquement lors de la création des autres bases

## 2. Créer la base "Todos"

Cette base stockera les actions concrètes liées aux idées.

### Propriétés à créer

| Propriété | Type | Options/Description |
|-----------|------|---------------------|
| Title | Title | (par défaut) |
| ParentIdea | Relation | → Ideas Logger |
| Status | Status | À faire, En cours, Terminé, Bloqué |
| Priority | Select | P1 (urgent), P2 (important), P3 (normal) |
| DueDate | Date | Échéance optionnelle |
| EstimatedMinutes | Number | Temps estimé en minutes |
| Context | Select | Bureau, Maison, Mobile, Partout |
| EnergyLevel | Select | Haute, Moyenne, Basse |
| CreatedAt | Date | Date de création |
| CompletedAt | Date | Date de complétion |
| Source | Select | Manual, VoiceLog, Generated |
| Order | Number | Pour tri dans l'idée parente |

### Étapes dans Notion

1. Créer une nouvelle page "Todos" de type Database
2. Ajouter toutes les propriétés ci-dessus
3. Pour "ParentIdea", choisir "Relation" puis sélectionner "Ideas Logger"
4. Cocher "Show on Ideas Logger" pour créer la relation bidirectionnelle

## 3. Créer la base "Logs"

Cette base stockera l'historique de toutes les mises à jour.

### Propriétés à créer

| Propriété | Type | Options/Description |
|-----------|------|---------------------|
| Title | Title | (résumé auto du log) |
| Idea | Relation | → Ideas Logger |
| Timestamp | Date | Date et heure de la mise à jour |
| UpdateType | Select | status_change, add_todo, add_info, scope_change |
| Content | Text | Détail de la mise à jour |
| RawTranscript | Text | Message original de l'utilisateur |
| TodosCreated | Relation | → Todos (si des todos ont été créés) |

### Étapes dans Notion

1. Créer une nouvelle page "Logs" de type Database
2. Ajouter toutes les propriétés ci-dessus
3. Pour "Idea", choisir "Relation" puis sélectionner "Ideas Logger"
4. Pour "TodosCreated", choisir "Relation" puis sélectionner "Todos"

## 4. Configurer les Rollups (optionnel mais recommandé)

Sur la base "Ideas Logger", ajouter ces Rollups pour voir les stats :

| Propriété | Type | Configuration |
|-----------|------|---------------|
| ActiveTodosCount | Rollup | Relation: Todos → Calcul: Count → Filtre: Status ≠ Terminé |
| NextTodoAction | Rollup | Relation: Todos → Propriété: Title → Filtre: Status = À faire → Show original |

## 5. Récupérer les IDs des bases

Pour le workflow n8n, vous aurez besoin des IDs des bases.

### Comment trouver l'ID d'une base

1. Ouvrir la base en mode "Full page"
2. L'URL ressemble à : `https://www.notion.so/votrenom/Base-Name-abc123def456...`
3. L'ID est la partie après le dernier `-` : `abc123def456...`
4. Format complet avec tirets : `abc123de-f456-7890-abcd-ef1234567890`

### IDs des bases

- Ideas Logger : `YOUR_IDEAS_DATABASE_ID`
- Todos : `YOUR_TODOS_DATABASE_ID`
- Logs : `YOUR_LOGS_DATABASE_ID`

## 6. Vérification

Après configuration, vérifiez que :

- [ ] Ideas Logger a les nouvelles propriétés (UpdateCount, LastUpdated)
- [ ] La relation Todos apparaît sur Ideas Logger
- [ ] La relation Logs apparaît sur Ideas Logger
- [ ] Todos a la relation ParentIdea vers Ideas Logger
- [ ] Logs a la relation Idea vers Ideas Logger
- [ ] Les Rollups affichent les bonnes valeurs (si configurés)

## 7. Intégration Notion

Assurez-vous que votre intégration Notion a accès aux 3 bases :

1. Aller sur https://www.notion.so/my-integrations
2. Sélectionner votre intégration "Idea Logger"
3. Vérifier que les 3 bases sont partagées avec l'intégration

Pour partager une base avec l'intégration :
1. Ouvrir la base en mode Full page
2. Cliquer sur "..." en haut à droite
3. "Add connections" → Sélectionner votre intégration
