from fastapi import APIRouter
from ecommerce.core import DbSession
from .dependencies import (
    CurrentUser
)
from . import service as users_service

router = APIRouter()

@router.get("/me")
def get_current_user(current_user: CurrentUser):
    return users_service.to_model(current_user)

@router.get("/me/balance")
def get_current_users_balance(current_user: CurrentUser):
    return {
        "balance": current_user.balance
    }

@router.get("/{id}")
def get_current_user_by_id(id: int, session:DbSession):
    return users_service.to_model(
        users_service.by_id_or_raise(id, session)
    )