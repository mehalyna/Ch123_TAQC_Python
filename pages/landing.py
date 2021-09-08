from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class LandingPage:
    """
    locators for landing page
    """

    SIGN_IN_UP_BUTTON_CSS = ".MuiButton-label"
    FIND_EVENT_BUTTON_XPATH = "//a[contains(text(),'Find event')]"
    CREATE_EVENT_BUTTON_XPATH = "//button[contains(text(),'Create event')]"
    JOIN_EVENTEXPRESS_BUTTON_XPATH = "//button[contains(text(),'Join EventsExpress')]"
    LOG_OUT_BUTTON_XPATH = "//div[@class='btn']"

    SIGN_IN_UP_BUTTON = driver.find_element_by_css_selector(SIGN_IN_UP_BUTTON_CSS)

    def click_sign_up_button(self, SIGN_IN_UP_BUTTON_CSS):
        element = driver.find_element(By.CSS_SELECTOR, SIGN_IN_UP_BUTTON_CSS)
        element.click()

    def click_find_event_button(self, FIND_EVENT_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, FIND_EVENT_BUTTON_XPATH)
        element.click()

    def click_create_event(self, CREATE_EVENT_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, CREATE_EVENT_BUTTON_XPATH)
        element.click()

    def click_join_eventexpress(self, JOIN_EVENTEXPRESS_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, JOIN_EVENTEXPRESS_BUTTON_XPATH)
        element.click()

    def click_log_out(self, LOG_OUT_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, LOG_OUT_BUTTON_XPATH)
        element.click()