from homework5.api.data.segment import body_for_creation, body_for_delete
from homework5.api.suite.base import BaseApiSuiteTest
from homework5.api.fixtures import *


class TestCompany(BaseApiSuiteTest):

    @pytest.mark.API
    def test_create_segment(self, api_client):
        segments_before_creation = api_client.get_segments_list()
        api_client.post_create_segment(json_data=body_for_creation)
        segments_after_creation = api_client.get_segments_list()
        assert segments_after_creation["count"] == segments_before_creation["count"] + 1, "Сегмент не создан"

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        count_segment_before_delete = api_client.get_segments_list()
        if count_segment_before_delete["count"] == 0:
            api_client.post_create_segment(json_data=body_for_creation)
            count_segment_before_delete = api_client.get_segments_list()
        body_for_delete[0]["source_id"] = count_segment_before_delete["items"][0]["id"]
        api_client.post_delete_segment(json_data=body_for_delete)
        count_segment_after_delete = api_client.get_segments_list()
        assert count_segment_after_delete["count"] == count_segment_before_delete["count"] - 1, "Сегмент не удален"

