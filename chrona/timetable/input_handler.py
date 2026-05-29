from chrona.timetable.timetable_entry import (
    TimetableEntry,
)


class TimetableInputHandler:
    def create_entry_from_input(
        self,
    ) -> TimetableEntry:

        print("\n=== Add Timetable Entry ===\n")

        day_of_week = input(
            "Day of Week: "
        )

        start_time = input(
            "Start Time (HH:MM): "
        )

        end_time = input(
            "End Time (HH:MM): "
        )

        activity = input(
            "Activity: "
        )

        entry_type = input(
            "Entry Type: "
        )

        return TimetableEntry(
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
            activity=activity,
            entry_type=entry_type,
        )