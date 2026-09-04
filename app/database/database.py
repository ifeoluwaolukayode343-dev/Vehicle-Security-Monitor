import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data") / "vehicle_security.db"


def get_connection():
    """Create and return a connection to the SQLite database."""

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    return connection


def initialize_database():
    """Create the security events table if it does not exist."""

    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS security_events (
            event_id TEXT PRIMARY KEY,
            vehicle_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            source TEXT NOT NULL,
            severity TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()