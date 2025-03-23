from dataclasses import dataclass

from core.domain.events import Event
from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
@dataclass(frozen=True)
class TestModelCreated(Event):
    model: m.TestModel
{% endif %}  # type: ignore
