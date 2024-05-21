import time
import typing
import allure
import pytest
import logging
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from homework5.PageObject.BasePage import BasePage
from homework5.api.fixtures import api_client

T = typing.TypeVar('T', bound=BasePage)


class BaseUiSuiteTest:
    authorize = True

    base_url: str
    browser: ChromiumDriver
    logger: logging.Logger
    api_client: api_client

    @pytest.fixture(autouse=True)
    def prepare(self, browser, logger, request, api_client):
        self.browser: ChromiumDriver = browser
        self.logger: logging.Logger = logger
        self.logger.info('PREPARE DONE')

        time.sleep(3)
        if self.authorize:
            self.browser.get(url="https://target.my.com/")
            time.sleep(3)
            api_client = request.getfixturevalue('cookies')
            for api_client in api_client:
                if api_client.domain in ".target.my.com":
                    cookie_dict = {
                        'domain': api_client.domain,
                        'name': api_client.name,
                        'value': api_client.value,
                        'secure': api_client.secure
                    }
                    self.browser.add_cookie(cookie_dict)
            self.browser.refresh()

    @allure.step('Getting page {page_class}')
    def get_page(self, page_class: typing.Type[T]) -> T:
        return page_class(self.browser)
