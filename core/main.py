from typing import List

from fastapi import FastAPI, HTTPException
import validators

from ddtrace import patch_all
from datadog import statsd
from sqlalchemy import select

from .db import session
from . import models
from . import pd_schemas

# patch_all()
app = FastAPI()


@app.get('/')
async def root():
    # statsd.increment('incomer', tags=['incomer:first'])
    return {'Hello': 'World'}


@app.get('/ulrs', response_model=List[pd_schemas.URL_INFO_SCHEMA])
async def get_urls():
    with session:
        urls = session.execute(select(models.URL)).all()
    return urls


@app.post('/short_code', response_model=pd_schemas.URL_INFO_SCHEMA)
async def short_code(income_url: pd_schemas.URL_IN_SCHEMA):
    if not validators.url(income_url.long_url):
        raise HTTPException(status_code=404, detail='Incorrect long_url')
    with session as s:
        url = models.URL(long_url=income_url.long_url)
        s.add(url)
        s.commit()
    return url



