import sqlalchemy as sa
from core.database.sql import get_metadata

METADATA = get_metadata()

{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
test_table = sa.Table(
    "test",
    METADATA,
    sa.Column("id", sa.UUID, primary_key=True, key="id_"),
    sa.Column("User Name", sa.String, nullable=False, key="user_name"),
    sa.Column("Age", sa.Integer, nullable=False, key="age"),
)
{% endif %}  # type: ignore
