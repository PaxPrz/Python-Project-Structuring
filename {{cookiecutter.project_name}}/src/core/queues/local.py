import logging
import typing


LOGGER = logging.getLogger(__name__)


class LocalQueue:
    QUEUES: typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]] = {}

    def __init__(
        self,
        queue_name: str,
    ):
        if queue_name not in self.QUEUES:
            self.QUEUES[queue_name] = []
        self.queue_name = queue_name

    def send(self, message: typing.Dict[str, typing.Any]):
        self.QUEUES[self.queue_name].append(message)

    def receive(self) -> typing.Dict[str, typing.Any]:
        item = {}
        if len(self.QUEUES[self.queue_name]) > 0:
            item = self.QUEUES[self.queue_name].pop(0)
        return item
