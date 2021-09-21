import pytest
from selenium import webdriver

from pages.common.BasePage import BasePage


@pytest.fixture(scope="function")
def app():
    driver = webdriver.Chrome()
    yield BasePage(driver)
    driver.quit()


