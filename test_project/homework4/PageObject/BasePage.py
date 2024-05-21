import datetime
import logging
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger('test')


def datetime_today():
    return str(datetime.datetime.today())


class BasePage:

    def __init__(self, driver):
        logger.info(f'Initializing page {self.__class__.__name__}...')
        self._driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self._driver, 10)

    def _get_waiter(self, time):
        return WebDriverWait(self._driver, time)

    def _find_element(self, by: str, locator: str) -> WebElement:
        return self._driver.find_element(by, locator)

    def _find_elements(self, by, locator) -> List[WebElement]:
        return self._driver.find_elements(by, locator)

    def _click(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        self._find_element(by, locator).click()

    def _send_keys(self, by, locator, text):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        self._find_element(by, locator).clear()
        self._find_element(by, locator).send_keys(text)

    def _get_page(self, url):
        self._driver.get(url)

    def _current_url(self):
        return self._driver.current_url

    def _current_url_starts_with(self, starts_url):
        return True if self._driver.current_url.startswith(f'{starts_url}') else False
