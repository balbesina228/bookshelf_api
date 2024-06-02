from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_authors(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name, biography=author.biography, birthdate=author.birthdate)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
