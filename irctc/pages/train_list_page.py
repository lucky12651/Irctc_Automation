from selenium.webdriver.common.by import By

from irctc.pages.base_page import BasePage


class TrainListPage(BasePage):
    AVAILABILITY_LINK = (By.CSS_SELECTOR, "td.link.ng-star-inserted")

    def select_and_book(self, train_index: int) -> None:
        class_xpath = (
            '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]'
            f"/div[{train_index}]/div[1]/app-train-avl-enq/div[1]/div[5]/div/table/tr/td[1]/div"
        )
        book_xpath = (
            '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]'
            f"/div[{train_index}]/div[1]/app-train-avl-enq/div[2]/div/span/span/button[1]"
        )
        self.click((By.XPATH, class_xpath))
        self.click(self.AVAILABILITY_LINK)
        self.click((By.XPATH, book_xpath))
        self.dismiss_ok_dialogs()
