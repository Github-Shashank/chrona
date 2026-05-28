from rich.table import Table

from chrona.task_engine.task import Task


class TaskRenderer:

    def render_task_table(self, tasks: list[Task]) -> Table:
        table = Table(title="Chrona Tasks")

        table.add_column("ID", style="cyan")
        table.add_column("Title", style="green")
        table.add_column("Priority", style="yellow")
        table.add_column("Status", style="magenta")

        for task in tasks:
            table.add_row(
                task.id[:8],
                task.title,
                str(task.priority),
                (
                    "[green]completed[/green]"
                    if task.status == "completed"
                    else "[yellow]pending[/yellow]"
                ),
            )

        return table