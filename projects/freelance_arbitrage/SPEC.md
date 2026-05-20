# Freelance Arbitrage Agent — Spec V1

## Objectif

Scraper Upwork et Fiverr en continu pour détecter les missions résolvables par IA (outils existants ou nouveaux outils rapides à builder), scorer chaque opportunité, alerter via Telegram, et générer des proposals prêts à soumettre via un dashboard Streamlit.

**Principe clé** : le scope est large — pas seulement les missions "tech/code". Toute mission qui semble manuelle et chronophage pour un humain mais résolvable en minutes avec un outil IA est une cible. Le type de la mission importe peu, la structure du problème est ce qui compte.

## Outils existants → missions ciblées

| Outil | Catégories Upwork/Fiverr | Tarif marché | Temps de livraison réel |
|-------|--------------------------|-------------|------------------------|
| Book Translator (#50) | Translation, Writing | 25-80$ | 20 min |
| ProofLab (#10) | Data Entry, Admin Support | 20-60$ | 5 min |
| Script GPT générique | Writing, Admin Support | 15-50$ | 3-10 min |
| Whisper transcription | Video & Audio | 20-80$ | 10 min |
| Python data cleaning | Data Entry, Excel/CSV | 20-60$ | 10 min |

## Catégories Upwork à scraper (scope large)

- Translation & Localization
- Writing & Content
- Data Entry & Admin Support
- Video & Audio (transcription, sous-titres)
- AI Services
- Document Processing

## Architecture

```text
Cron toutes les 2h (configurable) ou lancement manuel
  ↓
scrapers/upwork.py    → scrape search results par catégorie + keywords
scrapers/fiverr.py    → scrape buyer requests
  ↓
Parser unifié → Mission(titre, description, budget_min, budget_max,
                         nb_proposals, posted_at, client_rating,
                         platform, url, categorie)
  ↓
scorer/scorer.py → GPT-4o-mini batch scoring
  - feasibility_score (0-3) : outil existant résout ça ?
  - build_score (0-2) : résolvable par nouveau build rapide ?
  - urgency_score (0-3) : fraîcheur du post
  - competition_score (0-2) : inverse du nb proposals
  - budget_score (0-3) : tarif relatif au temps estimé
  - total_score = somme pondérée → 0-100
  ↓
Si total_score > 75 → bot/telegram.py → alerte immédiate
  ↓
data/missions.db (SQLite) → historique toutes missions scorées
  ↓
dashboard/app.py (Streamlit) → UI complète
```

## Schema SQLite

```sql
CREATE TABLE missions (
    id TEXT PRIMARY KEY,           -- hash(platform + url)
    platform TEXT,                 -- "upwork" | "fiverr"
    title TEXT,
    description TEXT,
    budget_min REAL,
    budget_max REAL,
    nb_proposals INTEGER,
    posted_at DATETIME,
    scraped_at DATETIME,
    category TEXT,
    url TEXT,
    client_rating REAL,
    feasibility_score INTEGER,     -- 0-3
    build_score INTEGER,           -- 0-2
    urgency_score INTEGER,         -- 0-3
    competition_score INTEGER,     -- 0-2
    budget_score INTEGER,          -- 0-3
    total_score INTEGER,           -- 0-100
    tool_match TEXT,               -- "book_translator" | "prooflab" | "new_build" | null
    alerted INTEGER DEFAULT 0,     -- 1 si alerte Telegram envoyée
    proposal_sent INTEGER DEFAULT 0,
    result TEXT                    -- "hired" | "rejected" | "no_response" | null
);
```

## Scorer GPT — prompt système

```text
Tu es un expert en arbitrage freelance. Tu analyses des missions Upwork/Fiverr pour
déterminer si elles peuvent être résolues rapidement avec des outils IA existants
ou de nouveaux outils simples à builder.

Outils existants disponibles :
- Book Translator : traduit un ePUB/PDF complet EN→FR (ou autre langue) en 20 min
- ProofLab : compare deux versions d'un PDF et détecte les changements visuellement en 5 min
- Script GPT : résumé, rédaction, extraction, nettoyage de texte en 3-10 min
- Whisper : transcription audio/vidéo en 10 min
- Python data : nettoyage CSV/Excel, extraction données PDF en 10 min

Pour chaque mission, réponds en JSON :
{
  "feasibility_score": 0-3,  // 0=impossible, 1=possible avec effort, 2=faisable, 3=trivial avec outil existant
  "tool_match": "book_translator|prooflab|whisper|gpt_script|data_python|new_build|none",
  "build_score": 0-2,  // si tool_match=new_build : 0=semaines, 1=jours, 2=heures
  "estimated_delivery_minutes": int,  // temps réel de livraison avec l'outil
  "reasoning": "string courte"  // pourquoi ce score
}
```

## Dashboard Streamlit — features V1

- Tableau principal : missions triées par total_score desc
- Filtres : platform / tool_match / score_min / budget_min / catégorie / date
- Colonne "Score" avec badge coloré (vert > 75, orange 50-75, rouge < 50)
- Bouton **"Générer proposal"** → appel GPT avec titre + description → proposal complet prêt à copier
- Bouton **"Marquer soumis"** → met à jour `proposal_sent = 1` dans SQLite
- Bouton **"Résultat"** → dropdown hired/rejected/no_response → mise à jour `result`
- Onglet **"Discovery"** : missions `tool_match = new_build` avec `build_score >= 1` — candidats backlog
- Onglet **"Stats"** : taux de réponse, revenu généré, meilleurs tools, meilleurs horaires

## Bot Telegram — messages d'alerte

Format d'alerte (score > 75) :

```
🎯 Mission score 87/100

💰 $45-65 | 📋 Translation | ⏱ 2h ago
📊 3 proposals déjà soumis

"Translate 280-page ebook from English to French, preserve layout"

🔧 Outil : Book Translator → livraison estimée 20 min
⚡ Concurrence faible — agis maintenant

🔗 [Voir la mission](url)
👉 /proposal_42 pour générer le texte
```

Commandes Telegram :
- `/proposal_{id}` → génère et envoie le proposal dans le chat Telegram
- `/stats` → résumé du jour (missions scrapées, alertes envoyées, proposals soumis)
- `/scan` → déclenche un scan immédiat sans attendre le cron

## Générateur de proposals — template de base

```
Hi [client_name or "there"],

I can complete this [X min/hours] — [raison courte liée à l'outil].

[Phrase sur l'expérience pertinente / preuve]

Deliverable: [format exact attendu] within [délai] of project start.

Happy to share a sample of similar work or answer any questions.

[Prénom]
```

GPT personnalise chaque proposal avec le contexte exact de la mission.

## Configuration (config.toml)

```toml
[scraper]
interval_hours = 2
categories = ["translation", "writing", "data-entry", "admin-support", "video-audio", "ai-services"]
min_budget = 15
max_proposals_threshold = 10  # ignorer missions avec > 10 proposals

[scoring]
alert_threshold = 75
weights = { feasibility = 0.4, urgency = 0.25, competition = 0.2, budget = 0.15 }

[telegram]
bot_token = ""  # depuis .env
chat_id = ""    # depuis .env

[openai]
model = "gpt-4o-mini"
```

## Fichiers

```
projects/freelance_arbitrage/
├── SPEC.md                    # ce fichier
├── config.toml                # configuration
├── requirements.txt
├── main.py                    # entry point : cron + orchestration
├── scrapers/
│   ├── __init__.py
│   ├── upwork.py              # scraper Upwork
│   ├── fiverr.py              # scraper Fiverr buyer requests
│   └── parser.py              # parser unifié → Mission dataclass
├── scorer/
│   ├── __init__.py
│   └── scorer.py              # GPT scoring batch
├── bot/
│   ├── __init__.py
│   └── telegram.py            # alertes + commandes /proposal /stats /scan
├── dashboard/
│   ├── __init__.py
│   └── app.py                 # Streamlit dashboard
└── data/
    └── missions.db            # SQLite (gitignored)
```

## Roadmap

**V1 (cette semaine)** : scraper Upwork + scorer GPT + alerte Telegram + dashboard Streamlit basique

**V2** : scraper Fiverr buyer requests + auto-submit Fiverr si score > 85 + tracking résultats

**V3** : Malt + PeoplePerHour + analytics "meilleur horaire de soumission" + A/B test proposals

## Notes

- Upwork bloque le scraping agressif → utiliser Playwright avec délais humains (2-5s entre pages) + rotation user-agent
- Fiverr buyer requests : section moins connue de Fiverr où les acheteurs postent leurs besoins — plus facile à scraper que les gigs
- Ne pas logguer les credentials Upwork/Fiverr dans le code — variables d'environnement uniquement
- SQLite suffit pour V1, migrer vers PostgreSQL si > 10k missions/semaine
