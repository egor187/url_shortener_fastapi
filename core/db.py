from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from . import pd_schemas, models
from .settings import get_settings


settings = get_settings()

engine = create_engine(settings.SQL_ALCHEMY_URL)
session = Session(engine)
models.Base.metadata.create_all(engine)


def write_long_url_to_db(income_url: pd_schemas.URL_IN_SCHEMA):
    with session:
        url = models.URL(long_url=income_url.long_url)
        session.add(url)
        session.commit()
        session.refresh(url)
    return url
