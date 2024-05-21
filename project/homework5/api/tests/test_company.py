from homework5.api.data.company import body
from homework5.api.suite.base import BaseApiSuiteTest
from homework5.api.fixtures import *

# json.dumps(response.json(), indent=4) отладка


class TestCompany(BaseApiSuiteTest):

    @pytest.mark.API
    def test_create_company(self, api_client, upload_file_path):
        companies_before_creation = api_client.get_companies_count()
        data_mediateka = api_client.post_upload_static_picture(upload_file_path)
        api_client.post_upload_picture_for_company(data_mediateka)
        body["banners"][0]["content"]["image_240x400"]["id"] = data_mediateka["content"]["id"]
        created_company = api_client.post_create_company(json_data=body)
        companies_after_creation = api_client.get_companies_count()
        assert companies_after_creation["active"] == companies_before_creation["active"] + 1, "Компания не создана"
        api_client.post_delete_company(json_data=[{"id": created_company["id"], "status": "deleted"}])
