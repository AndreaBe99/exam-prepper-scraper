"""Configuration management for the scraper application.

This module loads environment variables and provides typed configuration constants.
"""

import os
from datetime import datetime
from pathlib import Path
from typing import Final

from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# --- Paths ---
BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
LOGS_DIR: Final[Path] = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# --- Scraper Settings ---
START_URL: Final[str] = os.getenv("START_URL", "https://www.examprepper.co/exam/5/1")

# --- Range Logic (Optional) ---
# We parse these as Integers or None
_start_val = os.getenv("QUESTION_RANGE_START")
_end_val = os.getenv("QUESTION_RANGE_END")

QUESTION_RANGE_START: Final[int | None] = int(_start_val) if _start_val else None
QUESTION_RANGE_END: Final[int | None] = int(_end_val) if _end_val else None

# --- Output Settings ---
EXAM_NAME: str | None = os.getenv("EXAM_NAME")
if EXAM_NAME is None:
    EXAM_NAME = "exam_results"
else:
    EXAM_NAME = EXAM_NAME.replace(" ", "_").lower()
OUTPUT_FORMAT: Final[str] = os.getenv("OUTPUT_FORMAT", "json").lower()
date: Final[str] = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = f"output/{EXAM_NAME}_{date}.{OUTPUT_FORMAT}"

LOG_FILE: Final[Path] = LOGS_DIR / "scraper.log"

# --- Chrome Options ---
HEADLESS: Final[bool] = os.getenv("HEADLESS", "false").lower() == "true"
