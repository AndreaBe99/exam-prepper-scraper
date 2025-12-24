"""Markdown Rendering Module.

Handles the logic of formatting Question objects into Markdown syntax.
"""

from datetime import datetime
from typing import Any


class MarkdownRenderer:
    """Converts exam data into formatted Markdown text."""

    def render_header(self, title: str, total_count: int) -> str:
        """Generates the document header.

        Args:
            title: The title of the document.
            total_count: Total number of questions.

        Returns:
            A formatted markdown string.
        """
        # Fix: Calculate timestamp here instead of using a broken placeholder
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"# {title}\n\n**Total Questions:** {total_count}\n**Generated:** {timestamp}\n\n---\n\n"

    def render_question(self, question: dict[str, Any]) -> str:
        """Formats a single question into Markdown.

        Args:
            question: A dictionary representing a question (from JSON).

        Returns:
            String containing the markdown representation.
        """
        q_id = question.get("id", "Unknown ID")
        text = question.get("text", "").replace("\n", "\n\n")
        options = question.get("options", {})

        # Handle correct answers safely (could be list or None)
        raw_correct = question.get("correct_answers", [])
        if isinstance(raw_correct, list):
            correct_answers = set(raw_correct)
        elif isinstance(raw_correct, str):
            correct_answers = {raw_correct}
        else:
            correct_answers = set()

        md_output = [f"### {q_id}\n", f"{text}\n"]

        # Render Options
        sorted_keys = sorted(options.keys())

        for key in sorted_keys:
            val = options[key]
            is_correct = key in correct_answers

            # Visual indicator for correct answer
            # if is_correct:
            #     line = f"- **{key}) {val}** ✅"
            # else:
            #     line = f"- {key}) {val}"
            line = f"- {key}) {val}"

            md_output.append(line)

        # Add a collapsed "Answer Key" section
        if correct_answers:
            correct_str = ", ".join(sorted(correct_answers))
            md_output.append(f"\n> **Correct Answer:** {correct_str}")

        md_output.append("\n---\n")
        return "\n".join(md_output)
