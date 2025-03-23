from core.database import DbConnection
from {{cookiecutter.project_slug}}.services import handlers as h  # type: ignore
from {{cookiecutter.project_slug}}.domain import commands as cmds  # type: ignore
from {{cookiecutter.project_slug}}.repository import sql as sql_repo  # type: ignore
from {{cookiecutter.project_slug}}.services import abstracts as a  # type: ignore


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
# This one is framework based. Use your framework

class TestAPIView(...):
    def list(self, request, *args, **kwargs):
        with DbConnection() as conn:
            repo = sql_repo.SqlQueryRepo(conn)
            models = repo.list_test_models()
            # In django you can use serializers here
        serialized_data = [model.to_dict() for model in models]
        return Response({
            "data": serialized_data,
        })

    def create(self, request, *args, **kwargs):
        payload = a.CreateTestModelPayload(**request.data)
        cmd = cmds.CreateTestModelCmd(payload())
        with DbConnection() as conn:
            repo = sql_repo.SqlRepo(conn)
            model = cmd.execute()
        return Response({
            "id": model.id
        })
{% endif %}  # type: ignore
