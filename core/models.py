from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from .helpers import get_short_code

Base = declarative_base()


class URL(Base):
    __tablename__ = 'URL'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.utcnow(), nullable=False)
    long_url = Column(String, nullable=False)
    code = Column(String, default=get_short_code, nullable=False)

    def __repr__(self):
        return f'URL instance: {self.created}: {self.long_url}: {self.code}'



