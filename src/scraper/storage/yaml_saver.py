"""Handles file storage, backups, and data merging."""

from dataclasses import asdict
from pathlib import Path

import yaml

from scraper.models.question import QuestionDTO
from scraper.storage.saver_interface import FileSaver


class YamlSaver(FileSaver):
    """Concrete saver implementation for YAML format."""

    def load_existing(self, filename: str) -> dict[str, QuestionDTO]:
        """See base class docstring."""
        if yaml is None:
            return {}

        path = Path(filename)
        if not path.exists():
            return {}

        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or []
                return {item["id"]: QuestionDTO(**item) for item in data}
        except Exception:
            return {}

    def save(self, data_map: dict[str, QuestionDTO], filename: str) -> None:
        """See base class docstring."""
        if yaml is None:
            raise ImportError("PyYAML is not installed.")

        output = [asdict(q) for q in data_map.values()]
        with open(filename, "w", encoding="utf-8") as f:
            yaml.dump(output, f, allow_unicode=True, default_flow_style=False)
