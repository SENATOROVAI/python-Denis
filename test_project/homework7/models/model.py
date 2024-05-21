from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Readlines(Base):

    __tablename__ = 'readlines'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Readlines(" \
               f"id='{self.id}'," \
               f"number_of_lines='{self.number_of_lines}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_lines = Column(String(30), nullable=False)


class RequestsType(Base):

    __tablename__ = 'request_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<RequestsType(" \
               f"id='{self.id}'," \
               f"number_of_method='{self.number_of_method}', " \
               f"method='{self.method}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_method = Column(String(300), nullable=False)
    method = Column(String(300), nullable=False)


class FrequentRequests(Base):

    __tablename__ = 'frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<FrequentRequests(" \
               f"id='{self.id}'," \
               f"requests_url='{self.requests_url}', " \
               f"requests_number='{self.requests_number}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requests_url = Column(String(300), nullable=False)
    requests_number = Column(String(300), nullable=False)


class HeaviestRequests(Base):

    __tablename__ = 'heaviest_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<HeaviestRequests(" \
               f"id='{self.id}'," \
               f"requests_url='{self.requests_url}', " \
               f"status_code='{self.status_code}', " \
               f"requests_size='{self.requests_size}', " \
               f"ip='{self.ip}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requests_url = Column(String(300), nullable=False)
    status_code = Column(String(300), nullable=False)
    requests_size = Column(String(300), nullable=False)
    ip = Column(String(300), nullable=False)


class TopFiveRequestsUsersWith5xx(Base):

    __tablename__ = 'top_five_requests_users_with_5xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<FrequentRequests(" \
               f"id='{self.id}'," \
               f"requests_number='{self.requests_number}', " \
               f"ip='{self.ip}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requests_number = Column(String(300), nullable=False)
    ip = Column(String(300), nullable=False)
