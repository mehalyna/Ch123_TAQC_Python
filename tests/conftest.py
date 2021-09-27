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
def admin_setup(app):
    """
        Login as an admin
    """
    app.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    return app
