import pytest
from homework5.api.client import ApiClient


@pytest.fixture(scope="session")
def get_user_auth(user, api_client):
    return api_client.get_user_auth


@pytest.fixture(scope="session")
def csrftoken(user, api_client, get_user_auth):
    return api_client.get_csrftoken()


@pytest.fixture(scope="function")
def upload_picture_for_company(api_client, get_user_auth, csrftoken, upload_file_path):
    return api_client.post_upload_picture_for_company


@pytest.fixture(scope="session")
def api_client(base_url, user):
    api_client = ApiClient(base_url)
    api_client.get_user_auth(email=user.EMAIL, password=user.PASSWORD)
    return api_client


@pytest.fixture(scope="session")
def cookies(user, api_client):
    return api_client.session.cookies
