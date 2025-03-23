from core.domain import events as eve
from core.utils import event_dispatcher


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
@event_dispatcher.register("{{cookiecutter.project_slug}}.TestModelCreated")
def send_notification(event: eve.TestModelCreated):
    pass
{% endif %}  # type: ignore
