"""Contains Selenium logic and Page Object definitions."""

import re
import time

from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from scraper.models.question import QuestionDTO


class ExamPage:
    """Page Object Model for the exam website."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Initializes the page object.

        Args:
            driver: The Selenium Chrome driver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def load(self, url: str) -> None:
        """Navigates to the URL and handles potential WAF blocks.

        Args:
            url: The target URL.

        Raises:
            TimeoutException: If the page content does not load in time.
        """
        logger.info(f"Navigating to {url}")
        self.driver.get(url)

        end_time = time.time() + 30
        while time.time() < end_time:
            try:
                self.driver.find_element(By.CLASS_NAME, "chakra-accordion")
                logger.debug("Page loaded successfully.")
                time.sleep(2)
                return
            except NoSuchElementException:
                pass

            if "Security Checkpoint" in self.driver.title:
                logger.warning("Detected Security Checkpoint. Waiting...")
                time.sleep(5)
                continue
            time.sleep(1)

        logger.error("Timeout waiting for page load.")
        raise TimeoutException("Page did not load within 30s.")

    def reveal_all_answers(self) -> None:
        """Clicks all 'Show Answer' buttons on the current page."""
        try:
            buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Show Answer')]")
            if not buttons:
                return

            logger.debug(f"Revealing answers for {len(buttons)} questions...")
            for btn in buttons:
                self.driver.execute_script("arguments[0].click();", btn)

            # Wait for CSS transitions (green borders) to apply
            time.sleep(1.5)
        except Exception as e:
            logger.warning(f"Could not reveal answers: {e}")

    def extract_questions(
        self, start_id: int | None = None, end_id: int | None = None
    ) -> tuple[list[QuestionDTO], bool, int]:
        """Extracts questions, respecting optional start/end limits.

        Args:
            start_id: The minimum question number (inclusive). If None, starts from 0.
            end_id: The maximum question number (inclusive). If None, goes indefinitely.

        Returns:
            A tuple containing:
            - list[QuestionDTO]: The extracted questions.
            - bool: limit_reached (True if we found a question > end_id).
            - int: max_id_found (The highest Question ID found on this page).
        """
        questions_data: list[QuestionDTO] = []
        limit_reached = False
        max_id_found = 0

        containers = self.driver.find_elements(By.CLASS_NAME, "chakra-accordion__item")

        if not containers:
            logger.debug("No question containers found in DOM.")

        for i, container in enumerate(containers):
            try:
                q_dto = self._parse_single_container(container, i + 1)
                if not q_dto:
                    continue

                q_num = self._extract_question_number(q_dto.id)
                max_id_found = max(max_id_found, q_num)

                # Check End Limit
                if end_id is not None and q_num > end_id:
                    logger.info(f"Reached Question {q_num}. Exceeds limit {end_id}.")
                    limit_reached = True
                    break

                # Check Start Limit
                if start_id is not None and q_num < start_id:
                    # Skip this question, but continue the loop
                    continue

                questions_data.append(q_dto)

            except Exception:
                logger.exception(f"Error parsing container #{i + 1}")
                continue

        return questions_data, limit_reached, max_id_found

    def go_to_next_page(self) -> bool:
        """Navigates to the next page.

        Returns:
            True if navigation was successful, False if no next page exists.
        """
        try:
            next_btns = self.driver.find_elements(By.XPATH, "//button[text()='Next']")
            if not next_btns:
                logger.info("Next button not found. End of exam.")
                return False

            next_btn = next_btns[0]
            if not next_btn.is_enabled():
                logger.info("Next button is disabled.")
                return False

            current_url = self.driver.current_url
            self.driver.execute_script("arguments[0].click();", next_btn)

            WebDriverWait(self.driver, 15).until(lambda d: d.current_url != current_url)
            time.sleep(2)
            return True

        except Exception as e:
            logger.error(f"Pagination error: {e}")
            return False

    def _extract_question_number(self, q_id_str: str) -> int:
        """Parses the numeric value from a Question ID string."""
        match = re.search(r"(\d+)", q_id_str)
        if match:
            return int(match.group(1))
        return 0

    def _parse_single_container(self, container: WebElement, index: int) -> QuestionDTO | None:
        """Extracts data from a single question DOM element."""
        try:
            btn_el = container.find_element(By.CLASS_NAME, "chakra-accordion__button")
            raw_id = btn_el.text.split("\n")[0].strip()
        except NoSuchElementException:
            raw_id = f"Unknown_Q_{index}"

        try:
            panel = container.find_element(By.CLASS_NAME, "chakra-accordion__panel")
            text_div = panel.find_element(By.XPATH, ".//div[contains(@class, 'css-naa3lg')]")
            q_text = text_div.text.strip()
        except NoSuchElementException:
            logger.warning(f"[{raw_id}] Could not find question text div.")
            return None

        options_map = {}
        correct_answers_list = []

        try:
            options_container = panel.find_element(By.XPATH, ".//div[contains(@class, 'css-j7qwjs')]")
            option_rows = options_container.find_elements(By.XPATH, "./div")
        except NoSuchElementException:
            logger.warning(f"[{raw_id}] No options container found.")
            return None

        for row in option_rows:
            try:
                label_el = row.find_element(By.XPATH, ".//p[contains(@class, 'css-xakj1w')]")
                label_text = label_el.text.replace(".", "").strip()

                val_el = row.find_element(By.XPATH, ".//div[contains(@class, 'css-cba290')]")
                val_text = val_el.text.strip()

                options_map[label_text] = val_text

                border_color = row.value_of_css_property("border-color")
                class_attr = row.get_attribute("class")

                is_green_border = "rgb(56, 161, 105)" in border_color or "rgb(72, 187, 120)" in border_color

                if is_green_border or "css-jjzrip" in class_attr:
                    correct_answers_list.append(label_text)

            except NoSuchElementException:
                continue

        return QuestionDTO(id=raw_id, text=q_text, options=options_map, correct_answers=correct_answers_list)
