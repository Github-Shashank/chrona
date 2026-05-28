import sys

from rich.console import Console

from chrona.storage.database import Database
from chrona.storage.task_repository import TaskRepository
from chrona.terminal.input_handler import InputHandler


console = Console()

database = Database()
database.initialize()

repository = TaskRepository(database)

input_handler = InputHandler()


def add_task():
    task = input_handler.create_task_from_input()
    repository.save_task(task)

    console.print(
        "\n[bold green]Task stored successfully[/bold green]"
    )


def list_tasks():
    tasks = repository.get_all_tasks()

    console.print("\n[bold green]Stored Tasks[/bold green]\n")

    for task in tasks:
        console.print(
            task.summary(),
            style="bold cyan"
        )


def main():
    if len(sys.argv) < 2:
        console.print(
            "[bold red]No command provided[/bold red]"
        )

        console.print(
            "\nUsage:"
        )

        console.print(
            "python -m chrona.main add"
        )

        console.print(
            "python -m chrona.main list"
        )

        return

    command = sys.argv[1]

    if command == "add":
        add_task()

    elif command == "list":
        list_tasks()

    else:
        console.print(
            f"[bold red]Unknown command:[/bold red] {command}"
        )


if __name__ == "__main__":
    main()

    database.close()