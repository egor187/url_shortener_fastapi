from sqlalchemy import create_engine, select
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


def get_urls_from_db():
    return session.scalars(select(models.URL)).all()


def get_long_url_from_db(short_code):
    with session:
        long_url = session.scalars(select(models.URL.long_url).filter_by(code=short_code)).first()
        if not long_url:
            return settings.DEFAULT_REDIRECT_URL
        return long_url
