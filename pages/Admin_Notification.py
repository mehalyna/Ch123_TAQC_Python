from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


TITLE_NOTIFICATION_FIELD_CSS = 'form > div:nth-child(1)'
SUBJECT_NOTIFICATION_FIELD_CSS = 'form > div:nth-child(2) > div > div > input'
MESSAGE_NOTIFICATION_FIELD_CSS = 'form > div:nth-child(3) > div > div > textarea'
USER_EMAIL_FIELD_NOTIFICATION_CSS = 'div > div > ul > li'
SAVE_BTN_NOTIFICATION_CSS = 'button.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary'
RESET_BTN_NOTIFICATION_CSS = 'button.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textSecondary.Mui-disabled.Mui'


class Notification:

    def __init__(self):
        self.driver = webdriver.Chrome('C:/WDriver/chromedriver.exe')
        self.driver.get('https://eventsexpress-test.azurewebsites.net/admin')

    def waiter(self):
        self.driver.implicitly_wait(10)

    def edit_notificaton_btn(self, notification_num):
        """method for clicking edit button"""
        self.driver.implicitly_wait(5)
        NOTIFICATION_BTN_CSS_SELECTOR = f'tr:nth-child({notification_num}) > td:nth-child(5) > a > button.text-info'
        self.driver.find_element(By.CSS_SELECTOR, NOTIFICATION_BTN_CSS_SELECTOR).click()

    def subject_clear_notification_field(self):
        """method for clearing subject field in specific notification"""
        self.driver.find_element(By.CSS_SELECTOR, SUBJECT_NOTIFICATION_FIELD_CSS).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.CSS_SELECTOR, SUBJECT_NOTIFICATION_FIELD_CSS).send_keys(Keys.BACKSPACE)

    def subject_notification_field(self, subject_text):
        """method for input text to subject notification button"""
        self.driver.find_element(By.CSS_SELECTOR, SUBJECT_NOTIFICATION_FIELD_CSS).send_keys(f'{subject_text}')

    def message_clear_notification_field(self):
        """method for clearing message field in specific notification"""
        self.driver.find_element(By.CSS_SELECTOR, MESSAGE_NOTIFICATION_FIELD_CSS).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.CSS_SELECTOR, MESSAGE_NOTIFICATION_FIELD_CSS).send_keys(Keys.BACKSPACE)

    def message_notification_field(self, message_text):
        """method for input message into message notification field"""
        self.driver.find_element(By.CSS_SELECTOR, MESSAGE_NOTIFICATION_FIELD_CSS).send_keys(f'{message_text}')

    def save_notification_btn(self):
        """method for clicking save button"""
        self.driver.find_element(By.CSS_SELECTOR, SAVE_BTN_NOTIFICATION_CSS).click()

    def reset_notification_btn(self):
        """method for clicking reset notification button"""
        self.driver.find_element(By.CSS_SELECTOR, RESET_BTN_NOTIFICATION_CSS).click()

    def email_copy_notification_btn(self):
        """method for clicking copy email button"""
        self.driver.find_element(By.CSS_SELECTOR, USER_EMAIL_FIELD_NOTIFICATION_CSS).click()
