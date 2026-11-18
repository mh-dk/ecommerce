from sqlalchemy.orm import Session
from ecommerce.core import ph
from .models import (
    DuplicatePhoneNumberDetails,
    User,
    UserIn,
    UserNotFoundDetails
)
from .exceptions import (
    DuplicatePhoneNumber,
    UserNotFound,
)

def by_id(user_id: int, session: Session):
    return session.get(User, user_id)

def by_id_or_raise(user_id: int, session: Session):
    user = session.get(User, user_id)
    if not user:
        raise UserNotFound("id", user_id).add_details(
            UserNotFoundDetails(
                indicator="id",
                value=user_id
            )
        )
    return user

def by_phone(phone_number: str, session: Session):
    return session.query(User).where(User.phone_number == phone_number).first()

def by_phone_or_raise(phone_number: str, session: Session):
    user = session.query(User).where(User.phone_number == phone_number).first()
    if not user:
        raise UserNotFound("phone number", phone_number).add_details(
            UserNotFoundDetails(
                indicator="phone",
                value=phone_number
            )
        )
    return user

def create_user(user_in: UserIn, session: Session):
    existing_user = by_phone(user_in.phone, session)
    if existing_user:
        raise DuplicatePhoneNumber().add_details(
            DuplicatePhoneNumberDetails(
                value=user_in.phone
            )
        )

    password_hash = ph.hash(user_in.password)
    user = User(
        firstname=user_in.firstname,
        lastname=user_in.lastname,
        phone_number=user_in.phone,
        email=user_in.email,
        password_hash=password_hash
    )

    session.add(user)
    session.flush()

    return user