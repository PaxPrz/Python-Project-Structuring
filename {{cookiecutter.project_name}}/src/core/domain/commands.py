import typing
from abc import ABC, abstractmethod

from core.domain import models as m
from shortuuid import uuid
from pydantic import BaseModel as PydanticBaseModel
from pydantic import fields, field_validator


class BaseCommand(PydanticBaseModel, ABC):
    cmd_id: str = fields.Field(default_factory=uuid)
    actor: typing.Optional[m.UserId] = fields.Field(default=None)

    @abstractmethod
    def execute(self, *args, **kwargs) -> m.BaseModel:
        raise NotImplementedError

    @classmethod
    def get_action_name(cls):
        return cls.__name__
