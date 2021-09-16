from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TITLE_NOTIFICATION_FIELD_CSS = 'form > div:nth-child(1)'
SUBJECT_NOTIFICATION_FIELD_CSS = 'form > div:nth-child(2) > div > div > input'
MESSAGE_NOTIFICATION_FIELD_CSS = 'form > div:nth-child(3) > div > div > textarea'
USER_EMAIL_FIELD_NOTIFICATION_CSS = 'div > div > ul > li'
NOTIFICATION_BTN_CSS_SELECTOR = 'tr:nth-child({notification_num}) > td:nth-child(5) > a > button.text-info'
SAVE_RESET_BTNS_NOTIFICATION_CSS = 'div.align-self-end'

class NotificationPage:
    """
        Admin notification edit page.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()

    def edit_notification_btn(self, notification_num):
        """
            Method for clicking edit button.
        """
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, NOTIFICATION_BTN_CSS_SELECTOR.format(notification_num)).click()

    def subject_clear_notification_field(self):
        """
            Method for clearing subject field in specific notification.
        """
        self.driver.find_element(By.CSS_SELECTOR, SUBJECT_NOTIFICATION_FIELD_CSS).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.CSS_SELECTOR, SUBJECT_NOTIFICATION_FIELD_CSS).send_keys(Keys.BACKSPACE)

    def subject_notification_field(self, subject_text):
        """
            Method for input text to subject notification button.
        """
        self.driver.find_element(By.CSS_SELECTOR, SUBJECT_NOTIFICATION_FIELD_CSS).send_keys(f'{subject_text}')

    def message_clear_notification_field(self):
        """
            Method for clearing message field in specific notification.
        """
        self.driver.find_element(By.CSS_SELECTOR, MESSAGE_NOTIFICATION_FIELD_CSS).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.CSS_SELECTOR, MESSAGE_NOTIFICATION_FIELD_CSS).send_keys(Keys.BACKSPACE)

    def message_notification_field(self, message_text):
        """
            Method for input message into message notification field.
        """
        self.driver.find_element(By.CSS_SELECTOR, MESSAGE_NOTIFICATION_FIELD_CSS).send_keys(message_text)

    def save_reset_btns_track(self, btn_name):
        self.driver.find_element(By.CSS_SELECTOR, SAVE_RESET_BTNS_NOTIFICATION_CSS)
        if btn_name in element.text:
            element.click()
            return


    def email_copy_notification_btn(self):
        """
            Method for clicking copy email button.
        """
        self.driver.find_element(By.CSS_SELECTOR, USER_EMAIL_FIELD_NOTIFICATION_CSS).click()
