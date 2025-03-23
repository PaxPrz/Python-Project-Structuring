import traceback
import typing
from dataclasses import dataclass, fields


NOTSENT = None


@dataclass(init=False)
class PayloadParser:
    """Can be used to document on API"""
    def __init__(self, **kwargs):
        names = set([f.name for f in fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)

    def __call__(self) -> typing.Dict[str, typing.Any]:
        return {key: value for key, value in self.__dict__.items() if value != NOTSENT}
