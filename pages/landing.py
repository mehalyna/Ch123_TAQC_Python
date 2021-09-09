from selenium import webdriver
from selenium.webdriver.common.by import By


class LandingPage:
    """
    Locators and methods for landing page.
    """

    SIGN_IN_UP_BUTTON_CSS = ".MuiButton-label"
    FIND_EVENT_BUTTON_XPATH = "//a[contains(text(),'Find event')]"
    CREATE_EVENT_BUTTON_XPATH = "//button[contains(text(),'Create event')]"
    JOIN_EVENTEXPRESS_BUTTON_XPATH = "//button[contains(text(),'Join EventsExpress')]"
    LOG_OUT_BUTTON_XPATH = "//div[@class='btn']"

    """Methods"""
    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_sign_up_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.SIGN_IN_UP_BUTTON_CSS)
        element.click()

    def click_find_event_button(self):
        element = self.driver.find_element(By.XPATH, self.FIND_EVENT_BUTTON_XPATH)
        element.click()

    def click_create_event(self):
        element = self.driver.find_element(By.XPATH, self.CREATE_EVENT_BUTTON_XPATH)
        element.click()

    def click_join_eventexpress(self):
        element = self.driver.find_element(By.XPATH, self.JOIN_EVENTEXPRESS_BUTTON_XPATH)
        element.click()

    def click_log_out(self):
        element = self.driver.find_element(By.XPATH, self.LOG_OUT_BUTTON_XPATH)
        element.click()
