from {{cookiecutter.project_slug}}.domain import models as m  # type: ignore
from {{cookiecutter.project_slug}}.domain import commands as cmds  # type: ignore
from {{cookiecutter.project_slug}}.domain import events as eve  # type: ignore
from {{cookiecutter.project_slug}}.adapters.repository import Repo  # type: ignore
from core.utils import event_dispatcher


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
def create_test_model(
    cmd: cmds.CreateTestModelCmd,
    repo: Repo,
    **kwargs,
) -> m.TestModel:
    events = (parent_events := kwargs.get("events")) or []
    model = cmd.execute()
    model = repo.create_test_model(model, actor=cmd.actor)
    events.append(
        eve.TestModelCreated(
            actor=cmd.actor,
            model=model,
        )
    )
    if parent_events is None:
        event_dispatcher.dispatch_all(events)
    return model
{% endif %}  # type: ignore
