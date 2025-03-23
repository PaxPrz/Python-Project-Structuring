import typing
import os
from pathlib import Path
from core import exceptions as exc
from core.error_codes import ErrorCode


class LocalStorage:
    def read(self, filename: typing.Union[str, Path], mode: str = "rb") -> bytes:
        try:
            with open(filename, mode) as f:
                content = f.read()
        except Exception as e:
            exc.err_logger(e)
            raise exc.AppException(
                f"Could not open file: {filename}",
                err_code=ErrorCode.STORAGEERROR,
            ) from e
        return content

    def write(
        self, filename: typing.Union[str, Path], mode: str = "wb", content: bytes = b""
    ):
        try:
            with open(filename, mode) as f:
                f.write(content)
        except Exception as e:
            exc.err_logger(e)
            raise exc.AppException(
                f"Could not write file: {filename}",
                err_code=ErrorCode.STORAGEERROR,
            ) from e

    def delete(self, filename: typing.Union[str, Path]):
        try:
            os.remove(filename)
        except Exception as e:
            exc.err_logger(e)
            raise exc.AppException(
                f"Could not delete file: {filename}",
                err_code=ErrorCode.STORAGEERROR,
            ) from e

    def __str__(self):
        return "LocalStorage"
