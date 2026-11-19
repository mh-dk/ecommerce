from typing import Literal
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped
from pydantic import BaseModel
from ecommerce.core import Base

# [---- orm models ----]
class Province(Base):
    __tablename__ = "provinces"

    name: Mapped[str] = mapped_column(String(20), primary_key=True)

class City(Base):
    __tablename__ = "cities"

    name: Mapped[str] = mapped_column(String(20), primary_key=True)
    province_name = mapped_column(String(20), ForeignKey("provinces.id"))

# [---- error models ----]
class LocationNotExistsDetails(BaseModel):
    indicator: Literal["city", "province"]
    value: str

class LocationMismatchDetails(BaseModel):
    value: str