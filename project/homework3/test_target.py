import time
import pytest
from selenium.webdriver.common.by import By


email = 'd.fomchenko@petrovich.ru'
password = '#MDE9#NvyedRPhq'
dashboard_url = 'https://target.my.com/dashboard'
main_page_url = 'https://target.my.com/'

fio = 'Рамблер И.А'
phone_number = '+79910134300'


@pytest.fixture
def login(browser):
    browser.get(dashboard_url)
    browser.find_element(By.CSS_SELECTOR, '.responseHead-module-button-2yl51i').click()
    browser.find_element(By.CSS_SELECTOR, '.authForm-module-input-3j70Dv').send_keys(email)
    browser.find_element(By.CSS_SELECTOR, '.authForm-module-inputPassword-3t7Qac').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '.authForm-module-button-1u2DYF').click()
    time.sleep(1)


@pytest.mark.UI
def test_login(browser, login):
    login_email = browser.find_element(By.CSS_SELECTOR, '.right-module-userNameWrap-3Odw2D').text
    assert browser.current_url == dashboard_url, 'Неправильный урл!'
    assert 'D.FOMCHENKO@PETROVICH.RU' in login_email, 'Отсутствует почта'
    starting_question = browser.find_element(By.CSS_SELECTOR, '.instruction-module-title-3Yn8SZ').text
    assert 'С чего начать?' in starting_question, 'Приветственный вопрос отсутствует'


@pytest.mark.UI
def test_logout(browser, login):
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.right-module-userNameWrap-3Odw2D').click()
    logout = browser.find_element(By.XPATH, '//a[@href="/logout"]')
    time.sleep(0.5)
    logout.click()
    assert browser.current_url == main_page_url, 'Неправильный урл!'
    login = browser.find_element(By.CSS_SELECTOR, '.responseHead-module-button-2yl51i').text
    assert 'Войти' in login


@pytest.mark.skip(reason='Баг')
@pytest.mark.UI
def test_edit_profile(browser, login):
    browser.find_element(By.XPATH, '//a[@href="/profile"]').click()
    browser.find_element(By.XPATH, '//div[@data-name="fio"]/div[@class="input__wrap"]/input').send_keys(fio)
    browser.find_element(By.XPATH, '//div[@data-name="phone"]/div[@class="input__wrap"]/input').send_keys(phone_number)
    browser.find_element(By.XPATH, '//div[@class="button__text"]').click()
    browser.refresh()
    assert browser.find_element(By.CSS_SELECTOR, '.right-module-userNameWrap-3Odw2D').text \
           == fio.upper(), 'Неверное отображение ФИО в хэдере'
    assert browser.find_element(By.XPATH, '//div[@data-name="fio"]/div[@class="input__wrap"]/input'). \
        get_attribute('value') == fio, 'Неверное отображение ФИО в инпуте'
    assert browser.find_element(By.XPATH, '//div[@data-name="phone"]/div[@class="input__wrap"]/input'). \
        get_attribute('value') == phone_number, 'Неверное отображение телефона в инпуте'
    browser.find_element(By.XPATH, '//div[@data-name="fio"]/div[@class="input__wrap"]/input').clear()
    browser.find_element(By.XPATH, '//div[@data-name="phone"]/div[@class="input__wrap"]/input').clear()
    browser.find_element(By.XPATH, '//div[@class="button__text"]').click()
    browser.get(dashboard_url)
    assert browser.find_element(By.CSS_SELECTOR, '.right-module-userNameWrap-3Odw2D').text \
           == email.upper(), 'Неверное отображение ФИО в хэдере'


@pytest.mark.UI
@pytest.mark.parametrize('url, locator', [(main_page_url + 'billing#deposit', '//a[@href="/billing"][@target]'),
                                          (main_page_url + 'statistics/summary', '//a[@href="/statistics"][@target]')])
def test_headers_menu(browser, url, locator, login):
    browser.find_element(By.XPATH, locator).click()
    time.sleep(2)
    assert browser.current_url == url, 'Неправильный урл!'
