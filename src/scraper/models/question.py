"""Defines the Data Transfer Objects (DTOs)."""

from dataclasses import dataclass, field


@dataclass
class QuestionDTO:
    """Data Transfer Object representing a single exam question.

    Attributes:
        id: The unique identifier of the question (e.g., "Question 1").
        text: The full text of the question prompt.
        options: A dictionary mapping option labels (A, B...) to option text.
        correct_answers: A list of labels corresponding to the correct options.
    """

    id: str
    text: str
    options: dict[str, str] = field(default_factory=dict)
    correct_answers: list[str] = field(default_factory=list)
