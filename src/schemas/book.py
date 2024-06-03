import datetime
from uuid import UUID

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    summary: str
    published_date: datetime.date


class Book(BookBase):
    id: UUID
    author_id: UUID

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    author_id: UUID


class BookUpdate(BookBase):
    pass
