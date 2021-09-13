from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By


class IssuesPage:
    """ Locators and methods for Issues page. """

    VIEW_BTN_CSS = "tr:nth-child({})  a > button"
    CHECK_CSS = ".checkbox > label"
    BTN_CSS = "form > div.d-flex > button"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_view(self, view_number):
        """
            Method for click on a needed view button.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.VIEW_BTN_CSS.format(view_number + 1), view_number)
        element.click()

    def click_issue_status_filter(self, issue_status):
        """
            Method for click on issue status checkbox depending on text value.
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.CHECK_CSS)
        for element in elements:
            if issue_status == element.text:
                element.click()
                return

    def click_status_button(self, name_button):
        """
            Method for click on button depending on text value.
        """
        elements = self.driver.find_element(By.CSS_SELECTOR, self.BTN_CSS)
        for element in elements:
            if name_button == element.text:
                element.click()
                return
