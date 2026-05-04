#!/usr/bin/env python3
"""
sync_calendar.py — Synchronise le calendrier de publication avec les frontmatters des posts.

Usage:
    python sync_calendar.py --create-stubs calendar_2026_Q2.json
    python sync_calendar.py --clear-dates SLUG1 SLUG2 ...
    python sync_calendar.py --fix-status SLUG=STATUS ...

Modes:
    --create-stubs FILE     Crée les dossiers et fichiers .md manquants depuis un JSON de définitions
    --clear-dates SLUG...   Vide la planned_date des posts spécifiés (→ section pending)
    --fix-status SLUG=S...  Force un status sur un post spécifique (ex: 2026-04-20-proofslab=Publié)
    --dry-run               Affiche les changements sans les appliquer

Exemples:
    python scripts/sync_calendar.py --create-stubs scripts/calendar_2026_Q2.json
    python scripts/sync_calendar.py --clear-dates 2026-04-22-claude-design-proofslab 2026-04-02-memory-logger-outputs
    python scripts/sync_calendar.py --fix-status 2026-04-20-proofslab-approbation-visuels=Publié
"""

import sys
import os
import json
import re
import argparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_ROOT, "posts")

FRONTMATTER_TEMPLATE = """\
---
title: "{title}"
slug: "{slug}"
type: {type}
projet: "{projet}"
status: {status}
planned_date: "{planned_date}"
slot: {slot}
linkedin_url: ""
concept: ""
tags: []
---

## Post LinkedIn

> À rédiger
"""


def find_post_file(slug):
    """Return path to the .md file for a given slug, or None if not found."""
    post_dir = os.path.join(POSTS_DIR, slug)
    post_file = os.path.join(post_dir, f"{slug}.md")
    if os.path.exists(post_file):
        return post_file
    return None


def create_stub(entry, dry_run=False):
    """Create a post directory and minimal .md file from a definition dict."""
    slug = entry["slug"]
    post_dir = os.path.join(POSTS_DIR, slug)
    post_file = os.path.join(post_dir, f"{slug}.md")

    if os.path.exists(post_file):
        print(f"  -- {slug} -> deja existant, skip")
        return False

    title = entry.get("titre", entry.get("title", "À compléter"))
    ptype = entry.get("type", "AUTOMATISATION")
    projet = entry.get("projet", "")
    status = entry.get("status", "À rédiger")
    planned_date = entry.get("planned_date", "")
    slot = entry.get("slot", "")

    content = FRONTMATTER_TEMPLATE.format(
        title=title,
        slug=slug,
        type=ptype,
        projet=projet,
        status=status,
        planned_date=planned_date,
        slot=slot,
    )

    if dry_run:
        print(f"  [DRY-RUN] Créerait {post_file}")
        return True

    os.makedirs(post_dir, exist_ok=True)
    with open(post_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK créé {post_file}")
    return True


def clear_planned_date(slug, dry_run=False):
    """Remove or empty the planned_date field in a post's frontmatter."""
    post_file = find_post_file(slug)
    if not post_file:
        print(f"  /!\\ {slug} -> fichier introuvable, skip")
        return False

    with open(post_file, "r", encoding="utf-8") as f:
        content = f.read()

    if not re.search(r'^planned_date:', content, re.MULTILINE):
        print(f"  -- {slug} -> pas de planned_date, skip")
        return False

    new_content = re.sub(
        r'^planned_date:.*$',
        'planned_date: ""',
        content,
        flags=re.MULTILINE
    )

    if new_content == content:
        print(f"  -- {slug} -> planned_date deja vide")
        return False

    if dry_run:
        print(f"  [DRY-RUN] Viderait planned_date de {slug}")
        return True

    with open(post_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  OK {slug} -> planned_date vidée")
    return True


def fix_status(slug, new_status, dry_run=False):
    """Force a specific status on a post."""
    post_file = find_post_file(slug)
    if not post_file:
        print(f"  /!\\ {slug} -> fichier introuvable, skip")
        return False

    with open(post_file, "r", encoding="utf-8") as f:
        content = f.read()

    if not re.search(r'^status:', content, re.MULTILINE):
        print(f"  -- {slug} -> pas de champ status, skip")
        return False

    new_content = re.sub(
        r'^status:.*$',
        f'status: {new_status}',
        content,
        flags=re.MULTILINE
    )

    if new_content == content:
        print(f"  -- {slug} -> status deja '{new_status}'")
        return False

    if dry_run:
        print(f"  [DRY-RUN] Mettrait status='{new_status}' sur {slug}")
        return True

    with open(post_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  OK {slug} -> status mis à jour: {new_status}")
    return True


def run_create_stubs(json_path, dry_run=False):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    stubs = data.get("create_stubs", [])
    if not stubs:
        print("Aucun stub à créer.")
        return

    print(f"\n=== CREATE STUBS ({len(stubs)} posts) ===\n")
    created = 0
    for entry in stubs:
        if create_stub(entry, dry_run=dry_run):
            created += 1
    print(f"\nOK {created}/{len(stubs)} posts créés.")


def run_clear_dates_from_json(json_path, dry_run=False):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    slugs = data.get("clear_planned_date", [])
    if not slugs:
        print("Aucune date à vider.")
        return

    print(f"\n=== CLEAR PLANNED DATES ({len(slugs)} posts) ===\n")
    cleared = 0
    for slug in slugs:
        if clear_planned_date(slug, dry_run=dry_run):
            cleared += 1
    print(f"\nOK {cleared}/{len(slugs)} dates vidées.")


def run_fix_status_from_json(json_path, dry_run=False):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    fixes = data.get("fix_status", [])
    if not fixes:
        return

    print(f"\n=== FIX STATUS ({len(fixes)} posts) ===\n")
    fixed = 0
    for item in fixes:
        if fix_status(item["slug"], item["status"], dry_run=dry_run):
            fixed += 1
    print(f"\nOK {fixed}/{len(fixes)} statuts corrigés.")


def main():
    parser = argparse.ArgumentParser(description="Synchronise le calendrier de publication")
    parser.add_argument("--create-stubs", metavar="JSON_FILE", help="Crée les posts manquants depuis un fichier JSON")
    parser.add_argument("--clear-dates", nargs="+", metavar="SLUG", help="Vide la planned_date des slugs spécifiés")
    parser.add_argument("--fix-status", nargs="+", metavar="SLUG=STATUS", help="Force un status (ex: slug=Publié)")
    parser.add_argument("--from-json", metavar="JSON_FILE", help="Applique create_stubs + clear_planned_date + fix_status depuis un fichier JSON")
    parser.add_argument("--dry-run", action="store_true", help="Affiche les changements sans les appliquer")
    args = parser.parse_args()

    if args.dry_run:
        print("[DRY-RUN mode activé — aucun fichier ne sera modifié]\n")

    if args.from_json:
        run_clear_dates_from_json(args.from_json, dry_run=args.dry_run)
        run_fix_status_from_json(args.from_json, dry_run=args.dry_run)
        run_create_stubs(args.from_json, dry_run=args.dry_run)
        return

    if args.create_stubs:
        run_create_stubs(args.create_stubs, dry_run=args.dry_run)

    if args.clear_dates:
        print(f"\n=== CLEAR PLANNED DATES ({len(args.clear_dates)} posts) ===\n")
        cleared = 0
        for slug in args.clear_dates:
            if clear_planned_date(slug, dry_run=args.dry_run):
                cleared += 1
        print(f"\nOK {cleared}/{len(args.clear_dates)} dates vidées.")

    if args.fix_status:
        print(f"\n=== FIX STATUS ({len(args.fix_status)} posts) ===\n")
        fixed = 0
        for item in args.fix_status:
            if "=" not in item:
                print(f"  /!\\ Format invalide '{item}' — attendu: SLUG=STATUS")
                continue
            slug, status = item.split("=", 1)
            if fix_status(slug.strip(), status.strip(), dry_run=args.dry_run):
                fixed += 1
        print(f"\nOK {fixed} statuts corrigés.")


if __name__ == "__main__":
    main()
