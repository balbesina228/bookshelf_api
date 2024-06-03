from uuid import UUID

import sqlalchemy.exc
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud
from . import schemas
from .database import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/authors", response_model=list[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return authors


@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: UUID, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.post("/authors", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    new_author = crud.create_author(db, author)
    return new_author


@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books


@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: UUID, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    try:
        new_book = crud.create_book(db, book)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail="Author with the specified ID not found")
    return new_book
