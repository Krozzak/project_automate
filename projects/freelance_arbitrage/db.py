"""SQLite database layer for missions."""

import sqlite3
from contextlib import contextmanager
from pathlib import Path

from scrapers.parser import Mission

DB_PATH = Path(__file__).parent / "data" / "missions.db"

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS missions (
    id TEXT PRIMARY KEY,
    platform TEXT,
    title TEXT,
    description TEXT,
    budget_min REAL,
    budget_max REAL,
    nb_proposals INTEGER,
    posted_at DATETIME,
    scraped_at DATETIME,
    category TEXT,
    url TEXT,
    client_rating REAL,
    feasibility_score INTEGER,
    build_score INTEGER,
    urgency_score INTEGER,
    competition_score INTEGER,
    budget_score INTEGER,
    total_score INTEGER,
    tool_match TEXT,
    estimated_delivery_minutes INTEGER,
    scoring_reasoning TEXT,
    alerted INTEGER DEFAULT 0,
    proposal_sent INTEGER DEFAULT 0,
    result TEXT
);
"""


@contextmanager
def get_db(path: Path = DB_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def init_db(path: Path = DB_PATH) -> None:
    with get_db(path) as conn:
        conn.execute(CREATE_TABLE)
        conn.commit()


def upsert_mission(mission: Mission, path: Path = DB_PATH) -> bool:
    """Insert or update a mission. Returns True if inserted (new), False if updated."""
    d = mission.to_dict()
    columns = ", ".join(d.keys())
    placeholders = ", ".join(["?"] * len(d))
    update_clause = ", ".join([f"{k} = excluded.{k}" for k in d.keys() if k != "id"])

    sql = f"""
    INSERT INTO missions ({columns}) VALUES ({placeholders})
    ON CONFLICT(id) DO UPDATE SET {update_clause}
    """

    with get_db(path) as conn:
        cursor = conn.execute(sql, list(d.values()))
        conn.commit()
        return cursor.rowcount > 0


def get_unalerted_high_scores(threshold: int, path: Path = DB_PATH) -> list[dict]:
    with get_db(path) as conn:
        rows = conn.execute(
            "SELECT * FROM missions WHERE total_score >= ? AND alerted = 0 ORDER BY total_score DESC",
            (threshold,)
        ).fetchall()
        return [dict(row) for row in rows]


def mark_alerted(mission_id: str, path: Path = DB_PATH) -> None:
    with get_db(path) as conn:
        conn.execute("UPDATE missions SET alerted = 1 WHERE id = ?", (mission_id,))
        conn.commit()


def get_today_stats(path: Path = DB_PATH) -> dict:
    with get_db(path) as conn:
        scraped = conn.execute("SELECT COUNT(*) FROM missions WHERE date(scraped_at) = date('now')").fetchone()[0]
        alerted = conn.execute("SELECT COUNT(*) FROM missions WHERE alerted = 1 AND date(scraped_at) = date('now')").fetchone()[0]
        proposals_sent = conn.execute("SELECT COUNT(*) FROM missions WHERE proposal_sent = 1").fetchone()[0]
        hired = conn.execute("SELECT COUNT(*) FROM missions WHERE result = 'hired'").fetchone()[0]

    return {"scraped": scraped, "alerted": alerted, "proposals_sent": proposals_sent, "hired": hired, "revenue": 0}
