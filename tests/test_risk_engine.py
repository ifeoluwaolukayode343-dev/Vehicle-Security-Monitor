from app.models.event import EventType, SecurityEvent, Severity
from app.services.risk_engine import RiskEngine


def create_event(event_type, severity):
    return SecurityEvent(
        event_id="EVT-001",
        vehicle_id="VSM-001",
        event_type=event_type,
        source="vehicle_sensor",
        severity=severity,
        description="Test security event",
    )


def test_low_risk_event():
    engine = RiskEngine()

    event = create_event(
        EventType.DOOR_OPEN,
        Severity.LOW,
    )

    score = engine.calculate_event_risk(event)

    assert score == 1


def test_tamper_event_has_high_risk_score():
    engine = RiskEngine()

    event = create_event(
        EventType.TAMPER_DETECTED,
        Severity.CRITICAL,
    )

    score = engine.calculate_event_risk(event)

    assert score == 15


def test_risk_level_classification():
    engine = RiskEngine()

    assert engine.get_risk_level(1) == "LOW"
    assert engine.get_risk_level(5) == "MEDIUM"
    assert engine.get_risk_level(10) == "HIGH"
    assert engine.get_risk_level(15) == "CRITICAL"