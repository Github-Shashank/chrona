from datetime import datetime
from typing import List

from chrona.storage.database import Database
from chrona.task_engine.task import Task


class TaskRepository:
    def __init__(self, database: Database):
        self.database = database

    def save_task(self, task: Task) -> None:
        self.database.cursor.execute(
            """
            INSERT INTO tasks VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                task.id,
                task.title,
                task.description,
                task.category,
                task.priority,
                task.estimated_duration,
                task.actual_deadline.isoformat(),
                task.expected_deadline.isoformat(),
                task.status,
                task.created_at.isoformat(),
                task.updated_at.isoformat(),
            ),
        )

        self.database.connection.commit()

    def get_all_tasks(self) -> List[Task]:
        rows = self.database.cursor.execute(
            "SELECT * FROM tasks"
        ).fetchall()

        tasks = []

        for row in rows:
            task = Task(
                id=row[0],
                title=row[1],
                description=row[2],
                category=row[3],
                priority=row[4],
                estimated_duration=row[5],
                actual_deadline=datetime.fromisoformat(row[6]),
                expected_deadline=datetime.fromisoformat(row[7]),
                status=row[8],
                created_at=datetime.fromisoformat(row[9]),
                updated_at=datetime.fromisoformat(row[10]),
            )

            tasks.append(task)

        return tasks