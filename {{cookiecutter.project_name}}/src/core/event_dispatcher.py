from __future__ import annotations

import logging
import typing
from collections import defaultdict

from core.domain.events import Event

LOGGER = logging.getLogger(__name__)


class SingletonMeta(type):
    """Meta type of Singleton Class"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class EventDispatcher(metaclass=SingletonMeta):
    """Singleton class working as event dispatcher"""

    def __init__(self):
        self._handlers = defaultdict(set)

    def register(self, message_type) -> typing.Callable:
        def inner(func):
            self._handlers[message_type].add(func)
            LOGGER.debug(f"Registered function for {message_type}: {func.__name__}")

        return inner

    def dispatch(self, event: Event) -> None:
        event_type = event.event_type()
        for handler in self._handlers[event_type]:
            handler(event)

    def dispatch_all(self, events: typing.List[Event]) -> None:
        for event in events:
            self.dispatch(event)
