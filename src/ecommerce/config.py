import os
from typing import overload

@overload
def config(name: str) -> str: ...
@overload
def config(name: str, default: str) -> str: ...

def config(name: str, default: str | None = None):
    result = os.environ.get(name, default)
    if (not result) and (not default):
        raise ValueError(f"environment variable {name} is needed and not set.")
    return result