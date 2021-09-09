from selenium import webdriver
from selenium.webdriver.common.by import By


class IssuesPage:
    """
    Locators and methods for Issues page.
    """

    VIEW_BUTTON_CSS = "tr:nth-child({})  a > button"
    FROM_DATA_INPUT_CSS = "div:nth-child(1) > div > div > input"
    TO_DATA_INPUT_CSS = "div:nth-child(2) > div > div > input"
    CHECKBOX_OPEN_CSS = "input[name='status[0]']"
    CHECKBOX_IN_PROGRESS_CSS = "input[name='status[1]']"
    CHECKBOX_RESOLVE_CSS = "input[name='status[2]']"
    RESET_BUTTON_XPATH = "//span[contains(text(),'Reset')]"
    SEARCH_BUTTON_XPATH = "//span[contains(text(),'Search')]"

    def __init__(self):
        self.driver = webdriver.Chrome()

    """
    Method for click on a view button.
    Need write factical number + 1.
    """
    def click_view(self, number):
        element = self.driver.find_element(By.CSS_SELECTOR, self.VIEW_BUTTON_CSS.format(number), number)
        element.click()

    #def from_data_input(self, data):
        #element = self.driver.find_element(By.CSS_SELECTOR, self.FROM_DATA_INPUT_CSS)
        #element

    #def to_data_input(self, data):
        #element = self.driver.find_element(By.CSS_SELECTOR, self.TO_DATA_INPUT_CSS)
        #element

    def click_checkbox_open(self, number):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHECKBOX_OPEN_CSS)
        element.click()

    def click_checkbox_in_progress(self, number):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHECKBOX_IN_PROGRESS_CSS)
        element.click()

    def click_checkbox_resolve(self, number):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHECKBOX_RESOLVE_CSS)
        element.click()

    def click_reset_button(self):
        element = self.driver.find_element(By.XPATH, self.RESET_BUTTON_XPATH)
        element.click()

    def click_search_button(self):
        element = self.driver.find_element(By.XPATH, self.SEARCH_BUTTON_XPATH)
        element.click()
