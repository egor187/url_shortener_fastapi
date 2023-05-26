from typing import List

from fastapi import FastAPI, HTTPException, responses, Query, Depends
import validators
from sqlalchemy.orm import Session

from core.db import write_long_url_to_db, get_urls_from_db, get_long_url_from_db, get_session
from core import pd_schemas
from core.settings import get_settings

app = FastAPI()
settings = get_settings()


@app.get('/')
async def root():
    return {'Hello': 'World'}


@app.get('/urls', response_model=List[pd_schemas.URL_INFO_SCHEMA])
async def get_urls(session: Session = Depends(get_session)):
    return get_urls_from_db(session)


@app.post('/short_code', response_model=pd_schemas.URL_INFO_SCHEMA)
async def short_code(income_url: pd_schemas.URL_IN_SCHEMA, session: Session = Depends(get_session)):
    if not validators.url(income_url.long_url):
        raise HTTPException(status_code=404, detail='Incorrect long_url')
    url = write_long_url_to_db(income_url=income_url, session=session)
    return url


@app.get('/forward/')
async def forward(
        short_code: str = Query(
            min_length=settings.DEFAULT_SHORT_CODE_LENGTH,
            max_length=settings.DEFAULT_SHORT_CODE_LENGTH
        ),
        redirect: bool = Query(default=False),
        session: Session = Depends(get_session)):
    long_url = get_long_url_from_db(short_code, session)
    if redirect:
        return responses.RedirectResponse(long_url)
    return responses.JSONResponse(long_url)
