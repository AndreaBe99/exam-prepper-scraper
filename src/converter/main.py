"""Main entry point for the Converter Application."""

import json
import sys
from pathlib import Path

from loguru import logger

from converter import config
from converter.renderer import MarkdownRenderer


def configure_logging() -> None:
    """Configures Loguru for console output."""
    logger.remove()
    logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>", level="INFO")


def load_data(filepath: Path) -> list[dict]:
    """Loads the source data from JSON.

    Args:
        filepath: Path to the JSON file.

    Returns:
        A list of question dictionaries.
    """
    if not filepath.exists():
        raise FileNotFoundError(f"Input file not found: {filepath}")

    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    """Main execution function."""
    configure_logging()
    logger.info("Starting Markdown Converter...")

    # 1. Load Data
    try:
        data = load_data(config.INPUT_FILE)
        logger.info(f"Loaded {len(data)} questions from {config.INPUT_FILE.name}")
    except Exception as e:
        logger.critical(f"Failed to load data: {e}")
        return

    # 2. Render Markdown
    renderer = MarkdownRenderer()
    md_content = [renderer.render_header("Exam Dump Export", len(data))]

    for i, question in enumerate(data, 1):
        try:
            # Sort loosely by ID if possible, otherwise keep file order
            md_block = renderer.render_question(question)
            md_content.append(md_block)
        except Exception as e:
            logger.warning(f"Skipping malformed question at index {i}: {e}")

    # 3. Save File
    try:
        with open(config.OUTPUT_MD_FILE, "w", encoding="utf-8") as f:
            f.write("".join(md_content))
        logger.success(f"Successfully exported to: {config.OUTPUT_MD_FILE}")
    except Exception as e:
        logger.critical(f"Failed to write markdown file: {e}")


if __name__ == "__main__":
    main()
