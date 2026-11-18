from fastapi import APIRouter
from ecommerce.auth.models import (
    LoginForm
)
from ecommerce.core import DbSession
from ecommerce.user.models import (
    UserIn
)
from . import service as auth_service

router = APIRouter()

@router.post("/signup")
def sign_up(user_in: UserIn, session: DbSession):
    return auth_service.signup(user_in, session)

@router.post("/login")
def login(form: LoginForm, session: DbSession):
    return auth_service.login(form, session)