import uuid

from sqlalchemy import Column, UUID, String, Date
from sqlalchemy.orm import relationship

from ..database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    birthdate = Column(Date)
    biography = Column(String)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")
