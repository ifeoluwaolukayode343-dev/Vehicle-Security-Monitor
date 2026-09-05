import sqlite3

from fastapi.testclient import TestClient

from app.database import database
from app.main import app
from app.services import event_logger


def test_health_check():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "online",
        "service": "Vehicle Security Monitor",
    }


def test_create_security_event(tmp_path, monkeypatch):
    database_path = tmp_path / "test_vehicle_security.db"

    test_connection = lambda: sqlite3.connect(database_path)

    monkeypatch.setattr(
        database,
        "get_connection",
        test_connection,
    )

    monkeypatch.setattr(
        event_logger,
        "get_connection",
        test_connection,
    )

    database.initialize_database()

    client = TestClient(app)

    event = {
        "event_id": "EVT-TEST-001",
        "vehicle_id": "VSM-TEST-001",
        "event_type": "TAMPER_DETECTED",
        "source": "test_sensor",
        "severity": "CRITICAL",
        "description": "Test tampering event.",
    }

    response = client.post("/events", json=event)

    assert response.status_code == 200

    data = response.json()

    assert data["event_id"] == "EVT-TEST-001"
    assert data["is_threat"] is True
    assert data["risk_score"] == 15
    assert data["risk_level"] == "CRITICAL"


def test_get_events(tmp_path, monkeypatch):
    database_path = tmp_path / "test_vehicle_security.db"

    test_connection = lambda: sqlite3.connect(database_path)

    monkeypatch.setattr(
        database,
        "get_connection",
        test_connection,
    )

    monkeypatch.setattr(
        event_logger,
        "get_connection",
        test_connection,
    )

    database.initialize_database()

    client = TestClient(app)

    response = client.get("/events")

    assert response.status_code == 200

    data = response.json()

    assert "events" in data
    assert isinstance(data["events"], list)