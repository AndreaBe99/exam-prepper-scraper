"""Data models for the quiz application."""

from dataclasses import dataclass


@dataclass
class Question:
    """Represents a single exam question loaded from the JSON."""

    id: str
    text: str
    options: dict[str, str]
    correct_answers: list[str]

    @property
    def is_multiple_choice(self) -> bool:
        """Returns True if there is more than one correct answer."""
        return len(self.correct_answers) > 1
