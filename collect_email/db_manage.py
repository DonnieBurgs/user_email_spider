from sqlalchemy import Column, Integer, String, create_engine, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:''@localhost:3306/Scrapy?charset=utf8', echo=False)


class UserEmails(Base):
    __tablename__ = 'user_email_keyword'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    index = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    asin = Column(String(20), nullable=False)
    stars = Column(Float, nullable=False)
    product_at_page = Column(Integer, nullable=False)
    product_index = Column(String(20), nullable=False)
    keyword = Column(String(100), nullable=False)

class AsinKeyword(Base):
    __tablename__ = 'asin_keyword'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    index = Column(Integer, nullable=False, primary_key=True)
    asin = Column(String(20), nullable=False)
    keyword = Column(String(100), nullable=False)

class AsinOfError(Base):
    __tablename__ = 'asin_of_error'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    asin_keyword = Column(String(100), nullable=False, primary_key=True)
    redo = Column(Boolean, nullable=False)