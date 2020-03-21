from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.environ.get('CONNECTION_STRING'))
session_factory = sessionmaker(bind=engine)


@contextmanager
def get_db():
    db = scoped_session(session_factory)
    try:
        yield db
    finally:
        db.close()
