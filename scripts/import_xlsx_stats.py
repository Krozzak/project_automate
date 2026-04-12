#!/usr/bin/env python3
"""
import_xlsx_stats.py — Import LinkedIn Analytics XLSX into dated snapshot files

Usage:
    python import_xlsx_stats.py [path_to_xlsx] [--snapshot-date YYYY-MM-DD] [--print] [--snapshot] [--update-frontmatters]

Options:
    path_to_xlsx         Path to LinkedIn XLSX export (default: most recent in Downloads)
    --snapshot-date      Date de l'export (default: today)
    --print              Affiche le rapport markdown (défaut si aucun flag)
    --snapshot           Crée posts/analytics-YYYY-MM-DD.md (snapshot daté, non écrasé)
    --write              Alias legacy pour --snapshot (compatibilité)
    --update-frontmatters  Met à jour linkedin_url dans les frontmatters des posts

Examples:
    python import_xlsx_stats.py --print
    python import_xlsx_stats.py --snapshot --update-frontmatters
    python import_xlsx_stats.py "C:/Users/silli/Downloads/Contenu_2026-01-04_2026-04-03_ThomasSilliard.xlsx" --snapshot
"""

import sys
import os
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime, date, timedelta
import re
import glob
import argparse

# ─── Paths ────────────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_ROOT, "posts")
ANALYTICS_FILE = os.path.join(POSTS_DIR, "analytics-data.md")  # legacy

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"

# ─── XLSX Parsing ─────────────────────────────────────────────────────────────

def read_shared_strings(z):
    with z.open("xl/sharedStrings.xml") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        strings = []
        for si in root.findall(f"{{{NS}}}si"):
            text = "".join(t.text or "" for t in si.iter(f"{{{NS}}}t"))
            strings.append(text)
    return strings


def parse_sheet(z, sheet_name, strings):
    """Parse a sheet and return list of dicts {col_letter: value}"""
    with z.open(f"xl/worksheets/{sheet_name}.xml") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        rows = []
        for row in root.findall(f".//{{{NS}}}row"):
            row_data = {}
            for cell in row.findall(f"{{{NS}}}c"):
                ref = cell.get("r")
                col = re.sub(r"\d", "", ref)
                t = cell.get("t")
                v_el = cell.find(f"{{{NS}}}v")
                if v_el is not None and v_el.text is not None:
                    val = strings[int(v_el.text)] if t == "s" else v_el.text
                    row_data[col] = val.strip()
            if row_data:
                rows.append(row_data)
    return rows


def parse_date(s):
    """Parse DD/MM/YYYY to date object"""
    try:
        return datetime.strptime(s.strip(), "%d/%m/%Y").date()
    except:
        return None


def clean_url(url):
    """Normalize LinkedIn URL"""
    url = url.strip()
    # Sometimes LinkedIn exports the URL with trailing params
    url = url.split("?")[0]
    return url

# ─── Sheet parsing ─────────────────────────────────────────────────────────────

def parse_global_stats(rows):
    """Sheet1: impressions totales + membres uniques"""
    result = {}
    for row in rows:
        a = row.get("A", "")
        b = row.get("B", "")
        if "Impressions" in a:
            result["impressions_totales"] = int(float(b)) if b else 0
        elif "Membres" in a:
            result["membres_uniques"] = int(float(b)) if b else 0
        elif "Performance globale" in a:
            result["periode"] = b
    return result


def parse_posts(rows):
    """
    Sheet3: deux tableaux côte à côte
    Gauche (A/B/C): URL | Date | Interactions  — trié par interactions
    Droite (E/F/G): URL | Date | Impressions   — trié par impressions
    """
    posts_by_url = {}

    for row in rows:
        # Tableau gauche
        url_a = clean_url(row.get("A", ""))
        date_b = parse_date(row.get("B", ""))
        inter_c = row.get("C", "")

        if url_a.startswith("https://www.linkedin.com") and date_b:
            if url_a not in posts_by_url:
                posts_by_url[url_a] = {"url": url_a, "date": date_b}
            try:
                posts_by_url[url_a]["interactions"] = int(float(inter_c))
            except:
                pass

        # Tableau droit
        url_e = clean_url(row.get("E", ""))
        date_f = parse_date(row.get("F", ""))
        imp_g = row.get("G", "")

        if url_e.startswith("https://www.linkedin.com") and date_f:
            if url_e not in posts_by_url:
                posts_by_url[url_e] = {"url": url_e, "date": date_f}
            try:
                posts_by_url[url_e]["impressions"] = int(float(imp_g))
            except:
                pass

    return list(posts_by_url.values())


def parse_followers(rows):
    """Sheet4: total followers + croissance par jour"""
    total = 0
    daily = {}
    in_table = False

    for row in rows:
        a = row.get("A", "")
        b = row.get("B", "")

        if "Nombre total" in a:
            try:
                total = int(float(b))
            except:
                pass

        # Detect table header
        if "Date" in a and "abonn" in b.lower():
            in_table = True
            continue

        if in_table:
            d = parse_date(a)
            if d:
                try:
                    v = int(float(b))
                    if v > 0:
                        daily[d] = v
                except:
                    pass

    return {"total": total, "daily": daily}


def parse_demographics(rows):
    """Sheet5: données démographiques"""
    demos = {}
    current_dim = None

    for row in rows:
        a = row.get("A", "")
        b = row.get("B", "")
        c = row.get("C", "")

        if a and not b and not c:
            current_dim = a
            demos[current_dim] = []
        elif current_dim and b and c:
            try:
                pct = round(float(c) * 100, 1)
                demos[current_dim].append({"label": b, "pct": pct})
            except:
                pass

    return demos

# ─── Slug matching ─────────────────────────────────────────────────────────────

def load_post_frontmatters():
    """Load all post frontmatters from posts/ directory"""
    posts = []
    for slug_dir in sorted(os.listdir(POSTS_DIR)):
        slug_path = os.path.join(POSTS_DIR, slug_dir)
        if not os.path.isdir(slug_path):
            continue
        md_file = os.path.join(slug_path, f"{slug_dir}.md")
        if not os.path.exists(md_file):
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter fields
        fm = {}
        fm["slug"] = slug_dir
        fm["file"] = md_file
        fm["content"] = content

        for field in ["planned_date", "status", "linkedin_url", "slot", "type"]:
            m = re.search(rf'^{field}:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
            if m:
                fm[field] = m.group(1).strip()

        if "planned_date" in fm:
            fm["planned_date_obj"] = parse_date(
                fm["planned_date"].replace("-", "/").replace('"', '')
            )
            if fm["planned_date_obj"] is None:
                # Try ISO format
                try:
                    fm["planned_date_obj"] = date.fromisoformat(
                        fm["planned_date"].strip().strip('"')
                    )
                except:
                    pass

        posts.append(fm)

    return posts


def match_posts_to_slugs(xlsx_posts, frontmatters):
    """
    Match each XLSX post (by publication date) to a slug.
    Strategy: try exact match on planned_date, then ±1 day.
    Flag MANUAL_CHECK if ambiguous (multiple slugs match same date).
    """
    results = []

    for xpost in xlsx_posts:
        pub_date = xpost["date"]
        candidates = []

        for fm in frontmatters:
            pd = fm.get("planned_date_obj")
            if pd is None:
                continue
            # Match within ±1 day
            if abs((pub_date - pd).days) <= 1:
                candidates.append(fm)

        if len(candidates) == 1:
            xpost["slug"] = candidates[0]["slug"]
            xpost["slug_file"] = candidates[0]["file"]
            xpost["planned_date"] = candidates[0].get("planned_date", "")
            xpost["match"] = "HIGH"
            xpost["fm"] = candidates[0]
        elif len(candidates) > 1:
            # Multiple candidates — pick "Publié" or "Programmé" ones first
            published = [c for c in candidates if c.get("status") in ("Publié", "Programmé", "Prêt")]
            if len(published) == 1:
                xpost["slug"] = published[0]["slug"]
                xpost["slug_file"] = published[0]["file"]
                xpost["planned_date"] = published[0].get("planned_date", "")
                xpost["match"] = "MEDIUM"
                xpost["fm"] = published[0]
            else:
                xpost["slug"] = "MANUAL_CHECK"
                xpost["match"] = "AMBIGUOUS"
                xpost["candidates"] = [c["slug"] for c in candidates]
                xpost["fm"] = None
        else:
            xpost["slug"] = "MANUAL_CHECK"
            xpost["match"] = "NO_MATCH"
            xpost["fm"] = None

        results.append(xpost)

    return results

# ─── Metrics ──────────────────────────────────────────────────────────────────

def compute_metrics(posts, snapshot_date):
    """Add age_days, ImpAdj7j, engagement_rate, tier to each post"""
    import math

    for p in posts:
        pub = p.get("date")
        if pub:
            p["age_days"] = (snapshot_date - pub).days
        else:
            p["age_days"] = 0

        imp = p.get("impressions", 0)
        age = max(p["age_days"], 1)

        if age >= 28:
            p["imp_adj7j"] = imp
            p["adj_flag"] = "mature"
        elif age < 7:
            p["imp_adj7j"] = round(imp * (7 / age))
            p["adj_flag"] = "provisoire"
        else:
            p["imp_adj7j"] = round(imp * (7 / age))
            p["adj_flag"] = "actif"

        inter = p.get("interactions", 0)
        if imp > 0:
            p["engagement_rate"] = round(inter / imp * 100, 2)
        else:
            p["engagement_rate"] = 0.0

    # Compute tiers based on ImpAdj7j distribution
    # Reference = mature + actif posts (age >= 7j). Provisoires included in tier
    # assignment using same thresholds — ImpAdj7j already normalizes for time.
    eligible = [p for p in posts if p.get("adj_flag") != "provisoire" and p.get("imp_adj7j", 0) > 0]
    if len(eligible) >= 3:
        vals = [p["imp_adj7j"] for p in eligible]
        mean = sum(vals) / len(vals)
        variance = sum((v - mean) ** 2 for v in vals) / len(vals)
        sigma = math.sqrt(variance)
        tier_a = mean + 0.5 * sigma
        tier_c = mean - 0.5 * sigma
        tier_d = mean - 1.5 * sigma

        def assign_tier(adj):
            if adj >= tier_a: return "A"
            elif adj >= tier_c: return "B"
            elif adj >= tier_d: return "C"
            else: return "D"

        for p in posts:
            adj = p.get("imp_adj7j", 0)
            if adj > 0:
                p["tier"] = assign_tier(adj)
            else:
                p["tier"] = ""
    else:
        for p in posts:
            p["tier"] = ""

    return posts

# ─── Followers spikes ─────────────────────────────────────────────────────────

def get_follower_spikes(daily, top_n=5):
    """Return top N days of follower gains"""
    sorted_days = sorted(daily.items(), key=lambda x: x[1], reverse=True)
    return sorted_days[:top_n]

# ─── Report generation ────────────────────────────────────────────────────────

def generate_report(global_stats, posts, followers, demographics, snapshot_date):
    lines = []
    lines.append(f"# LinkedIn Analytics — Snapshot {snapshot_date.strftime('%Y-%m-%d')}")
    lines.append(f"")
    lines.append(f"> Snapshot généré le {snapshot_date.strftime('%Y-%m-%d')} via export XLSX LinkedIn.")
    lines.append(f"> Fichier en lecture seule — ne pas modifier manuellement.")
    lines.append(f"> API LinkedIn Community Management : **en attente d'approbation** — sync automatique disponible dès approbation.")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # ── Stats globales ──
    lines.append(f"## Stats globales (snapshot {snapshot_date.strftime('%d/%m/%Y')})")
    lines.append(f"")
    lines.append(f"| Métrique | Valeur |")
    lines.append(f"|---|---|")
    periode = global_stats.get("periode", "")
    lines.append(f"| Période | {periode} |")
    lines.append(f"| Impressions totales | {global_stats.get('impressions_totales', '—')} |")
    lines.append(f"| Membres uniques atteints | {global_stats.get('membres_uniques', '—')} |")
    lines.append(f"| Followers au {snapshot_date.strftime('%d/%m/%Y')} | {followers.get('total', '—')} |")
    matched = [p for p in posts if p.get("match") in ("HIGH", "MEDIUM")]
    lines.append(f"| Posts matchés | {len(matched)} |")
    # Computed averages from eligible posts
    eligible = [p for p in posts if p.get("adj_flag") != "provisoire" and p.get("imp_adj7j", 0) > 0]
    if eligible:
        er_moy = round(sum(p.get("engagement_rate", 0) for p in eligible) / len(eligible), 2)
        imp_moy = round(sum(p.get("imp_adj7j", 0) for p in eligible) / len(eligible))
        lines.append(f"| EngagementRate moyen | {er_moy}% |")
        lines.append(f"| Impressions moyennes / post | {imp_moy} |")
    lines.append(f"| Dernière sync | {snapshot_date.strftime('%Y-%m-%d')} (XLSX manuel) |")
    lines.append(f"| Prochaine sync | via Workflow A dès API approuvée |")
    lines.append(f"")

    # ── Followers growth ──
    lines.append(f"## Croissance followers")
    lines.append(f"")
    lines.append(f"- Total au {snapshot_date.strftime('%d/%m/%Y')} : {followers.get('total', '—')}")
    spikes = get_follower_spikes(followers.get("daily", {}), top_n=5)
    if spikes:
        spike_str = ", ".join(f"{d.strftime('%d/%m')} +{v}" for d, v in spikes)
        lines.append(f"- Pics notables (top 5) : {spike_str}")
    lines.append(f"")

    # ── Démographie ──
    lines.append(f"## Démographie audience (snapshot {snapshot_date.strftime('%d/%m/%Y')})")
    lines.append(f"")
    lines.append(f"| Dimension | Top valeurs |")
    lines.append(f"|---|---|")
    for dim, items in demographics.items():
        if not items:
            continue
        top = ", ".join(f"{x['label']} ({x['pct']}%)" for x in items[:3])
        lines.append(f"| {dim} | {top} |")
    lines.append(f"")

    # ── Posts table ──
    lines.append(f"## Posts (chronologique)")
    lines.append(f"")
    lines.append(f"| Date pub | Slug | Type | Impressions | Interactions | EngRate% | ImpAdj7j | Flag | Tier | linkedin_url |")
    lines.append(f"| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    # Sort by publication date
    sorted_posts = sorted(posts, key=lambda p: p.get("date") or date.min)

    for p in sorted_posts:
        slug = p.get("slug", "MANUAL_CHECK")
        fm = p.get("fm") or {}
        pub_date = p["date"].strftime("%Y-%m-%d") if p.get("date") else "—"
        ptype = fm.get("type", "—")
        imp = p.get("impressions", "—")
        inter = p.get("interactions", "—")
        er = p.get("engagement_rate", "—")
        adj = p.get("imp_adj7j", "—")
        flag = p.get("adj_flag", "—")
        url = p.get("url", "")

        if slug == "MANUAL_CHECK":
            candidates = p.get("candidates", [])
            slug_display = f"MANUAL_CHECK ({', '.join(candidates)})" if candidates else "MANUAL_CHECK"
        else:
            slug_display = slug

        tier = p.get("tier", "")
        lines.append(f"| {pub_date} | {slug_display} | {ptype} | {imp} | {inter} | {er} | {adj} | {flag} | {tier} | {url} |")

    lines.append(f"")

    # ── Règles éditoriales ── (preserved from existing file, placeholder)
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Règles éditoriales actives")
    lines.append(f"")
    lines.append(f"> Voir `.private/projects/productivity/linkedin_auto/WRITING_RULES.md` pour le détail complet.")
    lines.append(f"> Lancer `/analyze-stats` pour calculer les verdicts des règles EN TEST.")
    lines.append(f"")

    return "\n".join(lines)


def generate_disambiguation_report(posts):
    """Print a summary of matching results for review"""
    print("\n=== RAPPORT DE MATCHING URL -> SLUG ===\n")
    print(f"{'Date':<12} {'Slug':<45} {'Imp':>6} {'Inter':>6} {'Match':<12}")
    print("-" * 90)
    for p in sorted(posts, key=lambda x: x.get("date") or date.min):
        pub = p["date"].strftime("%d/%m/%Y") if p.get("date") else "—"
        slug = p.get("slug", "MANUAL_CHECK")
        if len(slug) > 44:
            slug = slug[:41] + "..."
        imp = p.get("impressions", "—")
        inter = p.get("interactions", "—")
        match = p.get("match", "—")
        print(f"{pub:<12} {slug:<45} {str(imp):>6} {str(inter):>6} {match:<12}")
        if match in ("AMBIGUOUS", "NO_MATCH"):
            candidates = p.get("candidates", [])
            if candidates:
                print(f"{'':>12}  Candidats : {', '.join(candidates)}")
            print(f"{'':>12}  URL : {p.get('url', '')}")
    print()


# ─── Frontmatter update ────────────────────────────────────────────────────────

def update_frontmatter_linkedin_url(fm, url):
    """Add or update linkedin_url field in post frontmatter file"""
    content = fm["content"]
    file_path = fm["file"]

    # Check if linkedin_url field exists
    if re.search(r"^linkedin_url:", content, re.MULTILINE):
        # Update existing (even if empty)
        new_content = re.sub(
            r'^linkedin_url:.*$',
            f'linkedin_url: "{url}"',
            content,
            flags=re.MULTILINE
        )
    else:
        # Insert after slot: field
        new_content = re.sub(
            r'^(slot:.*?)$',
            f'\\1\nlinkedin_url: "{url}"',
            content,
            flags=re.MULTILINE
        )
        # Fallback: insert after planned_date if no slot field
        if "linkedin_url" not in new_content:
            new_content = re.sub(
                r'^(planned_date:.*?)$',
                f'\\1\nlinkedin_url: "{url}"',
                content,
                flags=re.MULTILINE
            )

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Import LinkedIn XLSX stats")
    parser.add_argument("xlsx_path", nargs="?", help="Path to XLSX file")
    parser.add_argument("--snapshot-date", help="Snapshot date YYYY-MM-DD (default: today)")
    parser.add_argument("--print", action="store_true", dest="do_print", help="Print report")
    parser.add_argument("--snapshot", action="store_true", help="Write posts/analytics-YYYY-MM-DD.md (dated snapshot)")
    parser.add_argument("--write", action="store_true", help="Alias for --snapshot (legacy)")
    parser.add_argument("--update-frontmatters", action="store_true", help="Update linkedin_url in post frontmatters")
    args = parser.parse_args()

    # --write is now an alias for --snapshot
    if args.write:
        args.snapshot = True

    # Default: print if no write/snapshot flag
    if not args.snapshot and not args.update_frontmatters:
        args.do_print = True

    # Snapshot date
    if args.snapshot_date:
        snapshot_date = date.fromisoformat(args.snapshot_date)
    else:
        snapshot_date = date.today()

    # XLSX path
    xlsx_path = args.xlsx_path
    if not xlsx_path:
        # Try to find most recent in Downloads
        downloads = os.path.expanduser("~/Downloads")
        candidates = glob.glob(os.path.join(downloads, "Contenu_*.xlsx"))
        if candidates:
            xlsx_path = max(candidates, key=os.path.getmtime)
            print(f"Auto-detected XLSX: {xlsx_path}")
        else:
            print("ERROR: No XLSX file found. Provide path as argument.")
            sys.exit(1)

    if not os.path.exists(xlsx_path):
        print(f"ERROR: File not found: {xlsx_path}")
        sys.exit(1)

    print(f"Reading {xlsx_path}...")

    # Parse XLSX
    with zipfile.ZipFile(xlsx_path, "r") as z:
        strings = read_shared_strings(z)

        # Detect sheet names
        with z.open("xl/workbook.xml") as f:
            wb_tree = ET.parse(f)
            wb_root = wb_tree.getroot()
            sheets = {}
            for i, sheet in enumerate(wb_root.findall(f".//{{{NS}}}sheet"), start=1):
                name = sheet.get("name", f"sheet{i}")
                sheets[i] = name

        sheet1_rows = parse_sheet(z, "sheet1", strings)
        sheet2_rows = parse_sheet(z, "sheet2", strings)
        sheet3_rows = parse_sheet(z, "sheet3", strings)
        sheet4_rows = parse_sheet(z, "sheet4", strings)
        sheet5_rows = parse_sheet(z, "sheet5", strings)

    global_stats = parse_global_stats(sheet1_rows)
    xlsx_posts = parse_posts(sheet3_rows)
    followers = parse_followers(sheet4_rows)
    demographics = parse_demographics(sheet5_rows)

    print(f"Posts trouvés dans XLSX : {len(xlsx_posts)}")

    # Load frontmatters
    frontmatters = load_post_frontmatters()
    print(f"Posts trouvés dans repo : {len(frontmatters)}")

    # Match URLs to slugs
    matched_posts = match_posts_to_slugs(xlsx_posts, frontmatters)

    # Compute metrics
    matched_posts = compute_metrics(matched_posts, snapshot_date)

    # Show disambiguation report
    generate_disambiguation_report(matched_posts)

    manual_checks = [p for p in matched_posts if p.get("match") in ("MANUAL_CHECK", "AMBIGUOUS", "NO_MATCH")]
    if manual_checks:
        print(f"/!\\ {len(manual_checks)} post(s) necessitent une verification manuelle (marques MANUAL_CHECK)")
        print()

    # Generate report
    report = generate_report(global_stats, matched_posts, followers, demographics, snapshot_date)

    if args.do_print:
        print("\n=== RAPPORT ANALYTICS ===\n")
        print(report)

    if args.snapshot:
        snapshot_filename = f"analytics-{snapshot_date.strftime('%Y-%m-%d')}.md"
        snapshot_path = os.path.join(POSTS_DIR, snapshot_filename)
        if os.path.exists(snapshot_path):
            print(f"/!\\ Snapshot existant : {snapshot_path}")
            print("    Utilise --snapshot-date pour spécifier une autre date, ou supprime le fichier manuellement.")
        else:
            with open(snapshot_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"OK snapshot créé : {snapshot_path}")

    if args.update_frontmatters:
        updated = 0
        skipped = 0
        for p in matched_posts:
            if p.get("match") in ("HIGH", "MEDIUM") and p.get("fm"):
                url = p.get("url", "")
                if url:
                    changed = update_frontmatter_linkedin_url(p["fm"], url)
                    if changed:
                        updated += 1
                        print(f"  OK {p['slug']} -> linkedin_url mis a jour")
                    else:
                        skipped += 1
                        print(f"  -- {p['slug']} -> deja a jour")
        print(f"\nOK {updated} frontmatters mis a jour, {skipped} deja a jour.")


if __name__ == "__main__":
    main()
