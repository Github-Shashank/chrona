from datetime import datetime

from chrona.task_engine.task import Task


class InputHandler:
    def create_task_from_input(self) -> Task:
        print("\n=== Create New Task ===\n")

        title = input("Title: ")
        description = input("Description: ")
        category = input("Category: ")

        priority = int(
            input("Priority (1-5): ")
        )

        estimated_duration = float(
            input("Estimated Duration (hours): ")
        )

        actual_deadline = datetime.fromisoformat(
            input(
                "Actual Deadline (YYYY-MM-DD HH:MM): "
            )
        )

        expected_deadline = datetime.fromisoformat(
            input(
                "Expected Deadline (YYYY-MM-DD HH:MM): "
            )
        )

        return Task(
            title=title,
            description=description,
            category=category,
            priority=priority,
            estimated_duration=estimated_duration,
            actual_deadline=actual_deadline,
            expected_deadline=expected_deadline,
        )