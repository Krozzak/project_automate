"""
Upwork scraper using camoufox (anti-detect Firefox) + Playwright.
Requires real Upwork credentials in .env (UPWORK_EMAIL, UPWORK_PASSWORD).

First run: will open browser for manual login, then saves session cookies.
Subsequent runs: uses saved cookies automatically.
"""

import asyncio
import hashlib
import json
import os
import re
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from .parser import Mission

load_dotenv()

COOKIES_FILE = Path(__file__).parent.parent / "data" / "upwork_cookies.json"

SEARCH_CONFIGS = [
    {"q": "translate ebook french", "category": "translation"},
    {"q": "epub translation french", "category": "translation"},
    {"q": "pdf translation french", "category": "translation"},
    {"q": "compare pdf documents", "category": "data-entry"},
    {"q": "pdf comparison redline", "category": "data-entry"},
    {"q": "document differences", "category": "admin-support"},
    {"q": "transcribe audio interview", "category": "video-audio"},
    {"q": "generate subtitles srt", "category": "video-audio"},
    {"q": "summarize pdf report", "category": "writing"},
    {"q": "extract data from pdf", "category": "data-entry"},
    {"q": "clean csv excel data", "category": "data-entry"},
    {"q": "virtual assistant tasks", "category": "admin-support"},
    {"q": "ai automation workflow", "category": "ai-services"},
]

UPWORK_SEARCH_URL = "https://www.upwork.com/nx/jobs/search/?q={query}&sort=recency&per_page=20"


async def scrape_upwork(max_results_per_query: int = 10) -> list[Mission]:
    try:
        from camoufox.async_api import AsyncCamoufox
    except ImportError:
        raise ImportError("camoufox not installed — run: pip install 'camoufox[geoip]'")

    missions = []

    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        page = await browser.new_page()

        if not await _load_session(page):
            await _login(page)

        for config in SEARCH_CONFIGS:
            url = UPWORK_SEARCH_URL.format(query=config["q"].replace(" ", "%20"))
            print(f"[upwork] Scraping: {config['q']}")

            try:
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(_human_delay(2, 5))

                if await _is_blocked(page):
                    print("[upwork] Blocked — retrying after delay")
                    await asyncio.sleep(30)
                    continue

                page_missions = await _parse_search_results(page, config["category"], max_results_per_query)
                missions.extend(page_missions)
                print(f"[upwork] Found {len(page_missions)} missions for '{config['q']}'")

            except Exception as e:
                print(f"[upwork] Error on '{config['q']}': {e}")
                continue

            await asyncio.sleep(_human_delay(2, 5))

        await _save_session(page)

    return _deduplicate(missions)


async def _login(page) -> None:
    email = os.getenv("UPWORK_EMAIL")
    password = os.getenv("UPWORK_PASSWORD")

    if not email or not password:
        raise ValueError("UPWORK_EMAIL and UPWORK_PASSWORD must be set in .env")

    print("[upwork] Logging in...")
    await page.goto("https://www.upwork.com/login", wait_until="networkidle")
    await asyncio.sleep(2)

    await page.fill("#login_username", email)
    await page.click("#login_password_continue")
    await asyncio.sleep(_human_delay(1, 2))

    await page.fill("#login_password", password)
    await page.click("#login_control_continue")
    await asyncio.sleep(_human_delay(3, 5))

    print("[upwork] Login complete — saving session")
    await _save_session(page)


async def _load_session(page) -> bool:
    if not COOKIES_FILE.exists():
        return False

    with open(COOKIES_FILE) as f:
        cookies = json.load(f)

    await page.context.add_cookies(cookies)
    await page.goto("https://www.upwork.com/nx/find-work/", wait_until="networkidle")
    await asyncio.sleep(2)

    is_logged_in = await page.query_selector("[data-test='nav-logged-in']") is not None
    if is_logged_in:
        print("[upwork] Session restored from cookies")
    return is_logged_in


async def _save_session(page) -> None:
    COOKIES_FILE.parent.mkdir(parents=True, exist_ok=True)
    cookies = await page.context.cookies()
    with open(COOKIES_FILE, "w") as f:
        json.dump(cookies, f)


async def _is_blocked(page) -> bool:
    title = await page.title()
    return "blocked" in title.lower() or "captcha" in title.lower() or "403" in title


async def _parse_search_results(page, category: str, max_results: int) -> list[Mission]:
    missions = []

    job_tiles = await page.query_selector_all("[data-test='job-tile-list'] article")

    for tile in job_tiles[:max_results]:
        try:
            mission = await _parse_job_tile(tile, category)
            if mission:
                missions.append(mission)
        except Exception as e:
            print(f"[upwork] Error parsing tile: {e}")

    return missions


async def _parse_job_tile(tile, category: str) -> Optional[Mission]:
    title_el = await tile.query_selector("[data-test='job-tile-title'] a")
    if not title_el:
        return None

    title = (await title_el.text_content()).strip()
    href = await title_el.get_attribute("href")
    url = f"https://www.upwork.com{href}" if href else ""

    desc_el = await tile.query_selector("[data-test='job-description-text']")
    description = (await desc_el.text_content()).strip() if desc_el else ""

    budget_min, budget_max = await _parse_budget(tile)
    nb_proposals = await _parse_proposals(tile)
    client_rating = await _parse_rating(tile)
    posted_at = await _parse_posted_at(tile)

    mission_id = hashlib.md5(f"upwork{url}".encode()).hexdigest()[:16]

    return Mission(
        id=mission_id,
        platform="upwork",
        title=title,
        description=description[:2000],
        budget_min=budget_min,
        budget_max=budget_max,
        nb_proposals=nb_proposals,
        posted_at=posted_at,
        category=category,
        url=url,
        client_rating=client_rating,
    )


async def _parse_budget(tile) -> tuple[Optional[float], Optional[float]]:
    budget_el = await tile.query_selector("[data-test='budget']")
    if not budget_el:
        return None, None

    text = (await budget_el.text_content()).strip()
    numbers = re.findall(r"[\d,]+\.?\d*", text.replace(",", ""))
    if len(numbers) >= 2:
        return float(numbers[0]), float(numbers[1])
    elif len(numbers) == 1:
        val = float(numbers[0])
        return val, val
    return None, None


async def _parse_proposals(tile) -> Optional[int]:
    prop_el = await tile.query_selector("[data-test='proposals-tier']")
    if not prop_el:
        return None
    text = await prop_el.text_content()
    numbers = re.findall(r"\d+", text)
    return int(numbers[0]) if numbers else None


async def _parse_rating(tile) -> Optional[float]:
    rating_el = await tile.query_selector("[data-test='feedback-rating']")
    if not rating_el:
        return None
    text = await rating_el.text_content()
    numbers = re.findall(r"\d+\.?\d*", text)
    return float(numbers[0]) if numbers else None


async def _parse_posted_at(tile) -> Optional[datetime]:
    time_el = await tile.query_selector("time")
    if not time_el:
        return None

    datetime_attr = await time_el.get_attribute("datetime")
    if datetime_attr:
        try:
            return datetime.fromisoformat(datetime_attr.replace("Z", "+00:00"))
        except ValueError:
            pass

    text = (await time_el.text_content()).lower()
    now = datetime.utcnow()
    if "minute" in text or "hour" in text:
        return now
    elif "yesterday" in text:
        return now - timedelta(days=1)
    elif "day" in text:
        days = int(re.findall(r"\d+", text)[0]) if re.findall(r"\d+", text) else 2
        return now - timedelta(days=days)
    return None


def _human_delay(min_s: float, max_s: float) -> float:
    import random
    return random.uniform(min_s, max_s)


def _deduplicate(missions: list[Mission]) -> list[Mission]:
    seen = set()
    unique = []
    for m in missions:
        if m.id not in seen:
            seen.add(m.id)
            unique.append(m)
    return unique
