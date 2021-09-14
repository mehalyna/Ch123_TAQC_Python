from selenium import webdriver
from selenium.webdriver.common.by import By


class ComunaPage:
    """
        Locators and methods for Comuna page.
    """
    COMUNA_NAV_MENU_ITEM_CSS = "li:nth-child(2) > a > span > span.nav-item-text"
    COMUNA_USER_ITEM_CSS = "div:nth-child({}) > a > div > div > h5"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_chat_comuna(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.COMUNA_NAV_MENU_ITEM_CSS)
        element.click()

    def click_comuna_user_chat(self, number):
        element = self.driver.find_element(By.CSS_SELECTOR, self.COMUNA_USER_ITEM_CSS.format(number))
        element.click()
