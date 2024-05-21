from homework5.PageObject.CompanyPage import CompanyPage
from homework5.suite.base import BaseUiSuiteTest

pytest_plugins = ["homework5.fixture.login"]


class TestCompany(BaseUiSuiteTest):

    def test_create_company_with_traffic(self, upload_file_path):
        page = self.get_page(CompanyPage)
        page.create_company_with_traffic(upload_file_path)
        created_company = page.created_company_text()
        assert created_company == CompanyPage.company_name, "Компания не создана"
