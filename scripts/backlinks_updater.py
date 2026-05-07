#!/usr/bin/env python3
"""
backlinks_updater.py — KM Backlinks Updater for Projet_Automate

Modes:
  (default)         Recalculate citedBy[] for all concept files
  --migrate         Add missing frontmatter to files that have none or a non-standard schema
  --scan            Generate UNLINKED_MENTIONS.md (concept titles found in text but not linked)

Usage:
  python scripts/backlinks_updater.py
  python scripts/backlinks_updater.py --migrate
  python scripts/backlinks_updater.py --scan
  python scripts/backlinks_updater.py --migrate --scan
  python scripts/backlinks_updater.py --migrate --dry-run
"""

import re
import sys
import unicodedata
import yaml
from pathlib import Path
from typing import Optional

# --- Paths ---
REPO_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = REPO_ROOT / ".private" / "notes" / "concepts"
UNLINKED_MENTIONS_FILE = REPO_ROOT / ".private" / "notes" / "UNLINKED_MENTIONS.md"

# Current clusters from _graph.json — not enforced, new clusters can be added freely in frontmatter
VALID_CLUSTERS = [
    "Productivité",
    "Cognition",
    "Systèmes",
    "IA & Outils",
    "Philosophie",
    "Finance & Marchés",
    "Travail & IA",
    "Stratégie & Levier",
    "Psychologie Sociale",
]

# Target frontmatter schema (canonical field order)
CANONICAL_FIELDS = [
    "title",
    "cluster",
    "relatedConcepts",
    "relatedProjects",
    "relatedArticles",
    "citedBy",
    "aliases",
    "tags",
    "status",
    "dateCreated",
    "sources",
]


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_file(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text). frontmatter_dict is {} if none."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            yaml_block = text[3:end].strip()
            body = text[end + 4:].lstrip("\n")
            try:
                fm = yaml.safe_load(yaml_block) or {}
            except yaml.YAMLError:
                fm = {}
            return fm, body
    return {}, text


def dump_frontmatter(fm: dict) -> str:
    """Serialize frontmatter dict to YAML block, respecting canonical field order."""
    ordered = {}
    for key in CANONICAL_FIELDS:
        if key in fm:
            ordered[key] = fm[key]
    for key, val in fm.items():
        if key not in ordered:
            ordered[key] = val
    return yaml.dump(ordered, allow_unicode=True, default_flow_style=False, sort_keys=False)


def write_file(path: Path, fm: dict, body: str):
    """Write frontmatter + body back to file."""
    fm_str = dump_frontmatter(fm)
    path.write_text(f"---\n{fm_str}---\n\n{body}", encoding="utf-8")


def slug_from_filename(filename: str) -> str:
    """Convert filename to kebab-case slug."""
    name = Path(filename).stem
    return name.replace("_", "-").replace(" ", "-").lower()


def title_from_filename(filename: str) -> str:
    """Extract readable title from filename."""
    return Path(filename).stem.replace("_", " ")


def extract_title_from_body(body: str, filename: str) -> str:
    """Extract title from first # heading in body."""
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        if " — " in title:
            title = title.split(" — ")[0].strip()
        return title
    return title_from_filename(filename)


def extract_date_from_body(body: str) -> Optional[str]:
    """Find a YYYY-MM-DD date in the body text."""
    match = re.search(r"\b(202\d-\d{2}-\d{2})\b", body)
    return match.group(1) if match else None


def norm(s: str) -> str:
    """Lowercase + remove accents for ASCII matching."""
    return unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()


def infer_cluster_from_title(title: str, body: str) -> str:
    """
    Infer cluster from concept title (primary signal) then body (fallback).
    Title-based matching is much more reliable than body scanning.
    """
    t = norm(title)

    # --- Title-based detection (ordered by specificity) ---

    # Memory / Cognition keywords in title
    if any(w in t for w in [
        "memoire", "memory", "oubli", "ebbinghaus", "retrieval", "spacing effect",
        "consolidation", "flashbulb", "reconsolidation", "mnemonique",
        "cognitive load", "dual process", "inner speech", "feynman",
        "aphantasie", "pensee conceptuelle", "apprentissage", "flow ",
        "attention residue", "curse of knowledge", "dunning", "dissonance",
    ]):
        return "Cognition"

    # Productivity keywords in title
    if any(w in t for w in [
        "time blind", "planning fallacy", "parkinson", "student syndrome",
        "wip limit", "wip ", "focus", "ultradian", "commitment device",
        "implementation intention", "ego depletion", "volonte", "definition of done",
        "procrastin", "clarity lock", "capacity overload", "context switch",
    ]):
        return "Productivité"

    # Finance keywords in title
    if any(w in t for w in [
        "polymarket", "gonzo", "inelastic", "bourse", "trading", "price ",
        "marche financier", "actif financier",
    ]):
        return "Finance & Marchés"

    # AI & Tools keywords in title
    if any(w in t for w in [
        "agentic", "context engineering", "architecture de test",
        "ia ", "agent autonome", "llm", "pivot pensee ia",
    ]):
        return "IA & Outils"

    # Work & AI keywords in title
    if any(w in t for w in [
        "codifiab", "so-so", "silent workforce", "ai identity",
    ]):
        return "Travail & IA"

    # Strategy & Leverage keywords in title
    if any(w in t for w in [
        "leverage", "permissionless", "specific knowledge", "long term",
        "run-build", "individu souverain", "judgment over time",
        "shelling point", "seuil critique", "masse critique",
        "goodhart", "ice score",
    ]):
        return "Stratégie & Levier"

    # Philosophy keywords in title
    if any(w in t for w in [
        "poiesis", "praxis", "phronesis", "aristote", "bonheur",
        "desire as", "utility vs", "happiness as", "work as play",
    ]):
        return "Philosophie"

    # Social Psychology keywords in title
    if any(w in t for w in [
        "perception", "impression management", "effet de halo", "parasocial",
        "signal theory", "identite percue", "cristallisation", "statut confere",
        "premiere impression", "tipping point", "specificity credibility",
        "narrative fallacy", "survivorship", "wysiati", "fantasme",
    ]):
        return "Psychologie Sociale"

    # Systems keywords in title
    if any(w in t for w in [
        "loi de gall", "small world", "emergence", "mecanisme design",
        "nsng", "skin in the game", "loss aversion", "variable ratio",
        "anti gaming", "comment to dm", "permission marketing",
        "golden hour", "keyword trigger", "copywriting hook",
        "direct response", "story doing",
    ]):
        return "Systèmes"

    # --- Body fallback for ambiguous titles ---
    b = norm(body[:400])
    if any(w in b for w in ["polymarket", "gonzo 40", "trading"]):
        return "Finance & Marchés"
    if any(w in b for w in ["agentic era", "llm", "agent autonome"]):
        return "IA & Outils"
    if any(w in b for w in ["naval ravikant", "leverage", "permissionless"]):
        return "Stratégie & Levier"
    if any(w in b for w in ["memoire", "memory", "cognit"]):
        return "Cognition"

    return "Cognition"  # safe default


# ---------------------------------------------------------------------------
# Migration
# ---------------------------------------------------------------------------

def needs_migration(fm: dict) -> bool:
    """True if frontmatter is missing or lacks canonical fields."""
    if not fm:
        return True
    required = {"title", "cluster", "relatedConcepts", "citedBy"}
    return not required.issubset(fm.keys())


def build_canonical_frontmatter(fm: dict, body: str, filename: str) -> dict:
    """Merge existing frontmatter with canonical schema."""
    new_fm = {}

    # title
    title = (
        fm.get("title") or fm.get("name") or fm.get("concept")
        or extract_title_from_body(body, filename)
    )
    new_fm["title"] = str(title).strip()

    # cluster
    new_fm["cluster"] = fm.get("cluster") or infer_cluster_from_title(new_fm["title"], body)

    # relatedConcepts
    existing = fm.get("relatedConcepts") or fm.get("related_concepts") or []
    new_fm["relatedConcepts"] = existing if isinstance(existing, list) else []

    # relatedProjects
    proj = fm.get("relatedProjects") or fm.get("related_projects") or fm.get("projet") or []
    if isinstance(proj, str):
        proj = [proj]
    new_fm["relatedProjects"] = proj if isinstance(proj, list) else []

    # relatedArticles — post_linked/post_lié are free-text strings, not slugs → drop them
    art = fm.get("relatedArticles") or []
    new_fm["relatedArticles"] = art if isinstance(art, list) else []

    # citedBy — always recalculated, never seeded from old fm
    new_fm["citedBy"] = []

    # aliases — bilingual structure
    existing_aliases = fm.get("aliases")
    if isinstance(existing_aliases, dict) and ("fr" in existing_aliases or "en" in existing_aliases):
        new_fm["aliases"] = existing_aliases
    else:
        new_fm["aliases"] = {"fr": [], "en": []}

    # tags
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    new_fm["tags"] = [t.lower().replace(" ", "-") for t in tags] if tags else []

    # status
    raw = str(fm.get("status") or fm.get("statut") or fm.get("ekenor") or "draft")
    if raw in ("✅", "published", "publié", "Publié"):
        new_fm["status"] = "published"
    elif raw in ("⏳", "ready", "En révision"):
        new_fm["status"] = "ready"
    else:
        new_fm["status"] = "draft"

    # dateCreated
    date = (
        fm.get("dateCreated") or fm.get("date") or fm.get("captured_at")
        or extract_date_from_body(body) or "2026-01-01"
    )
    new_fm["dateCreated"] = str(date)[:10]

    # sources
    src = fm.get("sources") or fm.get("source") or fm.get("source_url") or []
    if isinstance(src, str):
        src = [src]
    new_fm["sources"] = src if isinstance(src, list) else []

    return new_fm


def run_migrate(dry_run: bool = False) -> int:
    """Add/normalize frontmatter for all concept files. Returns count of migrated files."""
    files = sorted(CONCEPTS_DIR.glob("*.md"))
    migrated = 0

    for path in files:
        if path.name in ("INDEX_CONCEPTS.md",) or path.name.endswith("_CONCEPTS.md"):
            continue

        fm, body = parse_file(path)
        if not needs_migration(fm):
            continue

        new_fm = build_canonical_frontmatter(fm, body, path.name)

        if dry_run:
            print(f"  [DRY RUN] {path.name}")
            print(f"    title={new_fm['title']!r}, cluster={new_fm['cluster']}, status={new_fm['status']}")
        else:
            write_file(path, new_fm, body)
            print(f"  Migrated: {path.name}")

        migrated += 1

    return migrated


# ---------------------------------------------------------------------------
# citedBy recalculation (default mode)
# ---------------------------------------------------------------------------

def run_update_cited_by():
    """Scan all concept files and recalculate citedBy[] for each."""
    files = sorted(CONCEPTS_DIR.glob("*.md"))
    concept_files = [
        f for f in files
        if f.name != "INDEX_CONCEPTS.md" and not f.name.endswith("_CONCEPTS.md")
    ]

    slug_to_path = {slug_from_filename(p.name): p for p in concept_files}
    cited_by: dict[str, set] = {s: set() for s in slug_to_path}

    for path in concept_files:
        fm, _ = parse_file(path)
        source_slug = slug_from_filename(path.name)
        for field in ("relatedConcepts", "relatedProjects", "relatedArticles"):
            for target_slug in (fm.get(field) or []):
                if isinstance(target_slug, str) and target_slug in cited_by:
                    cited_by[target_slug].add(source_slug)

    updated = 0
    for path in concept_files:
        fm, body = parse_file(path)
        slug = slug_from_filename(path.name)
        new_cb = sorted(cited_by.get(slug, set()))
        if new_cb != sorted(fm.get("citedBy") or []):
            fm["citedBy"] = new_cb
            write_file(path, fm, body)
            print(f"  Updated citedBy: {path.name} <- {new_cb}")
            updated += 1

    print(f"\nDone: citedBy updated in {updated} files ({len(concept_files)} total)")


# ---------------------------------------------------------------------------
# --scan: unlinked mentions
# ---------------------------------------------------------------------------

def run_scan():
    """Find concept titles mentioned in bodies but not in relatedConcepts."""
    files = sorted(CONCEPTS_DIR.glob("*.md"))
    concept_files = [
        f for f in files
        if f.name != "INDEX_CONCEPTS.md" and not f.name.endswith("_CONCEPTS.md")
    ]

    concepts = []
    for path in concept_files:
        fm, body = parse_file(path)
        slug = slug_from_filename(path.name)
        title = fm.get("title") or extract_title_from_body(body, path.name)
        aliases_raw = fm.get("aliases") or {}
        fr_aliases = aliases_raw.get("fr", []) if isinstance(aliases_raw, dict) else []
        concepts.append({"slug": slug, "title": title, "path": path, "fr_aliases": fr_aliases})

    lines = [
        "# Unlinked Mentions — Suggestions de liens\n",
        f"_Généré le {__import__('datetime').date.today()}_\n",
        "Concepts trouvés dans le texte d'autres fiches mais absents de `relatedConcepts`.\n",
    ]
    total = 0

    for source in concepts:
        fm, body = parse_file(source["path"])
        declared = set(fm.get("relatedConcepts") or [])
        suggestions = []

        for target in concepts:
            if target["slug"] == source["slug"] or target["slug"] in declared:
                continue
            for term in ([target["title"]] + target["fr_aliases"]):
                if len(term) < 5:
                    continue
                if re.search(r"\b" + re.escape(term) + r"\b", body, re.IGNORECASE):
                    suggestions.append(f"  - `{target['slug']}` (via \"{term}\")")
                    total += 1
                    break

        if suggestions:
            lines.append(f"\n## {source['path'].name}\n")
            lines.extend(suggestions)

    lines.append(f"\n---\n_Total : {total} suggestions_\n")
    UNLINKED_MENTIONS_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ {total} unlinked mentions -> {UNLINKED_MENTIONS_FILE}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    do_migrate = "--migrate" in args
    do_scan = "--scan" in args
    do_dry_run = "--dry-run" in args

    if not any([do_migrate, do_scan]):
        print("Updating citedBy for all concept files...")
        run_update_cited_by()
        return

    if do_migrate:
        print(f"Migrating frontmatter ({'DRY RUN' if do_dry_run else 'LIVE'})...")
        count = run_migrate(dry_run=do_dry_run)
        print(f"\nDone: {count} files {'would be ' if do_dry_run else ''}migrated")

    if do_scan:
        print("\nScanning for unlinked mentions...")
        run_scan()


if __name__ == "__main__":
    main()
