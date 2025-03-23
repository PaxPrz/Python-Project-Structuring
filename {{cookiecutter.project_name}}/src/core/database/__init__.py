import sqlalchemy as sa
from functools import partial
from core.settings import (
    DATABASE_URI,
)
from .connections import PostgresConnection

engine = None
DbConnection = lambda: None  # noqa

if DATABASE_URI:
    engine = sa.create_engine(DATABASE_URI, pool_size=4)
    DbConnection = partial(PostgresConnection, engine=engine)
