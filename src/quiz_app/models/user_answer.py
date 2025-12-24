"""Data models for the quiz application."""

from dataclasses import dataclass

from quiz_app.models.question import Question


@dataclass
class UserAnswer:
    """Tracks the user's response to a question."""

    question: Question
    selected_options: list[str]
    time_taken_seconds: float = 0.0

    @property
    def is_correct(self) -> bool:
        """Checks if the selected options match the correct answers.
        Sorting ensures ['A', 'B'] equals ['B', 'A'].
        """
        return sorted(self.selected_options) == sorted(self.question.correct_answers)
