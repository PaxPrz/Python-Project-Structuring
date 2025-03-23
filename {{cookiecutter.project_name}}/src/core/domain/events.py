import typing
from dataclasses import dataclass, field
from datetime import datetime

from shortuuid import uuid

from core.domain import models as m

EventId = typing.NewType("EventId", str)


@dataclass(frozen=True, eq=False)
class Event:
    """Base class for domain events"""

    id_: EventId = field(default_factory=uuid, init=False)
    created_on: datetime = field(default_factory=datetime.utcnow, init=False)
    actor: typing.Optional[m.UserId]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)

    @classmethod
    def event_type(cls):
        return "{}.{}".format(cls.__module__.split(".")[0], cls.__name__)
