from ecommerce.exceptions import ServiceError
from .models import (
    UserNotFoundDetails
)

class UserNotFound(ServiceError[UserNotFoundDetails]):
    status_code=404
    error_code="user.not_found"
    msg_template="no user with {0} {1} was found."