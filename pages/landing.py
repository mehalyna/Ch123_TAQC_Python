from selenium import webdriver
from selenium.webdriver.common.by import By


class LandingPage:
    """
        Locators and methods for landing page.
    """

    SIGN_IN_UP_BTN_CSS = ".MuiButton-label"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_sign_up_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.SIGN_IN_UP_BTN_CSS)
        element.click()

    def click_find_event_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.FIND_EVENT_BTN_CSS)
        element.click()

    def click_create_event(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CREATE_EVENT_BTN_CSS)
        element.click()

    def click_join_eventexpress(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.JOIN_EVENTEXPRESS_BTN_CSS)
        element.click()

    def click_log_out(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.LOG_OUT_BTN_CSS)
        element.click()
