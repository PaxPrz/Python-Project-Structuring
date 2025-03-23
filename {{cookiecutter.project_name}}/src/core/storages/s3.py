import typing
import boto3
from pathlib import Path
from core import exceptions as exc
from core.error_codes import ErrorCode
from core import settings


AWS_REGION = getattr(settings, "AWS_REGION", "ap-southeast-2")
AWS_ACCESS_KEY_ID = getattr(settings, "AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = getattr(settings, "AWS_SECRET_ACCESS_KEY", None)


class S3Storage:
    def __init__(
        self,
        bucket_name: str,
        *,
        aws_region: str = AWS_REGION,
        aws_access_key_id: typing.Optional[str] = AWS_ACCESS_KEY_ID,
        aws_secret_access_key: typing.Optional[str] = AWS_SECRET_ACCESS_KEY,
    ):
        config = {"region_name": aws_region}
        if aws_access_key_id and aws_secret_access_key:
            config.update(
                {
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                }
            )
        self.client = boto3.client("s3", **config)
        self.bucket_name = bucket_name

    def read(self, filename: typing.Union[str, Path], mode: str = None) -> bytes:
        try:
            object = self.client.get_object(
                Bucket=self.bucket_name,
                Key=filename,
            )
            return object.get("Body").read()
        except Exception as e:
            exc.err_logger(e)
            raise exc.AppException(
                f"Could not read from S3 bucket: {self.bucket_name} [{filename}]",
                err_code=ErrorCode.S3READERROR,
            ) from e

    def write(
        self, filename: typing.Union[str, Path], mode: str = None, content: bytes = b""
    ):
        try:
            self.client.put_object(
                Body=content,
                Bucket=self.bucket_name,
                Key=filename,
            )
        except Exception as e:
            exc.err_logger(e)
            raise exc.AppException(
                f"Could not write to S3 bucket: {self.bucket_name} [{filename}]",
                err_code=ErrorCode.S3WRITEERROR,
            ) from e

    def delete(self, filename: typing.Union[str, Path]):
        try:
            self.client.delete_object(
                Bucket=self.bucket_name,
                Key=filename,
            )
        except Exception as e:
            exc.err_logger(e)
            raise exc.AppException(
                f"Could not delete from S3 bucket: {self.bucket_name} [{filename}]",  # nosec
                err_code=ErrorCode.S3DELETEERROR,
            ) from e

    def __str__(self):
        return f"S3Storage: {self.bucket_name}"
