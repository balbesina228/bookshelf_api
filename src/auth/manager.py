from typing import Optional, Annotated
from uuid import UUID

from fastapi import Depends, Request, Form
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import BaseUserManager, UUIDIDMixin, models, exceptions
from pydantic import EmailStr

from config import SECRET_KEY
from .database import User, get_user_db


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.username} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
