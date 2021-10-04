import pytest
import config
from selenium import webdriver
from pages.common.BasePage import BasePage
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def app():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield BasePage(driver)
    driver.quit()


@pytest.fixture(scope="function")
def admin_setup(app):
    """
        Login as an admin
    """
    app.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.admin_email, config.admin_pass)
    return app
