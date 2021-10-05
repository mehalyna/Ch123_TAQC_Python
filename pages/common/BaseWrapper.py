from selenium.common.exceptions import NoSuchElementException
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common.Logger_config import LoggerConfig

mylogger = LoggerConfig(logger="BaseWrapper").getlog()
# LoggerConfig(logger="BaseWrapper").delete_log()

class BaseWrapper:

    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        self.driver = driver
        self.base_url = config.BASE_URL

    def find_element_by_css(self, locator, timeout=10):
        """
            Method for search element by css selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                                                      message=f"Can't find element by locator {locator}")
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            mylogger.info(f"Element located {locator} found successful")
            return element
        except TimeoutError:
            mylogger.error(f"Element located {locator} not found, timeout")
        except NoSuchElementException:
            mylogger.error(f"Element located {locator} not found")

    def find_element_by_xpath(self, locator, timeout=10):
        """
            Method for search element by xpath selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message=f"Can't find element by locator {locator}")
            element = self.driver.find_element(By.XPATH, locator)
            mylogger.info(f"Element located {locator} found successful")
            return element
        except TimeoutError:
            mylogger.error(f"Element located {locator} not found, timeout")
        except NoSuchElementException:
            mylogger.error(f"Element located {locator} not found")


    def find_elements(self, locator, timeout=10):
        """
            Method for search elements by css selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)),
                                                      message=f"Can't find elements by locator {locator}")
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator)
            mylogger.info(f"Elements located {locator} found successful")
            return elements
        except TimeoutError:
            mylogger.error(f"Elements located {locator} not found, timeout")
        except NoSuchElementException:
            mylogger.error(f"Element located {locator} not found")


    def find_elements_by_xpath(self, locator, timeout=10):
        """
            Method for search elements by xpath selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                      message=f"Can't find elements by locator {locator}")
            elements = self.driver.find_elements(By.XPATH, locator)
            mylogger.info(f"Elements located {locator} found successful")
            return elements
        except TimeoutError:
            mylogger.error(f"Elements located {locator} not found, timeout")
        except NoSuchElementException:
            mylogger.error(f"Elements located {locator} not  found")


    def go_to_site(self):
        """
            Method for go to the base_url
        """
        try:
            site = self.driver.get(config.BASE_URL)
            mylogger.info("Site downloaded")
            return site
        except TimeoutError:
            mylogger.error("Site downloading failed, timeout")

