from fastapi import APIRouter
from ecommerce.users.views import router as users_router
from ecommerce.auth.views import router as auth_router
from ecommerce.vendors.views import router as vendors_router
from ecommerce.products.views import router as products_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["Users"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(vendors_router, prefix="/vendors", tags=["Vendors"])
router.include_router(products_router, prefix="/products", tags=["products"])