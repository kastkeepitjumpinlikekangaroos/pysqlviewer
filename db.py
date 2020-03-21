from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.environ.get('CONNECTION_STRING'))

