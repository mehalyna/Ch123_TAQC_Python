from selenium import webdriver
from selenium.webdriver.common.by import By


class InputElement:
    """
        Class for sending data to input field.
    """
    def __init__(self, selector):
        """
            Method for class fields declaration.
        """
        self.driver = webdriver.Chrome()
        self.selector = selector

    def send_data(self, string):
        """
        Method for sending data to input field.
        :param string: Variable string should contain text which we need to enter.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.selector).send_keys(string)

