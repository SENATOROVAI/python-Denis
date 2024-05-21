import logging

from homework5.locators.LoginLocators import MainPageLocators
from homework5.PageObject.BasePage import BasePage

logger = logging.getLogger('test')


class MainPage(BasePage):
    """
        PageObject: https://target.my.com/
    """
    locators = MainPageLocators()

    MAIN_PAGE_URL = 'https://target.my.com/'

    def login_by_email(self, email, password):
        logger.info('Get https://target.my.com')
        self._get_page(self.MAIN_PAGE_URL)
        logger.info('Click HEADER_LOGIN_BUTTON')
        self._click(*self.locators.HEADER_LOGIN_BUTTON)
        logger.info(f'Enter email: {email}')
        self._send_keys(*self.locators.EMAIL_INPUT, email)
        logger.info(f'Enter password: {password}')
        self._send_keys(*self.locators.PASSWORD_INPUT, password)
        logger.info('Click LOGIN_BUTTON')
        self._click(*self.locators.LOGIN_BUTTON)
