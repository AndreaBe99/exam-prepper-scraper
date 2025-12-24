"""Handles file storage, backups, and data merging."""

import csv
import json
from dataclasses import asdict
from pathlib import Path

from loguru import logger

from scraper.models.question import QuestionDTO
from scraper.storage.saver_interface import FileSaver


class CsvSaver(FileSaver):
    """Concrete saver implementation for CSV format."""

    def load_existing(self, filename: str) -> dict[str, QuestionDTO]:
        """See base class docstring."""
        path = Path(filename)
        if not path.exists():
            return {}

        results = {}
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # JSON strings need parsing back to python objects
                    row["options"] = json.loads(row["options"])
                    row["correct_answers"] = json.loads(row["correct_answers"])
                    results[row["id"]] = QuestionDTO(**row)
        except Exception as e:
            logger.warning(f"Error loading CSV {filename}: {e}")
        return results

    def save(self, data_map: dict[str, QuestionDTO], filename: str) -> None:
        """See base class docstring."""
        if not data_map:
            return

        output = []
        for q in data_map.values():
            row = asdict(q)
            # Serialize complex types for CSV
            row["options"] = json.dumps(row["options"], ensure_ascii=False)
            row["correct_answers"] = json.dumps(row["correct_answers"], ensure_ascii=False)
            output.append(row)

        keys = output[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(output)
