import typing

import allure
import pytest
import logging
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from homework4.PageObject.BasePage import BasePage

T = typing.TypeVar('T', bound=BasePage)


class BaseSuiteTest:

    base_url: str
    browser: ChromiumDriver
    logger: logging.Logger

    @pytest.fixture(autouse=True)
    def prepare(self, browser, logger):
        self.browser: ChromiumDriver = browser
        self.logger: logging.Logger = logger
        self.logger.info('PREPARE DONE')

    @allure.step('Getting page {page_class}')
    def get_page(self, page_class: typing.Type[T]) -> T:
        return page_class(self.browser)
