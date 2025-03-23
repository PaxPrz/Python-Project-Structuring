import typing

from core.protocols import DbConnection
from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore


class DjangoRepo:
    def __init__(self, conn: typing.Optional[DbConnection] = None):
        ...

    {% if cookiecutter.add_example_code == 'y' %}  # type: ignore
    def get_test_model(
        self, id: m.TestModelId, actor: typing.Optional[m.core_m.UserId] = None
    ) -> m.TestModel:
        ...

    def create_test_model(
        self, model: m.TestModel, actor: typing.Optional[m.core_m.UserId] = None
    ) -> m.TestModel:
        ...
    {% endif %}  # type: ignore


class DjangoQueryRepo:
    def __init__(self, conn: typing.Optional[DbConnection] = None):
        self.conn = conn

    {% if cookiecutter.add_example_code == 'y' %}  # type: ignore
    def list_test_models(self) -> typing.List[m.TestModel]:
        ...
    {% endif %}  # type: ignore
