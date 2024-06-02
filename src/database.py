import sqlalchemy.exc
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = "db_bookshelf"

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:12345@localhost:5432/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
