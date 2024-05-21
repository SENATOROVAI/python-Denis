import os
import shutil
import sys
import logging
from selenium.webdriver.chrome.service import Service
import allure
import pytest
from selenium.webdriver import Chrome, ChromeOptions, Remote
from webdriver_manager.chrome import ChromeDriverManager
from homework5.api.fixtures import *


@pytest.fixture()
def logger(test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
    log_file = os.path.join(test_dir, 'debug.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False

    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    allure.attach.file(log_file, 'debug.log', attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def user():
    class User:
        EMAIL = 'd.fomchenko@petrovich.ru'
        PASSWORD = '#MDE9#NvyedRPhq'

    return User()


@pytest.fixture
def browser(request, test_dir, ui_config):
    selenoid = ui_config['selenoid']
    vnc = ui_config['vnc']
    options = ChromeOptions()
    prefs = {}
    if selenoid is not None:
        capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100.0',
            'sessionTimeout': "10m"
        }
        if vnc:
            capabilities['browserVersion'] += '_vnc'
            capabilities['enableVNC'] = True

        driver = Remote(selenoid + '/wd/hub', options=options, desired_capabilities=capabilities)
    else:
        manager = ChromeDriverManager(log_level=0)
        path = manager.install()

        service = Service(executable_path=path)
        driver = Chrome(service=service, options=options)

    driver.maximize_window()

    driver.implicitly_wait(20)
    options.add_experimental_option("prefs", prefs)

    yield driver
    if request.node.rep_call.failed:
        screenshot_path = os.path.join(test_dir, 'failure.png')
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_log_path = os.path.join(test_dir, 'browser.log')
        with open(browser_log_path, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_log_path, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--url', help='SUT stand')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def ui_config(request):
    if request.config.getoption('--selenoid'):
        selenoid = 'http://127.0.0.1:4444'
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False

    else:
        selenoid = None
        vnc = False

    return {'selenoid': selenoid, 'vnc': vnc}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture()
def upload_file_path(repo_root):
    return os.path.join(repo_root, "files/240x400.jpg")


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_dir = base_dir


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture()
def test_dir(request):
    test_name = request._pyfuncitem.nodeid
    test_dir = os.path.join(request.config.base_dir, test_name.replace('/', '_')
                            .replace(':', '_')
                            .replace('-', '_')
                            .replace('[', '_')
                            .replace(']', ''))
    os.makedirs(test_dir)
    return test_dir
