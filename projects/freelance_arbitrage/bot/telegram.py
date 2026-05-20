"""
Telegram bot for Freelance Arbitrage Agent.
Sends alerts for high-score missions and handles /proposal /stats /scan commands.
"""

import os
from datetime import datetime

import aiohttp
from dotenv import load_dotenv

load_dotenv()

TOOL_LABELS = {
    "book_translator": "Book Translator",
    "prooflab": "ProofLab",
    "whisper": "Whisper (transcription)",
    "gpt_script": "Script GPT",
    "data_python": "Python data",
    "new_build": "Nouveau build",
    "none": "Aucun",
}


class TelegramBot:
    def __init__(self, config: dict):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN") or config.get("telegram", {}).get("bot_token", "")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID") or config.get("telegram", {}).get("chat_id", "")
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    async def send_alert(self, mission) -> bool:
        if not self.token or not self.chat_id:
            print("[telegram] Bot not configured — skipping alert")
            return False

        age = _format_age(mission.posted_at)
        tool_label = TOOL_LABELS.get(mission.tool_match or "none", "?")
        budget_str = _format_budget(mission.budget_min, mission.budget_max)
        proposals_str = f"{mission.nb_proposals} proposals" if mission.nb_proposals is not None else "?"

        text = (
            f"🎯 Mission score {mission.total_score}/100\n\n"
            f"💰 {budget_str} | 📋 {mission.category} | ⏱ {age}\n"
            f"📊 {proposals_str} déjà soumis\n\n"
            f'"{mission.title[:120]}"\n\n'
            f"🔧 Outil : {tool_label} → livraison estimée {mission.estimated_delivery_minutes or '?'} min\n"
            f"💬 {mission.scoring_reasoning or ''}\n\n"
        )

        if mission.url:
            text += f"🔗 [Voir la mission]({mission.url})\n"
        text += f"👉 /proposal_{mission.id} pour générer le texte"

        return await self._send_message(text, parse_mode="Markdown")

    async def send_stats(self, stats: dict) -> bool:
        text = (
            f"📊 Stats du jour — {datetime.now().strftime('%d/%m/%Y')}\n\n"
            f"🔍 Missions scrapées : {stats.get('scraped', 0)}\n"
            f"⚡ Alertes envoyées : {stats.get('alerted', 0)}\n"
            f"📤 Proposals soumis : {stats.get('proposals_sent', 0)}\n"
            f"✅ Recrutements : {stats.get('hired', 0)}\n"
            f"💰 Revenu : {stats.get('revenue', 0)}$"
        )
        return await self._send_message(text)

    async def send_proposal(self, mission_id: str, proposal_text: str) -> bool:
        text = f"📝 Proposal pour mission `{mission_id}`:\n\n{proposal_text}"
        return await self._send_message(text, parse_mode="Markdown")

    async def _send_message(self, text: str, parse_mode: str = "") -> bool:
        if not self.token or not self.chat_id:
            return False

        payload = {"chat_id": self.chat_id, "text": text, "disable_web_page_preview": False}
        if parse_mode:
            payload["parse_mode"] = parse_mode

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{self.base_url}/sendMessage", json=payload, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                    result = await resp.json()
                    if not result.get("ok"):
                        print(f"[telegram] API error: {result}")
                        return False
                    return True
        except Exception as e:
            print(f"[telegram] Send error: {e}")
            return False


def _format_age(posted_at) -> str:
    if not posted_at:
        return "?"
    from datetime import timezone
    now = datetime.now(timezone.utc)
    if posted_at.tzinfo is None:
        posted_at = posted_at.replace(tzinfo=timezone.utc)
    delta = now - posted_at
    hours = int(delta.total_seconds() / 3600)
    if hours < 1:
        return "< 1h ago"
    elif hours < 24:
        return f"{hours}h ago"
    else:
        return f"{delta.days}d ago"


def _format_budget(budget_min, budget_max) -> str:
    if budget_min is None and budget_max is None:
        return "Budget ?"
    if budget_min == budget_max:
        return f"${int(budget_min)}"
    if budget_min and budget_max:
        return f"${int(budget_min)}-{int(budget_max)}"
    val = budget_max or budget_min
    return f"${int(val)}"
