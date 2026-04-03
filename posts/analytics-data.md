# LinkedIn Analytics — Source de vérité

> Généré le 2026-04-03 via export XLSX LinkedIn + corrections manuelles session /analyze-stats.
> Ce fichier servira à construire la page /analytics sur Ekenor.
> API LinkedIn Community Management : **en attente d'approbation** — sync automatique disponible dès approbation.

---

## Stats globales (snapshot 03/04/2026)

| Métrique | Valeur |
|---|---|
| Période | 04/01/2026 - 03/04/2026 |
| Impressions totales | 4807 |
| Membres uniques atteints | 866 |
| Followers au 03/04/2026 | 339 |
| Posts publiés (comptés) | 16 |
| Dernière sync | 2026-04-03 (XLSX manuel + corrections session) |
| Prochaine sync | via Workflow A dès API approuvée |

## Croissance followers

- Total au 03/04/2026 : 339
- Pics notables (top 5) : 17/03 +9, 09/03 +7, 08/03 +6, 18/03 +5, 04/02 +4
- Corrélation probable : pics 08-09/03 = deuxième vague should-i-buy-it ; pics 17-18/03 = ai-proof-job-scanner

## Démographie audience (snapshot 03/04/2026)

| Dimension | Top valeurs |
|---|---|
| Intitulés de poste | Responsable de projet (2.4%), Fondateur (2.1%), Ingénieur Full Stack (1.8%), Ingénieur logiciel (1.8%) |
| Localisations | Montréal (70.2%), Paris (5.0%), Toronto (3.2%), Yvetot (1.8%), Rouen (1.5%) |
| Séniorité | Expérimenté (38.9%), Premier emploi (26.5%), Directeur (7.4%), PDG (6.7%), Manager (5.5%) |
| Taille entreprise | +10 000 employés, 51-200, 1001-5000, 11-50, 201-500 |

---

## Moyennes de référence (calculées le 03/04/2026)

> Calculées sur 13 posts éligibles (age ≥ 7j, stats disponibles). Exclut : memory-logger (provisoire J+4), leak-claude-code (provisoire J+2).

| Métrique | Valeur | Base de calcul |
|---|---|---|
| EngagementRate moyen | 1.65% | 13 posts |
| Impressions moyennes (brutes) | 328 | 13 posts |
| ImpAdj7j moyen | 285 | 13 posts |
| Médiane ImpAdj7j | 245 | 13 posts |
| Seuil Tier A (ImpAdj7j) | > 382 | moy + 0.5σ |
| Seuil Tier C (ImpAdj7j) | < 188 | moy - 0.5σ |

---

## Posts (chronologique)

> ImpAdj7j = impressions × (7 / age_jours), capped à impressions brutes si age ≥ 56j.
> Flag : mature = age ≥ 56j | actif = 7-55j | provisoire = < 7j (exclu des moyennes).
> Interactions XLSX = likes + commentaires combinés (pas de breakdown disponible sans API).

| Date pub | Slug | Type | Impressions | Interactions | EngRate% | ImpAdj7j | Flag | Tier | linkedin_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-02-02 | ideas-logger-demo | AUTOMATISATION | 811 | 22 | 2.71 | 811 | mature | **A** | https://www.linkedin.com/feed/update/urn:li:activity:7424081686419857408 |
| 2026-02-09 | score-ice | MÉTA | 500 | 6 | 1.20 | 500 | mature | **A** |  https://www.linkedin.com/feed/update/urn:li:activity:7426618394608582658 |
| 2026-02-16 | loi-de-gall | RETOUR_EXP | 368 | 5 | 1.36 | 368 | mature | **A** | https://www.linkedin.com/feed/update/urn:li:activity:7429155092739690497 |
| 2026-02-23 | ego-depletion | RÉFLEXION | 245 | 5 | 2.04 | 245 | mature | B | https://www.linkedin.com/feed/update/urn:li:activity:7431691855224008704 |
| 2026-03-02 | todo-manager-demo | AUTOMATISATION | 160 | 1 | 0.63 | 160 | mature | C | https://www.linkedin.com/feed/update/urn:li:activity:7434228527006277632 |
| 2026-03-05 | savoir-quoi-faire | RÉFLEXION / BILAN | 474 | 9 | 1.90 | 474 | mature | **A** | https://www.linkedin.com/feed/update/urn:li:activity:7435315757825024001 |
| 2026-03-07 | pentagon-anthropic-openai | ACTUALITÉ | 190 | 1 | 0.53 | 190 | actif | B | https://www.linkedin.com/feed/update/urn:li:activity:7436063141509091328 |
| 2026-03-09 | should-i-buy-it | AUTOMATISATION | 306 | 6 | 1.96 | 306 | actif | B | https://www.linkedin.com/feed/update/urn:li:activity:7436750197331963904 |
| 2026-03-12 | friction-positive | RÉFLEXION | 107 | 1 | 0.93 | 107 | actif | C | https://www.linkedin.com/feed/update/urn:li:activity:7437837330511679489 |
| 2026-03-16 | ai-proof-job-scanner | AUTOMATISATION | 353 | 8 | 2.27 | 137 | actif | C | https://www.linkedin.com/feed/update/urn:li:activity:7439290652489740288 |
| 2026-03-19 | utility-vs-meaning | RÉFLEXION | 181 | 3 | 1.66 | 84 | actif | C | https://www.linkedin.com/feed/update/urn:li:activity:7440374086372929536 |
| 2026-03-23 | ekenor-lancement | AUTOMATISATION | 271 | 7 | 2.58 | 172 | actif | C | https://www.linkedin.com/feed/update/urn:li:activity:7441823643233435648 |
| 2026-03-26 | pourquoi-newsletter | OPINION | 176 | 3 | 1.70 | 154 | actif | C | https://www.linkedin.com/feed/update/urn:li:activity:7442910753302548481 |
| 2026-03-30 | memory-logger | AUTOMATISATION | 324 | 2 | 0.62 | 567 | **provisoire** | — | https://www.linkedin.com/feed/update/urn:li:activity:7444364062630703104 |
| 2026-04-01 | leak-claude-code | ACTUALITÉ | 258 | 0 | 0.00 | 903 | **provisoire** | — | https://www.linkedin.com/feed/update/urn:li:activity:7445098597164945409 |

> **Note ideas-logger-demo** : outlier structurel — premier post du compte, effet "félicitations de démarrage" du réseau. 811 imp non reproductibles dans ce contexte.
> **Note score-ice** : 2ème post du compte, bénéficie encore de l'effet nouveauté. 500 imp à pondérer.
> **Note leak-claude-code** : post spontané hors-calendrier (fait dans les transports, Grok + Nano Banana + Canva). 258 imp à J+2 = bon signal pour un post ACTUALITÉ improvisé. À réévaluer J+7.
> **Note memory-logger** : 324 imp à J+4, ImpAdj7j 567 = meilleur signal de momentum depuis ideas-logger. Premier post avec carousel explicatif (vs screenshot n8n). À confirmer J+7.
> **Note Lundi vs Jeudi** : corrélation type/slot — les posts Lundi sont majoritairement AUTOMATISATION, les Jeudi RÉFLEXION. La différence de perf (Lundi +90%) reflète peut-être le type plus que le slot.

---

## Classement ImpAdj7j au 03/04/2026

| Rang | Slug | ImpAdj7j | ER% | Tier | Note |
|---|---|---|---|---|---|
| — | leak-claude-code | 903 | 0.00 | [PROVISOIRE J+2] | hors-calendrier, 0 interactions |
| — | memory-logger | 567 | 0.62 | [PROVISOIRE J+4] | carousel, fort momentum |
| 1 | ideas-logger-demo | 811 | 2.71 | **A** | outlier premier post |
| 2 | score-ice | 500 | 1.20 | **A** | outlier 2ème post |
| 3 | savoir-quoi-faire | 474 | 1.90 | **A** | bilan perso + chiffres |
| 4 | loi-de-gall | 368 | 1.36 | **A** | |
| 5 | should-i-buy-it | 306 | 1.96 | B | humour + référence personnelle (chat) |
| 6 | ego-depletion | 245 | 2.04 | B | meilleur ER/imp ratio du top 6 |
| 7 | pentagon-anthropic-openai | 190 | 0.53 | B | ACTUALITÉ, ER faible |
| 8 | ekenor-lancement | 172 | 2.58 | C | **meilleur ER global** — récent, grandira |
| 9 | pourquoi-newsletter | 154 | 1.70 | C | récent |
| 10 | ai-proof-job-scanner | 137 | 2.27 | C | récent, bon ER |
| 11 | utility-vs-meaning | 84 | 1.66 | C | |
| 12 | todo-manager-demo | 35 | 0.63 | C | |
| 13 | friction-positive | 34 | 0.93 | C | post le moins distribué |

---

## Insights terrain (session 03/04/2026)

Ces observations viennent de retours directs et de perception qualitative — à croiser avec les stats futures.

- **Effet premier/deuxième post** : ideas-logger (811) et score-ice (500) bénéficient de l'effet nouveauté réseau. À ne pas compter dans les tendances reproductibles.
- **Humour + référence personnelle** : should-i-buy-it a généré du warm engagement (retours d'amis sur la référence au chat). Signal : les détails personnels inattendus créent de la complicité. Non mesurable via ER mais réel.
- **Posts concept purs** : friction-positive et utility-vs-meaning (RÉFLEXION abstraits sans ancrage personnel fort) = les 2 plus faibles du corpus. Signal clair.
- **Carousel vs screenshot n8n** : décision prise dès memory-logger — carousel explicatif workflow > screenshot technique. Plus accessible, meilleur rendu visuel.
- **Lien site dans le post** : ekenor.com pas encore connu de l'audience. Règle à tester : mettre le lien directement dans le post (pas en commentaire) pour favoriser la conversion vs le reach.
- **Stratégie 2 volets** : tester AUTOMATISATION en deux posts liés (ex: Memory Logger → Memory Logger Outputs). Double la fréquence AUTOMATISATION sans doubler le travail de création.

---

## Règles éditoriales actives

> Voir `.private/projects/productivity/linkedin_auto/WRITING_RULES.md` pour le détail complet.
> Lancer `/analyze-stats` pour calculer les verdicts des règles EN TEST.

### Verdicts calculés le 03/04/2026

**accroche-polarisante** : AMBIGUË (1+/1neutre/1−) — loi-de-gall ER 1.36% (neutre), ego-depletion 2.04% (+), friction-positive 0.93% (−). Résultat parasité : friction-positive est le post le moins distribué du corpus (107 imp), son ER faible peut refléter la distribution, pas la règle. → Étendre à 5 posts avant verdict.

**phrase-punch-finale** : VALIDÉE protocole (2/3+) — ego-depletion 2.04% (+), todo-manager 0.63% (−), savoir-quoi-faire 1.90% (+). Nuance terrain : peut aussi être une question SI elle est un vrai appel à l'action (pas question bateau). → En attente de confirmation formelle.

**accroche-chiffre-contraste** : EN COURS (2 posts + 1 provisoire) — savoir-quoi-faire 1.90% (+), utility-vs-meaning 1.66% (neutre), memory-logger provisoire. → Décision après J+7 memory-logger.

**angle-personnel-narratif** : EN COURS (1/3 posts) — memory-logger provisoire. → 2 posts supplémentaires requis.

**lien-site-dans-post** : À TESTER — nouvelle règle à partir du prochain post applicable.
