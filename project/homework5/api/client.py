import json
import logging
from json import JSONDecodeError
from urllib.parse import urljoin
import allure
import requests


logger = logging.getLogger('test')


class AuthFailureException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    my_target = "https://target.my.com/"

    @staticmethod
    def _logging_pre(url, headers, data, files):
        text = f'Performing request:\n' \
               f'URL: {url}\n' \
               f'HEADERS: {headers}\n' \
               f'DATA: {data}\n\n' \
               f'FILES: {files}\n\n' \

        allure.attach(text, 'request', attachment_type=allure.attachment_type.TEXT)
        logger.info(text)

    @staticmethod
    def _logging_post(response):
        try:
            data = json.dumps(response.json(), indent=4)
        except JSONDecodeError:
            data = response.text

        text = 'Got response:\n' \
               f'RESPONSE STATUS: {response.status_code}\n' \
               f'RESPONSE CONTENT: {data}\n\n'

        allure.attach(text, 'response', attachment_type=allure.attachment_type.TEXT)
        logger.info(text)

    def _request_csrf(self, method, url, params=None, headers=None, data=None, json_data=None, files=None):
        csrftoken = self.get_csrftoken()
        logger.info('-' * 100 + '\n')
        self._logging_pre(url, headers, data or json_data, files)
        response = self.session.request(method, url, headers=csrftoken, params=params, data=data, json=json_data,
                                        files=files)
        self._logging_post(response)
        return response

    def _request(self, method, url, params=None, data=None, headers=None, json_data=None, files=None,
                 allow_redirects=None, cookies=None):
        logger.info('-' * 100 + '\n')
        self._logging_pre(url, headers, data or json_data, files)
        response = self.session.request(method, url, headers=headers, params=params, data=data, json=json_data,
                                        files=files, cookies=cookies, allow_redirects=allow_redirects)
        self._logging_post(response)
        return response

    @allure.step
    def get_user_auth(self, email, password):
        url = urljoin("https://auth-ac.my.com/", "auth")
        data = {"email": email, "password": password,
                "continue": urljoin(self.my_target, "/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email")}
        response = self._request("POST", url, data, headers={"Referer": self.my_target}, allow_redirects=False)
        cookies_login = response.cookies
        h_1 = response.headers
        response_1 = self._request("GET", url=f"{h_1['location']}", cookies=cookies_login, allow_redirects=False)
        h_2 = response_1.headers
        response_2 = self._request("GET", url=f"{h_2['Location']}", cookies=cookies_login, allow_redirects=False)
        h_3 = response_2.headers
        response_3 = self._request("GET", url=f"{h_3['Location']}", cookies=cookies_login, allow_redirects=False)
        b_4 = response_3.headers
        response_4 = self._request("GET", url=f"{b_4['Location']}", cookies=cookies_login, allow_redirects=False)
        cookies_auth = {"sdc": f"{response_4.cookies.get('sdc')}", "mc": f"{response_2.cookies.get('mc')}"}
        get_csrftoken = self._request("GET", url=urljoin(self.my_target, "csrf/"), cookies=cookies_auth)
        cookies_auth["csrftoken"] = get_csrftoken.cookies.get("csrftoken")
        if response_4.status_code != 302:
            raise AuthFailureException(f"Authorization failed with [{response_4.status_code}]: {response_4.text}")
        return cookies_auth

    @allure.step
    def get_csrftoken(self):
        csrftoken = {}
        get_csrftoken = self._request("GET", url=urljoin(self.my_target, "csrf/"))
        csrftoken["X-CSRFToken"] = get_csrftoken.cookies.get("csrftoken")
        if get_csrftoken.status_code != 200:
            raise AuthFailureException(f"Get csrftoken failed with [{get_csrftoken.status_code}]: {get_csrftoken.text}")
        return csrftoken

    @allure.step
    def post_upload_static_picture(self, upload_file_path):
        file = {}
        content_type = 'image/jpeg'
        file['file'] = (upload_file_path, open(upload_file_path, 'rb'), content_type)
        static = self._request_csrf("POST", url=urljoin(self.my_target, "api/v2/content/static.json"), files=file)
        return {"content": {"id": static.json()["id"]}, "description": "240x400.jpg"}

    @allure.step
    def post_upload_picture_for_company(self, data_mediateka):
        mediateka = self._request_csrf("POST", url=urljoin(self.my_target, "api/v2/mediateka.json"),
                                       json_data=data_mediateka)
        if mediateka.status_code != 201:
            raise AuthFailureException(f"Upload picture failed with [{mediateka.status_code}]: {mediateka.text}")
        return mediateka.json()

    @allure.step
    def post_create_company(self, json_data):
        response = self._request_csrf("POST", url=urljoin(self.my_target, "api/v2/campaigns.json"), json_data=json_data)
        if response.status_code != 200:
            raise AuthFailureException(f"Create company failed with [{response.status_code}]: {response.text}")
        return response.json()

    @allure.step
    def get_companies_count(self):
        response = self._request("GET", url=urljoin(self.my_target, "api/v2/campaigns_count.json"))
        if response.status_code != 200:
            raise AuthFailureException(f"Get company failed with [{response.status_code}]: {response.text}")
        return response.json()

    @allure.step
    def post_delete_company(self, json_data):
        response = self._request_csrf("POST", url=urljoin(self.my_target, "/api/v2/campaigns/mass_action.json"),
                                      json_data=json_data)
        if response.status_code != 204:
            raise AuthFailureException(f"Delete company failed with [{response.status_code}]: {response.text}")
        return response

    @allure.step
    def post_create_segment(self, json_data):
        response = self._request_csrf("POST", url=urljoin(self.my_target, "/api/v2/remarketing/segments.json"),
                                      json_data=json_data)
        if response.status_code != 200:
            raise AuthFailureException(f"Create segment failed with [{response.status_code}]: {response.text}")
        return response.json()

    @allure.step
    def get_segments_list(self):
        response = self._request("GET", url=urljoin(self.my_target, "/api/v2/remarketing/segments.json"))
        if response.status_code != 200:
            raise AuthFailureException(f"Get segment failed with [{response.status_code}]: {response.text}")
        return response.json()

    @allure.step
    def post_delete_segment(self, json_data):
        response = self._request_csrf("POST", url=urljoin(self.my_target, "/api/v1/remarketing/mass_action/delete.json"),
                                      json_data=json_data)
        if response.status_code != 200:
            raise AuthFailureException(f"Delete segment failed with [{response.status_code}]: {response.text}")
        return response.json()
