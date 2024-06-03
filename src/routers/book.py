from uuid import UUID

import sqlalchemy.exc
from fastapi import Depends, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from ..schemas.book import Book, BookCreate, BookUpdate

router = APIRouter()


@router.get("/", response_model=list[Book])
def read_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books


@router.get("/{book_id}", response_model=Book)
def read_book(book_id: UUID, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    try:
        new_book = crud.create_book(db, book)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail="Author with the specified ID not found")
    return new_book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: UUID, author_id: UUID, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book with the specified ID not found")
    return db_book


@router.delete("/{book_id}")
def delete_book(book_id: UUID, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if book is None:
        return HTTPException(status_code=400, detail="Book with the specified ID not found")
    return Response(status_code=204)
