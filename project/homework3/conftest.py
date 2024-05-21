import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

manager = ChromeDriverManager()
path = manager.install()

@pytest.fixture
def browser():
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.implicitly_wait(12)
    yield driver
    driver.quit()



