from selenium.webdriver.common.by import By

from irctc.config import IRCTC_URL
from irctc.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[contains(., 'LOGIN') or contains(., 'Login')]")
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="User Name"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Password"]')

    def open_home(self) -> None:
        self.open(IRCTC_URL)

    def fill_credentials(self, username: str, password: str) -> None:
        self.click(self.LOGIN_LINK)
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)

    def wait_for_manual_login(self) -> None:
        self.pause_for_user("Solve the login captcha in the browser, then click SIGN IN.")
