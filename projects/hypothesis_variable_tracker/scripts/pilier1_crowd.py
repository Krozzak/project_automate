"""
HVT — Pilier 1 : Crowd sourcing (Reddit)

Usage:
    python pilier1_crowd.py --thesis-slug YYYY-MM-DD-slug --variables "var1, var2, var3"
    python pilier1_crowd.py --thesis-slug YYYY-MM-DD-slug --variables "var1, var2" --subreddits "MachineLearning, artificial, LocalLLaMA"

Output: projects/hypothesis_variable_tracker/theses/{thesis-slug}/pilier_crowd.md
"""

import argparse
import os
import sys
from datetime import date
from pathlib import Path

THESES_DIR = Path(__file__).parent.parent / "theses"
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

# Subreddits par domaine (auto-détection basée sur les mots-clés des variables)
DOMAIN_SUBREDDITS = {
    "ia": ["MachineLearning", "artificial", "LocalLLaMA", "ChatGPT", "singularity"],
    "dev": ["programming", "cscareerquestions", "learnprogramming", "webdev"],
    "sante": ["askdocs", "medical", "nootropics", "longevity"],
    "finance": ["personalfinance", "investing", "financialindependence", "stocks"],
    "business": ["entrepreneur", "startups", "smallbusiness", "marketing"],
    "default": ["AskReddit", "explainlikeimfive", "science"],
}


def get_reddit_client():
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    user_agent = os.environ.get("REDDIT_USER_AGENT", "HVT-bot/1.0")

    if not client_id or not client_secret:
        script_dir = Path(__file__).parent
        print(
            f"[ERROR] Credentials Reddit manquants.\n"
            f"   Configure REDDIT_CLIENT_ID et REDDIT_CLIENT_SECRET dans .private/CREDENTIALS.md\n"
            f"   puis ajoute-les comme variables d'environnement.\n"
            f"   Guide : {script_dir / 'SETUP_REDDIT.md'}"
        )
        sys.exit(1)

    try:
        import praw
    except ImportError:
        print("[ERROR] Module 'praw' manquant. Lance : pip install praw")
        sys.exit(1)

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )


def detect_subreddits(variables: list[str]) -> list[str]:
    """Détecte les subreddits pertinents selon les mots-clés des variables."""
    variables_lower = " ".join(variables).lower()
    selected = []

    keyword_map = {
        "ia": ["ia", "intelligence artificielle", "llm", "gpt", "claude", "ai", "machine learning", "modèle"],
        "dev": ["développeur", "developer", "code", "programmation", "software", "ingénieur"],
        "sante": ["santé", "médical", "health", "symptôme", "traitement", "maladie"],
        "finance": ["finance", "investissement", "bourse", "crypto", "argent", "revenus"],
        "business": ["business", "startup", "entrepreneur", "marketing", "client", "produit"],
    }

    for domain, keywords in keyword_map.items():
        if any(kw in variables_lower for kw in keywords):
            selected.extend(DOMAIN_SUBREDDITS[domain][:3])

    if not selected:
        selected = DOMAIN_SUBREDDITS["default"]

    return list(dict.fromkeys(selected))[:5]  # max 5 subreddits, sans doublons


def search_reddit(reddit, variable: str, subreddits: list[str], limit: int = 20) -> list[dict]:
    """Recherche sur Reddit pour une variable donnée."""
    results = []

    for sub_name in subreddits:
        try:
            subreddit = reddit.subreddit(sub_name)
            posts = subreddit.search(variable, sort="relevance", time_filter="year", limit=limit)

            for post in posts:
                if post.score < 10 or post.upvote_ratio < 0.7:
                    continue

                # Extraire données du post + top comment
                top_comment = ""
                post.comments.replace_more(limit=0)
                if post.comments:
                    top_c = post.comments[0]
                    top_comment = top_c.body[:500] if hasattr(top_c, "body") else ""

                results.append({
                    "subreddit": sub_name,
                    "title": post.title,
                    "score": post.score,
                    "upvote_ratio": post.upvote_ratio,
                    "url": f"https://reddit.com{post.permalink}",
                    "selftext": post.selftext[:300] if post.selftext else "",
                    "top_comment": top_comment,
                })

        except Exception as e:
            print(f"  ⚠️  Erreur sur r/{sub_name} : {e}")
            continue

    # Trier par score
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:15]  # garder top 15 par variable


def format_results_as_markdown(variable: str, results: list[dict]) -> str:
    """Formate les résultats Reddit en markdown."""
    if not results:
        return f"*Aucun résultat pertinent trouvé pour cette variable.*\n"

    lines = []
    lines.append("| Subreddit | Post | Extrait clé | Score | URL |")
    lines.append("|-----------|------|-------------|-------|-----|")

    for r in results:
        extrait = r["top_comment"] or r["selftext"] or r["title"]
        extrait = extrait.replace("\n", " ").replace("|", "│")[:200]
        title = r["title"].replace("|", "│")[:80]
        lines.append(
            f"| r/{r['subreddit']} | {title} | {extrait} | {r['score']} | [lien]({r['url']}) |"
        )

    return "\n".join(lines) + "\n"


def build_output(thesis_slug: str, variables: list[str], subreddits: list[str], all_results: dict) -> str:
    """Génère le contenu complet de pilier_crowd.md."""
    today = date.today().isoformat()

    lines = [
        f"---",
        f"pilier: crowd",
        f"thesis_slug: {thesis_slug}",
        f"date_collecte: {today}",
        f"sources: [{', '.join(subreddits)}]",
        f"---",
        f"",
        f"# Pilier 1 — Crowd sourcing",
        f"",
        f"> **Règle** : données spécifiques uniquement — chiffres réels, protocoles précis, timelines concrètes.",
        f"> Subreddits interrogés : {', '.join(['r/' + s for s in subreddits])}",
        f"",
    ]

    for i, variable in enumerate(variables, 1):
        lines.append(f"## Variable {i} — {variable}")
        lines.append("")
        results = all_results.get(variable, [])
        lines.append(format_results_as_markdown(variable, results))

    lines.extend([
        "---",
        "",
        "## Signaux de convergence",
        "",
        "*À remplir manuellement : si ≥3 sources indépendantes mentionnent le même protocole/chiffre, noter ici.*",
        "",
        "- [ ] {Signal convergent 1}",
        "- [ ] {Signal convergent 2}",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="HVT — Pilier 1 Crowd sourcing (Reddit)")
    parser.add_argument("--thesis-slug", required=True, help="Slug de la thèse (ex: 2026-05-15-ia-remplace-devs)")
    parser.add_argument("--variables", required=True, help="Variables séparées par virgule")
    parser.add_argument("--subreddits", default="", help="Subreddits spécifiques (optionnel, séparés par virgule)")
    args = parser.parse_args()

    variables = [v.strip() for v in args.variables.split(",") if v.strip()]
    if not variables:
        print("[ERROR] Aucune variable fournie.")
        sys.exit(1)

    print(f"[HVT] Pilier 1 : Crowd sourcing")
    print(f"   These : {args.thesis_slug}")
    print(f"   Variables ({len(variables)}) : {', '.join(variables)}")

    reddit = get_reddit_client()

    if args.subreddits:
        subreddits = [s.strip() for s in args.subreddits.split(",") if s.strip()]
    else:
        subreddits = detect_subreddits(variables)

    print(f"   Subreddits : {', '.join(['r/' + s for s in subreddits])}")

    output_dir = THESES_DIR / args.thesis_slug
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "pilier_crowd.md"

    all_results = {}
    for variable in variables:
        print(f"\n   Recherche : '{variable}'...")
        results = search_reddit(reddit, variable, subreddits)
        all_results[variable] = results
        print(f"   -> {len(results)} resultats pertinents")

    content = build_output(args.thesis_slug, variables, subreddits, all_results)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n[OK] Pilier 1 ecrit : {output_path}")
    total = sum(len(v) for v in all_results.values())
    print(f"   {total} entrees au total sur {len(variables)} variables")


if __name__ == "__main__":
    main()
