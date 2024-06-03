from uuid import UUID

from fastapi import Depends, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from ..schemas.author import Author, AuthorCreate, AuthorUpdate

router = APIRouter()


@router.get("/", response_model=list[Author])
def read_authors(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return authors


@router.get("/{author_id}", response_model=Author)
def read_author(author_id: UUID, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/", response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = crud.create_author(db, author)
    return new_author


@router.put("/{author_id}", response_model=Author)
def update_author(author_id: UUID, author: AuthorUpdate, db: Session = Depends(get_db)):
    db_author = update_author(db, author_id=author_id, author=author)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.delete("/{author_id}")
def delete_author(author_id: UUID, db: Session = Depends(get_db)):
    author = crud.delete_author(db, author_id)
    if author is None:
        return HTTPException(status_code=400, detail="Author with the specified ID not found")
    return Response(status_code=204)
