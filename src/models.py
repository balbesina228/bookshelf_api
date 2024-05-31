import uuid

from sqlalchemy import Column, DateTime, UUID, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    birthdate = Column(DateTime)
    biography = Column(String)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"))
    published_date = Column(DateTime)
    summary = Column(String)
