from datetime import datetime, timezone, timedelta
import jwt
from sqlalchemy.orm import Session
from ecommerce import config
from ecommerce.user.models import (
    UserIn
)
from ecommerce.user import service as user_service
from ecommerce.auth.models import (
    AuthToken,
    LoginForm
)
from ecommerce.auth.exceptions import (
    BadToken,
    WrongCredentials
)

def generate_token(user_id: int):
    now = datetime.now(timezone.utc)
    return jwt.encode(
        {
            "sub": str(user_id),
            "iat": now,
            "exp": now + timedelta(days=30)
        }, 
        config.JWT_SECRET,
        algorithm="HS256"
    )

def data_from_token(token: str):
    try:
        return jwt.decode(
            token,
            config.JWT_SECRET,
            algorithms=["HS256"],
            leeway=10,
            options={"require": ["exp", "iat"]}
        )
    except (
        jwt.PyJWTError
    ):
        raise BadToken()

def token_from_header(header:str):
    try:
        type, token = header.split(" ")
    except ValueError:
        raise BadToken()

    if type != "Bearer":
        raise BadToken()

    return token

def signup(user_in: UserIn, session: Session):
    user = user_service.create_user(user_in, session)
    token = generate_token(user.id)
    return AuthToken(
        type="bearer",
        token=token
    )

def login(form: LoginForm, session: Session):
    user = user_service.by_phone(form.phone, session)
    if not user:
        raise WrongCredentials()
    if not user.verify_password(form.password):
        raise WrongCredentials()

    token = generate_token(user.id)
    return AuthToken(
        type="bearer",
        token=token
    )