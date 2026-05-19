"""
HVT -- Pilier 4 : Documentation scientifique (Semantic Scholar + arXiv)

Usage:
    python pilier4_science.py --thesis-slug YYYY-MM-DD-slug --variables "var1, var2, var3"
    python pilier4_science.py --thesis-slug YYYY-MM-DD-slug --variables "var1, var2" --min-year 2018 --min-citations 10

Output: projects/hypothesis_variable_tracker/theses/{thesis-slug}/pilier_science.md

APIs utilisees (gratuites, sans authentification) :
- Semantic Scholar : https://api.semanticscholar.org/graph/v1/paper/search
- arXiv : http://export.arxiv.org/api/query
"""

import argparse
import sys
import time
import json
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

try:
    import requests
    requests.packages.urllib3.disable_warnings()
except ImportError:
    print("[ERROR] Module 'requests' manquant. Lance : pip install requests")
    sys.exit(1)

THESES_DIR = Path(__file__).parent.parent / "theses"

SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
ARXIV_URL = "http://export.arxiv.org/api/query"  # HTTP, pas HTTPS, evite les pb SSL Windows

SS_FIELDS = "title,authors,year,citationCount,abstract,externalIds,openAccessPdf"
HEADERS = {"User-Agent": "HVT-research-bot/1.0"}


def fetch_semantic_scholar(query: str, limit: int = 10, min_year: int = 2015, min_citations: int = 5) -> list[dict]:
    """Requete Semantic Scholar API publique avec retry sur 429."""
    params = {
        "query": query,
        "fields": SS_FIELDS,
        "limit": min(limit * 2, 50),
    }

    for attempt in range(3):
        try:
            resp = requests.get(
                SEMANTIC_SCHOLAR_URL,
                params=params,
                headers=HEADERS,
                timeout=20,
                verify=True,
            )
            if resp.status_code == 429:
                wait = (attempt + 1) * 12
                print(f"  [rate-limit] Semantic Scholar 429 -- attente {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            data = resp.json()
            break
        except requests.exceptions.RequestException as e:
            print(f"  [warn] Semantic Scholar erreur (tentative {attempt + 1}/3) : {e}")
            if attempt < 2:
                time.sleep(5)
            else:
                return []
    else:
        print("  [warn] Semantic Scholar inaccessible apres 3 tentatives.")
        return []

    papers = []
    for p in data.get("data", []):
        year = p.get("year") or 0
        citations = p.get("citationCount") or 0
        abstract = p.get("abstract") or ""

        if year < min_year or citations < min_citations or not abstract:
            continue

        authors = [a.get("name", "") for a in p.get("authors", [])[:3]]
        authors_str = ", ".join(authors) + (" et al." if len(p.get("authors", [])) > 3 else "")

        paper_id = p.get("paperId", "")
        open_pdf = (p.get("openAccessPdf") or {}).get("url", "")
        url_paper = open_pdf or f"https://www.semanticscholar.org/paper/{paper_id}"

        papers.append({
            "title": p.get("title", ""),
            "authors": authors_str,
            "year": year,
            "citations": citations,
            "abstract": abstract[:400],
            "url": url_paper,
            "source": "Semantic Scholar",
        })

        if len(papers) >= limit:
            break

    return papers


def fetch_arxiv(query: str, limit: int = 5, min_year: int = 2023) -> list[dict]:
    """Requete arXiv API (HTTP pour eviter pb SSL Windows)."""
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": limit * 2,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    try:
        resp = requests.get(ARXIV_URL, params=params, headers=HEADERS, timeout=15, verify=False)
        resp.raise_for_status()
        xml_data = resp.content
    except requests.exceptions.RequestException as e:
        print(f"  [warn] arXiv erreur : {e}")
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"  [warn] arXiv parse erreur : {e}")
        return []

    papers = []
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        summary_el = entry.find("atom:summary", ns)
        published_el = entry.find("atom:published", ns)
        id_el = entry.find("atom:id", ns)

        if not all(el is not None for el in [title_el, summary_el, published_el, id_el]):
            continue

        year = int(published_el.text[:4]) if published_el.text else 0
        if year < min_year:
            continue

        authors = [
            a.find("atom:name", ns).text
            for a in entry.findall("atom:author", ns)[:3]
            if a.find("atom:name", ns) is not None
        ]
        authors_str = ", ".join(authors) + (" et al." if len(entry.findall("atom:author", ns)) > 3 else "")

        papers.append({
            "title": title_el.text.strip().replace("\n", " "),
            "authors": authors_str,
            "year": year,
            "citations": "N/A",
            "abstract": summary_el.text.strip()[:400].replace("\n", " "),
            "url": id_el.text.strip(),
            "source": "arXiv",
        })

        if len(papers) >= limit:
            break

    return papers


def format_papers_as_markdown(papers: list[dict]) -> str:
    """Formate les papers en tableau markdown."""
    if not papers:
        return "*Aucun paper pertinent trouve pour cette variable.*\n"

    lines = ["| Titre | Auteurs | Annee | Resultat cle | Citations | Source | URL |"]
    lines.append("|-------|---------|-------|-------------|-----------|--------|-----|")

    for p in papers:
        title = p["title"].replace("|", "/")[:80]
        authors = p["authors"].replace("|", "/")[:40]
        abstract = p["abstract"].replace("|", "/")[:200]
        lines.append(
            f"| {title} | {authors} | {p['year']} | {abstract} | {p['citations']} | {p['source']} | [lien]({p['url']}) |"
        )

    return "\n".join(lines) + "\n"


def build_output(thesis_slug: str, variables: list[str], all_results: dict) -> str:
    """Genere le contenu complet de pilier_science.md."""
    today = date.today().isoformat()

    lines = [
        f"---",
        f"pilier: science",
        f"thesis_slug: {thesis_slug}",
        f"date_collecte: {today}",
        f"sources: [semantic_scholar, arxiv]",
        f"---",
        f"",
        f"# Pilier 4 -- Documentation scientifique",
        f"",
        f"> **Regle** : papers testant directement les variables. Filtres : abstract disponible, annee > 2015, citationCount > 5 (sauf arXiv recent).",
        f"",
    ]

    gaps = []

    for i, variable in enumerate(variables, 1):
        lines.append(f"## Variable {i} -- {variable}")
        lines.append("")

        results = all_results.get(variable, {"ss": [], "arxiv": []})
        ss_papers = results.get("ss", [])
        arxiv_papers = results.get("arxiv", [])

        if ss_papers:
            lines.append("### Semantic Scholar")
            lines.append("")
            lines.append(format_papers_as_markdown(ss_papers))
        else:
            lines.append("*Aucun resultat Semantic Scholar.*\n")

        if arxiv_papers:
            lines.append("### arXiv (recent 2023+)")
            lines.append("")
            lines.append(format_papers_as_markdown(arxiv_papers))

        if not ss_papers and not arxiv_papers:
            gaps.append(f"Var {i} ({variable})")

        lines.append("")

    if gaps:
        lines.extend([
            "---",
            "",
            "## Gaps identifies",
            "",
            "*Variables pour lesquelles aucun paper direct n'a ete trouve :*",
            "",
        ])
        for gap in gaps:
            lines.append(f"- {gap}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="HVT -- Pilier 4 Documentation scientifique")
    parser.add_argument("--thesis-slug", required=True, help="Slug de la these")
    parser.add_argument("--variables", required=True, help="Variables separees par virgule")
    parser.add_argument("--min-year", type=int, default=2015, help="Annee minimum (defaut: 2015)")
    parser.add_argument("--min-citations", type=int, default=5, help="Citations minimum Semantic Scholar (defaut: 5)")
    parser.add_argument("--limit", type=int, default=5, help="Nombre max de papers par variable par source (defaut: 5)")
    args = parser.parse_args()

    variables = [v.strip() for v in args.variables.split(",") if v.strip()]
    if not variables:
        print("[ERROR] Aucune variable fournie.")
        sys.exit(1)

    print(f"[HVT] Pilier 4 : Documentation scientifique")
    print(f"   These : {args.thesis_slug}")
    print(f"   Variables ({len(variables)}) : {', '.join(variables)}")
    print(f"   Filtres : annee >= {args.min_year}, citations >= {args.min_citations}")

    output_dir = THESES_DIR / args.thesis_slug
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "pilier_science.md"

    all_results = {}
    for i, variable in enumerate(variables, 1):
        print(f"\n   Variable {i}/{len(variables)} : '{variable}'...")

        ss_papers = fetch_semantic_scholar(
            variable,
            limit=args.limit,
            min_year=args.min_year,
            min_citations=args.min_citations,
        )
        print(f"   Semantic Scholar -> {len(ss_papers)} papers")

        time.sleep(2)

        arxiv_papers = fetch_arxiv(variable, limit=3, min_year=2023)
        print(f"   arXiv -> {len(arxiv_papers)} papers")

        all_results[variable] = {"ss": ss_papers, "arxiv": arxiv_papers}

        if i < len(variables):
            time.sleep(2)

    content = build_output(args.thesis_slug, variables, all_results)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    total_ss = sum(len(v["ss"]) for v in all_results.values())
    total_arxiv = sum(len(v["arxiv"]) for v in all_results.values())
    print(f"\n[OK] Pilier 4 ecrit : {output_path}")
    print(f"   {total_ss} papers Semantic Scholar + {total_arxiv} papers arXiv sur {len(variables)} variables")


if __name__ == "__main__":
    main()
