from fastapi import FastAPI

from app.models.event import SecurityEvent
from app.services.event_logger import EventLogger
from app.services.risk_engine import RiskEngine
from app.services.security_engine import SecurityEngine
from app.database.database import initialize_database

app = FastAPI(
    title="Vehicle Security Monitor",
    description="Cybersecurity monitoring API for vehicle security events.",
    version="1.0.0",
)

initialize_database()

security_engine = SecurityEngine()
risk_engine = RiskEngine()
event_logger = EventLogger()


@app.get("/health")
def health_check():
    """Check whether the Vehicle Security Monitor API is running."""

    return {
        "status": "online",
        "service": "Vehicle Security Monitor",
    }


@app.post("/events")
def create_event(event: SecurityEvent):
    """Analyze, calculate risk, and store a vehicle security event."""

    analysis = security_engine.analyze_event(event)
    risk_score = risk_engine.calculate_event_risk(event)
    risk_level = risk_engine.get_risk_level(risk_score)

    event_logger.save_event(event)

    return {
        "event_id": event.event_id,
        "vehicle_id": event.vehicle_id,
        "event_type": event.event_type.value,
        "is_threat": analysis["is_threat"],
        "risk_score": risk_score,
        "risk_level": risk_level,
        "alert": analysis["alert"],
    }


@app.get("/events")
def get_events():
    """Retrieve stored vehicle security events."""

    return {
        "events": event_logger.get_events()
    }