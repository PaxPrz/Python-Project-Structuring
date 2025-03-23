from __future__ import annotations

import logging
import typing
from dataclasses import dataclass, field, fields
from uuid import UUID, uuid4


LOGGER = logging.getLogger(__name__)
UserId = typing.NewType("UserId", int)


@dataclass
class FlagModel:
    _flags: typing.Dict[str, typing.Any] = field(default_factory=dict)

    def get_flag(self, key: str) -> typing.Any:
        return self._flags.get(key, False)

    def set_flag(self, key: str, value: typing.Any = True) -> None:
        self._flags.update({key: value})


@dataclass
class BaseModel(FlagModel):
    id_: UUID = field(default_factory=uuid4)

    @classmethod
    def from_dict(cls, obj: typing.Dict[str, typing.Any]):
        return cls(**obj)

    def to_dict(self):
        # Use this for sqlalchemy queries
        return {
            key.name: getattr(self, key.name, None)
            for key in fields(self)
            if not key.name.startswith("_")
        }

    def update(self, **kwargs) -> BaseModel:
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self
