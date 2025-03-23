import logging
import typing
import json
import boto3
from core import settings
from core import exceptions as exc
from core.error_codes import ErrorCode


LOGGER = logging.getLogger(__name__)


AWS_REGION = getattr(settings, "AWS_REGION", "ap-southeast-2")
AWS_ACCESS_KEY_ID = getattr(settings, "AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = getattr(settings, "AWS_SECRET_ACCESS_KEY", None)


class SQSQueue:
    def __init__(
        self,
        queue_name: str,
        *,
        aws_region: str = AWS_REGION,
        aws_access_key_id: typing.Optional[str] = AWS_ACCESS_KEY_ID,
        aws_secret_access_key: typing.Optional[str] = AWS_SECRET_ACCESS_KEY,
        raise_exception: bool = False,
    ):
        self.raise_exception = raise_exception
        config = {"region_name": aws_region}
        if aws_access_key_id and aws_secret_access_key:
            config.update(
                {
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                }
            )
        self.queue_name = queue_name
        self.sqs = boto3.resource(
            "sqs",
            **config,
        )
        self.queue = self.sqs.get_queue_by_name(QueueName=self.queue_name)

    def send(self, message: typing.Dict[str, typing.Any]):
        data = json.dumps(message)
        try:
            response = self.queue.send_message(MessageBody=data)
        except Exception as e:
            LOGGER.error(f"Error sending message to SQS: {str(e)}")
            if self.raise_exception:
                raise exc.AppException(
                    str(e), err_code=ErrorCode.SQSCLIENTERROR
                ) from e
        return response

    def receive(self) -> typing.Dict[str, typing.Any]:
        payload = {}
        try:
            for message in self.queue.receive_messages():
                data = message.body
                payload = json.loads(data)
                message.delete()
        except Exception as e:
            LOGGER.error(f"Error receiving message from SQS: {str(e)}")
            if self.raise_exception:
                raise exc.AppException(
                    str(e), err_code=ErrorCode.SQSCLIENTERROR
                ) from e
        return payload
