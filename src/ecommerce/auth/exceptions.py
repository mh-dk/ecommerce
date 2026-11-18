from typing import Any
from ecommerce.exceptions import ServiceError

class WrongCredentials(ServiceError[Any]):
    status_code=401
    error_code="auth.wrong_credentials"
    msg_template="wrong phone number or password."

class BadToken(ServiceError[Any]):
    status_code=401
    error_code="auth.bad_token"
    msg_template="token invalid, expiered or missing"