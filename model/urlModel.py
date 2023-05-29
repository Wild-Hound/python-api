from sqlalchemy import Column, Integer, String, Date
from config.url_shortenerConfig import Base


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    main_url = Column(String, unique=True)
    redirect_url = Column(String, unique=True)
    views = Column(Integer)
    edits = Column(Integer)
    created = Column(Date)
