import typing
import logging
import boto3
from core import exceptions as exc
from core.error_codes import ErrorCode
from core import settings


LOGGER = logging.getLogger(__name__)
AWS_REGION = getattr(settings, "AWS_REGION", "ap-southeast-2")
AWS_ACCESS_KEY_ID = getattr(settings, "AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = getattr(settings, "AWS_SECRET_ACCESS_KEY", None)
EMAIL_FROM = getattr(settings, "EMAIL_FROM", None)


class SES:
    charset = "UTF-8"

    def __init__(
        self,
        email_from: str = EMAIL_FROM,
        *,
        aws_region: str = AWS_REGION,
        aws_access_key_id: typing.Optional[str] = AWS_ACCESS_KEY_ID,
        aws_secret_access_key: typing.Optional[str] = AWS_SECRET_ACCESS_KEY,
    ):
        self.email_from = email_from
        config = {"region_name": aws_region}
        if aws_access_key_id and aws_secret_access_key:
            config.update(
                {
                    "aws_access_key_id": aws_secret_access_key,
                    "aws_secret_access_key": aws_secret_access_key,
                }
            )
        self.client = boto3.client("ses", **config)

    def send_email(
        self,
        email_to: typing.Union[typing.List[str], str],
        subject: str,
        body: str,
        html_body: typing.Optional[str] = None,
        fail_silently: bool = False,
    ) -> bool:
        if isinstance(email_to, str):
            email_to = [email_to]
        body = {
            "Text": {
                "Data": body,
                "Charset": self.charset,
            }
        }
        if html_body:
            body.update(
                {
                    "Html": {
                        "Data": html_body,
                        "Charset": self.charset,
                    }
                }
            )
        try:
            self.client.send_email(
                Source=self.email_from,
                Destination={
                    "ToAddresses": [
                        email_to[0],
                    ],
                    "CcAddresses": email_to[1:],
                },
                Message={
                    "Subject": {
                        "Data": subject,
                        "Charset": self.charset,
                    },
                    "Body": body,
                },
            )
        except Exception as e:
            LOGGER.error(f"Error while sending email [{subject}]: {str(e)}")
            exc.err_logger(e)
            if fail_silently:
                return False
            raise exc.AppException(
                str(e),
                err_code=ErrorCode.EMAILCLIENTERROR,
            )
        return True
