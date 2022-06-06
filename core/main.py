from typing import List

from fastapi import FastAPI, HTTPException
import validators

from sqlalchemy import select

from .db import session, write_long_url_to_db
from . import models
from . import pd_schemas

app = FastAPI()


@app.get('/')
async def root():
    return {'Hello': 'World'}


@app.get('/urls', response_model=List[pd_schemas.URL_INFO_SCHEMA])
async def get_urls():
    with session:
        urls = session.execute(select(models.URL)).all()
    return urls


@app.post('/short_code', response_model=pd_schemas.URL_INFO_SCHEMA)
async def short_code(income_url: pd_schemas.URL_IN_SCHEMA):
    if not validators.url(income_url.long_url):
        raise HTTPException(status_code=404, detail='Incorrect long_url')
    url = write_long_url_to_db(income_url=income_url)
    return url



