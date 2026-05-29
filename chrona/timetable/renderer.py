from rich.table import Table

from chrona.timetable.timetable_entry import (
    TimetableEntry,
)


class TimetableRenderer:
    def render_table(
        self,
        entries: list[TimetableEntry],
    ) -> Table:

        table = Table(
            title="Chrona Timetable"
        )

        table.add_column(
            "ID",
            style="cyan"
        )

        table.add_column(
            "Day",
            style="green"
        )

        table.add_column(
            "Time",
            style="yellow"
        )

        table.add_column(
            "Activity",
            style="magenta"
        )

        table.add_column(
            "Type",
            style="blue"
        )

        for entry in entries:
            table.add_row(
                entry.id[:8],
                entry.day_of_week,
                f"{entry.start_time} - {entry.end_time}",
                entry.activity,
                entry.entry_type,
            )

        return table