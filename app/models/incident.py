from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


class IncidentType(str, Enum):
    VEHICLE_INTRUSION = "VEHICLE_INTRUSION"
    BRUTE_FORCE_ACCESS = "BRUTE_FORCE_ACCESS"
    ELECTRICAL_ATTACK = "ELECTRICAL_ATTACK"


class IncidentSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class SecurityIncident(BaseModel):
    incident_id: str
    vehicle_id: str
    incident_type: IncidentType
    severity: IncidentSeverity
    risk_score: int = Field(ge=0)
    description: str
    related_events: list[str]
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )