"""Configuration module for the Converter package."""

import os
from pathlib import Path
from typing import Final

from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

# --- Paths ---
BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent

# Input File (Same as Scraper Output)
INPUT_FILE: Final[Path] = Path(os.getenv("EXAM_QUESTIONS_FILE"))

# Output Markdown File
OUTPUT_MD_FILE: Final[Path] = BASE_DIR / "exam_export.md"

# Grouping settings (e.g., create a new header every 50 questions)
CHUNK_SIZE: Final[int] = 50
