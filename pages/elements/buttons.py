from selenium import webdriver
from selenium.webdriver.common.by import By


class ButtonElements:
    """
        Class for click on Button by text button.
    """
    def __init__(self, selector):
        self.driver = webdriver.Chrome()
        self.selector = selector

    def click_btn_by_name(self, btn_name):
        """
            Method for click on a needed button by text button and css selector.
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return
