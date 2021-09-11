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

    def click_view(self, number):
        """
            Method for click on a needed view button.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.VIEW_BTN_CSS.format(number + 1), number)
        element.click()

    """
        There should be a code for entering the date in the datepicker but I cannot fill it with data.
        Please, help me...
    """

    def click_checkbox(self, key):
        if key.lower() == "open":
            element = self.driver.find_element(By.CSS_SELECTOR, self.CHECK_CSS.format('0'))
            element.click()
        elif key.lower() == "in progress":
            element = self.driver.find_element(By.CSS_SELECTOR, self.CHECK_CSS.format('1'))
            element.click()
        elif key.lower() == "resolve":
            element = self.driver.find_element(By.CSS_SELECTOR, self.CHECK_CSS.format('2'))
            element.click()
        else:
            return "checkbox not find"

    def click_reset_button(self):
        element = self.driver.find_element(By.XPATH, self.RESET_BTN_XPATH)
        element.click()

    def click_search_button(self):
        element = self.driver.find_element(By.XPATH, self.SEARCH_BTN_XPATH)
        element.click()

