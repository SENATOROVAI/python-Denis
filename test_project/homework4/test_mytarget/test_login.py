import time
import pytest
from homework4.locators.CompanyLocators import CompanyLocators
from homework4.suite.base import BaseSuiteTest
from homework4.PageObject.MainPage import MainPage

pytest_plugins = ["homework4.fixture.login"]

correct_email = 'd.fomchenko@petrovich.ru'
correct_password = '#MDE9#NvyedRPhq'
target_login_url = 'https://account.my.com/login'
target_my_url = 'https://target.my.com'
incorrect_login_message = 'Invalid login or password'
enter_email_or_phone = 'Please input email or mobile phone number'
wrong_password = 'Invalid password format'
no_error_message = 'Отсутствует сообщение об ошибке!'
wrong_url = 'Неправильный урzл!'


class TestLogin(BaseSuiteTest):

    locators = CompanyLocators()

    @pytest.mark.parametrize('email, password', [(correct_email, "000000"), (correct_email, correct_email)])
    def test_login_with_wrong_email_or_password(self, email, password):
        page = self.get_page(MainPage)
        time.sleep(2)
        page.login_by_email(email, password)
        message = page._find_element(*page.locators.INCORRECT_LOGIN_LOCATOR).text
        assert page._current_url_starts_with(target_login_url), wrong_url
        assert message == incorrect_login_message, no_error_message

    @pytest.mark.parametrize('email, password', [(correct_email.replace("@", ""), correct_password),
                                                 (correct_password, correct_password)])
    def test_login_with_incorrect_email(self, email, password):
        page = self.get_page(MainPage)
        page.login_by_email(email, password)
        time.sleep(2)
        message = page._find_element(*page.locators.WRONG_CREDENTIALS_LOCATOR).text
        assert page._current_url_starts_with(target_my_url), wrong_url
        assert message == enter_email_or_phone, no_error_message

    def test_login_with_empty_password(self):
        page = self.get_page(MainPage)
        page.login_by_email(correct_email, " ")
        time.sleep(2)
        message = page._find_element(*page.locators.WRONG_CREDENTIALS_LOCATOR).text
        assert page._current_url_starts_with(target_my_url), wrong_url
        assert message == wrong_password, no_error_message
