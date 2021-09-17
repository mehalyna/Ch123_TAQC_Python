from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseContext:
    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        self.driver = driver

    def find_element_by_css(self, locator, time=10):
        """
            Method for search element by css selector with wait
        """
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                                               message=f"Can't find element by locator {locator}")
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def find_element_by_xpath(self, locator, time=10):
        """
            Method for search element by xpath selector with wait
        """
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locator)),
                                               message=f"Can't find element by locator {locator}")
        return self.driver.find_element(By.XPATH, locator)

    def find_elements(self, locator, time=10):
        """
            Method for search elements by css selector with wait
        """
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)),
                                               message=f"Can't find elements by locator {locator}")
        return self.driver.find_elements(By.CSS_SELECTOR, locator)
