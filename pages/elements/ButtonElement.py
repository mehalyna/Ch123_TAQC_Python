from pages.common.baseContext import BaseContext
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonElement(BaseContext):
    """
        Class for click on Button by xpath and css selector.
    """
    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def click_btn_by_css(self):
        """
            Method for click on a needed button by css selector.
        """
        button = self.find_element_by_css(self.selector)
        button.click()

    def click_btn_by_xpath(self):
        """
            Method for click on a needed button by xpath selector.
        """
        button = self.find_element_by_xpath(self.selector)
        button.click()

    def hover_and_click_by_css(self, wait_time=10):
        """
            Method for click on a needed button by css selector with hover over the item and wait.
        """
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(
            EC.element_to_be_clickable(By.CSS_SELECTOR, self.selector)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
