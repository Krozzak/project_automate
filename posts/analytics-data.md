# LinkedIn Analytics — Source de vérité

> Généré le 2026-05-11 via export XLSX LinkedIn + session /analyze-stats.
> Ce fichier servira à construire la page /analytics sur Ekenor.
> API LinkedIn Community Management : **en attente d'approbation** — sync automatique disponible dès approbation.
> Snapshots historiques : `posts/analytics/` (par date).

---

## Stats globales (snapshot 11/05/2026)

| Métrique | Valeur |
|---|---|
| Période | 12/05/2025 - 11/05/2026 |
| Impressions totales | 6 634 |
| Membres uniques atteints | 1 099 |
| Followers au 11/05/2026 | 382 (+18 vs 19/04) |
| Posts matchés | 22 (hors provisoire et MANUAL_CHECK non résolu) |
| Dernière sync | 2026-05-11 (XLSX manuel) |
| Prochaine sync | via Workflow A dès API approuvée |

## Croissance followers

- Total au 11/05/2026 : 382 (+18 vs 19/04, +43 vs 03/04)
- Pics notables (top 5) : 17/03 +9, 09/03 +7, 14/04 +7, 08/03 +6, 14/10 +6
- Corrélation probable : pics 08-09/03 = should-i-buy-it ; pics 17-18/03 = ai-proof-job-scanner ; 14/04 = Time Tracker posts ; croissance stable mai 2026 post-360Brew

## Démographie audience (snapshot 11/05/2026)

| Dimension | Top valeurs |
|---|---|
| Intitulés de poste | Responsable de projet (2.4%), Fondateur (2.1%), Ingénieur Full Stack (1.8%), Ingénieur logiciel (1.8%) |
| Localisations | Montréal (70.2%), Paris (5.0%), Toronto (3.2%), Yvetot (1.8%), Rouen (1.5%) |
| Séniorité | Expérimenté (38.9%), Premier emploi (26.5%), Directeur (7.4%), PDG (6.7%), Manager (5.5%) |
| Taille entreprise | +10 000 employés, 51-200, 1001-5000, 11-50, 201-500 |

---

## Moyennes de référence (calculées le 11/05/2026)

> Calculées sur 21 posts éligibles (age ≥ 7j, stats disponibles). Exclut : workflow-publication-claude-code (provisoire J+6).
> Posts algo1-360brew et km-graphe-custom absents du XLSX (publiés trop proches de la date d'export).

| Métrique | Valeur | Base de calcul |
|---|---|---|
| EngagementRate moyen | 1.62% | 20 posts (mythos exclu — interactions nulles) |
| ImpAdj7j moyen | 161 | 21 posts |
| Médiane ImpAdj7j | 163 | 21 posts |
| Écart-type ImpAdj7j | ~185 | 21 posts |
| Seuil Tier A (ImpAdj7j) | > 254 | moy + 0.5σ |
| Seuil Tier C (ImpAdj7j) | < 68 | moy - 0.5σ |

---

## Posts (chronologique)

> ImpAdj7j = impressions × (7 / age_jours), capped à impressions brutes si age ≥ 56j.
> Flag : mature = age ≥ 56j | actif = 7-55j | provisoire = < 7j (exclu des moyennes).
> Interactions XLSX = likes + commentaires combinés (pas de breakdown disponible sans API).

| Date pub | Slug | Type | Impressions | Interactions | EngRate% | ImpAdj7j | Flag | Tier | linkedin_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-02-02 | 2026-02-03-ideas-logger-demo | AUTOMATISATION | 818 | 22 | 2.69 | 818 | mature | **A** ⚠️ outlier | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_pendant-longtemps-je-navais-pas-un-probl%C3%A8me-ugcPost-7423871838407106560-K930 |
| 2026-02-09 | 2026-02-10-score-ice | MÉTA | 504 | 6 | 1.19 | 504 | mature | **A** ⚠️ outlier | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_la-semaine-derni%C3%A8re-jai-partag%C3%A9-comment-share-7426387664716783616-lp0D |
| 2026-02-16 | 2026-02-17-loi-de-gall | RETOUR_EXP | 371 | 5 | 1.35 | 371 | mature | **A** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_lia-g%C3%A9n%C3%A8re-vite-et-cest-le-pi%C3%A8ge-mon-ugcPost-7428966489354895360-5DCQ |
| 2026-02-23 | 2026-02-23-ego-depletion | RÉFLEXION | 248 | 5 | 2.02 | 248 | mature | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_la-discipline-cest-surfait-en-vrai-chaque-share-7431529416373014528-0smn |
| 2026-03-02 | 2026-03-02-todo-manager-demo | AUTOMATISATION | 163 | 1 | 0.61 | 163 | mature | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_lia-a-rendu-lex%C3%A9cution-accessible-%C3%A0-tout-ugcPost-7434071525500235776-wr0a |
| 2026-03-05 | 2026-03-05-savoir-quoi-faire | RÉFLEXION / BILAN | 475 | 9 | 1.89 | 475 | mature | **A** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_en-2025-javais-un-seul-projet-en-cours-share-7434073946594902016-QrTf |
| 2026-03-07 | 2026-03-07-pentagon-anthropic-openai | ACTUALITÉ | 193 | 1 | 0.52 | 193 | mature | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_quitgpt-share-7436057673466347520-FaCG |
| 2026-03-09 | 2026-03-09-should-i-buy-it | AUTOMATISATION | 371 | 8 | 2.16 | 371 | mature | **A** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_je-suis-sur-amazon-je-vois-un-truc-pour-ugcPost-7436539538065215488-Nj7b |
| 2026-03-12 | 2026-03-12-friction-positive | RÉFLEXION | 110 | 1 | 0.91 | 110 | mature | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_on-passe-son-temps-%C3%A0-supprimer-la-friction-share-7437685334953574401-qwW7 |
| 2026-03-16 | 2026-03-16-ai-proof-job-scanner | AUTOMATISATION | 361 | 8 | 2.22 | 361 | mature | **A** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_lia-va-transformer-ton-poste-la-question-ugcPost-7439285332115836929-n0yz |
| 2026-03-19 | 2026-03-19-utility-vs-meaning | RÉFLEXION | 197 | 3 | 1.52 | 197 | mature | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_jai-automatis%C3%A9-une-partie-de-mes-t%C3%A2ches-share-7440216527011770368--qdn |
| 2026-03-23 | 2026-03-23-ekenor-lancement | AUTOMATISATION | 299 | 7 | 2.34 | 43 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_jai-lanc%C3%A9-un-site-ce-nest-pas-un-blog-share-7441682022038683648-kjW5 |
| 2026-03-26 | 2026-03-26-pourquoi-newsletter | OPINION | 229 | 4 | 1.75 | 35 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_je-passe-mes-dimanches-matin-%C3%A0-discuter-de-share-7442545205934854144-ge-G |
| 2026-03-30 | 2026-03-30-memory-logger | AUTOMATISATION | 385 | 2 | 0.52 | 64 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_jai-essay%C3%A9-de-me-rappeler-dun-voyage-dil-ugcPost-7444358249165897728-V2Ii |
| 2026-04-01 | 2026-04-01-leak-claude-code | ACTUALITÉ | 373 | 1 | 0.27 | 65 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_r%C3%A9sum%C3%A9-des-meilleures-features-leaked-share-7445098596074524672-vUg7 |
| 2026-04-06 | 2026-04-06-time-tracker-estimation | AUTOMATISATION | 317 | 4 | 1.26 | 63 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_mon-manager-ma-dit-que-jestimais-toujours-ugcPost-7446595075729649664-Hezd |
| 2026-04-09 | 2026-04-09-time-tracker-dashboard | AUTOMATISATION | 125 | 2 | 1.60 | 27 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_dapr%C3%A8s-mon-time-tracker-je-sous-estime-ugcPost-7447625403311095808-HXhZ |
| 2026-04-13 | 2026-04-13-mythos-anthropic | ACTUALITÉ | 114 | — | — | 29 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_les-%C3%A9quipes-marketing-danthropic-devraient-share-7449580233109749760-10Qr |
| 2026-04-16 | 2026-04-16-retard-de-phase | OPINION | 93 | 2 | 2.15 | 26 | actif | **C** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_dans-la-tech-une-innovation-sort-toutes-share-7450521427839143936-X6oI |
| 2026-04-20 | 2026-04-20-proofslab-approbation-visuels | AUTOMATISATION | 370 | 12 | 3.24 | 123 | actif | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_proofslab-approbation-pdf-avant-impression-ugcPost-7451745014809927681-WGbo |
| 2026-04-24 | 2026-04-24-claude-design-proofslab | ACTUALITÉ | 226 | 5 | 2.21 | 93 | actif | **B** | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_analyse-claude-design-ugcPost-7453208352551268353-S0Y_ |
| 2026-05-05 | 2026-05-05-workflow-publication-claude-code | AUTOMATISATION | 162 | 5 | 3.09 | 189 | **provisoire** J+6 | — | https://www.linkedin.com/posts/thomas-silliard-4b7b8a1b1_en-3-mois-jai-publi%C3%A9-24-posts-linkedin-ugcPost-7457428568499888128-uVIX |
| 2026-05-08 | 2026-05-08-algo1-360brew | AUTOMATISATION | — | — | — | — | absent export | — | |
| 2026-05-12 | 2026-05-12-km-graphe-custom | AUTOMATISATION | — | — | — | — | absent export | — | |

> **Note ideas-logger-demo** : outlier structurel — premier post du compte, effet "félicitations de démarrage" du réseau. Non reproductible.
> **Note score-ice** : 2ème post du compte, bénéficie encore de l'effet nouveauté.
> **Note memory-logger** : ImpAdj7j stabilisé à 64 (actif 42j) — impressions brutes 385 mais distribution lente.
> **Note leak-claude-code** : ImpAdj7j stabilisé à 65 (actif 40j). Post ACTUALITÉ hors-calendrier = distribution limitée.
> **Note ekenor-lancement** : fort ER (2.34%) mais ImpAdj7j 43 — algo pénalise lien site dans le corps.
> **Note proofslab-approbation-visuels** : meilleur ER du corpus (3.24%) avec ImpAdj7j 123. Signal audience qualifiée.
> **Note mythos-anthropic** : interactions = 0 dans XLSX — probablement données incomplètes, ER non calculable.
> **Note Lundi vs Jeudi** : corrélation type/slot — les posts Lundi sont majoritairement AUTOMATISATION, les Jeudi RÉFLEXION. La différence de perf (Lundi +90%) reflète peut-être le type plus que le slot.

---

## Classement ImpAdj7j au 11/05/2026

| Rang | Slug | ImpAdj7j | ER% | Tier | Note |
|---|---|---|---|---|---|
| [PROVISOIRE J+6] | workflow-publication-claude-code | 189 | 3.09% | — | à confirmer ~12/05 |
| 1 | ideas-logger-demo | 818 | 2.69% | **A** | outlier premier post |
| 2 | score-ice | 504 | 1.19% | **A** | outlier 2ème post |
| 3 | savoir-quoi-faire | 475 | 1.89% | **A** | bilan perso + chiffres |
| 4 | loi-de-gall | 371 | 1.35% | **A** | |
| 5 | should-i-buy-it | 371 | 2.16% | **A** | humour + référence personnelle |
| 6 | ai-proof-job-scanner | 361 | 2.22% | **A** | bon ER + distribution forte |
| 7 | ego-depletion | 248 | 2.02% | **B** | |
| 8 | utility-vs-meaning | 197 | 1.52% | **B** | |
| 9 | pentagon-anthropic-openai | 193 | 0.52% | **B** | ACTUALITÉ, ER faible |
| 10 | todo-manager-demo | 163 | 0.61% | **B** | |
| 11 | proofslab-approbation-visuels | 123 | 3.24% | **B** | **meilleur ER du corpus** |
| 12 | friction-positive | 110 | 0.91% | **B** | post le moins distribué corpus |
| 13 | claude-design-proofslab | 93 | 2.21% | **B** | |
| 14 | memory-logger | 64 | 0.52% | **C** | impressions brutes 385 — distribution lente |
| 15 | leak-claude-code | 65 | 0.27% | **C** | hors-calendrier, ER faible |
| 16 | time-tracker-estimation | 63 | 1.26% | **C** | lien-site-dans-post testé |
| 17 | ekenor-lancement | 43 | 2.34% | **C** | fort ER — algo pénalise lien site |
| 18 | pourquoi-newsletter | 35 | 1.75% | **C** | OPINION sans ancrage projet |
| 19 | time-tracker-dashboard | 27 | 1.60% | **C** | |
| 20 | mythos-anthropic | 29 | — | **C** | interactions nulles XLSX |
| 21 | retard-de-phase | 26 | 2.15% | **C** | impressions faibles (93) |

---

## Insights terrain (session 11/05/2026)

- **Effet premier/deuxième post** : ideas-logger (818) et score-ice (504) bénéficient de l'effet nouveauté réseau. À ne pas compter dans les tendances reproductibles.
- **Humour + référence personnelle** : should-i-buy-it a généré du warm engagement (retours d'amis sur la référence au chat). Signal : les détails personnels inattendus créent de la complicité. Non mesurable via ER mais réel.
- **Posts concept purs** : friction-positive et utility-vs-meaning (RÉFLEXION abstraits sans ancrage personnel fort) = parmi les plus faibles du corpus. Signal clair.
- **Carousel vs screenshot n8n** : décision prise dès memory-logger — carousel explicatif workflow > screenshot technique. Plus accessible, meilleur rendu visuel.
- **Lien site dans le post** : pénalise la distribution (ekenor-lancement ImpAdj7j 43 malgré ER 2.34%). Règle en test.
- **ER élevé post-360Brew** : proofslab (3.24%) et claude-design (2.21%) = les 2 meilleurs ER du corpus. L'audience devient plus qualifiée même si la distribution baisse. Signal de ciblage 360Brew qui fonctionne.
- **Posts actifs récents (mars-avril)** : ImpAdj7j systématiquement bas (26-65) malgré impressions brutes correctes (93-385) — la distribution s'est stabilisée plus lentement que prévu.

---

## Règles éditoriales actives

> Voir `.private/projects/productivity/linkedin_auto/WRITING_RULES.md` pour le détail complet.
> Lancer `/analyze-stats` pour calculer les verdicts des règles EN TEST.

### Verdicts calculés le 11/05/2026

**phrase-punch-finale** : ✅ VALIDÉE (2/3+, protocole atteint) — ego-depletion 2.02% (+24%), todo-manager 0.61% (−62%), savoir-quoi-faire 1.89% (+17%). Nuance : todo-manager 163 imp, ER bas peut refléter distribution autant que règle.

**accroche-chiffre-contraste** : ❌ INVALIDE (1+/2−, 3/3 posts) — savoir-quoi-faire 1.89% (+), utility-vs-meaning 1.52% (−), memory-logger 0.52% (−). Déplacée en Règles Abandonnées.

**accroche-polarisante** : AMBIGUË (2+/1neutre/1−/1absent export) — ego-depletion 2.02% (+), retard-de-phase 2.15% (+), loi-de-gall 1.35% (neutre), friction-positive 0.91% (− ⚠️ parasité), algo1-360brew absent XLSX. → Verdict final après prochain export.

**angle-personnel-narratif** : AMBIGUË (1+/1neutre/1−) — retard-de-phase 2.15% (+), time-tracker-estimation 1.26% (neutre), memory-logger 0.52% (−). → Continuer sur 2 posts supplémentaires (loreal-mirage-urgence = candidat naturel).

**lien-site-dans-post** : EN TEST (1/3 posts) — time-tracker-estimation 1.26% (neutre). → Continuer sur 2 prochains posts avec lien ekenor.com.

**chiffres-cote-a-cote** : EN TEST (1/3 mesurable) — proofslab-approbation-visuels 3.24% (+). mythos-anthropic interactions nulles = non comptabilisé. → 2 posts restants avant verdict.

**cta-mot-cle-commentaire** : PROVISOIRE — workflow-publication-claude-code J+6 au 11/05. → Verdict à confirmer lors du prochain export.
