from app.models.incident import (
    IncidentSeverity,
    IncidentType,
    SecurityIncident,
)


def test_security_incident_creation():
    incident = SecurityIncident(
        incident_id="INC-001",
        vehicle_id="VSM-001",
        incident_type=IncidentType.VEHICLE_INTRUSION,
        severity=IncidentSeverity.CRITICAL,
        risk_score=25,
        description="Possible unauthorized vehicle intrusion detected.",
        related_events=[
            "EVT-101",
            "EVT-102",
            "EVT-103",
        ],
    )

    assert incident.incident_id == "INC-001"
    assert incident.vehicle_id == "VSM-001"
    assert incident.incident_type == IncidentType.VEHICLE_INTRUSION
    assert incident.severity == IncidentSeverity.CRITICAL
    assert incident.risk_score == 25
    assert incident.related_events == [
        "EVT-101",
        "EVT-102",
        "EVT-103",
    ]


def test_incident_timestamp_is_created_automatically():
    incident = SecurityIncident(
        incident_id="INC-002",
        vehicle_id="VSM-002",
        incident_type=IncidentType.BRUTE_FORCE_ACCESS,
        severity=IncidentSeverity.HIGH,
        risk_score=12,
        description="Multiple suspicious access attempts detected.",
        related_events=[
            "EVT-201",
            "EVT-202",
        ],
    )

    assert incident.timestamp is not None
    assert incident.timestamp.tzinfo is not None


def test_incident_risk_score_cannot_be_negative():
    try:
        SecurityIncident(
            incident_id="INC-003",
            vehicle_id="VSM-003",
            incident_type=IncidentType.ELECTRICAL_ATTACK,
            severity=IncidentSeverity.HIGH,
            risk_score=-1,
            description="Invalid test incident.",
            related_events=["EVT-301"],
        )

        assert False, "Negative risk score should be rejected."

    except ValueError:
        assert True