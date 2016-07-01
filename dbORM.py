from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import spiderConfig
Base = declarative_base()


class Users(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    team = Column(String)


class Posts(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    authorId = Column(Integer)
    date = Column(String)
    status = Column(String)
    tmstmp = Column(Integer)

engine = create_engine(spiderConfig.DBCONNECTOR)

DBSession = sessionmaker(bind=engine)
session = DBSession()
