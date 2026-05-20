# YouTube Transcript Bot — Spec V1

> Brique 1a de la Phase 1 d'ingestion (#8 Knowledge Management)
> **Statut** : 🟡 EN COURS — 2026-05-14
> **Base** : extension de `Knowledge_Curator_v1.json` (workflow n8n local existant)

---

## Contexte — Ce qui existe déjà

| Workflow | Statut | Rôle |
|----------|--------|------|
| `Knowledge_Ingestion_v1.2.json` | ✅ Live (n8n cloud) | Telegram → Notion Reading Queue — métadonnées YouTube via oEmbed, **pas de transcript** |
| `Knowledge_Curator_v1.json` | 🔵 En cours (n8n local) | URL → transcript (Jina sur page YouTube) → GPT → fichiers `.md` locaux |

**Ce qui manque** : le Curator v1 est déclenché manuellement depuis Telegram. Il faut le connecter à la Reading Queue Notion pour traiter automatiquement les vidéos ajoutées par l'Ingestion bot.

---

## Problème résolu

Quand tu envoies une URL YouTube à `@KnowledgeIngestionBot`, la page Notion est créée dans la Reading Queue mais le transcript n'est pas généré. Ce projet complète la boucle : la vidéo ajoutée déclenche l'extraction du transcript + l'analyse GPT + la création du fichier `.md` de digest.

---

## Flux cible

```text
@KnowledgeIngestionBot reçoit URL YouTube (EXISTANT)
  → Knowledge_Ingestion_v1.2 : crée page Notion Reading Queue (EXISTANT)
  → Webhook → Knowledge_Curator_v1 (n8n local) : déclenche traitement YT (À CONNECTER)

Knowledge_Curator_v1 (n8n local) :
  → Fetch YouTube transcript via r.jina.ai (EXISTANT — branche video)
  → Normalize Content
  → Read INDEX_CONCEPTS.md
  → GPT Knowledge Curator : digest + fiches (max 3 concepts)
  → Write Digest → .private/notes/sources/YYYY-MM-DD-slug-digest.md (EXISTANT)
  → Write Fiches → .private/notes/inbox/YYYY-MM-DD-concept-slug.md (EXISTANT)
  → [NOUVEAU] Update Notion Reading Queue : Status → "Traité" + lien digest
  → Send Telegram Confirmation
```

---

## Ce qu'il faut construire

### Étape 1 — Connecter Ingestion → Curator (webhook)

Dans `Knowledge_Ingestion_v1.2.json`, après la création de la page Notion Reading Queue, ajouter :
- **IF node** : `sourceType === 'video'` ?
- **HTTP node** : POST vers `http://localhost:5678/webhook/knowledge-curator` avec `{ url, pageId, sourceType }`

Dans `Knowledge_Curator_v1.json`, ajouter un **Webhook Trigger** (en plus du Telegram Trigger existant) :
- Route : `/webhook/knowledge-curator`
- Payload attendu : `{ url, pageId, sourceType }`
- Brancher vers le même pipeline que le trigger Telegram

### Étape 2 — Mettre à jour la Notion Reading Queue après traitement

À la fin du workflow Curator v1, ajouter un **Notion node** :
- Opération : `updatePage`
- Page ID : `{{ $json.pageId }}` (transmis depuis l'Ingestion bot)
- Propriétés à mettre à jour :
  - `Status` → `Traité`
  - `ProcessedAt` → date du jour
  - Un champ texte avec le chemin du digest généré

**Notion Reading Queue ID** : `3315ee6f-1580-80c0-9daf-ef7d00faf968`
**Credential** : `ZZ0Z1YmN9wAMVVUe`

### Étape 3 — Variable d'environnement n8n local

Le Curator v1 utilise `$env.NOTES_BASE_PATH`. Sur Windows :

```
NOTES_BASE_PATH = D:/Projet_Automate/.private/notes
```

À définir dans n8n local Settings > Environment Variables.

---

## Format des fichiers de sortie

### Digest source (`notes/sources/`)

```markdown
---
type: source-digest
title: [Titre de la vidéo]
slug: [slug-kebab]
url: https://youtube.com/watch?v=...
source_type: video
author: [Chaîne YouTube]
processed_at: YYYY-MM-DD
statut: En attente de validation
fiches_generated:
  - YYYY-MM-DD-concept-slug-1
  - YYYY-MM-DD-concept-slug-2
---

# [Titre] — Digest de traitement

> Source / Traité le / Statut

## Résumé exécutif
## Idées clés extraites
## Fiches de notes générées (checkboxes)
## Notes de traitement IA
## Contenu complet (transcript brut)
```

### Fiches inbox (`notes/inbox/`)

Respectent le format des fiches `notes/concepts/` — déplacer manuellement après validation.

---

## Stack technique

| Composant | Outil | Notes |
|-----------|-------|-------|
| Automation | n8n local (localhost:5678) | Accès filesystem requis |
| Trigger | Webhook (depuis Ingestion bot) + Telegram (direct) | Double entrée |
| Transcript YouTube | `get_transcript.py` (youtube-transcript-api) | Sous-titres natifs YouTube, 0 API tierce, fallback gracieux si absent |
| LLM | GPT-4o-mini (`openai-creds` — à mapper vers `Y4EKfFwKu05nkWfH`) | ~$0.001/source |
| Storage | ReadWriteFile node n8n local | `.private/notes/sources/` + `.private/notes/inbox/` |
| Notification | Telegram (`BGutoRtuK2XPMMTl`) | Bot existant |

---

## Fichiers du projet

| Fichier | Description |
|---------|-------------|
| `Knowledge_Ingestion_v1.2.json` | Archive — version sans transcript |
| `Knowledge_Ingestion_v1.3.json` | ✅ Version actuelle — inclut branche YouTube transcript |
| `Knowledge_Curator_SPEC.md` | Spec complète Phase 1 (architecture, formats, GPT prompt) |

---

## Prochaines étapes (checklist)

- [ ] Définir `NOTES_BASE_PATH` dans n8n local (Settings > Environment Variables)
- [ ] Corriger le credential OpenAI dans Curator v1 : remplacer `openai-creds` par `Y4EKfFwKu05nkWfH`
- [ ] Activer le webhook trigger dans Curator v1
- [ ] Ajouter le nœud webhook call dans Knowledge_Ingestion_v1.2 (branche `sourceType === video`)
- [ ] Ajouter le nœud Notion updatePage à la fin du Curator v1 (Status → Traité)
- [ ] Tester avec une vidéo YouTube courte (< 10 min) pour vérifier le transcript via Jina
- [ ] Vérifier que les dossiers `notes/sources/` et `notes/inbox/` existent

---

## Connexions avec le reste du système

- **Input** : `@KnowledgeIngestionBot` (workflow Ingestion v1.2 live)
- **Output → `/process-reading-queue`** : les fichiers digest dans `notes/sources/` sont la source de cette commande
- **Output → `/brainstorm`** : les fiches inbox sont les candidats directs pour de nouvelles fiches concepts
- **Extension future (1b)** : même architecture Curator pour articles web (Jina) et PDFs
