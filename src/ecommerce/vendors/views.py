from fastapi import APIRouter
from ecommerce.core import DbSession
from ecommerce.users.dependencies import CurrentUser
from .models import (
    VendorIn
)
from . import service as vendors_service
from ecommerce.products import service as products_service

router = APIRouter()

@router.get("/{id}")
def vendor_by_id(id: int, session: DbSession):
    return vendors_service.to_model(
        vendors_service.get_or_raise(id, session)
    )

@router.get("/{id}/products")
def vendors_products(id: int, session:DbSession):
    products = products_service.by_vendor(id, session)
    return (products_service.to_model(product) for product in products)

@router.get("/owner/me")
def current_users_vendor(current_user: CurrentUser, session: DbSession):
    vendors = vendors_service.by_owner(current_user.id, session)
    return (vendors_service.to_model(vendor) for vendor in vendors)

@router.get("/owner/{owner_id}")
def vendor_by_owner(owner_id: int, session: DbSession):
    vendors = vendors_service.by_owner(owner_id, session)
    return (vendors_service.to_model(vendor) for vendor in vendors)

@router.post("/")
def create_vendor(vendor_in: VendorIn, current_user: CurrentUser, session: DbSession):
    return vendors_service.to_model(
        vendors_service.create_vendor(
            vendor_in,
            current_user,
            session
        )
    )