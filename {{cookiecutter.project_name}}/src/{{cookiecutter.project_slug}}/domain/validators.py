from pydantic import BaseModel as PydanticBaseModel, field_validator

from core import exceptions as exc
from core.error_codes import ErrorCode
from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore
from {{cookiecutter.project_slug}}.domain import constants as c  # type: ignore


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
class UserNameValidator(PydanticBaseModel):
    """Validates Username has character requirements satisfied or not"""
    @field_validator("user_name", check_fields=False)
    def validate_user_name(cls, v, values, **kwargs):
        if not v or len(v) < c.MIN_USER_NAME_CHARACTER:
            raise exc.AppException(
                f"Expected {c.MIN_USER_NAME_CHARACTER} Minimum Characters",
                location="user_name",
                err_code=ErrorCode.INVALIDDATA,
            )


class UserAgeValidator(PydanticBaseModel):
    """Validates user age"""
    @field_validator("age", check_fields=False)
    def validate_age(cls, v, values, **kwargs):
        if v is None or v < c.MAX_AGE:
            raise exc.AppException(
                f"Age must be less than {c.MAX_AGE}",
                location="age",
                err_code=ErrorCode.INVALIDDATA,
            )
{% endif %}  # type: ignore
