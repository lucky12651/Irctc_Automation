from __future__ import annotations

from selenium.common.exceptions import TimeoutException

from irctc.config import Settings
from irctc.driver import create_chrome_driver
from irctc.pages.login_page import LoginPage
from irctc.pages.passenger_page import PassengerPage
from irctc.pages.search_page import SearchPage
from irctc.pages.train_list_page import TrainListPage


class BookingFlow:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.driver = create_chrome_driver()

    def run(self) -> None:
        wait = self.settings.wait_seconds
        login_page = LoginPage(self.driver, wait)
        search_page = SearchPage(self.driver, wait)
        train_list_page = TrainListPage(self.driver, wait)
        passenger_page = PassengerPage(self.driver, wait)

        try:
            login_page.open_home()
            login_page.fill_credentials(self.settings.username, self.settings.password)
            login_page.wait_for_manual_login()

            search_page.search(
                self.settings.from_station,
                self.settings.to_station,
                self.settings.journey_date,
                self.settings.quota,
            )
            train_list_page.select_and_book(self.settings.train_index)
            passenger_page.fill_passenger(
                self.settings.passenger_name,
                self.settings.age,
                self.settings.gender,
            )
            passenger_page.continue_after_review()
            passenger_page.continue_to_payment()
            print("Complete payment in the browser window.")
        except TimeoutException as exc:
            print(f"Timed out waiting for a page element: {exc}")
            raise
        finally:
            input("Press Enter to close the browser...")
            self.driver.quit()
