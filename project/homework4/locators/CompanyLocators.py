from selenium.webdriver.common.by import By


class CompanyLocators:

    CREATE_NEW_COMPANY_LOCATOR      = (By.XPATH, '//a[@href="/campaign/new"]')
    CREATE_ANOTHER_COMPANY_LOCATOR  = (By.CSS_SELECTOR, '.button-module-button-1v2gG_.button-module-blue-3nuTZJ')
    PURPOSE_TRAFFIC_COMPANY_LOCATOR = (By.XPATH, '//div[@cid="view605"]')
    LINK_INPUT                      = (By.CSS_SELECTOR, '.mainUrl-module-searchInput-1yPahG')
    COMPANY_NAME_INPUT              = (By.XPATH, '//div[@cid="view680"]/div[@class="input__wrap"]/input[@type="text"]')
    BANNER_FORMAT_LOCATOR           = (By.XPATH, '//div[@id="patterns_banner_4"]')
    UPLOAD_PICTURE240X240           = (By.CSS_SELECTOR, '.roles-module-buttonWrap-2SwE2M')
    UPLOAD_PICTURE240X240_XPATH     = (By.XPATH, '//input[@data-test="image_240x400"]')
    CROP_PICTURE240X240_LOCATOR     = (By.XPATH, '//input[@class="image-cropper__save js-save"]')
    ACCEPT_COMPANY_CREATION_LOCATOR = (By.XPATH, '//div[@class="footer__button js-save-button-wrap"]')
    CREATED_COMPANY_NAME_LOCATOR    = (By.XPATH, '//a[@class="nameCell-module-campaignNameLink-2WGamp"]')
