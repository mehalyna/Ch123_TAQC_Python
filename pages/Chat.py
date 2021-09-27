from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.elements.InputElement import InputElement
from pages.elements.buttonElement import ButtonElement


class ChatPage:
    """
        Locators and methods for Chat Page.
    """
    CHAT_SMALL_AVATAR_BTN_CSS = ".SmallAvatar"
    MESSAGE_TEXTAREA_CSS = "textarea"
    SEND_BTN_CSS = "button[type='submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.small_avatar_btn = ButtonElement(self.CHAT_SMALL_AVATAR_BTN_CSS)
        self.send_message = InputElement(self.MESSAGE_TEXTAREA_CSS)
        self.click_send_btn = ButtonElement(self.SEND_BTN_CSS)

    def click_textarea(self):
        """
            Method for click on textarea 'Type your message...'
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.MESSAGE_TEXTAREA_CSS)
        element.click()
