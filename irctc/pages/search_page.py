from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from irctc.pages.base_page import BasePage


class SearchPage(BasePage):
    FROM_STATION = (By.CSS_SELECTOR, 'input[aria-controls="pr_id_1_list"]')
    TO_STATION = (By.CSS_SELECTOR, 'input[aria-controls="pr_id_2_list"]')
    STATION_SUGGESTION = (By.CSS_SELECTOR, "ul li[role='option'], .ui-autocomplete-list-item")
    JOURNEY_DATE = (By.CSS_SELECTOR, "p-calendar input, input[placeholder='Journey Date']")
    QUOTA_DROPDOWN = (By.ID, "journeyQuota")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(., 'Search') or contains(., 'SEARCH')]")

    def search(self, from_station: str, to_station: str, journey_date: str, quota: str) -> None:
        self.dismiss_ok_dialogs()
        self._fill_station(self.FROM_STATION, from_station)
        self._fill_station(self.TO_STATION, to_station)
        self._set_journey_date(journey_date)
        self._select_quota(quota)
        self.click(self.SEARCH_BUTTON)
        print("Searching trains...")

    def _fill_station(self, locator: tuple[str, str], station: str) -> None:
        field = self.type_text(locator, station)
        try:
            suggestion = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.STATION_SUGGESTION)
            )
            self.click_element(suggestion)
        except TimeoutException:
            field.send_keys(Keys.TAB)

    def _set_journey_date(self, date_text: str) -> None:
        field = self.type_text(self.JOURNEY_DATE, date_text)
        field.send_keys(Keys.TAB)

    def _select_quota(self, quota: str) -> None:
        self.click(self.QUOTA_DROPDOWN)
        self.click((By.XPATH, f"//li[@aria-label='{quota}']"))
