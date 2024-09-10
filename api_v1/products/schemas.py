from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )  # явно указывает что нужно брать свойства с атрибутов модели
    id: int
