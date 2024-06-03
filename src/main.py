from uuid import UUID

import sqlalchemy.exc
from fastapi import FastAPI, Depends, HTTPException, Response
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


@app.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: UUID, author: schemas.AuthorUpdate, db: Session = Depends(get_db)):
    db_author = crud.update_author(db, author_id=author_id, author=author)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@app.delete("/authors/{author_id}")
def delete_author(author_id: UUID, db: Session = Depends(get_db)):
    author = crud.delete_author(db, author_id)
    if author is None:
        return HTTPException(status_code=400, detail="Author with the specified ID not found")
    return Response(status_code=204)


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


@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: UUID, author_id: UUID, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book with the specified ID not found")
    return db_book


@app.delete("/books/{book_id}")
def delete_book(book_id: UUID, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if book is None:
        return HTTPException(status_code=400, detail="Book with the specified ID not found")
    return Response(status_code=204)
