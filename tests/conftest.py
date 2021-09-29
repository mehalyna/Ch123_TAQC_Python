import allure
from allure_commons.types import AttachmentType
import config
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.common.BasePage import BasePage


@pytest.fixture(scope="function")
def app():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield BasePage(driver)
    driver.quit()


@pytest.fixture(scope="function")
def admin_setup(app):
    """
        Login as an admin
    """
    app.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    return app


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook the "item" object on a test failure
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, app):
    """
    Make screenshot on a test failure
    """
    yield
    if request.node.rep_setup.failed:
        make_screenshot(app.driver, request.function.__name__)
    elif request.node.rep_call.failed:
        make_screenshot(app.driver, request.function.__name__)


def make_screenshot(driver, function_name):
    allure.attach(driver.get_screenshot_as_png(),
                  name=function_name,
                  attachment_type=AttachmentType.PNG)
