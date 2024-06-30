import uuid
from typing import Any
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import Cookie
from src.auth.schemas import CookieCreate


async def generate_cookie(db: AsyncSession, cookie: CookieCreate):
    cookie_value = str(uuid.uuid4())
    db_cookie = Cookie(
        id=cookie_value,
        username=cookie.username
    )
    db.add(db_cookie)
    await db.commit()
    await db.refresh(db_cookie)
    return db_cookie


async def read_cookie(db: AsyncSession, cookie: str):
    result = await db.execute(select(Cookie).filter(Cookie.id == cookie))
    return result.scalars().first()


async def delete_cookie(db: AsyncSession, cookie: str):
    db_cookie = await read_cookie(db, cookie)
    if not db_cookie:
        return None
    await db.delete(db_cookie)
    await db.commit()
    return {"message": f"Cookie {cookie} deleted successfully."}