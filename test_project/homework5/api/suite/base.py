from homework5.conftest import *
from homework5.api.fixtures import *
from homework5.api.client import ApiClient


class BaseApiSuiteTest:

    base_url: str
    logger: logging.Logger
    api_client: ApiClient

    @pytest.fixture(autouse=True)
    def prepare(self, logger, api_client):
        self.logger: logging.Logger = logger
        self.api_client: ApiClient = api_client
        self.logger.info('PREPARE DONE')
