from __future__ import annotations

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    OK_BUTTON = (By.XPATH, "//button[normalize-space()='OK' or normalize-space()='Ok']")

    def __init__(self, driver: WebDriver, wait_seconds: int = 20) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_seconds)

    def open(self, url: str) -> None:
        self.driver.get(url)
        self.dismiss_ok_dialogs()

    def find(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: tuple[str, str], text: str) -> WebElement:
        field = self.visible(locator)
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(text)
        return field

    def pause_for_user(self, message: str) -> None:
        print(message)
        input("Press Enter here after you are done in the browser...")

    def dismiss_ok_dialogs(self) -> None:
        for _ in range(3):
            try:
                WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable(self.OK_BUTTON)
                ).click()
            except (TimeoutException, ElementClickInterceptedException):
                break
