from typing import List

from chrona.timetable.timetable_entry import TimetableEntry
from chrona.storage.database import Database


class TimetableRepository:
    def __init__(self, database: Database):
        self.database = database

    def save_entry(
        self,
        entry: TimetableEntry,
    ) -> None:

        self.database.cursor.execute(
            """
            INSERT INTO timetable_entries
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                entry.id,
                entry.day_of_week,
                entry.start_time,
                entry.end_time,
                entry.activity,
                entry.entry_type,
            ),
        )

        self.database.connection.commit()

    def get_all_entries(
        self,
    ) -> List[TimetableEntry]:

        rows = self.database.cursor.execute(
            """
            SELECT * FROM timetable_entries
            """
        ).fetchall()

        entries = []

        for row in rows:
            entry = TimetableEntry(
                id=row[0],
                day_of_week=row[1],
                start_time=row[2],
                end_time=row[3],
                activity=row[4],
                entry_type=row[5],
            )

            entries.append(entry)

        return entries