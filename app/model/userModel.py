from sqlalchemy import Column, Integer, String, Date
from config.slowConfig import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    age = Column(Integer)
    created = Column(Date)
