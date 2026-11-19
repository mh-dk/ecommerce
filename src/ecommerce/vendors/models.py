from typing import Literal
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from ecommerce.core import Base

# [---- orm models ----]
class Vendor(Base):
    __tablename__ = "vendors"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    owner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.name"), nullable=False)
    city_name: Mapped[str] = mapped_column(String(20), ForeignKey("cities.name"), nullable=False)
    province: Mapped[str] = mapped_column(String(20), ForeignKey("provinces.name"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(True), server_default=func.now())

# [---- error models ----]
class VendorDoesNotExistDetails(BaseModel):
    indicator: Literal["id", "owner"]
    value: int | str

# [---- logic models ----]
class VendorIn(BaseModel):
    name: str
    city: str
    province: str

class VendorOut(BaseModel):
    id: int
    name: str
    owner: int
    city: str
    province: str
    created_at: datetime