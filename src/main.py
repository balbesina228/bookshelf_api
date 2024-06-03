from uuid import UUID

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
    return crud.create_author(db, author)
