import pytest
from tests_api.Application import App


@pytest.fixture(scope="function")
def api_app():
    app = App()
    return app
