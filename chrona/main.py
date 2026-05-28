import sys

from rich.console import Console

from chrona.storage.database import Database
from chrona.storage.task_repository import TaskRepository
from chrona.terminal.input_handler import InputHandler
from chrona.terminal.task_renderer import TaskRenderer

renderer = TaskRenderer()

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

    table = renderer.render_task_table(tasks)

    console.print(table)


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

    elif command == "complete":

        if len(sys.argv) < 3:
            console.print(
                "[bold red]Task ID required[/bold red]"
            )
            return

        task_id = sys.argv[2]

        complete_task(task_id)

    elif command == "delete":

        if len(sys.argv) < 3:
            console.print(
                "[bold red]Task ID required[/bold red]"
            )
            return

        task_id = sys.argv[2]

        delete_task(task_id)

    else:
        console.print(
            f"[bold red]Unknown command:[/bold red] {command}"
        )

def complete_task(task_id: str):
    success = repository.complete_task(task_id)

    if success:
        console.print(
            "[bold green]Task completed successfully[/bold green]"
        )
    else:
        console.print(
            "[bold red]Task not found[/bold red]"
        )

def delete_task(task_id: str):
    success = repository.delete_task(task_id)

    if success:
        console.print(
            "[bold green]Task deleted successfully[/bold green]"
        )
    else:
        console.print(
            "[bold red]Task not found[/bold red]"
        )

if __name__ == "__main__":
    main()

    database.close()