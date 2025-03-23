import logging
import sqlalchemy as sa
import psycopg2
import contextlib
from core import exceptions as exc
from core.error_codes import ErrorCode


LOGGER = logging.getLogger(__name__)


class PostgresConnection:
    def __init__(self, engine: sa.Engine):
        self.engine = engine
        self.url = self.engine.url
        self.conn = None
        self._execute = None

    @contextlib.contextmanager
    def begin(self):
        if self.conn is None or self.conn.closed:
            self.conn = self.engine.connect()
        try:
            if not self.conn.in_transaction():
                with self.conn.begin() as transaction:
                    self._transaction = transaction
                    yield self
            else:
                yield self
        finally:
            pass

    def __enter__(self):
        self.conn = self.engine.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            LOGGER.error(f"Database Exception: {str(exc_type)}\n{str(exc_val)}")
            self.conn.rollback()
            if isinstance(exc_type, psycopg2.Error):
                raise exc.AppException(
                    msg=exc_val, error_code=ErrorCode.DBERROR, __traceback__=exc_tb
                )
            raise
        self.conn.commit()
        self.conn.close()

    def execute(self, query, values=None):
        if values is not None:
            self._execute = self.conn.execute(query, values)
        else:
            self._execute = self.conn.execute(query)
        return self._execute

    def fetchall(self):
        if not self._execute:
            raise ValueError("Have no query to execute")
        return self._execute.fetchall()

    def fetchone(self):
        if not self._execute:
            raise ValueError("Have no query to execute")
        return self._execute.fetchone()

    def fetchval(self, pos: int = 0):
        if not self._execute:
            raise ValueError("Have no query to execute")
        return self.fetchone()[pos]