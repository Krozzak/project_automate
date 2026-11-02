# sync-concepts

Crée les fiches de connaissance (concepts, auteurs, livres) du site Ekenor avec leurs compagnons (motion design, photo), puis met à jour `_graph.json`. Chaque création se termine par une vérification.

## Contexte

- Site Ekenor : `d:/Projet_Newsletter_Hub/` (GitHub `Krozzak/ekenor`) — **lire son `CLAUDE.md` avant d'écrire** (section « Collection concepts »)
- Index graphe : `d:/Projet_Newsletter_Hub/src/content/concepts/_graph.json`
- Fiches : `d:/Projet_Newsletter_Hub/src/content/concepts/*.md` — FR `[sharedSlug].md`, EN `[sharedSlug]-en.md`
- Types supportés : `concept` (défaut), `author`, `book` — champ `knowledgeType` dans le frontmatter
- Charte v2 du site : `docs/DESIGN_SYSTEM.md`, `docs/MOTION_CONCEPTS.md`, `src/components/concepts-v2/`. Si la branche courante ne les a pas encore (refonte pas fusionnée), les lire avec `git show <branche>:docs/MOTION_CONCEPTS.md` et travailler sur une branche qui contient `src/components/concepts-v2/motion/_Frame.astro`.
- Script de vérification : `d:/Projet_Automate/projects/knowledge_curator/scripts/check-ekenor-concepts.mjs`
- Ce skill est versionné dans `d:/Projet_Automate/.claude/commands/sync-concepts.md` ; la commande globale `~/.claude/commands/sync-concepts.md` n'est qu'un renvoi vers ce fichier. Modifier uniquement la version du repo.

## Règles permanentes

### R1 — Références croisées : toujours le `sharedSlug`, jamais `-en`

Dans `relatedConcepts`, `relatedProjects`, `relatedArticles` et `citedBy`, on écrit **toujours le `sharedSlug`, sans suffixe `-en`**, y compris dans les fichiers anglais (`*-en.md`). Le suffixe `-en` sert seulement au nom de fichier.

- ✅ `"specific-knowledge"` — ❌ `"specific-knowledge-en"`
- Pourquoi : une référence en `-en` ne se résout pas, la fiche liée disparaît des pages EN (bug de novembre 2026 : 1 293 références cassées sur 173 fiches).
- Le frontmatter EN est une copie du FR (seuls `lang`, `title`, `summary` et le corps changent) : ne jamais « traduire » les slugs.

### R2 — Motion design sur mesure pour chaque nouvelle fiche concept

Toute nouvelle fiche `knowledgeType: concept` arrive avec son infographie animée, créée **en même temps** que la fiche : `src/components/concepts-v2/motion/<sharedSlug>.astro` dans le repo du site. Découverte automatique : aucun champ à ajouter dans le frontmatter.

**`docs/MOTION_CONCEPTS.md` existe : le suivre** (anatomie du composant, cadre `_Frame.astro`, classes du kit `_kit.css`, checklist §7). Lire au moins `loi-de-gall.astro` et un autre exemple avant d'écrire. Points non négociables :

- Une petite infographie qui fait comprendre et retenir **ce** concept : 3 à 6 éléments, une boucle de 8 à 12 s (`--fxs-dur`) qui raconte un mini-récit **avant → mécanisme → résultat**, puis tient l'état final. Toujours dessinée pour la fiche, jamais un gabarit. Référence : la Loi de Gall (V1 → +1 → +2 → V3, chaque étape validée par une coche, puis « conçu d'un coup : ne marche pas »).
- SVG `viewBox 0 0 560 300` (fourni par `_Frame`), animations **en CSS uniquement**, keyframes préfixées par une abréviation du slug (`fxs-<abrév>-`, ex. `fxs-lt-` pour `long-term-games`).
- Palette de la charte (`docs/DESIGN_SYSTEM.md`) via les classes du kit, jamais d'hex en dur : encre `#0F1117` (`fxs-ink`), accent sarcelle `#1F7A6E` (`fxs-line`, `fxs-acc`), vert `#15803D` (`fxs-good`), rouge `#B91C1C` (`fxs-bad`), couleur de la famille en touche. Aucun émoji, aucun dégradé décoratif, aucune ombre.
- État de base = état final : avec « réduire les animations », l'image reste complète et lisible. La vignette (`thumb`) doit rester lisible sans libellés.
- Tous les libellés dans `TEXT`, en `{ fr, en }` ; `aria` = une phrase qui résume l'idée (pas « animation de… ») ; `caption` = une phrase.
- **Aucun chiffre inventé** : une valeur n'apparaît que si elle est dans la fiche et sa source, sinon elle est marquée « exemple ».

Si `docs/MOTION_CONCEPTS.md` n'existe pas sur la branche de travail ni ailleurs, appliquer ces mêmes points directement (SVG 560×300, couleurs ci-dessus en hex).

### R3 — Fiche auteur : photo libre ou rien

Pour une fiche `knowledgeType: author`, chercher une photo **libre**, sur Wikimedia Commons d'abord.

1. Licences acceptées : domaine public, CC0, CC BY, CC BY-SA. **Refusées** : NC, ND, « fair use », « tous droits réservés ». Lire la licence sur la page du fichier (ou via l'API : `https://commons.wikimedia.org/w/api.php?action=query&titles=File:<nom>&prop=imageinfo&iiprop=url|extmetadata&format=json` → `LicenseShortName`, `LicenseUrl`, `Artist`).
2. Si le fichier vient de Flickr (mention Flickr dans la source ou modèle de revue Flickr), ouvrir aussi la page Flickr d'origine et **noter la licence actuelle sur Flickr** dans le résumé final et le message de commit.
3. Télécharger l'original dans un dossier temporaire neuf, le regarder, puis recadrer en **carré centré sur le visage**, 480 × 480 px (Pillow : `crop` → `resize((480, 480), Image.LANCZOS)`). Enregistrer `public/concepts/<sharedSlug>/photo.jpg` (qualité ~85) et `photo.webp`. Regarder le résultat avant de continuer.
4. Frontmatter **FR et EN** (mêmes valeurs sauf le crédit, dans la langue du fichier) :
   ```yaml
   photo: "/concepts/<sharedSlug>/photo.jpg"
   photoCredit: "Photo : <auteur>, <licence>, via Wikimedia Commons (recadrée)"   # EN : "Photo: <author>, <licence>, via Wikimedia Commons (cropped)"
   photoSource: "https://commons.wikimedia.org/wiki/File:…"
   photoLicenseUrl: "https://creativecommons.org/licenses/by-sa/2.0/"
   ```
5. **Pas de photo libre** : ne mettre **aucun** champ photo (le site affiche les initiales dans un cercle pointillé). Jamais de photo « trouvée » sur un site de presse, d'éditeur ou un réseau social.

### R4 — Fiche livre : pas de couverture sans droits

Une couverture seulement si elle est sous licence libre ou avec une autorisation écrite. Sinon, **aucun champ de couverture** : le site affiche une tuile typographique (titre, auteur, année tirés de `origin`). Ne jamais reprendre une couverture de libraire, d'éditeur ou d'Open Library comme si elle était libre.

État actuel du site : le schéma n'a pas de champ `cover` et le site n'affiche **jamais** de couverture (`CLAUDE.md`). Donc ne rien ajouter (ni `cover`, ni `coverImage`) sur une fiche livre ; si une couverture libre ou autorisée existe, la signaler dans le résumé (licence + URL + preuve) pour décision.

### R5 — Graphe : `sharedSlug` et type

Dans `_graph.json`, chaque `slug` et chaque entrée de `relatedConcepts` est un `sharedSlug` (sans `-en`), et chaque nœud porte son `type` (`concept`, `author` ou `book` pour les fiches ; les nœuds `article` / `project` existants gardent le leur). Le `type` = le `knowledgeType` de la fiche.

## Instructions

### Préalable — Mettre à jour le repo du site

Avant toute lecture ou écriture, remettre `main` à jour dans `d:/Projet_Newsletter_Hub` :

```bash
cd d:/Projet_Newsletter_Hub
git fetch origin
git status -sb                      # ahead / behind par rapport à origin/main
git switch main && git pull --ff-only origin main
```

- `--ff-only` : jamais de merge automatique. Si `main` a des commits locaux non poussés **et** du retard (branches divergées), le pull échoue : **s'arrêter**, lister `git log --oneline origin/main..main` et demander à Thomas s'il faut rebaser, merger ou pousser avant de continuer.
- Modifications non commitées qui bloquent le switch ou le pull : s'arrêter et les signaler, ne rien jeter (`stash`, `reset`, `checkout --`) sans accord.
- Puis créer la branche de travail depuis ce `main` à jour (ou partir de la branche de la charte v2 si elle n'est pas encore fusionnée — voir Contexte).

### 0. Créer les fiches (si la session en crée)

Pour chaque nouvelle fiche :

1. Choisir le `sharedSlug` (anglais, kebab-case) ; vérifier qu'aucune fiche ni nœud ne l'utilise déjà.
2. Écrire `[sharedSlug].md` (FR, source de vérité du frontmatter) puis `[sharedSlug]-en.md` (même frontmatter, `lang: en`, `title` et `summary` traduits) — références croisées selon **R1**.
3. Selon le type :
   - `concept` → créer le motion design (**R2**) dans la foulée, pas « plus tard ».
   - `author` → chercher la photo (**R3**).
   - `book` → aucune couverture (**R4**).
4. Puis enchaîner sur les étapes 1 à 6 pour indexer la fiche dans le graphe.

### 1. Lire l'index existant

Lis `_graph.json` pour avoir :
- La liste des concepts déjà indexés (slugs)
- Les clusters existants avec leurs couleurs
- Les liens existants entre concepts

### 2. Identifier les nouvelles fiches

Compare les fichiers `.md` FR dans `src/content/concepts/` (exclure les `-en.md`) avec les slugs déjà dans `_graph.json`.

Les nouvelles fiches = fichiers présents dans le dossier mais absents de `_graph.json`. Inclut concepts, auteurs et livres.

**Vérification anti-doublon** : pendant cette lecture, comparer le titre de chaque nouvelle fiche avec les entrées existantes. Si un doublon est détecté, signaler avant de continuer.

### 3. Pour chaque nouvelle fiche

Lis sa fiche `.md` et extrais :
- `sharedSlug` (c'est le `slug` du nœud — **R5**)
- `title` (depuis le frontmatter)
- `summary` court (≤15 mots, résumé de la première phrase du frontmatter `summary`)
- `knowledgeType` (depuis le frontmatter — `concept` si absent)

Puis décide :
- **`cluster`** : quel cluster parmi les existants correspond le mieux ? Créer un nouveau cluster seulement si aucun existant ne convient vraiment.
- **`relatedConcepts`** : voir règle ci-dessous.

### 4. Règle des relatedConcepts — PRIORITÉ AUX LIENS INTER-CLUSTERS

Les nouveaux concepts d'un même batch viennent souvent de la même recherche et sont naturellement liés entre eux. Ce lien implicite est moins utile pour le graphe que les connexions avec des concepts existants d'autres clusters.

**Règle :**
- Pour chaque nouveau concept, trouver **en priorité** 2-3 concepts existants d'**autres clusters** avec lesquels il a un lien fort.
- Compléter ensuite avec 1-2 liens intra-cluster si vraiment pertinents.
- Maximum 10 `relatedConcepts` par nœud (pas de limite arbitraire si les liens sont vraiment pertinents).

**Liens inter-clusters à rechercher activement :** un concept de Psychologie Sociale peut pointer vers Cognition (mécanismes mentaux sous-jacents), Stratégie & Levier (applications pratiques), Systèmes (dynamiques collectives), Productivité (biais qui impactent le travail).

### 5. Mettre à jour les liens bidirectionnels

Si le nouveau concept A pointe vers un concept B existant, vérifie si B doit aussi pointer vers A. Ajoute le lien dans B si logique (ne pas surcharger — max 5 relatedConcepts par nœud). Reporter le lien dans les **deux** fichiers de B (FR et EN), en `sharedSlug` (**R1**).

### 6. Écrire dans `_graph.json`

- Ajoute les nouvelles entrées dans le tableau `"concepts"` avec le champ `"type"` (`"concept"`, `"author"` ou `"book"`) et `"slug"` = `sharedSlug`
- Les entrées **existantes sans champ `type`** doivent être mises à jour avec `"type": "concept"` (migration one-shot)
- Ajoute les nouveaux clusters dans `"clusters"` si nécessaire
- Met à jour les `relatedConcepts` des concepts existants si des liens bidirectionnels ont été ajoutés
- Ne jamais supprimer ou modifier les entrées existantes sauf pour ajouter des liens bidirectionnels, le champ `type`, ou retirer un suffixe `-en` fautif

### 7. Vérification (obligatoire, avant tout commit)

Depuis `d:/Projet_Newsletter_Hub`, en passant les `sharedSlug` créés ou modifiés dans la session :

```bash
node d:/Projet_Automate/projects/knowledge_curator/scripts/check-ekenor-concepts.mjs <slug-1> <slug-2> …
```

Le script échoue (code 1) si :
- une valeur de `relatedConcepts` / `relatedProjects` / `relatedArticles` / `citedBy` finit par `-en` (fiches **et** articles) — **R1** ;
- un nœud de `_graph.json` a un slug ou un lien en `-en`, n'a pas de `type`, ou un type différent du `knowledgeType` de sa fiche ; une fiche créée est absente du graphe — **R5** ;
- une fiche créée n'a pas sa paire FR + EN ;
- un concept créé n'a pas `motion/<sharedSlug>.astro`, ou celui-ci contient un hex, un dégradé, un émoji, des keyframes sans préfixe `fxs-`, pas d'`aria { fr, en }`, ou une boucle hors 8–12 s — **R2** ;
- un auteur a des champs photo incomplets, une licence NC/ND/fair use, des fichiers `photo.jpg` / `photo.webp` manquants, ou FR ≠ EN — **R3** ;
- un livre porte une couverture, ou une fiche non-auteur porte des champs photo — **R4**.

Puis :
- `npm run build` (il vérifie aussi les liens) ;
- pour chaque motion design : regarder la fiche en FR et EN, thème clair et sombre, avec et sans « réduire les animations », et la vignette sur `/fr/concepts/` (checklist `docs/MOTION_CONCEPTS.md` §7) ;
- pour chaque photo : ouvrir `photo.jpg` et vérifier que le visage est centré.

Ne pas commiter tant que le script n'affiche pas `✓ Fiches OK`. Corriger, relancer.

### 8. Résumé

Affiche un résumé :
```
✅ X nouvelles fiches : [slugs] (concepts / auteurs / livres)
🎞️ Motion design : [slugs des composants créés]
📷 Photos : [slug — licence — source (+ licence Flickr actuelle)] · sans photo libre : [slugs]
🔗 Y liens créés (dont Z bidirectionnels, W inter-clusters)
📁 Clusters : [liste avec nombre de concepts par cluster]
🧪 Vérification : ✓ Fiches OK · build OK
```

## Notes

- Le `summary` dans `_graph.json` peut être différent du frontmatter — il doit être court (≤15 mots) pour être utile à Claude lors des futures mises à jour.
- Les liens sont non-directionnels dans le graphe 3D — A→B et B→A représentent le même lien visuellement.
- Pas de limite rigide sur les `relatedConcepts` — mettre tous les liens vraiment pertinents (auteurs et livres peuvent avoir 8-10 liens car ils ont théorisé plusieurs concepts du graphe).
- Les slugs restent en anglais. Les titres dans `_graph.json` et dans les fichiers FR `.md` doivent être en français.
