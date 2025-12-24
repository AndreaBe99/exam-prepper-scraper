"""Configuration module.

Loads settings from environment variables and defines file paths.
"""

import os
from pathlib import Path
from typing import Final

from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

# --- Paths ---
# resolving to src/ root
BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
LOGS_DIR: Final[Path] = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# File path to the scraped JSON
QUESTIONS_FILE: Final[Path] = Path(os.getenv("EXAM_QUESTIONS_FILE", "output/exam_results.json"))
QUIZ_LOG_FILE: Final[Path] = LOGS_DIR / "quiz_session.log"

# --- Exam Settings ---
# Default to 10 questions if not set
MAX_QUESTIONS: Final[int] = int(os.getenv("EXAM_MAX_QUESTIONS", "10"))
# Default to 15 minutes if not set
TIMER_MINUTES: Final[int] = int(os.getenv("EXAM_TIMER_MINUTES", "15"))
