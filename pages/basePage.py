from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.baseContext import BaseContext


class BasePage(BaseContext):
    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        super().__init__(driver)
        self.base_url = "https://eventsexpress-test.azurewebsites.net/"

    def go_to_site(self):
        """
            Method for go to the base_url
        """
        return self.driver.get(self.base_url)
