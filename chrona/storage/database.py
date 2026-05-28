import sqlite3
from pathlib import Path


DATABASE_PATH = Path("chrona.db")


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def initialize(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                category TEXT,
                priority INTEGER,
                estimated_duration REAL,
                actual_deadline TEXT,
                expected_deadline TEXT,
                status TEXT,
                created_at TEXT,
                updated_at TEXT
            )
            """
        )

        self.connection.commit()

    def close(self) -> None:
        self.connection.close()