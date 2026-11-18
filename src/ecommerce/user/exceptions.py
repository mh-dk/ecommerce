from ecommerce.exceptions import ServiceError
from .models import (
    UserNotFoundDetails,
    DuplicatePhoneNumberDetails
)

class UserNotFound(ServiceError[UserNotFoundDetails]):
    status_code=404
    error_code="user.not_found"
    msg_template="no user with {0} {1} was found."

class DuplicatePhoneNumber(ServiceError[DuplicatePhoneNumberDetails]):
    status_code=409
    error_code="user.duplicate_phone"
    msg_template="a user with this phone number already exists."