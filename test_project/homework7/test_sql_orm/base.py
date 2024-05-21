import pytest
from homework7.models.model import Readlines, RequestsType, FrequentRequests, HeaviestRequests, \
    TopFiveRequestsUsersWith5xx
from homework7.mysql_orm.client import MysqlORMClient
from homework7.utils.builder_orm import MysqlORMBuilder


class Prepare:

    def prepare(self, upload_file_path):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client, upload_file_path):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        self.prepare(upload_file_path)


    def get_readlines(self):
        self.mysql.session.commit()
        readlines_id = self.mysql.session.query(Readlines)

        return readlines_id.all()

    def get_request(self):
        self.mysql.session.commit()
        request_id = self.mysql.session.query(RequestsType)

        return request_id.all()

    def get_frequent_request(self):
        self.mysql.session.commit()
        frequent_request_id = self.mysql.session.query(FrequentRequests)

        return frequent_request_id.all()

    def get_heaviest_request(self):
        self.mysql.session.commit()
        frequent_request_id = self.mysql.session.query(HeaviestRequests)

        return frequent_request_id.all()

    def get_top_five_requests_users_with_5xx(self):
        self.mysql.session.commit()
        top_five_requests_users_with_5xx_id = self.mysql.session.query(TopFiveRequestsUsersWith5xx)

        return top_five_requests_users_with_5xx_id.all()

