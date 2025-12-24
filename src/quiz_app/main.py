"""Main entry point for the Quiz Application."""

from loguru import logger

from quiz_app import config
from quiz_app.engine import QuizEngine
from quiz_app.ui import QuizUI


def configure_logging() -> None:
    """Configures Loguru to write to file only.

    We remove the default console handler because printing logs to stdout/stderr
    will break the 'rich' and 'questionary' TUI layout.
    """
    logger.remove()
    logger.add(
        config.QUIZ_LOG_FILE,
        rotation="5 MB",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} - {message}",
    )


def main() -> None:
    """Main execution function."""
    configure_logging()

    # 1. Initialize UI and Engine
    ui = QuizUI()
    engine = QuizEngine(
        filepath=config.QUESTIONS_FILE, max_questions=config.MAX_QUESTIONS, time_limit_minutes=config.TIMER_MINUTES
    )

    # 2. Load Data
    try:
        engine.load_and_shuffle()
    except Exception as e:
        logger.exception("Fatal error loading exam data.")
        ui.console.print(f"[bold red]Error loading exam:[/bold red] {e}")
        return

    # 3. Welcome Screen
    ui.show_welcome(len(engine.questions), config.TIMER_MINUTES)
    engine.start_timer()

    # 4. Game Loop
    for i, question in enumerate(engine.questions, 1):
        # A. Check Timer
        remaining = engine.get_remaining_time()
        if engine.is_time_up():
            logger.warning("Time limit reached during exam.")
            ui.console.print("\n[bold red on white] ⏰ TIME IS UP! [/bold red on white]")
            break

        # B. Update Display
        ui.show_header(i, len(engine.questions), remaining)

        # C. Get User Input
        try:
            selected = ui.ask_question(question)
        except KeyboardInterrupt:
            logger.warning("User interrupted quiz (Ctrl+C).")
            ui.console.print("\n[yellow]Quiz cancelled by user.[/yellow]")
            return

        # D. Record Answer (Logging happens inside here)
        engine.record_answer(question, selected)

    # 5. Final Results
    stats = engine.calculate_score()
    ui.show_results(stats, engine.user_answers)

    # 6. Save Study Guide
    try:
        report_path = engine.save_report()
        ui.console.print(f"\n[bold green]📝 Study guide saved to:[/bold green] [underline]{report_path}[/underline]")
    except Exception as e:
        logger.error(f"Failed to save report: {e}")
        ui.console.print(f"\n[bold red]Failed to save study guide:[/bold red] {e}")


if __name__ == "__main__":
    main()
