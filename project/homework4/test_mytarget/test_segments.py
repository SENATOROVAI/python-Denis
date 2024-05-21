import time

from homework4.PageObject.SegmentPage import SegmentPage
from homework4.suite.base import BaseSuiteTest

pytest_plugins = ["homework4.fixture.login"]


class TestMyTarget(BaseSuiteTest):

    def test_create_new_segment(self, login_target):
        page = self.get_page(SegmentPage)
        page.click_header_audience()
        segments_count_before = page.count_segments()
        page.create_new_segment()
        created_segment = page.created_segment_text()
        segments_count_after = page.count_segments()
        assert created_segment == SegmentPage.segment_name
        assert segments_count_before + 1 == segments_count_after

    def test_delete_segment(self, login_target):
        page = self.get_page(SegmentPage)
        page.click_header_audience()
        segments_count_before = page.count_segments()
        page.delete_segment()
        time.sleep(3)
        segments_count_after = page.count_segments()
        if segments_count_before == 0:
            segments_count_before += 1
        assert segments_count_before - 1 == segments_count_after


