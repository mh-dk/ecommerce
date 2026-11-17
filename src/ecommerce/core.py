from typing import Annotated
from argon2 import PasswordHasher
from fastapi import Request, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session as SqlAlchemySession
from ecommerce import config

engine = create_engine(config.SQLALCHEMY_URL)
Session = sessionmaker(engine)
ph = PasswordHasher()

class Base(DeclarativeBase):
    ...

def get_database_session(request: Request):
    return request.state.session

type DbSession = Annotated[SqlAlchemySession, Depends(get_database_session)]