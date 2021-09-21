import allure
import pytest
import config
from selenium import webdriver
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
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
