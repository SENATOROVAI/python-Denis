import time
import pytest
from homework5.PageObject.MainPage import MainPage
from homework5.test_mytarget.test_login import correct_email, correct_password


@pytest.fixture
def login_target(browser, login=correct_email, password=correct_password):
    page = MainPage(browser)
    page.login_by_email(login, password)
    time.sleep(1)


@pytest.fixture
def main_page(browser):
    MainPage(browser)
    time.sleep(1)
