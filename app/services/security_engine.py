from app.models.event import EventType, SecurityEvent, Severity


class SecurityEngine:
    """Analyzes vehicle security events and detects threats."""

    def analyze_event(self, event: SecurityEvent) -> dict:
        """Analyze a single security event."""

        if event.event_type == EventType.TAMPER_DETECTED:
            return {
                "is_threat": True,
                "risk_level": "CRITICAL",
                "alert": "Vehicle tampering detected.",
            }

        if event.event_type == EventType.IGNITION_ATTEMPT:
            return {
                "is_threat": False,
                "risk_level": "MEDIUM",
                "alert": "Ignition attempt detected.",
            }

        if event.event_type == EventType.UNLOCK_ATTEMPT:
            if event.severity in {Severity.HIGH, Severity.CRITICAL}:
                return {
                    "is_threat": True,
                    "risk_level": "HIGH",
                    "alert": "Suspicious unlock attempt detected.",
                }

            return {
                "is_threat": False,
                "risk_level": "LOW",
                "alert": "Unlock attempt recorded.",
            }

        if event.event_type == EventType.DOOR_OPEN:
            return {
                "is_threat": False,
                "risk_level": "LOW",
                "alert": "Door opening recorded.",
            }

        if event.event_type == EventType.MOTION_DETECTED:
            return {
                "is_threat": False,
                "risk_level": "LOW",
                "alert": "Vehicle movement detected.",
            }

        if event.event_type == EventType.BATTERY_ANOMALY:
            return {
                "is_threat": True,
                "risk_level": "HIGH",
                "alert": "Vehicle battery anomaly detected.",
            }

        return {
            "is_threat": False,
            "risk_level": "LOW",
            "alert": "Event recorded.",
        }