from sqlalchemy import Column, Integer, String, DateTime, Boolean
from config.url_shortenerConfig import Base


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    main_url = Column(String, unique=True)
    redirect_url = Column(String, unique=True)
    https = Column(Boolean, default=True)
    views = Column(Integer)
    edits = Column(Integer)
    created = Column(DateTime)
