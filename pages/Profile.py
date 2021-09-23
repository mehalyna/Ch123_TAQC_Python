from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.elements.datepickers import DatePicker
from pages.elements.buttonElement import ButtonElement
from pages.elements.buttons import ButtonElements
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProfilePage:
    """
       Locators and methods for Profile Page.
    """
    EDIT_PROFILE_BTN_CSS = "a:nth-child(1) > button"
    # Expansion panel Locators
    EXPANSION_PANEL_ALL_BTN_CSS = '.MuiExpansionPanelSummary-content > p:nth-child(1)'
    # Locators for action inside expansion panels manage notification
    MANAGE_NOTIFICATION_SAVE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(6)  button[type = 'submit']"
    # Locators for action inside expansion panels Username
    USERNAME_INP_CSS = "input[name^='userName']"
    USERNAME_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)  button[type= 'button'] "
    USERNAME_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)  button[type= 'submit'] "
    # Locators for action inside expansion panels Change Avatar
    CHANGE_AVATAR_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)  button[type= 'button']"
    CHANGE_AVATAR_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)  button[type= 'submit']"
    CHANGE_AVATAR_CROP_BTN_CSS = ".ImageResizer  button[type= 'button'] "
    CHANGE_AVATAR_UPLOAD_NEW_PICTURE = "#panel1bh-content > div > p > form > div:nth-child(1) > div > div > div"
    # Locators for action inside expansion panels Gender
    GENDER_DROPDOWN_CSS = ".MuiExpansionPanel-root:nth-child(3)  form > div:nth-child(1) > div"
    GENDER_OPT_CSS = "div > select"
    GENDER_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(3)  button[type= 'submit']"
    # Locators for action inside expansion panels Date of Birth
    DATE_OF_BIRTH_DATAPICKER_CSS = "input[type ='date']"
    DATE_OF_BIRTH_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)  button[type= 'button']"
    DATE_OF_BIRTH_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)  button[type= 'submit']"
    # Locators for action inside expansion panels Favorite Categories
    FAVORITE_CATEGORIES_SELECT_CATEGORIES_FORM_CSS = ".MuiExpansionPanel-root:nth-child(5) input "
    FAVORITE_CATEGORIES_CATEGORIES_LIST = "#rw_1_listbox li"
    FAVORITE_CATEGORIES_SAVE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(5)  button[type= 'submit']"
    # Locators for action inside expansion panels Linked Accounts
    LINKED_ACCOUNTS_GOOGLE_BTN_CSS = ".btnGoogle > i"
    LINKED_ACCOUNTS_MAIL_BTN_CSS = ".btnGoogle > svg"
    LINKED_ACCOUNTS_FACEBOOK_BTN_CSS = ".btnFacebook"
    # Locators for action inside expansion panels Change Password
    CHANGE_PASSWORD_CURRENT_PASSWORD_INP_CSS = "input[name^='oldPassword']"
    CHANGE_PASSWORD_NEW_PASSWORD_INP_CSS = "input[name^='newPassword']"
    CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP_CSS = "input[name^='repeatPassword']"
    CHANGE_PASSWORD_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)  button[type= 'button']"
    CHANGE_PASSWORD_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)  button[type= 'submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.expansion_panel_by_name_btn = ButtonElements(self.EXPANSION_PANEL_ALL_BTN_CSS)
        self.change_avatar_submit_btn = ButtonElement(self.CHANGE_AVATAR_SUBMIT_BTN_CSS)
        self.change_avatar_crop_btn = ButtonElement(self.CHANGE_AVATAR_CROP_BTN_CSS)
        self.change_avatar_clear_btn = ButtonElement(self.CHANGE_AVATAR_CLEAR_BTN_CSS)
        self.change_avatar_upload_new_picture_btn = ButtonElement(self.CHANGE_AVATAR_UPLOAD_NEW_PICTURE)
        self.expansion_panel_date_of_birth_dtp = DatePicker(self.DATE_OF_BIRTH_DATAPICKER_CSS)
        self.username_clear_btn = ButtonElement(self.USERNAME_CLEAR_BTN_CSS)
        self.username_submit_btn = ButtonElement(self.USERNAME_SUBMIT_BTN_CSS)
        self.gender_submit_btn = ButtonElement(self.GENDER_SUBMIT_BTN_CSS)
        self.favorite_categories_save_btn = ButtonElement(self.FAVORITE_CATEGORIES_SAVE_BTN_CSS)
        self.password_submit_btn = ButtonElement(self.CHANGE_PASSWORD_SUBMIT_BTN_CSS)
        self.password_clear_btn = ButtonElement(self.CHANGE_PASSWORD_CLEAR_BTN_CSS)
        self.date_of_birth_clear_btn = ButtonElement(self.DATE_OF_BIRTH_CLEAR_BTN_CSS)
        self.date_of_birth_submit_btn = ButtonElement(self.DATE_OF_BIRTH_SUBMIT_BTN_CSS)
        self.linked_account_google_btn = ButtonElement(self.LINKED_ACCOUNTS_GOOGLE_BTN_CSS)
        self.linked_account_facebook_btn = ButtonElement(self.LINKED_ACCOUNTS_FACEBOOK_BTN_CSS)
        self.linked_account_mail_btn = ButtonElement(self.LINKED_ACCOUNTS_MAIL_BTN_CSS)




    def input_new_username(self, new_name, wait_time = 10):
        """
            Method to input new username
            string new name of a user
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.USERNAME_INP_CSS)))
        element.send_keys(new_name)

    def change_gender_option(self, option):
        """
           Method for changing gender
           string param opti: Male, Female, other
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_DROPDOWN_CSS)
        element.click()
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, self.GENDER_OPT_CSS))
        dropdown.select_by_visible_text(option)


    def choose_favorite_categories(self, wait_time = 10, *categories):
        """
           Method for choosing favorite categories
           string categories : Fishing, Football, Gaming, Golf, Meeting, Mount, Sea, Sport, Summer
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.FAVORITE_CATEGORIES_SELECT_CATEGORIES_FORM_CSS)))
        element.click()
        elements = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.FAVORITE_CATEGORIES_CATEGORIES_LIST)))
        for el in elements:
            if el.text in categories:
                el.click()
                return

    def change_password(self, current_password, new_password, wait_time=10):
        """
           Method for changing password
           param current_password, new_password
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.CHANGE_PASSWORD_CURRENT_PASSWORD_INP_CSS)))
        element.send_keys(current_password)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_NEW_PASSWORD_INP_CSS)
        element.send_keys(new_password)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP_CSS)
        element.send_keys(new_password)


