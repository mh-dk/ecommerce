from ecommerce.exceptions import ServiceError

class ProductNotFound(ServiceError):
    status_code = 404
    error_code = "product.not_found"
    msg_template = "no product with {0} {1} was found"