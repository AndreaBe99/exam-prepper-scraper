"""Handles file storage, backups, and data merging."""

import shutil
from datetime import datetime
from pathlib import Path

from loguru import logger


def create_backup(filepath: str) -> None:
    """Creates a timestamped backup of the existing file.

    If the file exists, it copies it to a new filename with the format:
    `backup_YYYYMMDD_HHMM_filename.ext`.

    Args:
        filepath: The path to the file to back up.
    """
    path = Path(filepath)
    if not path.exists():
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_name = f"backup_{timestamp}_{path.name}"
    backup_path = path.parent / backup_name

    try:
        shutil.copy(path, backup_path)
        logger.info(f"Backup created: {backup_path}")
    except OSError as e:
        logger.error(f"Failed to create backup: {e}")
