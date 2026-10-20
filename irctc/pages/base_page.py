from __future__ import annotations

import sys

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    OK_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='OK' or normalize-space()='Ok' or normalize-space()='ok']",
    )
    DIALOG_CLOSE = (
        By.CSS_SELECTOR,
        "span.ui-dialog-titlebar-close, button.ui-dialog-titlebar-close, .pi-times, .fa-times",
    )
    OVERLAY = (By.CSS_SELECTOR, ".ui-dialog-mask, .custom-blur-mask, .ui-widget-overlay")

    def __init__(self, driver: WebDriver, wait_seconds: int = 20) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_seconds)

    def open(self, url: str) -> None:
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 8).until(
                EC.any_of(
                    EC.presence_of_element_located(self.OK_BUTTON),
                    EC.presence_of_element_located(self.OVERLAY),
                )
            )
        except TimeoutException:
            pass
        self.dismiss_ok_dialogs()

    def find(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.click_element(element)

    def click_element(self, element: WebElement) -> None:
        try:
            element.click()
        except ElementClickInterceptedException:
            self.dismiss_ok_dialogs()
            self.driver.execute_script("arguments[0].click();", element)

    def is_visible(self, locator: tuple[str, str], timeout: float = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def type_text(self, locator: tuple[str, str], text: str) -> WebElement:
        field = self.visible(locator)
        try:
            field.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", field)
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(text)
        return field

    def pause_for_user(self, message: str, wait_locator: tuple[str, str] | None = None) -> None:
        print(message)
        if wait_locator is not None:
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located(wait_locator))
            return
        if sys.stdin.isatty():
            input("Press Enter here after you are done in the browser...")

    def dismiss_ok_dialogs(self) -> None:
        for locator in (self.OK_BUTTON, self.DIALOG_CLOSE):
            try:
                button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))
                try:
                    button.click()
                except (ElementClickInterceptedException, StaleElementReferenceException):
                    try:
                        self.driver.execute_script("arguments[0].click();", button)
                    except StaleElementReferenceException:
                        continue
            except TimeoutException:
                continue

        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.OVERLAY))
        except TimeoutException:
            self.driver.execute_script(
                """
                document.querySelectorAll('.ui-dialog-mask, .custom-blur-mask, .ui-widget-overlay')
                    .forEach(el => el.remove());
                """
            )
