import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from homework7.models.model import Base


class MysqlORMClient:

    def __init__(self, user, password, db_name, host='localhost', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        sm = sessionmaker(bind=self.connection.engine)
        self.session = sm()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_readlines(self):
        if not inspect(self.engine).has_table('readlines'):
            Base.metadata.tables['readlines'].create(self.engine)

    def create_requests_type(self):
        if not inspect(self.engine).has_table('requests_type'):
            Base.metadata.tables['request_type'].create(self.engine)

    def create_frequent_requests(self):
        if not inspect(self.engine).has_table('frequent_requests'):
            Base.metadata.tables['frequent_requests'].create(self.engine)

    def create_heaviest_requests(self):
        if not inspect(self.engine).has_table('heaviest_requests'):
            Base.metadata.tables['heaviest_requests'].create(self.engine)

    def create_top_five_requests_users_with_5xx(self):
        if not inspect(self.engine).has_table('top_five_requests_users_with_5xx'):
            Base.metadata.tables['top_five_requests_users_with_5xx'].create(self.engine)
