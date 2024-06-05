from uuid import UUID

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import BookModel, AuthorModel
from .schemas import BookCreate, BookUpdate, AuthorCreate, AuthorUpdate


async def get_authors(db: AsyncSession, skip: int = 0, limit: int = 30):
    result = await db.execute(select(AuthorModel).offset(skip).limit(limit))
    return result.scalars().all()


async def get_author(db: AsyncSession, author_id: UUID):
    result = await db.execute(select(AuthorModel).filter(AuthorModel.id == author_id))
    return result.scalars().first()


async def create_author(db: AsyncSession, author: AuthorCreate):
    db_author = AuthorModel(
        name=author.name,
        biography=author.biography,
        birthdate=author.birthdate
    )
    db.add(db_author)
    await db.commit()
    await db.refresh(db_author)
    return db_author


async def update_author(db: AsyncSession, author_id: UUID, author: AuthorUpdate):
    db_author = get_author(db, author_id)
    if not db_author:
        return None

    update_data = author.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_author, key, value)

    await db.commit()
    await db.refresh(db_author)
    return db_author


async def delete_author(db: AsyncSession, author_id: UUID):
    db_author = get_author(db, author_id)
    if not db_author:
        return None
    await db.delete(db_author)
    await db.commit()
    return {"message": f"Author with ID {author_id} deleted successfully."}


async def get_books(db: AsyncSession, skip: int = 0, limit: int = 50):
    result = await db.execute(select(BookModel).offset(skip).limit(limit))
    return result.scalars().all()


async def get_book(db: AsyncSession, book_id: UUID):
    result = await db.execute(select(BookModel).filter(BookModel.id == book_id))
    return result.scalars().first()


async def create_book(db: AsyncSession, book: BookCreate):
    db_book = BookModel(
        title=book.title,
        summary=book.summary,
        published_date=book.published_date,
        author_id=book.author_id
    )
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


async def update_book(db: AsyncSession, book_id: UUID, book: BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    await db.commit()
    await db.refresh(db_book)
    return db_book


async def delete_book(db: AsyncSession, book_id: UUID):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    await db.delete(db_book)
    await db.commit()
    return {"message": f"Book with ID {book_id} deleted successfully."}
