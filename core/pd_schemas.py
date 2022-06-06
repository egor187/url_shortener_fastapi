import datetime

from pydantic import BaseModel


class URL_INFO_SCHEMA(BaseModel):
    id: int
    created: datetime.datetime
    long_url: str
    code: str

    class Config:
        orm_mode = True


class URL_IN_SCHEMA(BaseModel):
    long_url: str = ...
