from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Mission:
    id: str                          # hash(platform + url)
    platform: str                    # "upwork" | "fiverr"
    title: str
    description: str
    budget_min: Optional[float]
    budget_max: Optional[float]
    nb_proposals: Optional[int]
    posted_at: Optional[datetime]
    scraped_at: datetime = field(default_factory=datetime.utcnow)
    category: str = ""
    url: str = ""
    client_rating: Optional[float] = None

    # Scoring fields (set by scorer)
    feasibility_score: Optional[int] = None
    build_score: Optional[int] = None
    urgency_score: Optional[int] = None
    competition_score: Optional[int] = None
    budget_score: Optional[int] = None
    total_score: Optional[int] = None
    tool_match: Optional[str] = None
    estimated_delivery_minutes: Optional[int] = None
    scoring_reasoning: Optional[str] = None

    alerted: int = 0
    proposal_sent: int = 0
    result: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "platform": self.platform,
            "title": self.title,
            "description": self.description,
            "budget_min": self.budget_min,
            "budget_max": self.budget_max,
            "nb_proposals": self.nb_proposals,
            "posted_at": self.posted_at.isoformat() if self.posted_at else None,
            "scraped_at": self.scraped_at.isoformat(),
            "category": self.category,
            "url": self.url,
            "client_rating": self.client_rating,
            "feasibility_score": self.feasibility_score,
            "build_score": self.build_score,
            "urgency_score": self.urgency_score,
            "competition_score": self.competition_score,
            "budget_score": self.budget_score,
            "total_score": self.total_score,
            "tool_match": self.tool_match,
            "estimated_delivery_minutes": self.estimated_delivery_minutes,
            "scoring_reasoning": self.scoring_reasoning,
            "alerted": self.alerted,
            "proposal_sent": self.proposal_sent,
            "result": self.result,
        }
