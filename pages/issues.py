from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By


class IssuesPage:
    """
    Locators and methods for Issues page.
    """

    VIEW_BTN_CSS = "tr:nth-child({})  a > button"
    FROM_DATA_INP_CSS = "div:nth-child(1) > div > div > input"
    TO_DATA_INP_CSS = "div:nth-child(2) > div > div > input"
    CHECK_CSS = "input[name='status[{}]']"
    RESET_BTN_XPATH = "//span[contains(text(),'Reset')]"
    SEARCH_BTN_XPATH = "//span[contains(text(),'Search')]"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_view(self, view_number):
        """
            Method for click on a needed view button.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.VIEW_BTN_CSS.format(view_number + 1), view_number)
        element.click()

    """
        There should be a code for entering the date in the datepicker but I cannot fill it with data.
        Please, help me...
    """

    def click_issue_status_filter(self, issue_status):
        """
            Method for click on a needed issue status checkbox.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHECK_CSS.format(issue_status.value))
        element.click()

    def click_reset_button(self):
        """
            Method for click on a 'Reset' button.
        """
        element = self.driver.find_element(By.XPATH, self.RESET_BTN_XPATH)
        element.click()

    def click_search_button(self):
        """
            Method for click on a 'Search' button.
        """
        element = self.driver.find_element(By.XPATH, self.SEARCH_BTN_XPATH)
        element.click()


class Issue_Statuses(Enum):
    OPEN = '0'
    IN_PROGRESS = '1'
    RESOLVE = '2'
