from fastapi import Response, Depends, Cookie, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import crud
from src.auth.database import get_async_session, get_session_data
from src.auth.schemas import CookieCreate

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login-cookie/")
async def auth_login_set_cookie(
        response: Response,
        cookie: CookieCreate,
        db: AsyncSession = Depends(get_async_session)
):
    session = await crud.generate_cookie(db, cookie)
    response.set_cookie(session.username, session.id)

    return session


@router.get("/check-cookie/")
async def auth_check_cookie(
        cookie_id: str,
        user_session_data: dict = Depends(get_session_data),
        db: AsyncSession = Depends(get_async_session)
):
    cookie = await crud.read_cookie(db, cookie_id)
    if cookie is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return cookie


@router.delete("/logout-cookie/")
async def auth_logout_cookie(
        response: Response,
        cookie_id: str,
        user_session_data: dict = Depends(get_session_data),
        db: AsyncSession = Depends(get_async_session)
):
    cookie = await crud.delete_cookie(db, cookie_id)
    if cookie is None:
        return HTTPException(status_code=401, detail="Not authenticated")

    return Response(status_code=204)
