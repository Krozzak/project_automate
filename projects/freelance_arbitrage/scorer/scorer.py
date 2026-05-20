"""
GPT-4o-mini batch scorer for freelance missions.
Scores feasibility, urgency, competition, budget → total 0-100.
"""

import json
import os
from datetime import datetime, timezone
from typing import Optional

from openai import AsyncOpenAI

from scrapers.parser import Mission

SYSTEM_PROMPT = """Tu es un expert en arbitrage freelance. Tu analyses des missions Upwork/Fiverr pour
déterminer si elles peuvent être résolues rapidement avec des outils IA existants
ou de nouveaux outils simples à builder.

Outils existants disponibles :
- book_translator : traduit un ePUB/PDF complet EN→FR (ou autre langue) en 20 min
- prooflab : compare deux versions d'un PDF et détecte les changements visuellement en 5 min
- gpt_script : résumé, rédaction, extraction, nettoyage de texte en 3-10 min
- whisper : transcription audio/vidéo en 10 min
- data_python : nettoyage CSV/Excel, extraction données PDF en 10 min

Pour chaque mission, réponds en JSON strict (aucun texte autour) :
{
  "feasibility_score": 0,
  "tool_match": "book_translator|prooflab|whisper|gpt_script|data_python|new_build|none",
  "build_score": 0,
  "estimated_delivery_minutes": 20,
  "reasoning": "explication courte"
}

Légende :
- feasibility_score : 0=impossible, 1=possible avec effort, 2=faisable, 3=trivial avec outil existant
- build_score (si tool_match=new_build) : 0=semaines, 1=jours, 2=heures — sinon toujours 0
- estimated_delivery_minutes : temps réel de livraison avec l'outil"""


async def score_missions(missions: list[Mission], config: dict) -> list[Mission]:
    if not missions:
        return []

    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = config.get("openai", {}).get("model", "gpt-4o-mini")
    weights = config.get("scoring", {}).get("weights", {
        "feasibility": 0.4, "urgency": 0.25, "competition": 0.2, "budget": 0.15
    })

    # Batch: send up to 10 missions per call
    batch_size = 10
    for i in range(0, len(missions), batch_size):
        batch = missions[i:i + batch_size]
        await _score_batch(client, model, batch, weights)

    return missions


async def _score_batch(client: AsyncOpenAI, model: str, batch: list[Mission], weights: dict) -> None:
    user_content = "\n\n".join([
        f"Mission {idx + 1}:\nTitre: {m.title}\nDescription: {m.description[:500]}\nBudget: {m.budget_min}-{m.budget_max}$\nProposals: {m.nb_proposals}"
        for idx, m in enumerate(batch)
    ])
    user_content += f"\n\nRéponds avec un tableau JSON : [{{'mission': 1, 'scores': {{...}}}}, ...]"

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ],
            response_format={"type": "json_object"},
            max_tokens=2000,
        )

        raw = json.loads(response.choices[0].message.content)
        results = raw.get("missions", raw) if isinstance(raw, dict) else raw

        if isinstance(results, list):
            for item in results:
                idx = item.get("mission", 0) - 1
                if 0 <= idx < len(batch):
                    _apply_scores(batch[idx], item.get("scores", item), weights)
        else:
            # Fallback: single mission response
            if len(batch) == 1:
                _apply_scores(batch[0], results, weights)

    except Exception as e:
        print(f"[scorer] GPT error: {e}")
        for m in batch:
            m.feasibility_score = 0
            m.build_score = 0
            m.urgency_score = 0
            m.competition_score = 0
            m.budget_score = 0
            m.total_score = 0


def _apply_scores(mission: Mission, scores: dict, weights: dict) -> None:
    mission.feasibility_score = int(scores.get("feasibility_score", 0))
    mission.build_score = int(scores.get("build_score", 0))
    mission.tool_match = scores.get("tool_match", "none")
    mission.estimated_delivery_minutes = scores.get("estimated_delivery_minutes")
    mission.scoring_reasoning = scores.get("reasoning", "")

    mission.urgency_score = _compute_urgency(mission)
    mission.competition_score = _compute_competition(mission)
    mission.budget_score = _compute_budget(mission)

    f = mission.feasibility_score / 3
    u = mission.urgency_score / 3
    c = mission.competition_score / 2
    b = mission.budget_score / 3

    raw = (
        f * weights.get("feasibility", 0.4) +
        u * weights.get("urgency", 0.25) +
        c * weights.get("competition", 0.2) +
        b * weights.get("budget", 0.15)
    )
    mission.total_score = int(raw * 100)


def _compute_urgency(mission: Mission) -> int:
    if not mission.posted_at:
        return 1
    now = datetime.now(timezone.utc)
    posted = mission.posted_at
    if posted.tzinfo is None:
        posted = posted.replace(tzinfo=timezone.utc)
    age_hours = (now - posted).total_seconds() / 3600
    if age_hours < 6:
        return 3
    elif age_hours < 24:
        return 2
    elif age_hours < 72:
        return 1
    return 0


def _compute_competition(mission: Mission) -> int:
    n = mission.nb_proposals
    if n is None:
        return 1
    if n == 0:
        return 2
    elif n <= 5:
        return 2
    elif n <= 10:
        return 1
    return 0


def _compute_budget(mission: Mission) -> int:
    budget = mission.budget_max or mission.budget_min
    if budget is None:
        return 1
    if budget >= 60:
        return 3
    elif budget >= 30:
        return 2
    elif budget >= 15:
        return 1
    return 0
