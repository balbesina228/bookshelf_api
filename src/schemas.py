import datetime
from uuid import UUID

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str


class Book(BookBase):
    id: UUID
    author_id: UUID

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    pass


class AuthorBase(BaseModel):
    name: str
    biography: str
    birthdate: datetime.datetime


class Author(AuthorBase):
    id: UUID
    books: list[Book] = []

    class Config:
        orm_mode = True


class AuthorCreate(AuthorBase):
    pass
