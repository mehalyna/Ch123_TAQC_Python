from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Profile:
    EDIT_PROFILE_BTN_CSS = "a:nth-child(1) > button"
    """
    Expansion panel Locators 
    """
    EXPANSION_PANEL_CHANGE_AVATAR_CSS = "#main > div > div:nth-child(1)"
    EXPANSION_PANEL_USERNAME_CSS = "#main > div > div:nth-child(2)"
    EXPANSION_PANEL_GENDER_CSS = "#main > div > div:nth-child(3)"
    EXPANSION_PANEL_DATE_OF_BIRTH_CSS = "#main > div > div:nth-child(4)"
    EXPANSION_PANEL_FAVORITE_CATEGORIES_CSS = "#main > div > div:nth-child(5)"
    EXPANSION_PANEL_MANAGE_NOTIFICATION_CSS = "#main > div > div:nth-child(6)"
    EXPANSION_PANEL_LINKED_ACCOUNTS_CSS = "#main > div > div:nth-child(7)"
    EXPANSION_PANEL_CHANGE_PASSWORD_CSS = "#main > div > div:nth-child(8)"

    """
    Locators for action inside expansion panels manage notification
    """
    MANAGE_NOTIFICATION_SAVE_BTN = "#panel5bh-content  button"
    """
    Locators for action inside expansion panels Username
    """
    USERNAME_INP = "input[name^='userName']"
    USERNAME_CLEAR_BTN = "#main > div > div:nth-child(2)  button[type= 'button'] "
    USERNAME_SUBMIT_BTN = "#main > div > div:nth-child(2)  button[type= 'submit'] "
    """  Locators for action inside expansion panels Change Avatar  """
    CHANGE_AVATAR_CLEAR_BTN = "#main > div > div:nth-child(1)  button[type= 'button']"
    CHANGE_AVATAR_SUBMIT_BTN = "#main > div > div:nth-child(1)  button[type= 'submit']"
    CHANGE_AVATAR_CROP_BTN = ".ImageResizer  button[type= 'button'] "
    """
    Locators for action inside expansion panels Gender
    """
    GENDER_DROPDOWN = "#panel2bh-content > div > p > form > div:nth-child(1) > div"
    GENDER_FEMALE_OPT = "select > option[value ='2']"
    GENDER_MALE_OPT = " select > option[value ='1']"
    GENDER_OTHER_OPT = " select > option[value ='3']"
    GENDER_SUBMIT_BTN = "#main > div > div:nth-child(3)  button[type= 'submit']"
    """
    Locators for action inside expansion panels Change Password
    """
    CHANGE_PASSWORD_CURRENT_PASSWORD_INP = "input[name^='oldPassword']"
    CHANGE_PASSWORD_NEW_PASSWORD_INP = "input[name^='newPassword']"
    CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP = "input[name^='repeatPassword']"
    CHANGE_PASSWORD_CLEAR_BTN = "#main > div > div:nth-child(8)  button[type= 'button']"
    CHANGE_PASSWORD_SUBMIT_BTN = "#main > div > div:nth-child(8)  button[type= 'submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://eventsexpress-test.azurewebsites.net/admin')

    def click_edit_your_profile_btn(self):
        '''Open edit profile page'''
        element = self.driver.find_element(By.CSS_SELECTOR, self.EDIT_PROFILE_BTN_CSS)
        element.click()

    def click_expansion_panel_change_avatar(self):
        '''opening expansion panel for change avatar'''
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_CHANGE_AVATAR_CSS)
        element.click()

    def click_expansion_panel_username(self):
        '''opening expansion panel for username avatar'''
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_USERNAME_CSS)
        element.click()

    def click_expansion_panel_gender(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_GENDER_CSS)
        element.click()

    def click_expansion_panel_date_of_birth(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_DATE_OF_BIRTH_CSS)
        element.click()

    def click_expansion_panel_favorite_categories(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_FAVORITE_CATEGORIES_CSS)
        element.click()

    def click_expansion_panel_manage_notification(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_MANAGE_NOTIFICATION_CSS)
        element.click()

    def click_expansion_linked_accounts(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_CSS)
        element.click()

    def click_expansion_panel_change_password(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_CHANGE_PASSWORD_CSS)
        element.click()

    def username_inp(self):
        '''input new username'''
        self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_INP).send_keys('amp')
        time.sleep(3)

    def click_username_clear_btn(self):
        '''clear field for input new username'''
        element = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_CLEAR_BTN)
        element.click()

    def click_username_submit_btn(self):
        '''submit new user name'''
        element = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_SUBMIT_BTN)
        element.click()

    def click_gender_dropdown(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_DROPDOWN)
        element.click()
        time.sleep(3)

    def click_gender_dropdown_female_option(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_FEMALE_OPT)
        element.click()

    def click_gender_dropdown_male_option(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_MALE_OPT)
        element.click()

    def click_gender_submit_btn(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_SUBMIT_BTN)
        element.click()

    def click_manage_notification_save(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.MANAGE_NOTIFICATION_SAVE_BTN)
        element.click()

    def change_password_current_password_inp(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_CURRENT_PASSWORD_INP).send_keys()

    def change_password_new_password_inp(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_NEW_PASSWORD_INP).send_keys()

    def change_password_repeat_new_password_inp(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP).send_keys()

    def change_password_clear_btn(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_CLEAR_BTN)
        element.click()


