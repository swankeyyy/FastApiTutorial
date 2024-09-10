from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Product, ProductCreate
from core.models import db_helper

router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])  # указывает какой тип вернется
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Product]:
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product=product)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
    )
