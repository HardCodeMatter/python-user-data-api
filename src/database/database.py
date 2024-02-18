from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from .config import settings


engine = create_engine(settings.DATABASE_URL_psycopg2, echo=True)
session_factory = sessionmaker(engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase): ...


def get_session():
    with session_factory() as session:
        try:
            yield session
        finally:
            session.close()
