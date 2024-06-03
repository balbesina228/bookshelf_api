import datetime
from uuid import UUID

from pydantic import BaseModel

from .book import Book


class AuthorBase(BaseModel):
    name: str
    biography: str
    birthdate: datetime.date


class Author(AuthorBase):
    id: UUID
    books: list[Book] = []

    class Config:
        orm_mode = True


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass
