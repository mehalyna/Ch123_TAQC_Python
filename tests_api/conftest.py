import pytest
from tests_api.Application import App
import config

@pytest.fixture(scope="function")
def header_admin():
    app = App()
    header = app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    return header

@pytest.fixture(scope="function")
def api_app():
    app = App()
    return app

@pytest.fixture(scope="function")
def header_user():
    app = App()
    header = app.get_header_login_admin("user@gmail.com",
            "user.password")
    return header

@pytest.fixture(scope="function")
def category_id(header_admin):
    id = header_admin.get_category_id()
    return id


@pytest.fixture(scope="function")
def category_name(header_admin):
    name = header_admin.get_category_name()
    return name

@pytest.fixture(scope="function")
def category_payload(header_admin):
    payload = header_admin.get_category_name()
    return payload
