import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from src.models.models import Base

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)


async def create_db_and_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await create_db_and_tables()


if __name__ == "__main__":
    asyncio.run(main())
