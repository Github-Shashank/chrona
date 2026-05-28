from rich.console import Console

from chrona.storage.database import Database
from chrona.storage.task_repository import TaskRepository
from chrona.terminal.input_handler import InputHandler


console = Console()

database = Database()
database.initialize()

repository = TaskRepository(database)

input_handler = InputHandler()

task = input_handler.create_task_from_input()

repository.save_task(task)

tasks = repository.get_all_tasks()

console.print("\n[bold green]Stored Tasks[/bold green]\n")

for task in tasks:
    console.print(task.summary(), style="bold cyan")

database.close()