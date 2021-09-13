from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC


class NavigationPage:
    """
        Locators and methods for navigation menu.
    """
    NAV_PAGE_TITLE_CSS = "span.nav-item-text"
    NAV_EDIT_PROFILE_CSS = "a:nth-child(1) > button"
    NAV_LOGOUT_CSS = "a:nth-child(2) > button"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def go_to_page(self, page_title):
        """
            Method for click on page depending on page_title value.
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.NAV_PAGE_TITLE_CSS)
        for element in elements:
            if page_title == element.text:
                element.click()
                return

    def click_navigation_edit_profile(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.NAV_EDIT_PROFILE_CSS)
        element.click()

    def click_log_out(self, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(
            EC.element_to_be_clickable(By.CSS_SELECTOR, self.NAV_LOGOUT_CSS)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
