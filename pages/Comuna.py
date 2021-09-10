from selenium import webdriver
from selenium.webdriver.common.by import By


class ComunaPage:
    """
        Locators and methods for Comuna page.
    """
    NAV_MENU_COMUNA_XPATH = "//span[text() = 'Comuna']"
    COMUNA_USER_CSS = "div:nth-child({}) > a > div > div > h5"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_chat_comuna(self):
        element = self.driver.find_element(By.XPATH, self.NAV_MENU_COMUNA_XPATH)
        element.click()

    def click_chat_comuna_user(self, number):
        element = self.driver.find_element(By.CSS_SELECTOR, self.COMUNA_USER_CSS.format(number), number)
        element.click()
