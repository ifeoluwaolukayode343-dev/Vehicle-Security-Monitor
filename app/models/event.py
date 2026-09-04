from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


class EventType(str, Enum):
    DOOR_OPEN = "DOOR_OPEN"
    IGNITION_ATTEMPT = "IGNITION_ATTEMPT"
    UNLOCK_ATTEMPT = "UNLOCK_ATTEMPT"
    MOTION_DETECTED = "MOTION_DETECTED"
    TAMPER_DETECTED = "TAMPER_DETECTED"
    BATTERY_ANOMALY = "BATTERY_ANOMALY"


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class SecurityEvent(BaseModel):
    event_id: str
    vehicle_id: str
    event_type: EventType
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
        )
    source: str
    severity: Severity
    description: str