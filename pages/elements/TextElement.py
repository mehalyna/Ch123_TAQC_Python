from pages.common.baseWrapper import BaseWrapper
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextElement(BaseWrapper):
    """
        Class for getting text of element
    """
    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def get_element_text_by_css(self, wait_time=10):
        """
            Method for getting text of element by CSS selector
        """
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.selector)))
        return self.find_element_by_css(self.selector).text

    def get_element_text_by_index(self, index, wait_time=10):
        """
            Method for getting text of element by index
        :index - index of element, which we need to enter
                into locator before getting text
        """
        element_selector = self.selector.format(index)
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
        return self.find_element_by_css(element_selector).text
