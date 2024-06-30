from fastapi import FastAPI

from src.auth.routers import router as auth_router
from src.routers import book_router, author_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(author_router, prefix="/authors", tags=["Authors"])

# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"]
# )

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"]
# )

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
