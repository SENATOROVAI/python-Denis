from homework7.test_sql_orm.base import Prepare
from collections import Counter
import operator


class TestRedlinesCount(Prepare):

    def prepare(self, upload_file_path):
        with open(upload_file_path) as fp:
            lines = 0
            for line in fp.readlines():
                line.split()
                lines += 1
        self.redlines = self.mysql_builder.create_readlines(number_of_lines=lines)

    def test_redlines_count(self):
        redlines = self.get_readlines()
        assert len(redlines) == 1


class TestRequests(Prepare):

    def prepare(self, upload_file_path):
        with open(upload_file_path) as fp:
            methods = []
            for line in fp.readlines():
                methods_list = line.split()
                methods.append(methods_list[5])
            methods = (Counter(methods))
            for key, value in methods.items():
                self.requests = self.mysql_builder.create_requests_type(number_of_method=value, method=key)

    def test_requests(self):
        requests = self.get_request()
        assert len(requests) == 5


class TestFrequentRequests(Prepare):

    def prepare(self, upload_file_path):
        with open(upload_file_path) as fp:
            from collections import Counter
            methods = []
            for line in fp.readlines():
                methods_list = line.split()
                methods.append(methods_list[6])

            methods_counter = Counter(methods)
            sorted_counter = sorted(methods_counter.items(), key=operator.itemgetter(1))
            sorted_dict = dict(sorted_counter[-10:])
            for key, value in sorted_dict.items():
                self.frequent_requests = self.mysql_builder.create_frequent_requests(requests_url=value,
                                                                                     requests_number=key)

    def test_frequent_requests(self):
        requests = self.get_frequent_request()
        assert len(requests) == 10


class TestHeaviestRequests(Prepare):

    def prepare(self, upload_file_path):
        with open(upload_file_path) as fp:
            methods = []
            for line in fp.readlines():
                methods_list = line.split()
                if methods_list[8].startswith("4"):
                    methods.append(methods_list)
            sorted_methods_list = sorted(methods, key=lambda x: int(x[9]))
            sorted_methods_list = sorted_methods_list[-5:]
            for value in sorted_methods_list:
                self.heaviest_requests = self.mysql_builder.create_heaviest_requests(requests_url=value[6],
                                                                                     status_code=value[8],
                                                                                     requests_size=value[9],
                                                                                     ip=value[0])

    def test_heaviest_requests(self):
        requests = self.get_heaviest_request()
        assert len(requests) == 5


class TestTopFiveRequestsUsersWith5xx(Prepare):

    def prepare(self, upload_file_path):
        with open(upload_file_path) as fp:
            methods = []
            for line in fp.readlines():
                methods_list = line.split()
                if methods_list[8].startswith("5"):
                    methods.append(methods_list[0])
            methods_counter = Counter(methods)
            sorted_counter = sorted(methods_counter.items(), key=operator.itemgetter(1))
            sorted_dict = dict(sorted_counter[-5:])
            for key, value in sorted_dict.items():
                self.requests = self.mysql_builder.create_top_five_requests_users_with_5xx(requests_number=value,
                                                                                           ip=key)

    def test_top_five_requests_users_with_5xx(self):
        requests = self.get_top_five_requests_users_with_5xx()
        assert len(requests) == 5
