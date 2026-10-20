from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from irctc.config import IRCTC_URL
from irctc.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[contains(., 'LOGIN') or contains(., 'Login')]")
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="User Name"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Password"]')
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(., 'SIGN IN') or contains(., 'Sign In')]")
    CAPTCHA_IMAGE = (By.CSS_SELECTOR, ".captcha-img, img[alt*='captcha' i], img[src*='captcha' i]")
    CAPTCHA_INPUT = (By.ID, "captcha")

    def open_home(self) -> None:
        self.open(IRCTC_URL)

    def fill_credentials(self, username: str, password: str) -> None:
        self.dismiss_ok_dialogs()
        self.click(self.LOGIN_LINK)
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)

    def complete_login(self) -> None:
        if self._captcha_is_visible():
            print("Captcha is present. Solve it in the browser, then click SIGN IN.")
        else:
            print("No captcha. Clicking SIGN IN.")
            self.click(self.SIGN_IN_BUTTON)
            if self._captcha_is_visible():
                print("Captcha appeared after SIGN IN. Solve it in the browser, then click SIGN IN.")

        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located(self.USERNAME_INPUT))
        print("Logged in. Continuing...")

    def _captcha_is_visible(self) -> bool:
        return self.is_visible(self.CAPTCHA_IMAGE, timeout=3) or self.is_visible(
            self.CAPTCHA_INPUT, timeout=1
        )
