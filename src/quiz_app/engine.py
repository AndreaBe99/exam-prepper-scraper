"""Quiz Engine Module.

Handles the business logic: loading data, randomization, scoring, and logging.
"""

import json
import random
import time
from datetime import datetime
from pathlib import Path

from loguru import logger

from quiz_app import config  # Import config to access REPORTS_DIR
from quiz_app.models.question import Question
from quiz_app.models.user_answer import UserAnswer


class QuizEngine:
    """Manages the state and logic of the quiz session."""

    def __init__(self, filepath: Path, max_questions: int, time_limit_minutes: int) -> None:
        """Initializes the quiz engine.

        Args:
            filepath: Path to the JSON file containing questions.
            max_questions: Maximum number of questions to ask.
            time_limit_minutes: Time limit for the exam.
        """
        self.filepath = filepath
        self.max_questions = max_questions
        self.time_limit_seconds = time_limit_minutes * 60

        self.questions: list[Question] = []
        self.user_answers: list[UserAnswer] = []
        self.start_time: float = 0.0

        logger.info(f"QuizEngine initialized. Max Questions: {max_questions}, Time Limit: {time_limit_minutes}m")

    def load_and_shuffle(self) -> None:
        """Loads questions from JSON, shuffles them, and selects the subset.

        Raises:
            FileNotFoundError: If the source JSON does not exist.
        """
        if not self.filepath.exists():
            logger.critical(f"Questions file not found at: {self.filepath}")
            raise FileNotFoundError(f"Questions file not found: {self.filepath}")

        try:
            with open(self.filepath, encoding="utf-8") as f:
                raw_data = json.load(f)
        except json.JSONDecodeError as e:
            logger.critical(f"Failed to parse JSON file: {e}")
            raise

        # Convert JSON dicts to Question objects
        all_questions = []
        for item in raw_data:
            # Skip invalid questions without answers (data cleaning)
            if not item.get("correct_answers"):
                continue

            q = Question(
                id=item["id"], text=item["text"], options=item["options"], correct_answers=item["correct_answers"]
            )
            all_questions.append(q)

        total_available = len(all_questions)
        logger.debug(f"Loaded {total_available} valid questions from file.")

        # Randomize
        random.shuffle(all_questions)

        # Slice to the requested number
        self.questions = all_questions[: self.max_questions]
        logger.info(f"Selected {len(self.questions)} questions for this session.")

    def start_timer(self) -> None:
        """Starts the internal exam timer."""
        self.start_time = time.time()
        logger.info("Timer started.")

    def get_remaining_time(self) -> float:
        """Returns seconds remaining in the exam."""
        elapsed = time.time() - self.start_time
        remaining = self.time_limit_seconds - elapsed
        return max(0.0, remaining)

    def is_time_up(self) -> bool:
        """Checks if the exam timer has expired."""
        return self.get_remaining_time() <= 0

    def record_answer(self, question: Question, selected_labels: list[str]) -> None:
        """Records the user's answer and logs the interaction.

        Args:
            question: The question object.
            selected_labels: List of option keys selected by user (e.g., ['A', 'C']).
        """
        answer = UserAnswer(question=question, selected_options=selected_labels)
        self.user_answers.append(answer)

        # LOGGING USER INTERACTION
        status = "CORRECT" if answer.is_correct else "WRONG"
        logger.info(
            f"Question ID: {question.id} | "
            f"User Selected: {selected_labels} | "
            f"Correct Answer: {question.correct_answers} | "
            f"Result: {status}"
        )

    def calculate_score(self) -> tuple[int, int, float]:
        """Calculates final stats.

        Returns:
            tuple: (correct_count, total_count, percentage)
        """
        total = len(self.user_answers)
        if total == 0:
            return 0, 0, 0.0

        correct = sum(1 for ans in self.user_answers if ans.is_correct)
        percentage = (correct / total) * 100

        logger.info(f"Quiz finished. Score: {correct}/{total} ({percentage:.2f}%)")
        return correct, total, percentage

    def save_report(self) -> Path:
        """Generates a Markdown study guide of the session.

        Returns:
            Path: The file path of the saved report.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quiz_report_{timestamp}.md"
        filepath = config.REPORTS_DIR / filename

        correct, total, percent = self.calculate_score()

        with open(filepath, "w", encoding="utf-8") as f:
            # Header
            f.write("# Quiz Session Report\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Final Score:** {correct}/{total} ({percent:.2f}%)\n\n")
            f.write("---\n\n")

            # Questions
            for idx, ans in enumerate(self.user_answers, 1):
                q = ans.question

                # Determine icon
                status_icon = "✅ Correct" if ans.is_correct else "❌ Incorrect"

                f.write(f"## Question {idx} (ID: {q.id})\n\n")
                f.write(f"{q.text}\n\n")

                f.write("### Options:\n")
                for key, value in q.options.items():
                    # Highlight correct answers in bold in the list
                    marker = ""
                    if key in q.correct_answers:
                        marker = " **(Correct Answer)**"
                    f.write(f"- **{key})** {value}{marker}\n")

                f.write("\n")
                f.write(f"**Your Answer:** {', '.join(ans.selected_options)}\n")
                f.write(f"**Result:** {status_icon}\n\n")
                f.write("---\n\n")

        logger.info(f"Study report saved to {filepath}")
        return filepath
