from app.models.event import EventType, SecurityEvent, Severity


def test_security_event_creation():
    event = SecurityEvent(
        event_id="EVT-001",
        vehicle_id="VSM-001",
        event_type=EventType.DOOR_OPEN,
        source="driver_door_sensor",
        severity=Severity.LOW,
        description="Driver door opened"
    )

    assert event.event_id == "EVT-001"
    assert event.vehicle_id == "VSM-001"
    assert event.event_type == EventType.DOOR_OPEN
    assert event.severity == Severity.LOW