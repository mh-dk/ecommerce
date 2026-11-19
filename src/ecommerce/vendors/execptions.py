from ecommerce.exceptions import ServiceError
from .models import VendorDoesNotExistDetails

class VendorDoesNotExist(ServiceError[VendorDoesNotExistDetails]):
    status_code = 404
    error_code = "vendor.not_exists"
    msg_template = "no vendor with {0} {1} exists"