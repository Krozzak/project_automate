# Freelance Arbitrage Agent — Analyse de marché

*Créé : 2026-05-16 — basé sur recherche web + exploration technique*

---

## 1. État des plateformes en 2026

### Upwork — tendances de demande

| Catégorie | Croissance | Pertinence arbitrage |
|-----------|-----------|----------------------|
| AI Video Generation | +329% | ⭐⭐⭐ (Runway, Kling, Sora) |
| AI Integration (automation, agents) | +178% | ⭐⭐⭐ (scripts GPT, n8n) |
| Data Annotation / Labeling | +154% | ⭐⭐⭐ (Python batch) |
| Full Stack Development | stable fort | ⭐ (trop technique) |
| Virtual Assistance | stable fort | ⭐⭐⭐ (GPT scripts, résumés, emails) |
| Data Analytics | stable fort | ⭐⭐ (Python data cleaning) |
| Graphic Design | stable fort | ⭐ (créatif difficile à automatiser) |
| Translation & Localization | stable | ⭐⭐⭐⭐ (Book Translator = avantage direct) |
| Document Processing | croissance | ⭐⭐⭐⭐ (ProofLab = avantage direct) |
| Transcription / Sous-titres | stable | ⭐⭐⭐⭐ (Whisper = avantage direct) |

### Catégories Upwork à scraper (ordre de priorité)

1. **Translation & Localization** — missions "translate ebook french", "epub translation", "pdf translation" → Book Translator
2. **Document Processing / Admin Support** — missions "compare PDF", "PDF redline", "document comparison" → ProofLab
3. **Video & Audio** — missions "transcription", "subtitle", "captions" → Whisper
4. **Writing & Content** — missions "summarize", "extract key points", "write blog from notes" → GPT script
5. **Data Entry & Admin** — missions "clean csv", "extract from pdf", "format spreadsheet" → Python data
6. **AI Services** — missions "build chatbot", "automate workflow", "AI integration" → nouveau build rapide

### Fiverr — spécificités

- Section **Buyer Requests** : clients postent leurs besoins directement (moins compétitif, moins connue)
- Format plus court : budget + description + deadline
- Anti-bot plus agressif que Upwork mais scrapeable
- Volume plus faible mais missions plus simples (< 100$)

---

## 2. Cartographie arbitrage — Outil × Mission

| Mission type (Upwork/Fiverr) | Outil | Temps réel de livraison | Tarif marché | Marge opérationnelle |
|------------------------------|-------|------------------------|--------------|---------------------|
| "Translate 300-page ebook EN→FR" | Book Translator | 20-30 min | 45-80$ | ~95% |
| "Translate PDF with layout preserved" | Book Translator | 20 min | 25-50$ | ~95% |
| "Compare two versions of our contract PDF" | ProofLab | 5 min | 20-60$ | ~95% |
| "Find differences between V1 and V2 document" | ProofLab | 5 min | 15-40$ | ~95% |
| "Transcribe 1h interview audio" | Whisper | 10 min | 20-50$ | ~95% |
| "Generate subtitles SRT for video" | Whisper | 10 min | 15-40$ | ~95% |
| "Summarize 50-page report into 2 pages" | GPT script | 3 min | 15-30$ | ~95% |
| "Extract all prices from these 20 PDFs" | Python data | 10 min | 20-50$ | ~95% |
| "Clean and deduplicate this CSV (5k rows)" | Python data | 5 min | 15-35$ | ~95% |
| "Build simple AI chatbot for my website" | Nouveau build | 2-4h | 100-300$ | ~70% |

---

## 3. Architecture technique — Décisions

### Scraping Upwork

**Contrainte principale** : Upwork bloque agressivement le scraping non authentifié.
- RSS feeds : **discontinués août 2024** — ne plus utiliser
- API GraphQL : existe mais requiert auth + rate limit strict
- Scraping direct (requests/httpx) : bloqué par Cloudflare

**Solution retenue** : [calebmwelsh/Upwork-Job-Scraper](https://github.com/calebmwelsh/Upwork-Job-Scraper)
- Stack : **camoufox** (Firefox anti-detect) + **Playwright**
- Authentification : `.env` avec credentials Upwork réels
- Délais humains entre pages (2-5s aléatoires)
- Rotation user-agent via camoufox
- Output : CSV → on adapte pour alimenter SQLite

**Camoufox** = fork de Firefox qui spoofie les signaux de fingerprinting (WebGL, Canvas, fonts, navigator, screen). Meilleur anti-detect disponible en open source pour contourner Cloudflare.

### Scraping Fiverr

**Options :**
1. Playwright maison avec délais humains (effort : 1-2j)
2. `fiverr-api` PyPI (état incertain, dernière MAJ 2023)
3. **Apify actor `automation-lab/fiverr-scraper`** — via API, pas de maintenance côté nous

**Décision pour V1** : Apify actor Fiverr (API call, zéro maintenance) + Playwright maison pour Upwork. En V2, si Apify trop cher, on internalise le scraper Fiverr.

### Scoring

**Modèle** : `gpt-4o-mini` — batch scoring (envoyer plusieurs missions d'un coup)
- Coût estimé : ~0.01$ par batch de 10 missions
- Latence : < 3s pour 10 missions

### Alertes Telegram

- Bot via `python-telegram-bot` library
- Commandes : `/proposal_{id}`, `/stats`, `/scan`
- Format alerte : score + budget + délai + outil recommandé + lien

### Dashboard Streamlit

- Local uniquement (V1) — accès direct SQLite
- Tabs : Opportunités (triées score desc) / Discovery (new_build candidates) / Stats
- Boutons : Générer proposal → copier / Marquer soumis / Résultat

---

## 4. Roadmap de build

### V1 — Cette semaine (après le 23 mai)

**Objectif** : premier scan fonctionnel + alerte Telegram pour une mission réelle

| Étape | Fichier | Durée estimée |
|-------|---------|---------------|
| Setup projet + deps | `requirements.txt`, `config.toml` | 30 min |
| Scraper Upwork (camoufox) | `scrapers/upwork.py` | 3-4h |
| Parser unifié | `scrapers/parser.py` | 1h |
| Scorer GPT batch | `scorer/scorer.py` | 1h |
| Bot Telegram (alertes) | `bot/telegram.py` | 1h |
| Dashboard Streamlit V1 | `dashboard/app.py` | 2h |
| Intégration SQLite | tout | 1h |
| **Total V1** | | **~10h** |

### V2 — Semaine suivante

- Scraper Fiverr Buyer Requests (Apify)
- Générateur proposal dans Telegram (`/proposal_{id}`)
- Auto-submit Fiverr si score > 85

### V3 — Mois suivant

- Malt + PeoplePerHour
- Analytics "meilleur horaire de soumission"
- A/B test proposals

---

## 5. Points d'attention techniques

### Crédentials Upwork
- Ne JAMAIS logger les credentials dans le code
- Fichier `.env` gitignored
- camoufox gère les cookies de session → une seule connexion manuelle initiale, ensuite automatique

### Rate limiting
- Upwork : 2-5s entre chaque page, max 50 missions par scan
- Fiverr via Apify : géré côté Apify

### Coûts d'opération
| Composant | Coût |
|-----------|------|
| GPT-4o-mini scoring | ~0.001$/mission |
| Apify Fiverr scraper | ~5$/1000 résultats |
| Infrastructure | 0$ (local) |
| **Total par mois** | **< 10$** pour usage raisonnable |

### Démarrage
Pour le premier scan Upwork, il faut :
1. Créer un compte Upwork (si pas encore fait — prévu lundi 19)
2. Configurer `.env` avec email + mot de passe
3. Premier lancement manuel pour valider l'auth camoufox

---

## 6. Prochaine action immédiate

Créer la structure de fichiers et les dépendances → scraper Upwork en premier (plus de volume, cible principale).

```bash
cd d:/Projet_Automate/projects/freelance_arbitrage
pip install playwright camoufox python-telegram-bot streamlit openai python-dotenv toml
playwright install firefox
```

*Sources : calebmwelsh/Upwork-Job-Scraper (GitHub), Upwork Press Release 2026 skills demand, fiverr-api PyPI, Apify marketplace*
