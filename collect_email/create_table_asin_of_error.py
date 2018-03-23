# coding= utf-8

from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.engine.url import URL
import logging

DB_SETTING = {
    'drivername': 'mysql+mysqlconnector',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'Scrapy',
    'username': 'root',
    'password': '',
    'query': {
        'charset': 'utf8'
    }
}

Base = declarative_base()

class UserEmails(Base):
    __tablename__ = 'asin_of_error'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    # id = Column(Integer, nullable = False, primary_key = True)
    # asin = Column(String(20), nullable=False)
    # keyword = Column(String(100), nullable=False)
    # redo = Column(Boolean, nullable=False)

    asin_keyword = Column(String(100), nullable=False, primary_key=True)
    redo = Column(Boolean, nullable=False)


def db_connect():
    return create_engine(URL(**DB_SETTING), pool_size=10, pool_recycle=3600, max_overflow=20)

if __name__ == '__main__':
    logger = logging.getLogger('')
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    try:
        Base.metadata.create_all(db_connect())
    except Exception:
        logging.exception('Create Failed !')
    else:
        logging.info('Created !')