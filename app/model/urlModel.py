from sqlalchemy import Column, Integer, String, Date
from config.slowConfig import Base


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    main_url = Column(String)
    redirect_url = Column(String)
    views = Column(Integer)
    edits = Column(Integer)
    created = Column(Date)
