from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


class NavigationPage:
    NAV_HOME_XPATH = "//span[text() = 'Home']"
    NAV_COMUNA_XPATH = "//span[text() = 'Comuna']"
    NAV_ADMIN_XPATH = "//span[text() = 'Admin']"
    NAV_ISSUES_XPATH = "//span[text() = 'Issues']"
    NAV_EDIT_PROFILE_CSS = ".svg-inline--fa.fa-cog.fa-w-16"
    NAV_LOGOUT_XPATH = "//a[@href='/home/events?page=1&radius=8']"

    def click_navigation_home(self, NAV_HOME_XPATH):
        element = driver.find_element(By.XPATH, NAV_HOME_XPATH)
        element.click()

    def click_navigation_comuna(self, NAV_COMUNA_XPATH):
        element = driver.find_element(By.XPATH, NAV_COMUNA_XPATH)
        element.click()

    def click_navigation_admin(self, NAV_ADMIN_XPATH):
        element = driver.find_element(By.XPATH, NAV_ADMIN_XPATH)
        element.click()

    def click_navigation_issues(self, NAV_ISSUES_XPATH):
        element = driver.find_element(By.XPATH, NAV_ISSUES_XPATH)
        element.click()

    def click_navigation_edit_profile(self, NAV_EDIT_PROFILE_CSS):
        element = driver.find_element(By.CSS_SELECTOR, NAV_EDIT_PROFILE_CSS)
        element.click()

    def click_log_out(self, NAV_LOGOUT_XPATH):
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.element_to_be_clickable(By.XPATH, NAV_LOGOUT_XPATH)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.click()
