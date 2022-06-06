from typing import List

from fastapi import FastAPI, HTTPException, responses, Query
import validators

from .db import write_long_url_to_db, get_urls_from_db, get_long_url_from_db
from . import pd_schemas
from .settings import get_settings

app = FastAPI()
settings = get_settings()

@app.get('/')
async def root():
    return {'Hello': 'World'}


@app.get('/urls', response_model=List[pd_schemas.URL_INFO_SCHEMA])
async def get_urls():
    return get_urls_from_db()


@app.post('/short_code', response_model=pd_schemas.URL_INFO_SCHEMA)
async def short_code(income_url: pd_schemas.URL_IN_SCHEMA):
    if not validators.url(income_url.long_url):
        raise HTTPException(status_code=404, detail='Incorrect long_url')
    url = write_long_url_to_db(income_url=income_url)
    return url


@app.get('/forward/')
async def forward(
        short_code: str = Query(
            min_length=settings.DEFAULT_SHORT_CODE_LENGTH,
            max_length=settings.DEFAULT_SHORT_CODE_LENGTH
        ),
        redirect: bool = Query(default=False)):
    long_url = get_long_url_from_db(short_code)
    if redirect:
        return responses.RedirectResponse(long_url)
    return responses.JSONResponse(long_url)
