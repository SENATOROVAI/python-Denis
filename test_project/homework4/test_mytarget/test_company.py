from homework4.PageObject.CompanyPage import CompanyPage
from homework4.suite.base import BaseSuiteTest

pytest_plugins = ["homework4.fixture.login"]


class TestCompany(BaseSuiteTest):

    def test_create_company_with_traffic(self, login_target, upload_file_path):
        page = self.get_page(CompanyPage)
        page.create_company_with_traffic(upload_file_path)
        created_company = page.created_company_text()
        assert created_company == CompanyPage.company_name
