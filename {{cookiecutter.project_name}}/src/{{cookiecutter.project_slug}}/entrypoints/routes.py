from {{cookiecutter.project_slug}}.entrypoints import route_handlers as rh  # type: ignore


{% if cookiecutter.add_example_code == 'y' %}  # type: ignore
# This one is framework based. Use your framework
routes = [
    # path("/api/list-test-models", rh.TestAPIView.list),
    # path("/api/create-model", rh.TestAPIView.create),
]
{% else %}  # type: ignore
routes = []
{% endif %}  # type: ignore
