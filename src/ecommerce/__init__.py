from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from ecommerce.auth import service as auth_service
from .core import Session
from .exceptions import ServiceError
from .views import router

app = FastAPI()

def service_error_response(exc: ServiceError):
    return JSONResponse(
        {
            "code": exc.error_code,
            "msg": exc.msg,
            "details": exc.details or {}
        },
        exc.status_code
    )

@app.middleware("http")
async def database_session_middleware(request: Request, call_next):
    with Session.begin() as session:
        request.state.session = session
        response = await call_next(request)

    return response

@app.middleware("http")
async def auth_token_middleware(request: Request, call_next):
    request.state.token_sub = None
    header = request.headers.get("Authorization")
    if not header:
        return await call_next(request)

    try:
        token = auth_service.token_from_header(header)
        data = auth_service.data_from_token(token)
    except ServiceError as exc:
        return service_error_response(exc)

    request.state.token_sub = data.get("sub")

    return await call_next(request)

@app.exception_handler(ServiceError)
async def service_error_hanler(request: Request, exc: ServiceError):
    return service_error_response(exc)

app.include_router(router)