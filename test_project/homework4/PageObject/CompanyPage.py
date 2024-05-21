import logging
import time

import allure

from homework4.PageObject.BasePage import BasePage, datetime_today
from homework4.locators.CompanyLocators import CompanyLocators

logger = logging.getLogger('test')


class CompanyPage(BasePage):
    """
        PageObject: https://target.my.com/campaign/new
    """
    locators = CompanyLocators()
    vk = 'https://vk.com'
    company_name = 'Новая компания ' + datetime_today()

    @allure.step('Click correct locator')
    def click_new_company_correct_locator(self):
        try:
            logger.info('Click CREATE_ANOTHER_COMPANY_LOCATOR')
            self._click(*self.locators.CREATE_ANOTHER_COMPANY_LOCATOR)
        except:
            logger.info('Click CREATE_NEW_COMPANY_LOCATOR (first company)')
            self._click(*self.locators.CREATE_NEW_COMPANY_LOCATOR)

    def create_company_with_traffic(self, upload_file_path):
        self.click_new_company_correct_locator()
        logger.info('Click PURPOSE_TRAFFIC_COMPANY_LOCATOR')
        self._click(*self.locators.PURPOSE_TRAFFIC_COMPANY_LOCATOR)
        logger.info(f'Enter LINK_INPUT: {self.vk}')
        self._send_keys(*self.locators.LINK_INPUT, self.vk)
        logger.info(f'Enter COMPANY_NAME: {self.company_name}')
        self._send_keys(*self.locators.COMPANY_NAME_INPUT, self.company_name)
        logger.info('Click BANNER_FORMAT_LOCATOR')
        self._click(*self.locators.BANNER_FORMAT_LOCATOR)
        logger.info(f'Upload file from: {upload_file_path}')
        self._find_element(*self.locators.UPLOAD_PICTURE240X240_XPATH).send_keys(upload_file_path)
        logger.info('')
        self._click(*self.locators.CROP_PICTURE240X240_LOCATOR)
        logger.info('')
        self._click(*self.locators.ACCEPT_COMPANY_CREATION_LOCATOR)
        time.sleep(5)

    @allure.step('Copy created company')
    def created_company_text(self):
        logger.info('Cope CREATED_COMPANY_NAME_LOCATOR (text)')
        return self._find_element(*self.locators.CREATED_COMPANY_NAME_LOCATOR).text
