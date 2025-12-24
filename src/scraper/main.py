"""Main entry point for the scraper."""

import sys
import time

import undetected_chromedriver as uc
from loguru import logger

from scraper import config
from scraper.browser import ExamPage
from scraper.models.question import QuestionDTO
from scraper.storage import FileSaver, SaverFactory, create_backup


def configure_logging() -> None:
    """Configures Loguru logger."""
    logger.remove()
    logger.add(sys.stderr, level="INFO", format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>")
    logger.add(
        config.LOG_FILE,
        rotation="10 MB",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} - {message}",
    )


def initialize_driver() -> uc.Chrome | None:
    """Initializes the Undetected Chrome Driver with configured options.

    Returns:
        The Chrome driver instance or None if initialization fails.
    """
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    if config.HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")

    try:
        # Auto-detect version
        driver = uc.Chrome(options=options)
        logger.debug("Undetected Chrome driver started successfully.")
        return driver
    except Exception as e:
        logger.critical(f"Failed to start Undetected Chrome: {e}")
        return None


def main() -> None:
    """Orchestrates the scraping process."""
    configure_logging()
    logger.info("Starting Scraper Application...")
    logger.info(f"Configuration: Start={config.QUESTION_RANGE_START}, End={config.QUESTION_RANGE_END}")

    # 1. Initialize Saver and Backup
    try:
        saver: FileSaver = SaverFactory.get_saver(config.OUTPUT_FORMAT)
        # Create a timestamped backup before touching the file
        create_backup(config.OUTPUT_FILE)
        # Load existing data into memory to allow updates
        master_question_map: dict[str, QuestionDTO] = saver.load_existing(config.OUTPUT_FILE)
        logger.info(f"Loaded {len(master_question_map)} existing questions.")
    except Exception as e:
        logger.critical(f"Initialization Error: {e}")
        return

    # 2. Initialize Driver
    driver = initialize_driver()
    if not driver:
        return

    try:
        page_object = ExamPage(driver)
        page_object.load(config.START_URL)

        page_num = 1

        while True:
            logger.info(f"--- Processing Page {page_num} ---")

            page_object.reveal_all_answers()

            # Extract data
            new_questions, limit_reached, max_id_on_page = page_object.extract_questions(
                start_id=config.QUESTION_RANGE_START, end_id=config.QUESTION_RANGE_END
            )

            # Manual Intervention Logic (Login Wall detection)
            if max_id_on_page == 0:
                logger.warning(f"No questions visible on Page {page_num}. Possible Login Wall.")
                print("\a")
                print("\n" + "=" * 60)
                print("🛑 PAUSED: LOGIN REQUIRED OR CAPTCHA")
                print("1. Go to the Chrome window.")
                print("2. Log in / Solve Captcha.")
                print("3. Ensure questions are visible.")
                print("4. Press ENTER here to resume.")
                print("=" * 60 + "\n")
                input("Press ENTER to resume scraping...")

                logger.info("Resuming...")
                page_object.reveal_all_answers()
                new_questions, limit_reached, max_id_on_page = page_object.extract_questions(
                    config.QUESTION_RANGE_START, config.QUESTION_RANGE_END
                )

            count = len(new_questions)
            if count > 0:
                logger.info(f"Extracted {count} relevant questions.")

                # Merge logic: Update master map
                for q in new_questions:
                    master_question_map[q.id] = q

                # Save the updated master map
                saver.save(master_question_map, config.OUTPUT_FILE)

            elif max_id_on_page > 0:
                logger.info(f"Page {page_num} scanned. No questions within target range.")

            if limit_reached:
                logger.success(f"Reached end limit (Question {config.QUESTION_RANGE_END}). Stopping.")
                break

            # Pagination
            has_next = page_object.go_to_next_page()
            if not has_next:
                logger.info("No more pages found. Scrape complete.")
                break

            page_num += 1
            time.sleep(2)

    except KeyboardInterrupt:
        logger.warning("Scraper stopped by user.")
    except Exception as e:
        logger.exception(f"An unexpected crash occurred: {e}")
    finally:
        logger.info("Closing browser...")
        if driver:
            try:
                driver.quit()
            except OSError:
                pass


if __name__ == "__main__":
    main()
