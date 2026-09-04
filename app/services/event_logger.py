from app.database.database import get_connection
from app.models.event import SecurityEvent


class EventLogger:
    """Stores and retrieves vehicle security events."""

    def save_event(self, event: SecurityEvent):
        """Save a security event to the database."""

        connection = get_connection()

        connection.execute(
            """
            INSERT INTO security_events (
                event_id,
                vehicle_id,
                event_type,
                timestamp,
                source,
                severity,
                description
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event.event_id,
                event.vehicle_id,
                event.event_type.value,
                event.timestamp.isoformat(),
                event.source,
                event.severity.value,
                event.description,
            ),
        )

        connection.commit()
        connection.close()

    def get_events(self):
        """Retrieve all stored security events."""

        connection = get_connection()

        cursor = connection.execute(
            """
            SELECT
                event_id,
                vehicle_id,
                event_type,
                timestamp,
                source,
                severity,
                description
            FROM security_events
            ORDER BY timestamp DESC
            """
        )

        events = cursor.fetchall()

        connection.close()

        return events