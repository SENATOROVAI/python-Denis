import logging
import time

from homework5.api.data.segment import body_for_creation
from homework5.api.fixtures import *
from homework5.PageObject.BasePage import BasePage, datetime_today
from homework5.locators.SegmentLocators import SegmentLocators
from homework5.test_mytarget.test_company import TestCompany

logger = logging.getLogger('test')


class SegmentPage(BasePage, ApiClient):
    """
        https://target.my.com/segments/segments_list
    """
    locators = SegmentLocators()

    segment_name = 'Новый сегмент ' + datetime_today()

    def click_header_audience(self):
        logger.info('Click HEADER_AUDIENCE_LOCATOR')
        self._click(*self.locators.HEADER_AUDIENCE_LOCATOR)

    def click_create_segment_correct_locator(self):
        try:
            logger.info('Click CREATE_SEGMENT_LOCATOR')
            self._click(*self.locators.CREATE_SEGMENT_LOCATOR)
        except:
            logger.info('Click CREATE_FIRST_SEGMENT_EVER_LOCATOR')
            self._click(*self.locators.CREATE_FIRST_SEGMENT_EVER_LOCATOR)

    def create_new_segment(self):
        self.click_create_segment_correct_locator()
        logger.info('Click CHECKBOX_SEGMENT_LOCATOR')
        self._click(*self.locators.CHECKBOX_SEGMENT_LOCATOR)
        logger.info('Click ADD_SEGMENT_LOCATOR')
        self._click(*self.locators.ADD_SEGMENT_LOCATOR)
        logger.info(f'Enter segment name: {self.segment_name}')
        self._send_keys(*self.locators.SEGMENT_NAME_LOCATOR, self.segment_name)
        logger.info('Click CREATE_NEW_SEGMENT_LOCATOR')
        self._click(*self.locators.CREATE_NEW_SEGMENT_LOCATOR)
        time.sleep(3)

    def created_segment_text(self):
        logger.info('Copy CREATED_SEGMENT_LOCATOR (text)')
        return self._find_element(*self.locators.CREATED_SEGMENT_LOCATOR).text

    def count_segments(self):
        logger.info('Count segments')
        return len(self._find_elements(*self.locators.CREATED_SEGMENT_LOCATOR))

    def delete_segment(self):
        logger.info('Click REMOVE_SEGMENT_LOCATOR')
        self._click(*self.locators.REMOVE_SEGMENT_LOCATOR)
        logger.info('Accept deleting')
        self._click(*self.locators.ACCEPT_REMOVE_LOCATOR)
