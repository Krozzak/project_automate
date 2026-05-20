"""
Freelance Arbitrage Agent — entry point.

Usage:
    python main.py           # Lance un scan complet (Upwork + Fiverr)
    python main.py --scan    # Idem
    python main.py --stats   # Affiche les stats du jour via Telegram
    python main.py --daemon  # Boucle continue (scan toutes les N heures)
"""

import asyncio
import sys
from pathlib import Path

import toml
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = Path(__file__).parent / "config.toml"


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return toml.load(CONFIG_PATH)
    return {}


async def run_scan(config: dict) -> None:
    from scrapers.upwork import scrape_upwork
    from scrapers.fiverr import scrape_fiverr
    from scorer.scorer import score_missions
    from bot.telegram import TelegramBot
    from db import init_db, upsert_mission, get_unalerted_high_scores, mark_alerted

    init_db()
    bot = TelegramBot(config)
    alert_threshold = config.get("scoring", {}).get("alert_threshold", 75)
    max_proposals = config.get("scraper", {}).get("max_proposals_threshold", 10)

    print("[main] Starting Upwork scrape...")
    upwork_missions = await scrape_upwork(max_results_per_query=10)
    print(f"[main] Upwork: {len(upwork_missions)} missions found")

    print("[main] Starting Fiverr scrape...")
    fiverr_missions = await scrape_fiverr(max_results_per_query=10)
    print(f"[main] Fiverr: {len(fiverr_missions)} missions found")

    all_missions = upwork_missions + fiverr_missions

    # Filter out over-competed missions before scoring
    filtered = [m for m in all_missions if (m.nb_proposals or 0) <= max_proposals]
    print(f"[main] After competition filter: {len(filtered)} missions to score")

    print("[main] Scoring...")
    scored = await score_missions(filtered, config)

    print("[main] Saving to DB...")
    for mission in scored:
        upsert_mission(mission)

    print("[main] Checking for high-score alerts...")
    to_alert = get_unalerted_high_scores(alert_threshold)
    print(f"[main] {len(to_alert)} missions above threshold {alert_threshold}")

    for row in to_alert:
        # Convert dict back to object-like for bot
        class MissionObj:
            pass
        m = MissionObj()
        for k, v in row.items():
            setattr(m, k, v)

        sent = await bot.send_alert(m)
        if sent:
            mark_alerted(row["id"])
            print(f"[main] Alert sent for: {row['title'][:60]}")

    print(f"[main] Scan complete. {len(scored)} missions scored, {len(to_alert)} alerts sent.")


async def run_daemon(config: dict) -> None:
    interval_hours = config.get("scraper", {}).get("interval_hours", 2)
    print(f"[main] Daemon mode — scanning every {interval_hours}h")
    while True:
        await run_scan(config)
        print(f"[main] Next scan in {interval_hours}h...")
        await asyncio.sleep(interval_hours * 3600)


async def run_stats(config: dict) -> None:
    from bot.telegram import TelegramBot
    from db import get_today_stats
    bot = TelegramBot(config)
    stats = get_today_stats()
    await bot.send_stats(stats)
    print(f"[main] Stats sent: {stats}")


def main():
    config = load_config()
    args = sys.argv[1:]

    if "--daemon" in args:
        asyncio.run(run_daemon(config))
    elif "--stats" in args:
        asyncio.run(run_stats(config))
    else:
        asyncio.run(run_scan(config))


if __name__ == "__main__":
    main()
