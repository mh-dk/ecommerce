from typing import Literal
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger, DateTime, Integer, ForeignKey, Text, String, func
from sqlalchemy.orm import Mapped, mapped_column
from ecommerce.core import Base

# [---- orm models ----]
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    vendor_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("vendors.id"), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    images_folder: Mapped[str] = mapped_column(String(500))
    price: Mapped[int] = mapped_column(BigInteger, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(True))

# [---- error models ----]
class ProductNotFoundDetails(BaseModel):
    indicator: Literal["id", "vendor"]
    value: int

# [---- logic models ----]
class ProductIn(BaseModel):
    vendor_id: int
    description: str | None = None
    price: int
    stock: int

class ProductOut(BaseModel):
    id: int
    vendor_id: int
    description: str
    price: int
    stock: int
    created_at: datetime