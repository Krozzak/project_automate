# Référentiel des règles d'écriture LinkedIn

> **Protocole** : 1 règle changée max par post. 3 posts min pour valider.
> Critère validation : 2/3 posts au-dessus de la moyenne historique (EngagementRate).
> Mis à jour automatiquement par le hook post-session `/write-post`.
>
> **Distinction avec la ligne éditoriale** :
> - `.private/LIGNE_EDITORIALE.md` = ton, voix, identité, ce qu'on évite (QUI tu es)
> - `WRITING_RULES.md` = techniques narratives testées et mesurées (COMMENT tu écris)
> Les règles ici sont empiriques — elles viennent des stats et des sessions d'écriture, pas des principes.

---

## Règles VALIDÉES ✅

Ces règles sont appliquées dans TOUS les posts. Ne pas les changer.

### voix-vecue-pas-pattern
**Statut** : VALIDÉE
**Formulation** : Ne jamais écrire depuis les features ou la structure du projet — écrire depuis l'expérience vécue. Demander à Thomas : comment il a vécu le problème, avec ses mots, ses chiffres, sa mécanique mentale. La V1 sans cette info produit un post "LinkedIn générique" reconnaissable (même structure que tout le monde). La V2 avec cette info produit quelque chose qui sonne naturel et personnel.
**Hypothèse** : Si le post part du vécu exact (chiffres réels, formulation personnelle, logique interne), alors il est indétectable comme post IA et s'identifie immédiatement comme authentique
**Ajoutée le** : 2026-04-05 (session TT.1 — V1 trop générique, V3 validée après 3 itérations)
**Posts testés** : 1 / 3
**Conclusion** : V1 TT.1 = pattern standard reconnaissable. V3 = voix personnelle après que Thomas a fourni : chiffre concret (2h→3-4h), mécanique mentale (temps brut idéal), logique de l'outil (coef×1). Ces 3 éléments ne sont pas dérivables du projet — il faut les demander.

### structure-3-actes
**Statut** : VALIDÉE
**Formulation** : Chaque post suit une structure à 3 actes adaptée au type (Problème → Solution → Résultat pour AUTOMATISATION ; Observation → Concept → Implication pour RÉFLEXION ; Chronologie → Lectures cachées → Insight pour ACTUALITÉ)
**Hypothèse** : Si la structure est cohérente avec le type de post, alors le lecteur suit le raisonnement sans effort
**Ajoutée le** : 2026-02-03 (post : ideas-logger-demo)
**Posts testés** : 10 / 3
**Conclusion** : Appliquée dans tous les posts depuis le début. Variations intentionnelles uniquement sur le type de clôture (question vs phrase punch), jamais sur la structure de base.

### max-2-takeaways
**Statut** : VALIDÉE
**Formulation** : Maximum 2 points indépendants par post — le reste va dans le backlog
**Hypothèse** : Si le post n'a qu'un message central clair, alors le lecteur le retient
**Ajoutée le** : 2026-02-03 (post : ideas-logger-demo)
**Posts testés** : 10 / 3
**Conclusion** : Jamais dépassé. Toutes les reformulations de posts trop chargés ont amélioré la clarté.

### sourcing-naturalisé
**Statut** : VALIDÉE
**Formulation** : Sourcer les concepts dans le flux (Nom + Époque + Contexte), jamais entre parenthèses ni comme citation d'expert
**Hypothèse** : Si le sourcing est narratif, alors le concept s'intègre sans casser le rythme
**Ajoutée le** : 2026-02-10 (post : score-ice)
**Posts testés** : 7 / 3
**Conclusion** : "Sean Ellis, le gars derrière le Growth Hacking" > "(Sean Ellis, 1970)". Appliqué systématiquement dans les posts à concept.

### récit-personnel-spécifique
**Statut** : VALIDÉE
**Formulation** : Nommer les vrais projets, les vrais chiffres, les vraies situations — jamais d'exemple générique
**Hypothèse** : Si on cite des détails réels (Twerk, Ideas Logger, le chat sur Amazon), alors le lecteur perçoit l'authenticité
**Ajoutée le** : 2026-02-03 (post : ideas-logger-demo)
**Posts testés** : 10 / 3
**Conclusion** : Présent dans tous les posts. Les reformulations qui généralisaient perdaient de l'authenticité.

### accroche-3-lignes
**Statut** : VALIDÉE
**Formulation** : L'accroche doit tenir en 3 lignes max (visible avant "voir plus" sur LinkedIn) et contenir le message principal ou la tension
**Hypothèse** : Si le lecteur voit la valeur dans les 3 premières lignes, alors il clique "voir plus"
**Ajoutée le** : 2026-02-03 (post : ideas-logger-demo)
**Posts testés** : 10 / 3
**Conclusion** : Toutes les reformulations d'accroche trop longues ont été raccourcies. Règle non négociable.

### concept-seulement-si-il-colle
**Statut** : VALIDÉE
**Formulation** : Ne pas plaquer un concept sur un message qui ne le demande pas — si le lien est forcé, enlever le concept
**Hypothèse** : Si le concept répond exactement au message central, alors il renforce. Sinon, il dilue.
**Ajoutée le** : 2026-03-05 (post : savoir-quoi-faire — Gollwitzer retiré après rédaction)
**Posts testés** : 4 / 3
**Conclusion** : Gollwitzer avait été rédigé puis retiré du post bilan car le lien était forcé. Validé : le post sans concept était plus fort.

### pas-de-teasing
**Statut** : VALIDÉE
**Formulation** : Ne jamais terminer par un teasing vers le prochain post ou le prochain mois
**Hypothèse** : Si la fin est nette et autonome, alors le post tient seul
**Ajoutée le** : 2026-02-17 (post : loi-de-gall — retiré du rewriting)
**Posts testés** : 8 / 3
**Conclusion** : Les quelques teasings essayés en mois 1 ont été supprimés au rewriting. Cohérent avec "pas de CTA".

---

## Règles EN TEST 🧪

### angle-personnel-narratif
**Statut** : EN TEST (2/3 posts)
**Formulation** : Partir d'une tension personnelle vécue plutôt que d'une présentation de projet — le post raconte quelque chose, il ne liste pas des features
**Hypothèse** : Si le post part d'une expérience personnelle concrète (une frustration, une époque, une décision), alors le lecteur s'identifie avant de s'intéresser au projet
**Ajoutée le** : 2026-03-22 (posts : ekenor-lancement + pourquoi-newsletter — E.1 sert de contrôle descriptif, E.2 de test narratif)
**Posts testés** : 2 / 3

| Post | EngagementRate | vs moyenne (1.65%) | Verdict |
| --- | --- | --- | --- |
| 2026-03-30-memory-logger | 0.62% | provisoire J+4 | provisoire |
| 2026-04-06-time-tracker-estimation | — | — | à mesurer |
| prochain post applicable | — | — | à faire |

**Conclusion** : memory-logger provisoire. 2 posts supplémentaires requis.

### lien-site-dans-post
**Statut** : EN TEST (1/3 posts)
**Formulation** : Inclure le lien ekenor.com directement dans le corps du post (pas en commentaire) — placé naturellement à la fin ou dans un CTA explicite
**Hypothèse** : Si le lien est dans le post, alors plus de personnes cliquent (conversion > reach) — l'algorithme peut légèrement pénaliser la distribution mais le trafic site augmente
**Ajoutée le** : 2026-04-03 (décision session /analyze-stats — audience ne connaît pas encore le site)
**Posts testés** : 1 / 3

| Post | EngagementRate | vs moyenne | Verdict |
| --- | --- | --- | --- |
| 2026-04-06-time-tracker-estimation | — | — | à mesurer |
| prochain post applicable | — | — | à faire |
| prochain post applicable | — | — | à faire |

**Conclusion** : Premier test sur TT.1 (Time Tracker). Lien placé naturellement avant la phrase punch finale. Résultat à mesurer J+7.

---

Ces règles sont en cours d'évaluation. Appliquer celle qui est EN TEST dans les prochains posts, noter le résultat.

### accroche-polarisante
**Statut** : EN TEST (résultat AMBIGUË — étendre à 5 posts)
**Formulation** : Commencer par une affirmation intentionnellement contre-intuitive ou polarisante (qui semble fausse) pour forcer la lecture de la nuance. Règle **contextuelle** — s'applique seulement si le contenu du post offre naturellement un angle contre-intuitif. Ne pas forcer si l'angle n'est pas là.
**Hypothèse** : Si l'accroche crée une tension cognitive ("c'est faux, je veux savoir pourquoi"), alors le taux de lecture complète augmente
**Ajoutée le** : 2026-02-17 (post : loi-de-gall — "L'IA génère vite. Et c'est le piège.")
**Posts testés** : 3 / 5 (2 posts supplémentaires requis)

| Post | EngagementRate | vs moyenne (1.65%) | Verdict |
| --- | --- | --- | --- |
| 2026-02-17-loi-de-gall | 1.36% | −17% (dans la moy.) | neutre |
| 2026-02-23-ego-depletion | 2.04% | +24% | + |
| 2026-03-12-friction-positive | 0.93% | −44% | − ⚠️ parasité (107 imp, post le moins distribué) |
| prochain post applicable | — | — | à faire |
| prochain post applicable | — | — | à faire |

**Conclusion** : Résultat AMBIGUË. friction-positive est le post le moins distribué du corpus (107 imp) — son ER faible peut refléter la distribution, pas la règle. Étendre à 5 posts avant verdict.

### phrase-punch-finale
**Statut** : EN TEST (verdict 2/3 atteint — confirmation en cours)
**Formulation** : Terminer par une phrase distillée (1-2 lignes) qui résume l'insight. Peut aussi être une question SI elle appelle une vraie réponse ou un vrai CTA — jamais une question bateau sans attente de réponse.
**Hypothèse** : Si la fin est une formule mémorable ou un appel concret, alors le lecteur retient l'idée ou interagit
**Ajoutée le** : 2026-02-23 (post : ego-depletion — "Un bon système ne fatigue pas. Il te permet d'aller plus loin." — premier test, simultané avec accroche-polarisante)
**Formalisée le** : 2026-03-02 (post : todo-manager-demo — test isolé, sans accroche-polarisante simultanée)
**Posts testés** : 3 / 3

| Post | EngagementRate | vs moyenne (1.65%) | Verdict |
| --- | --- | --- | --- |
| 2026-02-23-ego-depletion | 2.04% | +24% | + |
| 2026-03-02-todo-manager-demo | 0.63% | −62% | − |
| 2026-03-05-savoir-quoi-faire | 1.90% | +15% | + |

**Conclusion** : Protocole 2/3 atteint. Verdict en attente de confirmation formelle. Nuance : todo-manager-demo n'avait que 160 impressions (distribution faible), son ER bas peut refléter la distribution autant que la règle.

### accroche-chiffre-contraste
**Statut** : EN TEST (décision après J+7 memory-logger ~06/04/2026)
**Formulation** : Ouvrir avec un contraste chiffré vérifiable (avant/après, ratio, timeline) qui prouve le message sans le dire
**Hypothèse** : Si l'accroche contient une preuve par les chiffres, alors la crédibilité est établie dès la ligne 1 — sans avoir à affirmer quoi que ce soit
**Ajoutée le** : 2026-03-05 (post : savoir-quoi-faire — "En 2025 j'avais 1 projet. En 2026, j'en ai construit 6 en moins de 3 mois.")
**Posts testés** : 3 / 3

| Post | EngagementRate | vs moyenne (1.65%) | Verdict |
| --- | --- | --- | --- |
| 2026-03-05-savoir-quoi-faire | 1.90% | +15% | + |
| 2026-03-19-utility-vs-meaning | 1.66% | +1% (dans la moy.) | neutre |
| 2026-03-30-memory-logger | 0.62% | provisoire J+4 | provisoire |

**Conclusion** : 2 posts confirmés (1+/1neutre), memory-logger provisoire. Décision après ~06/04/2026.

---

## Règles ARCHIVÉES ❌

_(vide — aucune règle invalidée à ce jour)_

---

## Variations connues (pas des règles — des adaptations par type)

Ces patterns sont des **adaptations contextuelles**, pas des règles à tester. Ils décrivent comment le style varie naturellement selon le type de post.

| Dimension | AUTOMATISATION | RÉFLEXION / BILAN | ACTUALITÉ |
| --- | --- | --- | --- |
| Clôture | Question finale ou CTA concret | Phrase punch | Fin ouverte, pas de question |
| Emojis | Rares ou absents | Absents | Absents |
| Longueur | 140-200 mots | 250-300 mots | Court (teaser) + long (newsletter) |
| Ton | "Je" pur, démonstratif | "Je" ou universel, réflexif | Analytique, pas de "je" |
| Visuel | Carousel 3 slides : (1) contraste/chiffres, (2) workflow, (3) output — fond `#f5f5f5`, logo ekenor.com bas gauche via Canva | 1 image conceptuelle | Illustration rare ou aucun |
| Concept sourcé | Rarement (pragmatique) | Souvent (si naturel) | Multi-niveaux ou aucun |

---

## Moyenne historique de référence

> À mettre à jour après chaque sync stats (Workflow A Stats Collector).

| Métrique | Valeur actuelle | Calculée sur N posts |
| --- | --- | --- |
| EngagementRate moyen | — | 0 posts avec stats |
| Impressions moyennes | — | 0 posts avec stats |
| Likes moyens | — | 0 posts avec stats |

_Note : Ideas Logger (post 1) avait 772 impressions / 18 réactions. Score ICE : 461 impressions / 4 réactions. Ces données sont partielles — remplir via Workflow A._

---

## Historique des décisions

| Date | Décision | Post déclencheur | Impact |
| --- | --- | --- | --- |
| 2026-03-20 | Initialisation du référentiel à partir de l'analyse des 10 premiers posts | — | — |
| 2026-03-20 | Post RÉFLEXION utility-vs-meaning — question finale choisie sur phrase punch (sujet ouvert) | utility-vs-meaning | accroche-chiffre-contraste : 2/3 posts |
| 2026-03-30 | Format carousel AUTOMATISATION fixé : 3 slides (contraste → workflow → output), fond `#f5f5f5`, logo ekenor.com bas gauche — template Canva réutilisable | memory-logger | Appliqué à tous les futurs posts AUTOMATISATION |
| 2026-04-03 | Idée à tester (manuel d'abord) : "commente WORKFLOW → je t'envoie le workflow en DM" — booste engagement algo + leads qualifiés. Si traction : automatiser via ManyChat | — | — |
| 2026-04-03 | Session /analyze-stats : phrase-punch-finale → verdict 2/3 atteint, en attente confirmation formelle. Nuance : peut aussi être question si vrai CTA | — | — |
| 2026-04-03 | accroche-polarisante → AMBIGUË, étendre à 5 posts. friction-positive (107 imp) possiblement parasité — résultat non concluant | — | — |
| 2026-04-03 | Nouvelle règle EN TEST : lien-site-dans-post — ekenor.com directement dans le corps, pas en commentaire | — | — |
| 2026-04-03 | Décision carousel : carousel explicatif workflow > screenshot n8n pour posts AUTOMATISATION — appliqué dès memory-logger | memory-logger | Standard visuel carousel fixé |
| 2026-04-03 | Stratégie 2 volets testée : AUTOMATISATION en input + output (ex: memory-logger → memory-logger-outputs) — double la fréquence sans doubler le travail | — | — |
| 2026-04-03 | Observation terrain : humour + référence personnelle concrète (chat dans should-i-buy-it) génère du warm engagement non capturé par ER | should-i-buy-it | À réutiliser intentionnellement |
| 2026-03-30 | Supprimer le bloc explicatif scientifique (Ebbinghaus/Roediger) — le flux narratif portait déjà l'idée, la parenthèse cassait le rythme | memory-logger | Règle déjà couverte par concept-seulement-si-il-colle |
| 2026-03-05 | Lâcher Gollwitzer (lien forcé) → valide la règle concept-seulement-si-il-colle | savoir-quoi-faire | Post plus fort sans le concept |
| 2026-03-02 | Test phrase punch finale au lieu de question | todo-manager-demo | En attente de stats |
| 2026-02-17 | Test accroche polarisante | loi-de-gall | En attente de stats |
