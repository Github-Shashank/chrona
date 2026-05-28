from typing import List

from chrona.task_engine.task import Task


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def get_pending_tasks(self) -> List[Task]:
        return [
            task
            for task in self.tasks
            if task.status == "pending"
        ]