from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "online",
        "service": "Vehicle Security Monitor",
    }


def test_create_security_event():
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


def test_get_events():
    response = client.get("/events")

    assert response.status_code == 200

    data = response.json()

    assert "events" in data
    assert isinstance(data["events"], list)