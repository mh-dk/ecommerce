from sqlalchemy.orm import Session
from ecommerce.vendors import service as vendors_service
from .models import (
    Product,
    ProductNotFoundDetails,
    ProductIn,
    ProductOut
)
from .exceptions import ProductNotFound

def to_model(product: Product):
    ProductOut(
        id=product.id,
        vendor_id=product.vendor_id,
        description=product.description,
        price=product.price,
        stock=product.stock,
        created_at=product.created_at
    )

def get(product_id: int, session: Session):
    return session.get(Product, product_id)

def get_or_raise(product_id: int, session: Session):
    product = get(product_id, session)

    if not product:
        raise ProductNotFound("id", product_id).add_details(
            ProductNotFoundDetails(
                indicator="id",
                value=product_id
            )
        )

    return product

def by_vendor(vendor_id: int, session: Session):
    return session.query(Product).where(Product.vendor_id == vendor_id).all()

def create_product(product_in: ProductIn, session: Session):
    vendor = vendors_service.get_or_raise(product_in.vendor_id, session)
    product = Product(
        vendor_id=vendor.id,
        description=product_in.description,
        price=product_in.price,
        stock=product_in.stock,
    )

    session.add(product)
    session.flush()

    return product