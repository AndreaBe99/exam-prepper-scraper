"""Handles file storage, backups, and data merging."""

from abc import ABC, abstractmethod

from scraper.models.question import QuestionDTO


class FileSaver(ABC):
    """Abstract base class for file saving strategies."""

    @abstractmethod
    def load_existing(self, filename: str) -> dict[str, QuestionDTO]:
        """Loads existing data from the file into a dictionary keyed by ID.

        Args:
            filename: The path to the file.

        Returns:
            A dictionary where keys are Question IDs and values are DTOs.
        """

    @abstractmethod
    def save(self, data_map: dict[str, QuestionDTO], filename: str) -> None:
        """Saves the merged data map to the file.

        Args:
            data_map: The dictionary of all questions (existing + new).
            filename: The target file path.
        """
