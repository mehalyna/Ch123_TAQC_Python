from selenium import webdriver
from selenium.webdriver.common.by import By


class ButtonElement:
    """
        Class for click on Button by css selector.
    """
    def __init__(self, selector):
        self.driver = webdriver.Chrome()
        self.selector = selector

    def click_btn_by_css(self):
        """
            Method for click on a needed button by css selector.
        """
        button = self.driver.find_element(By.CSS_SELECTOR, self.selector)
        button.click()

    def click_btn_by_xpath(self):
        """
            Method for click on a needed button by css selector.
        """
        button = self.driver.find_element(By.XPATH, self.selector)
        button.click()
