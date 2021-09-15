from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class ButtonElements(BasePage):
    """
        Class for click on Button by text button.
    """
    def __init__(self, selector):
        super().__init__()
        #self.driver = webdriver.Chrome()
        self.selector = selector

    def click_btn_by_name(self, btn_name):
        """
            Method for click on a needed button by text button and css selector.
        """
        elements = self.find_elements(self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return
