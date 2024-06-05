from fastapi import FastAPI

from .auth.auth import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
from .routers import book_router, author_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(author_router, prefix="/authors", tags=["Authors"])

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)
