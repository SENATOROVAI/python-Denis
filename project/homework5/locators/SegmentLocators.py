from selenium.webdriver.common.by import By


class SegmentLocators:

    HEADER_AUDIENCE_LOCATOR              = (By.XPATH, '//a[@href="/segments"]')
    CREATE_SEGMENT_LOCATOR               = (By.XPATH, '//button[@class="button button_submit"]')
    CHECKBOX_SEGMENT_LOCATOR             = (By.XPATH, '//input[@type="checkbox"]')
    ADD_SEGMENT_LOCATOR                  = (By.XPATH, '//div[text()="Добавить сегмент"]')
    SEGMENT_NAME_LOCATOR                 = (By.XPATH, '//div[@class="js-segment-name"]/div//input')
    CREATED_SEGMENT_LOCATOR              = (By.XPATH, '//div[@class="cells-module-nameCell-zlAsWX"]')
    CREATE_NEW_SEGMENT_LOCATOR           = (By.XPATH, '//div[text()="Создать сегмент"]')

    REMOVE_SEGMENT_LOCATOR               = (By.XPATH, '//span[@class="icon-cross cells-module-removeCell-2x-ZuB"]')
    ACCEPT_REMOVE_LOCATOR                = (By.XPATH, '//div[text()="Удалить"]')

    CREATE_FIRST_SEGMENT_EVER_LOCATOR    = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
