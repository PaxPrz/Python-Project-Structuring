from __future__ import annotations
from io import BytesIO
from core.domain import models as m
from pathlib import Path
from enum import Enum
import typing


class DbConnection(typing.Protocol):
    def execute(self, query, values=None) -> DbConnection:
        ...

    def fetchall(self) -> typing.List[typing.Any]:
        ...

    def fetchone(self) -> typing.Any:
        ...

    def fetchval(self) -> typing.Any:
        ...


class AsyncDbConnection(typing.Protocol):
    async def execute(self, query, values=None) -> AsyncDbConnection:
        ...

    def fetchall(self) -> typing.List[typing.Any]:
        ...

    def fetchone(self) -> typing.Any:
        ...

    def fetchval(self) -> typing.Any:
        ...


class EmailService(typing.Protocol):
    def send_email(
        self,
        email_to: typing.Union[typing.List[str], str],
        subject: str,
        body: str,
        html_body: typing.Optional[str] = None,
        fail_silently: bool = False,
    ) -> bool:
        ...


class Queue(typing.Protocol):
    def send(self, message: typing.Dict[str, typing.Any]):
        ...

    def receive(self) -> typing.Dict[str, typing.Any]:
        ...


class Storage(typing.Protocol):
    def read(self, filename: typing.Union[str, Path], mode: str = None) -> bytes:
        ...

    def write(
        self, filename: typing.Union[str, Path], mode: str = None, content: bytes = b""
    ):
        ...

    def delete(self, filename: typing.Union[str, Path]):
        ...
