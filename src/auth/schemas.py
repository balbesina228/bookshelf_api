from pydantic import BaseModel
from uuid import UUID


class CookieBase(BaseModel):
    pass


class Cookie(CookieBase):
    id: UUID

    class Config:
        orm_mode = True


class CookieCreate(CookieBase):
    username: str
