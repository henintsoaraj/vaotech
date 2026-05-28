from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id         = Column(Integer, primary_key=True)
    title      = Column(String)
    url        = Column(String)
    source     = Column(String)
    score      = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)