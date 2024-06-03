from uuid import UUID

from sqlalchemy.orm import Session

from .models import BookModel, AuthorModel
from .schemas import BookCreate, BookUpdate, AuthorCreate, AuthorUpdate


def get_authors(db: Session, skip: int = 0, limit: int = 30):
    return db.query(AuthorModel).offset(skip).limit(limit).all()


def get_author(db: Session, author_id: UUID):
    return db.query(AuthorModel).filter(AuthorModel.id == author_id).first()


def create_author(db: Session, author: AuthorCreate):
    db_author = AuthorModel(
        name=author.name,
        biography=author.biography,
        birthdate=author.birthdate
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author_id: UUID, author: AuthorUpdate):
    db_author = get_author(db, author_id)
    if not db_author:
        return None

    update_data = author.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_author, key, value)

    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: UUID):
    db_author = get_author(db, author_id)
    if not db_author:
        return None
    db.delete(db_author)
    db.commit()
    return {"message": f"Author with ID {author_id} deleted successfully."}


def get_books(db: Session, skip: int = 0, limit: int = 50):
    return db.query(BookModel).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: UUID):
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def create_book(db: Session, book: BookCreate):
    db_book = BookModel(
        title=book.title,
        summary=book.summary,
        published_date=book.published_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: UUID, book: BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: UUID):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return {"message": f"Book with ID {book_id} deleted successfully."}
