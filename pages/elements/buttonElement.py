from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            Method for click on a needed button by xpath selector.
        """
        button = self.driver.find_element(By.XPATH, self.selector)
        button.click()

    def click_by_css_with_wait(self, wait_time=10):
        """
            Method for click on a needed button by css selector with wait.
        """
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(
            EC.element_to_be_clickable(By.CSS_SELECTOR)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def click_btn_by_index_css(self, index):
        """
        Method for click on a needed button by index and css selector.
        :param index: Variable index should contain number which we need to enter.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.selector.format(index)).click()
