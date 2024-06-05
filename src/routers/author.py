from uuid import UUID

from fastapi import Depends, HTTPException, Response, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.auth import current_active_user
from .. import crud
from ..dependencies import get_db
from ..schemas.author import Author, AuthorCreate, AuthorUpdate

router = APIRouter()


@router.get("/", response_model=list[Author])
async def read_authors(
        db: AsyncSession = Depends(get_db),
        user=Depends(current_active_user)
):
    authors = await crud.get_authors(db)
    return authors


@router.get("/{author_id}", response_model=Author)
async def read_author(
        author_id: UUID,
        db: AsyncSession = Depends(get_db),
        user=Depends(current_active_user)
):
    author = await crud.get_author(db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/", response_model=Author)
async def create_author(
        author: AuthorCreate,
        db: AsyncSession = Depends(get_db),
        user=Depends(current_active_user)
):
    new_author = await crud.create_author(db, author)
    return new_author


@router.put("/{author_id}", response_model=Author)
async def update_author(
        author_id: UUID,
        author: AuthorUpdate,
        db: AsyncSession = Depends(get_db),
        user=Depends(current_active_user)
):
    db_author = update_author(db, author_id=author_id, author=author)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.delete("/{author_id}")
async def delete_author(
        author_id: UUID,
        db: AsyncSession = Depends(get_db),
        user=Depends(current_active_user)
):
    author = await crud.delete_author(db, author_id)
    if author is None:
        return HTTPException(status_code=400, detail="Author with the specified ID not found")
    return Response(status_code=204)
