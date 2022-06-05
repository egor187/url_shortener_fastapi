from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .settings import get_settings


settings = get_settings()

engine = create_engine(settings.SQL_ALCHEMY_URL)
session = Session(engine)
