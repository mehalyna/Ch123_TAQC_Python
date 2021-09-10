from selenium import webdriver
from selenium.webdriver.common.by import By


class ChatPage:
    """
        Locators and methods for Chat Page.
    """
    CHAT_SMALL_AVATAR_CLASS_NAME = "SmallAvatar"
    MESSAGE_TEXTAREA_XPATH = "//div/textarea"
    SEND_BUTTON_XPATH = "//button[@type='submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_chat_small_avatar(self):
        element = self.driver.find_element(By.CLASS_NAME, self.CHAT_SMALL_AVATAR)
        element.click()

    def click_textarea(self):
        element = self.driver.find_element(By.XPATH, self.MESSAGE_TEXTAREA_XPATH)
        element.click()

    def send_textarea(self, message):
        element = self.driver.find_element(By.XPATH, self.MESSAGE_TEXTAREA_XPATH)
        element.send_keys(message)

    def click_send_button(self):
        element = self.driver.find_element(By.XPATH, self.SEND_BUTTON_XPATH)
        element.click()
