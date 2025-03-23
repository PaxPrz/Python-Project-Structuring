from pydantic import fields
from core.domain.commands import BaseCommand
from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore
from {{cookiecutter.project_slug}}.domain import validators as val # type: ignore


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
class CreateTestModelCmd(BaseCommand, val.UserNameValidator, val.UserAgeValidator):
    user_id: m.core_m.UserId
    user_name: str
    age: int
{% endif %}  # type: ignore
