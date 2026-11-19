from sqlalchemy.orm import Session
from .models import (
    Province,
    City
)
from .exceptions import (
    LocationNotExists,
    LocationMismatch
)

def validate(province: str, city: str, session: Session):
    city_obj = session.get(City, city)
    if not city_obj:
        raise LocationNotExists("city", city)
    province_obj = session.get(Province, province)
    if not province_obj:
        raise LocationNotExists("province", province)

    if city_obj.province_name != province_obj.name:
        raise LocationMismatch(city_obj.name, province_obj.name)