from sqlalchemy import Column, Integer, String
from config.bookConfig import Base


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
