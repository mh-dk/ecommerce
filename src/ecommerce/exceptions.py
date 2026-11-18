from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class ServiceError(Exception, Generic[T]):
    status_code = 400
    error_code = "service.error"
    msg_template = "error at {location}"

    def __init__(self, *args, **kwargs) -> None:
        self.msg = self.msg_template.format(args, kwargs)
        self.details:T | None = None
        super().__init__(f"a service error with code {self.error_code} occurred.", self.msg)

    def add_details(self, details:T):
        self.details = details
        return self