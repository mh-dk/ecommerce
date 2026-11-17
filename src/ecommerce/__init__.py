from fastapi import FastAPI, Request
from .core import Session

app = FastAPI()

@app.middleware("http")
async def database_session_middleware(request: Request, call_next):
    with Session.begin() as session:
        request.state.session = session
        response = await call_next(request)

    return response