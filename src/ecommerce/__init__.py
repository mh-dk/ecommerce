from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .core import Session
from .exceptions import ServiceError

app = FastAPI()

@app.middleware("http")
async def database_session_middleware(request: Request, call_next):
    with Session.begin() as session:
        request.state.session = session
        response = await call_next(request)

    return response

@app.exception_handler(ServiceError)
async def service_error_hanler(request: Request, exc: ServiceError):
    return JSONResponse(
        {
            "code": exc.error_code,
            "details": exc.details
        },
        exc.status_code
    )