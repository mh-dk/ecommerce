from typing import Annotated
from fastapi import Request, Depends, Header
from ecommerce.core import DbSession
from ecommerce.auth.exceptions import (
    BadToken
)
from ecommerce.user.models import (
    User
)
from ecommerce.user import service as user_service

def current_user(
    request:Request, 
    session: DbSession,
    Authorization: Annotated[str, Header()] # forcing Authorization header
):
    try:
        user_id = int(request.state.token_sub)
    except ValueError:
        raise BadToken()

    if user_id:
        user = user_service.by_id(user_id, session)
        if not user:
            raise BadToken()
        return user

type CurrentUser = Annotated[User | None, Depends(current_user)]