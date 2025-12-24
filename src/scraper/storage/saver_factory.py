"""Handles file storage, backups, and data merging."""

from typing import Literal

from scraper.storage.csv_saver import CsvSaver
from scraper.storage.json_saver import JsonSaver
from scraper.storage.saver_interface import FileSaver
from scraper.storage.yaml_saver import YamlSaver


class SaverFactory:
    """Factory to create file savers."""

    @staticmethod
    def get_saver(format_type: Literal["json", "csv", "yaml"]) -> FileSaver:
        """Factory method to return a specific saver instance.

        Args:
            format_type: The desired format ('json', 'csv', or 'yaml').

        Returns:
            An instance of a class inheriting from FileSaver.
        """
        if format_type == "json":
            return JsonSaver()
        if format_type == "csv":
            return CsvSaver()
        if format_type == "yaml":
            return YamlSaver()
        raise ValueError(f"Unsupported format: {format_type}")
