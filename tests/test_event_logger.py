from app.database.database import initialize_database
from app.models.event import EventType, SecurityEvent, Severity
from app.services.event_logger import EventLogger


def test_event_can_be_saved_and_retrieved(tmp_path, monkeypatch):
    database_path = tmp_path / "test_vehicle_security.db"

    monkeypatch.setattr(
        "app.database.database.DATABASE_PATH",
        database_path,
    )

    monkeypatch.setattr(
        "app.services.event_logger.get_connection",
        lambda: __import__("sqlite3").connect(database_path),
    )

    initialize_database()

    logger = EventLogger()

    event = SecurityEvent(
        event_id="EVT-001",
        vehicle_id="VSM-001",
        event_type=EventType.DOOR_OPEN,
        source="driver_door_sensor",
        severity=Severity.LOW,
        description="Driver door opened",
    )

    logger.save_event(event)

    events = logger.get_events()

    assert len(events) == 1
    assert events[0][0] == "EVT-001"
    assert events[0][1] == "VSM-001"
    assert events[0][2] == "DOOR_OPEN"