from app.models.event import EventType, SecurityEvent, Severity


class RiskEngine:
    """Calculates the security risk associated with vehicle events."""

    SEVERITY_POINTS = {
        Severity.LOW: 1,
        Severity.MEDIUM: 3,
        Severity.HIGH: 6,
        Severity.CRITICAL: 10,
    }

    def calculate_event_risk(self, event: SecurityEvent) -> int:
        """Calculate the risk points for a single event."""

        points = self.SEVERITY_POINTS[event.severity]

        if event.event_type == EventType.TAMPER_DETECTED:
            points += 5

        elif event.event_type == EventType.UNLOCK_ATTEMPT:
            points += 2

        elif event.event_type == EventType.BATTERY_ANOMALY:
            points += 2

        return points

    def get_risk_level(self, risk_score: int) -> str:
        """Convert a numerical risk score into a risk level."""

        if risk_score >= 15:
            return "CRITICAL"

        if risk_score >= 10:
            return "HIGH"

        if risk_score >= 5:
            return "MEDIUM"

        return "LOW"