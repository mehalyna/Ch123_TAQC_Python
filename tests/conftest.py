import pytest
from selenium import webdriver

import config
from pages.common.BasePage import BasePage


@pytest.fixture(scope="function")
def app():
    driver = webdriver.Chrome()
    yield BasePage(driver)
    driver.quit()


@pytest.fixture(scope="function")
def admin_login(app):
    """
        Login as an admin
    """
    app.modal.login(config.admin_email, config.admin_pass)
