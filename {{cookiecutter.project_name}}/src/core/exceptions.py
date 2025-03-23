import typing
import traceback

from core.error_codes import ErrorCode


class AppException(Exception):
    def __init__(
        self,
        msg: str,
        location: typing.Optional[str] = None,
        err_code: ErrorCode = ErrorCode.UNKNOWN,
        **kwargs,
    ):
        """
        msg: error message
        location: location that point the error
        """
        super().__init__(msg, **kwargs)
        self.location = location
        self.err_code = err_code


def err_logger(e: typing.Optional[Exception] = None):
    traceback.print_exc()
