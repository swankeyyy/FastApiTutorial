from fastapi import APIRouter
from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])  # указывает какой тип вернется
async def get_products(session):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(session, product: ProductCreate):
    return await crud.create_product(session=session, product=product)


@router.get("/{product_id}", response_model=Product)
async def get_product(session, product_id: int):
    return await crud.get_product(session=session, product_id=product_id)
