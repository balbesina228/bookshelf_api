import uuid

from sqlalchemy import Column, UUID, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .models import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"))
    published_date = Column(Date)
    summary = Column(String)

    author = relationship("Author", back_populates="books")
