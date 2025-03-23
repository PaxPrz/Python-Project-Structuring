import typing
from core import exceptions as exc
from core.error_codes import ErrorCode

from core.protocols import DbConnection
from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore


class FakeRepo:
    _test_models = []

    def __init__(self, conn: typing.Optional[DbConnection] = None):
        self.conn = conn

    {% if cookiecutter.add_example_code == 'y' %}  # type: ignore
    def get_test_model(
        self, id: m.TestModelId, actor: typing.Optional[m.core_m.UserId] = None
    ) -> m.TestModel:
        for d in self._test_models:
            if d.id == id:
                return d
        raise exc.AppException(
            f"Test Model with {id=} does not exists.",
            err_code=ErrorCode.MISSINGDATA,
        )

    def create_test_model(
        self, model: m.TestModel, actor: typing.Optional[m.core_m.UserId] = None
    ) -> m.TestModel:
        self._test_models.append(model)
        return model
    {% endif %}  # type: ignore


class FakeQueryRepo:
    _test_models = []

    def __init__(self, conn: typing.Optional[DbConnection] = None):
        self.conn = conn

    {% if cookiecutter.add_example_code == 'y' %}  # type: ignore
    def list_test_models(self) -> typing.List[m.TestModel]:
        return self._test_models
    {% endif %}  # type: ignore
