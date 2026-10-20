from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from irctc.pages.base_page import BasePage


class PassengerPage(BasePage):
    NAME_INPUT = (
        By.CSS_SELECTOR,
        "app-passenger p-autocomplete input, app-passenger input[placeholder*='Name']",
    )
    AGE_INPUT = (
        By.XPATH,
        "//app-passenger//input[contains(@placeholder, 'Age') or @maxlength='3' or @maxlength='2']",
    )
    GENDER_SELECT = (By.CSS_SELECTOR, "app-passenger select")
    EXTRA_RADIO = (By.ID, "2")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.train_Search.btnDefault")
    CAPTCHA_INPUT = (By.ID, "captcha")

    def fill_passenger(self, name: str, age: str, gender: str) -> None:
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.AGE_INPUT, age)
        self._select_gender(gender)
        try:
            self.click(self.EXTRA_RADIO)
        except TimeoutException:
            print("No extra radio option found; continuing.")

    def continue_after_review(self) -> None:
        self.click(self.CONTINUE_BUTTON)
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.CAPTCHA_INPUT))
            self.pause_for_user(
                "Solve the captcha in the browser, then click continue.",
                wait_locator=self.CAPTCHA_INPUT,
            )
        except TimeoutException:
            print("No captcha on this step.")

    def continue_to_payment(self) -> None:
        self.click(self.CONTINUE_BUTTON)

    def _select_gender(self, gender: str) -> None:
        gender_select = Select(self.find(self.GENDER_SELECT))
        value = gender.upper()
        if value == "M":
            gender_select.select_by_index(1)
        elif value == "F":
            gender_select.select_by_index(2)
        else:
            raise ValueError("gender must be 'M' or 'F'")
