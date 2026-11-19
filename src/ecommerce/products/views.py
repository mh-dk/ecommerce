from fastapi import APIRouter
from ecommerce.core import DbSession
from .models import ProductIn
from . import service as product_service

router = APIRouter()

@router.post("/")
def create_product(product_in: ProductIn, session: DbSession):
    return product_service.to_model(
        product_service.create_product(product_in, session)
    )

@router.get("/{id}")
def get_product_by_id(id: int, session: DbSession):
    return product_service.to_model(
        product_service.get_or_raise(id, session)
    )