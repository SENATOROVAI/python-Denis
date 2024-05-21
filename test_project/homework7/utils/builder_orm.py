from faker import Faker

from homework7.models.model import Readlines, RequestsType, FrequentRequests, HeaviestRequests, \
    TopFiveRequestsUsersWith5xx

fake = Faker()


class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client

    def create_readlines(self, number_of_lines=None):
        if number_of_lines is None:
            number_of_lines = fake.name()

        readlines = Readlines(
            number_of_lines=number_of_lines
        )

        self.client.session.add(readlines)
        self.client.session.commit()
        return readlines

    def create_requests_type(self, number_of_method=None, method=None):
        if number_of_method is None:
            number_of_method = fake.first_name()
        if method is None:
            method = "kek"
        requests_type = RequestsType(
            number_of_method=number_of_method,
            method=method
        )

        self.client.session.add(requests_type)
        self.client.session.commit()
        return requests_type

    def create_frequent_requests(self, requests_url=None, requests_number=None):
        if requests_url is None:
            requests_url = fake.first_name()
        if requests_number is None:
            requests_number = "kek"
        frequent_requests = FrequentRequests(
            requests_url=requests_url,
            requests_number=requests_number
        )

        self.client.session.add(frequent_requests)
        self.client.session.commit()
        return FrequentRequests

    def create_heaviest_requests(self, requests_url=None, status_code=None, requests_size=None, ip=None):
        if requests_url is None:
            requests_url = fake.first_name()
        if status_code is None:
            status_code = "kek"
        if requests_size is None:
            requests_size = "lol"
        if ip is None:
            ip = "zaza"

        heaviest_requests = HeaviestRequests(
            requests_url=requests_url,
            status_code=status_code,
            requests_size=requests_size,
            ip=ip
        )

        self.client.session.add(heaviest_requests)
        self.client.session.commit()
        return HeaviestRequests

    def create_top_five_requests_users_with_5xx(self, ip=None, requests_number=None):
        if ip is None:
            ip = fake.first_name()
        if requests_number is None:
            requests_number = "kek"
        top_five_requests_users_with_5xx = TopFiveRequestsUsersWith5xx(
            ip=ip,
            requests_number=requests_number
        )

        self.client.session.add(top_five_requests_users_with_5xx)
        self.client.session.commit()
        return top_five_requests_users_with_5xx
