import typing
import sqlalchemy as sa

from core.protocols import DbConnection
from core import exceptions as exc
from core.error_codes import ErrorCode
from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore
from {{cookiecutter.project_slug}}.adapters import orm as o  # type: ignore


class SqlRepo:
    def __init__(self, conn: DbConnection):
        self.conn = conn

    {% if cookiecutter.add_example_code == 'y' %}  # type: ignore
    def get_test_model(
        self, id: m.TestModelId, actor: typing.Optional[m.core_m.UserId] = None
    ) -> typing.List[m.TestModel]:
        query = sa.select([
            o.test_table.c.id,
            o.test_table.c.user_name,
            o.test_table.c.age,
        ]).where(
            o.test_table.c.id == id
        )
        item = self.conn.execute(query).fetchone()
        if not item:
            raise exc.AppException(
                f"Test Model with {id=} does not exist.",
                err_code=ErrorCode.MISSINGDATA,
            )
        return m.TestModel(
            id=item.id,
            user_name=item.user_name,
            age=item.age,
        )

    def create_test_model(
        self, model: m.TestModel, actor: typing.Optional[m.core_m.UserId] = None
    ) -> m.TestModel:
        query = sa.insert(o.test_table).values({
            "id": model.id,
            "user_name": model.user_name,
            "age": model.age,
        })
        self.conn.execute(query)
        return model
    {% endif %}  # type: ignore


class SqlQueryRepo:
    def __init__(self, conn: typing.Optional[DbConnection]):
        self.conn = conn

    {% if cookiecutter.add_example_code == 'y' %}  # type: ignore
    def list_test_models(self) -> typing.List[m.TestModel]:
        query = sa.select([
            o.test_table.c.id,
            o.test_table.c.user_name,
            o.test_table.c.age,
        ])
        resp = self.conn.execute(query).fetchall()
        return [
            m.TestModel(
                id=item.id,
                user_name=item.user_name,
                age=item.age,
            )
            for item in resp
        ]
    {% endif %}  # type: ignore
