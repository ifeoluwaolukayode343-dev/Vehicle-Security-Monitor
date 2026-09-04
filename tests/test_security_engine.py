from app.models.event import EventType, SecurityEvent, Severity
from app.services.security_engine import SecurityEngine


def create_event(event_type, severity):
    return SecurityEvent(
        event_id="EVT-001",
        vehicle_id="VSM-001",
        event_type=event_type,
        source="vehicle_sensor",
        severity=severity,
        description="Test security event",
    )


def test_tamper_detection():
    engine = SecurityEngine()

    event = create_event(
        EventType.TAMPER_DETECTED,
        Severity.CRITICAL,
    )

    result = engine.analyze_event(event)

    assert result["is_threat"] is True
    assert result["risk_level"] == "CRITICAL"


def test_normal_door_opening():
    engine = SecurityEngine()

    event = create_event(
        EventType.DOOR_OPEN,
        Severity.LOW,
    )

    result = engine.analyze_event(event)

    assert result["is_threat"] is False
    assert result["risk_level"] == "LOW"


def test_suspicious_unlock_attempt():
    engine = SecurityEngine()

    event = create_event(
        EventType.UNLOCK_ATTEMPT,
        Severity.HIGH,
    )

    result = engine.analyze_event(event)

    assert result["is_threat"] is True
    assert result["risk_level"] == "HIGH"