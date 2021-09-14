from selenium import webdriver
from selenium.webdriver.common.by import By


class ChatPage:
    """
        Locators and methods for Chat Page.
    """
    CHAT_SMALL_AVATAR_BTN_CLASS_NAME = "SmallAvatar"
    MESSAGE_TEXTAREA_CSS = "textarea"
    SEND_BTN_CSS = "button[type='submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_chat_small_avatar(self):
        """ Method for click small avatar on chat page."""
        element = self.driver.find_element(By.CLASS_NAME, self.CHAT_SMALL_AVATAR_BTN_CLASS_NAME)
        element.click()

    def click_textarea(self):
        """ Method for click on textarea 'Type your message...' """
        element = self.driver.find_element(By.CSS_SELECTOR, self.MESSAGE_TEXTAREA_CSS)
        element.click()

    def send_textarea(self, message):
        """ Method for type message in text area 'Type your message...' """
        element = self.driver.find_element(By.CSS_SELECTOR, self.MESSAGE_TEXTAREA_CSS)
        element.send_keys(message)

    def click_send_button(self):
        """ Method for click "Send" button """
        element = self.driver.find_element(By.CSS_SELECTOR, self.SEND_BTN_CSS)
        element.click()
