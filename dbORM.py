from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

engine = create_engine(
    'mysql+mysqlconnector://root:password@localhost:3306/internBlog')

DBSession = sessionmaker(bind=engine)
session = DBSession()
