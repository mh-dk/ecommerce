from sqlalchemy.orm import Session
from ecommerce.users.models import User
from ecommerce.location import service as location_service
from .models import (
    Vendor,
    VendorDoesNotExistDetails,
    VendorIn,
    VendorOut
)
from .execptions import (
    VendorDoesNotExist
)

def to_model(vendor: Vendor):
    return VendorOut(
        id=vendor.id,
        name=vendor.name,
        owner=vendor.owner_id,
        city=vendor.city_name,
        province=vendor.province,
        created_at=vendor.created_at
    )

def get(vendor_id: int, session: Session):
    return session.get(Vendor, vendor_id)

def get_or_raise(vendor_id: int, session: Session):
    vendor = get(vendor_id, session)

    if not vendor:
        raise VendorDoesNotExist("id", vendor_id).add_details(
            VendorDoesNotExistDetails(
                indicator="id",
                value=vendor_id
            )
        )

    return vendor

def by_owner(owner_id: int, session: Session):
    return session.query(Vendor).where(Vendor.owner_id == owner_id).all()

def create_vendor(model: VendorIn, user: User, session: Session):
    location_service.validate(
        model.province,
        model.city,
        session
    )

    vendor = Vendor(
        name = model.name,
        owner_id = user.id,
        city_name = model.city,
        province = model.province
    )

    session.add(vendor)
    session.flush()

    print(vendor.id)

    return vendor