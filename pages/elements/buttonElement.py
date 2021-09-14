from selenium import webdriver
from selenium.webdriver.common.by import By


class ButtonElements:
    """
        Class for click on Button by css selector.
    """
    def __init__(self, selector):
        self.driver = webdriver.Chrome()
        self.css_selector = selector

    def click_btn(self, selector):
        """
            Method for click on a needed button by css selector.
        """
        button = self.driver.find_element(By.CSS_SELECTOR, selector)
        button.click()
