from fastapi import FastAPI, Depends
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


@app.get("/authors")
def read_authors(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return authors


@app.post("/authors")
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)
