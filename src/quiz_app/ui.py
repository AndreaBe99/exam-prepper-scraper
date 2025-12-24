"""User Interface Module.

Handles visual rendering using Rich and input using Questionary.
"""

from datetime import timedelta

import questionary
from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table

from quiz_app.models.question import Question
from quiz_app.models.user_answer import UserAnswer


class QuizUI:
    """Handles all terminal input/output operations."""

    def __init__(self) -> None:
        """Initializes the Rich Console."""
        self.console = Console()

    def show_welcome(self, num_questions: int, minutes: int) -> None:
        """Displays the exam splash screen.

        Args:
            num_questions: Total questions in this session.
            minutes: Allowed time in minutes.
        """
        self.console.clear()
        title = "[bold cyan]GCP Professional Architect Exam Simulation[/bold cyan]"
        info = f"\nQuestions: [yellow]{num_questions}[/yellow]\nTime Limit: [yellow]{minutes} mins[/yellow]"

        self.console.print(Panel(info, title=title, border_style="blue", padding=(1, 2)))
        self.console.input("\nPress [bold green]ENTER[/bold green] to start...")

    def show_header(self, current_idx: int, total: int, remaining_seconds: float) -> None:
        """Displays the top status bar with progress and timer.

        Args:
            current_idx: Current question number (1-based).
            total: Total questions.
            remaining_seconds: Seconds left on timer.
        """
        self.console.clear()

        # Format time as MM:SS
        time_str = str(timedelta(seconds=int(remaining_seconds)))

        # Color code time (Red if < 2 mins)
        color = "red" if remaining_seconds < 120 else "green"

        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right", ratio=1)
        grid.add_row(
            f"Question [bold]{current_idx}/{total}[/bold]",
            f"Time Remaining: [bold {color}]{time_str}[/bold {color}]",
        )
        self.console.print(Panel(grid, style="white on black"))

    def ask_question(self, question: Question) -> list[str]:
        """Displays the question and prompts for an answer.

        Args:
            question: The question object to display.

        Returns:
            A list of selected option keys (e.g. ['A', 'C']).
        """
        # Display Question Text
        self.console.print(Panel(Markdown(question.text), title=f"ID: {question.id}", border_style="cyan"))
        self.console.print("")

        # Display Options via Rich Table (Handles wrapping for long text)
        # We use a grid table to align "A)" with the text, allowing the text to wrap nicely.
        grid = Table.grid(expand=True, padding=(0, 1))
        grid.add_column(style="yellow bold", width=4)  # Key column (e.g. "A)")
        grid.add_column(style="white")  # Text column

        for k, v in question.options.items():
            grid.add_row(f"{k})", v)
            grid.add_row("", "")  # Empty row for spacing between options

        self.console.print(grid)
        self.console.print("")
        # -------------------------------------------------------------------------

        # Prepare simple choices for Questionary (just the keys)
        choices = [questionary.Choice(title=f"Option {k}", value=k) for k in question.options.keys()]

        # Use Checkbox for multiple choice, Select list for single choice
        if question.is_multiple_choice:
            self.console.print(
                "[italic yellow]ℹ️  Multiple correct answers allowed "
                "(Select with Space, Confirm with Enter)[/italic yellow]"
            )
            answer = questionary.checkbox(
                "Select your answer(s):",
                choices=choices,
                style=questionary.Style([("answer", "fg:cyan bold")]),
                qmark="👉",
            ).ask()
        else:
            answer = questionary.select(
                "Select your answer:",
                choices=choices,
                style=questionary.Style([("answer", "fg:cyan bold")]),
                qmark="👉",
            ).ask()
            # Wrap single result in list for consistency
            if answer:
                answer = [answer]

        return answer if answer else []

    def show_results(self, score: tuple[int, int, float], answers: list[UserAnswer]) -> None:
        """Displays the final report card.

        Args:
            score: Tuple of (correct_count, total_count, percentage).
            answers: List of UserAnswer objects containing history.
        """
        self.console.clear()
        correct, total, percent = score

        # 1. Summary Panel
        color = "green" if percent >= 70 else "red"
        summary = (
            f"\nScore: [bold {color}]{correct}/{total}[/bold {color}]\n"
            f"Percentage: [bold {color}]{percent:.1f}%[/bold {color}]"
        )
        self.console.print(Panel(summary, title="Exam Completed", border_style=color))

        # 2. Review Table
        table = Table(title="Detailed Review", box=box.ROUNDED, expand=True)
        table.add_column("Q.ID", style="cyan", no_wrap=True)
        table.add_column("Result", justify="center")
        table.add_column("Your Answer", style="magenta")
        table.add_column("Correct Answer", style="green")

        for ans in answers:
            is_correct = ans.is_correct
            status_icon = "✅" if is_correct else "❌"

            user_str = ", ".join(ans.selected_options)
            correct_str = ", ".join(ans.question.correct_answers)

            # Highlight incorrect rows visually
            style = "dim" if is_correct else "bold white"

            table.add_row(ans.question.id, status_icon, user_str, correct_str, style=style)

        self.console.print(table)
