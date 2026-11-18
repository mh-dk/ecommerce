from typing import Literal
from pydantic import BaseModel

# [---- logic models ----]
class AuthToken(BaseModel):
    type: Literal["bearer"]
    token: str

class LoginForm(BaseModel):
    phone: str
    password: str