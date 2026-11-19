from ecommerce.exceptions import ServiceError
from .models import (
    LocationNotExistsDetails,
    LocationMismatchDetails
)

class LocationNotExists(ServiceError[LocationNotExistsDetails]):
    status_code = 422
    error_code = "location.not_exists"
    msg_template = "no {0} with the name {1} is acceptable in the server."

class LocationMismatch(ServiceError[LocationMismatchDetails]):
    status_code = 422
    error_code = "location.mismatch"
    msg_template = "city {0} is not part of {1}"