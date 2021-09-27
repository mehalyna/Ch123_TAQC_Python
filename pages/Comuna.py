from selenium import webdriver
from pages.elements.buttonElement import ButtonElement


class ComunaPage:
    """
        Locators and methods for Comuna page.
    """
    COMUNA_USER_ITEM_CSS = "div:nth-child({}) > a > div > div > h5"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.comuna_user_chat = ButtonElement(self.COMUNA_USER_ITEM_CSS)
