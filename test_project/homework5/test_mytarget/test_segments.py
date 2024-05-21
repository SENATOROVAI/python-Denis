import time
from homework5.PageObject.SegmentPage import SegmentPage
from homework5.api.data.segment import body_for_creation
from homework5.suite.base import BaseUiSuiteTest

pytest_plugins = ["homework5.fixture.login"]


class TestMyTarget(BaseUiSuiteTest):

    def test_create_new_segment(self):
        page = self.get_page(SegmentPage)
        page.click_header_audience()
        segments_count_before = page.count_segments()
        page.create_new_segment()
        created_segment = page.created_segment_text()
        segments_count_after = page.count_segments()
        assert created_segment == SegmentPage.segment_name, "Сегмент не создан!"
        assert segments_count_before + 1 == segments_count_after, "Сегмент не создан!"

    def test_delete_segment(self, api_client):
        api_client.post_create_segment(json_data=body_for_creation)
        page = self.get_page(SegmentPage)
        page.click_header_audience()
        segments_count_before = page.count_segments()
        page.delete_segment()
        time.sleep(3)
        segments_count_after = page.count_segments()
        assert segments_count_before - 1 == segments_count_after, "Сегмент не удален!"


