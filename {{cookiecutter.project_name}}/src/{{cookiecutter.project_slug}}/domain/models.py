from __future__ import annotations

import typing
import logging
from uuid import UUID
from dataclasses import dataclass, field

from core.domain import models as core_m


LOGGER = logging.getLogger(__name__)

TestModelId = typing.NewType("TestModelId", UUID)


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
@dataclass
class TestModel(core_m.BaseModel):
    user_name: str
    age: int
{% endif %}  # type: ignore
