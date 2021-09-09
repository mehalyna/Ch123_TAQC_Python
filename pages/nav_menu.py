from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class NavigationPage:
    """
        Locators and methods for navigation menu.
    """
    NAV_HOME_XPATH = "//span[text() = 'Home']"
    NAV_COMUNA_XPATH = "//span[text() = 'Comuna']"
    NAV_ADMIN_XPATH = "//span[text() = 'Admin']"
    NAV_ISSUES_XPATH = "//span[text() = 'Issues']"
    NAV_EDIT_PROFILE_CSS = ".svg-inline--fa.fa-cog.fa-w-16"
    NAV_LOGOUT_XPATH = "//a[@href='/home/events?page=1&radius=8']"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_navigation_home(self):
        element = self.driver.find_element(By.XPATH, self.NAV_HOME_XPATH)
        element.click()

    def click_navigation_comuna(self):
        element = self.driver.find_element(By.XPATH, self.NAV_COMUNA_XPATH)
        element.click()

    def click_navigation_admin(self):
        element = self.driver.find_element(By.XPATH, self.NAV_ADMIN_XPATH)
        element.click()

    def click_navigation_issues(self):
        element = self.driver.find_element(By.XPATH, self.NAV_ISSUES_XPATH)
        element.click()

    def click_navigation_edit_profile(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.NAV_EDIT_PROFILE_CSS)
        element.click()

    def click_log_out(self, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(
            EC.element_to_be_clickable(By.XPATH, self.NAV_LOGOUT_XPATH)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
