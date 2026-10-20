from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_chrome_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    return webdriver.Chrome(options=options)
