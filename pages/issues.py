from pages.elements.buttons import ButtonElements
from pages.elements.datepickers import DatePicker
from selenium import webdriver
from selenium.webdriver.common.by import By


class IssuesPage:
    """ Locators and methods for Issues page. """

    VIEW_BTN_CSS = "tr:nth-child({})  a > button"
    CHECK_CSS = ".checkbox > label"
    BTN_CSS = "form > div.d-flex > button"
    DATAPICKER_FROM_CSS = ".form-group:nth-child(1) .MuiInputBase-input.MuiInput-input"
    DATAPICKER_TO_CSS = ".form-group:nth-child(2) .MuiInputBase-input.MuiInput-input"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.status_btns = ButtonElements(self.BTN_CSS)
        self.date_from = DatePicker(self.DATAPICKER_FROM_CSS)
        self.date_to = DatePicker(self.DATAPICKER_TO_CSS)

    def click_view(self, view_number):
        """
            Method for click on a needed view button.
        """
        element = self.driver.find_elements(By.CSS_SELECTOR, self.VIEW_BTN_CSS.format(view_number + 1))
        element.click()

    def click_issue_status_filter(self, issue_status):
        """
            Method for click on issue status checkbox depending on text value.
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.CHECK_CSS)
        for element in elements:
            if issue_status in element.text:
                element.click()
                return
