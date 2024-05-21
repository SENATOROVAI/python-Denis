from selenium.webdriver.common.by import By


class MainPageLocators:

    HEADER_LOGIN_BUTTON          = (By.CSS_SELECTOR, '.responseHead-module-button-2yl51i')
    EMAIL_INPUT                  = (By.CSS_SELECTOR, '.authForm-module-input-3j70Dv')
    PASSWORD_INPUT               = (By.CSS_SELECTOR, '.authForm-module-inputPassword-3t7Qac')
    LOGIN_BUTTON                 = (By.CSS_SELECTOR, '.authForm-module-button-1u2DYF')
    INCORRECT_LOGIN_LOCATOR      = (By.XPATH, '//div[@class="formMsg_text"]')
    WRONG_CREDENTIALS_LOCATOR    = (By.CSS_SELECTOR, '.notify-module-content-3S0RQM')
