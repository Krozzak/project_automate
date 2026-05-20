"""
Fiverr Buyer Requests scraper via Apify actor.
Fallback: Playwright-based direct scraper (V2).

Apify actor: automation-lab/fiverr-scraper
Requires APIFY_API_TOKEN in .env.
"""

import hashlib
import os
from datetime import datetime
from typing import Optional

import aiohttp
from dotenv import load_dotenv

from .parser import Mission

load_dotenv()

APIFY_BASE_URL = "https://api.apify.com/v2"
FIVERR_ACTOR = "automation-lab~fiverr-scraper"

SEARCH_QUERIES = [
    {"q": "translate ebook french", "category": "translation"},
    {"q": "translate pdf french", "category": "translation"},
    {"q": "compare pdf differences", "category": "data-entry"},
    {"q": "transcribe audio", "category": "video-audio"},
    {"q": "summarize document", "category": "writing"},
    {"q": "extract data pdf", "category": "data-entry"},
    {"q": "clean spreadsheet data", "category": "data-entry"},
]


async def scrape_fiverr(max_results_per_query: int = 10) -> list[Mission]:
    api_token = os.getenv("APIFY_API_TOKEN")
    if not api_token:
        print("[fiverr] APIFY_API_TOKEN not set — skipping Fiverr scraping")
        return []

    missions = []

    async with aiohttp.ClientSession() as session:
        for config in SEARCH_QUERIES:
            print(f"[fiverr] Scraping: {config['q']}")
            try:
                raw_results = await _apify_run(session, api_token, config["q"], max_results_per_query)
                page_missions = [_parse_apify_result(r, config["category"]) for r in raw_results]
                page_missions = [m for m in page_missions if m is not None]
                missions.extend(page_missions)
                print(f"[fiverr] Found {len(page_missions)} results for '{config['q']}'")
            except Exception as e:
                print(f"[fiverr] Error on '{config['q']}': {e}")

    return _deduplicate(missions)


async def _apify_run(session: aiohttp.ClientSession, api_token: str, query: str, max_items: int) -> list[dict]:
    run_url = f"{APIFY_BASE_URL}/acts/{FIVERR_ACTOR}/run-sync-get-dataset-items"
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {
        "search": query,
        "maxItems": max_items,
        "type": "buyer-requests",  # section Buyer Requests — moins connue, moins compétitive
    }

    async with session.post(run_url, json=payload, headers=headers, timeout=aiohttp.ClientTimeout(total=120)) as resp:
        if resp.status != 200:
            text = await resp.text()
            raise ValueError(f"Apify error {resp.status}: {text[:200]}")
        return await resp.json()


def _parse_apify_result(raw: dict, category: str) -> Optional[Mission]:
    title = raw.get("title", "").strip()
    if not title:
        return None

    url = raw.get("url", "")
    description = raw.get("description", "")[:2000]
    budget = raw.get("budget")
    budget_min = budget_max = None
    if isinstance(budget, (int, float)):
        budget_min = budget_max = float(budget)
    elif isinstance(budget, dict):
        budget_min = budget.get("min")
        budget_max = budget.get("max")

    posted_at = None
    if raw.get("postedAt"):
        try:
            posted_at = datetime.fromisoformat(raw["postedAt"].replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            pass

    mission_id = hashlib.md5(f"fiverr{url}".encode()).hexdigest()[:16]

    return Mission(
        id=mission_id,
        platform="fiverr",
        title=title,
        description=description,
        budget_min=budget_min,
        budget_max=budget_max,
        nb_proposals=raw.get("offersCount"),
        posted_at=posted_at,
        category=category,
        url=url,
        client_rating=None,
    )


def _deduplicate(missions: list[Mission]) -> list[Mission]:
    seen = set()
    unique = []
    for m in missions:
        if m.id not in seen:
            seen.add(m.id)
            unique.append(m)
    return unique
