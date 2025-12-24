"""Handles file storage, backups, and data merging."""

import json
from dataclasses import asdict
from pathlib import Path

from loguru import logger

from scraper.models.question import QuestionDTO
from scraper.storage.saver_interface import FileSaver


class JsonSaver(FileSaver):
    """Concrete saver implementation for JSON format."""

    def load_existing(self, filename: str) -> dict[str, QuestionDTO]:
        """See base class docstring."""
        path = Path(filename)
        if not path.exists():
            return {}

        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
                return {item["id"]: QuestionDTO(**item) for item in data}
        except (json.JSONDecodeError, OSError):
            logger.warning(f"Could not load existing JSON from {filename}. Starting fresh.")
            return {}

    def save(self, data_map: dict[str, QuestionDTO], filename: str) -> None:
        """See base class docstring."""
        # Convert map values to list of dicts
        output = [asdict(q) for q in data_map.values()]

        # Sort by ID (heuristic: extract number)
        # We do a basic sort to keep the file tidy
        try:
            output.sort(key=lambda x: int(x["id"].split()[-1]) if " " in x["id"] else 0)
        except (ValueError, IndexError):
            pass

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
