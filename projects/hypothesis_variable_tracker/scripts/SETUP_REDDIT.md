# Setup Reddit API — HVT Pilier 1

Le script `pilier1_crowd.py` nécessite une Reddit API app de type **script** (usage personnel, gratuit).

---

## Étape 1 — Créer une Reddit API app

1. Va sur : https://www.reddit.com/prefs/apps
2. Clique **"Create App"** ou **"Create Another App"**
3. Remplis :
   - **Name** : `HVT-bot` (ou ce que tu veux)
   - **Type** : ⦿ **script**
   - **Description** : `Hypothesis Variable Tracker — recherche académique personnelle`
   - **About URL** : laisser vide
   - **Redirect URI** : `http://localhost:8080` (obligatoire même pour un script)
4. Clique **"Create app"**

---

## Étape 2 — Récupérer les credentials

Après création, Reddit affiche :
- **client_id** : la chaîne sous le nom de l'app (ex: `aBcDeFgHiJ1234`)
- **client_secret** : le champ "secret" (ex: `xY9z-AbCdEf123456789`)

---

## Étape 3 — Ajouter dans .private/CREDENTIALS.md

Ajouter une section :

```markdown
## Reddit API — HVT Pilier 1

- Client ID : aBcDeFgHiJ1234
- Client Secret : xY9z-AbCdEf123456789
- User Agent : HVT-bot/1.0 by u/{ton_username_reddit}
- App type : script
- Créé le : YYYY-MM-DD
```

---

## Étape 4 — Configurer les variables d'environnement

Dans PowerShell (session courante) :

```powershell
$env:REDDIT_CLIENT_ID = "aBcDeFgHiJ1234"
$env:REDDIT_CLIENT_SECRET = "xY9z-AbCdEf123456789"
$env:REDDIT_USER_AGENT = "HVT-bot/1.0 by u/{ton_username_reddit}"
```

Pour les rendre permanentes (optionnel) :

```powershell
[System.Environment]::SetEnvironmentVariable("REDDIT_CLIENT_ID", "aBcDeFgHiJ1234", "User")
[System.Environment]::SetEnvironmentVariable("REDDIT_CLIENT_SECRET", "xY9z-AbCdEf123456789", "User")
[System.Environment]::SetEnvironmentVariable("REDDIT_USER_AGENT", "HVT-bot/1.0 by u/{ton_username_reddit}", "User")
```

---

## Étape 5 — Installer les dépendances

```powershell
/c/Users/silli/AppData/Local/Programs/Python/Python313/python.exe -m pip install praw
```

---

## Test rapide

```powershell
$env:REDDIT_CLIENT_ID = "..."
$env:REDDIT_CLIENT_SECRET = "..."
$env:REDDIT_USER_AGENT = "HVT-bot/1.0 by u/{username}"

/c/Users/silli/AppData/Local/Programs/Python/Python313/python.exe projects/hypothesis_variable_tracker/scripts/pilier1_crowd.py `
  --thesis-slug test `
  --variables "intelligence artificielle, remplacement emplois"
```

---

## Notes

- L'API Reddit en mode script est gratuite et sans limite stricte pour un usage personnel
- Rate limit officiel : 60 requêtes/minute — le script respecte ce seuil
- L'app "script" ne nécessite pas de OAuth complet ni de callback URL fonctionnelle
