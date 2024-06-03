from fastapi import FastAPI

from .routers import book_router, author_router
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(author_router, prefix="/authors", tags=["Authors"])
