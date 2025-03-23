import typing
from dataclasses import dataclass, field

from core.abstracts import (
    PayloadParser
)

{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
@dataclass(init=False)
class CreateTestModelPayload(PayloadParser):
    """
    user_name: Short Name of User
    age: Age of User
    """
    user_name: str
    age: typing.Optional[int] = field(default=18)
{% endif %}  # type: ignore
