import os
import pytest

from mysql_orm.client import MysqlORMClient


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture()
def upload_file_path(repo_root):
    return os.path.join(repo_root, "files/access.log")


def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='admin', password='admin', db_name='test_python')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()

    mysql_orm_client.connect(db_created=True)

    if not hasattr(config, 'workerinput'):
        mysql_orm_client.create_readlines()
        mysql_orm_client.create_requests_type()
        mysql_orm_client.create_frequent_requests()
        mysql_orm_client.create_heaviest_requests()
        mysql_orm_client.create_top_five_requests_users_with_5xx()

    config.mysql_orm_client = mysql_orm_client


@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()

