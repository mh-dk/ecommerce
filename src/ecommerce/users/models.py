from typing import Literal
from datetime import datetime
from argon2.exceptions import VerifyMismatchError
from pydantic import BaseModel
from sqlalchemy import BigInteger, String, DateTime, Text, func
from sqlalchemy.orm import InstanceEvents, Mapped, mapped_column
from ecommerce.core import Base, ph

# [---- orm models ----]
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    balance: Mapped[int] = mapped_column(BigInteger, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(True))
    password_hash = mapped_column(Text)

    def verify_password(self, input: str):
        try:
            return ph.verify(self.password_hash, input)
        except VerifyMismatchError:
            return False

# [---- error models ----]
class UserNotFoundDetails(BaseModel):
    indicator: Literal["id"] | Literal["phone"]
    value: int | str

class DuplicatePhoneNumberDetails(BaseModel):
    value: str

# [---- logic models ----]
class UserIn(BaseModel):
    firstname: str
    lastname: str
    phone: str
    email: str | None = None
    password: str

class UserOut(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone: str
    email: str | None = None
    singed_up_at: datetime