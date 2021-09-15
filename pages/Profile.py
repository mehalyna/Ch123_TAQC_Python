from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ProfilePage:
    """Locators and methods for Profile Page."""
    EDIT_PROFILE_BTN_CSS = "a:nth-child(1) > button"
    """ Expansion panel Locators  """
    EXPANSION_PANEL_AVATAR_CHANGE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)"
    EXPANSION_PANEL_USERNAME_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)"
    EXPANSION_PANEL_GENDER_BTN_CSS = ".MuiExpansionPanel-root:nth-child(3)"
    EXPANSION_PANEL_DATE_OF_BIRTH_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)"
    EXPANSION_PANEL_FAVORITE_CATEGORIES_BTN_CSS = ".MuiExpansionPanel-root:nth-child(5)"
    EXPANSION_PANEL_MANAGE_NOTIFICATION_BTN_CSS = ".MuiExpansionPanel-root:nth-child(6)"
    EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS = ".MuiExpansionPanel-root:nth-child(7)"
    EXPANSION_PANEL_CHANGE_PASSWORD_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)"
    """Locators for action inside expansion panels manage notification """
    MANAGE_NOTIFICATION_SAVE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(6)  button[type = 'submit']"
    """Locators for action inside expansion panels Username"""
    USERNAME_INP_CSS = "input[name^='userName']"
    USERNAME_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)  button[type= 'button'] "
    USERNAME_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)  button[type= 'submit'] "
    """  Locators for action inside expansion panels Change Avatar  """
    CHANGE_AVATAR_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)  button[type= 'button']"
    CHANGE_AVATAR_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)  button[type= 'submit']"
    CHANGE_AVATAR_CROP_BTN_CSS = ".ImageResizer  button[type= 'button'] "
    CHANGE_AVATAR_UPLOAD_NEW_PICTURE = "#panel1bh-content > div > p > form > div:nth-child(1) > div > div > div"
    """Locators for action inside expansion panels Gender """
    GENDER_DROPDOWN_CSS = "#panel2bh-content > div > p > form > div:nth-child(1) > div"
    GENDER_OPT_CSS = "div > select"
    GENDER_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(3)  button[type= 'submit']"
    """ Locators for action inside expansion panels Date of Birth """
    DATE_OF_BIRTH_DATAPICKER_CSS = "input[type ='date']"
    DATE_OF_BIRTH_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)  button[type= 'button']"
    DATE_OF_BIRTH_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)  button[type= 'submit']"
    """ Locators for action inside expansion panels Favorite Categories"""
    FAVORITE_CATEGORIES_SELECT_CATEGORIES_FORM_CSS = "#panel4bh-content > div > p > div > form "
    """ Locators for action inside expansion panels Linked Accounts """
    LINKED_ACCOUNTS_GOOGLE_BTN_CSS = ".btnGoogle > i"
    LINKED_ACCOUNTS_MAIL_BTN_CSS = ".btnGoogle > svg"
    LINKED_ACCOUNTS_FACEBOOK_BTN_CSS = ".btnFacebook"
    """ Locators for action inside expansion panels Change Password """
    CHANGE_PASSWORD_CURRENT_PASSWORD_INP_CSS = "input[name^='oldPassword']"
    CHANGE_PASSWORD_NEW_PASSWORD_INP_CSS = "input[name^='newPassword']"
    CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP_CSS = "input[name^='repeatPassword']"
    CHANGE_PASSWORD_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)  button[type= 'button']"
    CHANGE_PASSWORD_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)  button[type= 'submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()


    def click_edit_your_profile_btn(self):
        """Opening edit profile page"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EDIT_PROFILE_BTN_CSS)
        element.click()

    def click_expansion_panel_change_avatar(self):
        """opening expansion panel change avatar"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_AVATAR_CHANGE_BTN_CSS)
        element.click()

    def click_expansion_panel_username(self):
        """opening expansion panel username """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_USERNAME_BTN_CSS)
        element.click()

    def click_expansion_panel_gender(self):
        """opening expansion panel gender"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_GENDER_BTN_CSS)
        element.click()

    def click_expansion_panel_date_of_birth(self):
        """opening expansion panel Date of birth"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_DATE_OF_BIRTH_BTN_CSS)
        element.click()

    def click_expansion_panel_favorite_categories(self):
        """opening expansion panel favorite categories"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_FAVORITE_CATEGORIES_BTN_CSS)
        element.click()

    def click_expansion_panel_manage_notification(self):
        """opening expansion panel manage notification"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_MANAGE_NOTIFICATION_BTN_CSS)
        element.click()

    def click_expansion_linked_accounts(self):
        """opening expansion Linked Accounts"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()

    def click_expansion_panel_change_password(self):
        """opening expansion change password"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_CHANGE_PASSWORD_BTN_CSS)
        element.click()

    def edit_existing_image(self):
        """
        Method for editing existing avatar image
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_AVATAR_CHANGE_BTN_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_AVATAR_CROP_BTN_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_AVATAR_SUBMIT_BTN_CSS)
        element.click()

    def change_username(self, new_name):
        """
        Method for changing username
        string new name of a user
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_USERNAME_BTN_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        element1 = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_INP_CSS)
        element1.send_keys(new_name)
        element2 = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_SUBMIT_BTN_CSS)
        element2.click()


    def click_username_clear_btn(self, name):
        """
        Method for clear field for input new username
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_USERNAME_BTN_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        element1 = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_INP_CSS)
        element1.send_keys(name)
        element = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_CLEAR_BTN_CSS)
        element.click()


    def changing_gender(self, opti):
        """
        Method for changing gender
        string param opti: Male, Female, other
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_GENDER_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_DROPDOWN_CSS)
        element.click()
        dropdown1 = Select(self.driver.find_element(By.CSS_SELECTOR, self.GENDER_OPT_CSS))
        dropdown1.select_by_visible_text(opti)
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_SUBMIT_BTN_CSS)
        element.click()

    def choose_favorite_categories(self):
        """
           Method for choosing_favorite_categories
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_FAVORITE_CATEGORIES_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.FAVORITE_CATEGORIES_SELECT_CATEGORIES_FORM_CSS)
        element.click()

    def change_password(self, current_password, new_password):
        """
           Method for changing password
           param current_password, new_password
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_CHANGE_PASSWORD_BTN_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_CURRENT_PASSWORD_INP_CSS)
        element.send_keys(current_password)
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_NEW_PASSWORD_INP_CSS)
        element.send_keys(new_password)
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP_CSS)
        element.send_keys(new_password)
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_SUBMIT_BTN_CSS)
        element.click()


    def change_password_clear_btn(self):
        """
         Method for clear all change password fields
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CHANGE_PASSWORD_CLEAR_BTN_CSS)
        element.click()

    def click_linked_account_google_btn(self):
        """connect google account to your profile"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.LINKED_ACCOUNTS_GOOGLE_BTN_CSS)
        element.click()

    def click_linked_account_facebook_btn(self):
        """connect facebook account to your profile"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.LINKED_ACCOUNTS_FACEBOOK_BTN_CSS)
        element.click()

    def click_linked_account_mail_btn(self):
        """connect mail to your profile"""
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.LINKED_ACCOUNTS_MAIL_BTN_CSS)
        element.click()

    def send_date_datepicker_to(self, day, month, year):
        """
            Method for send data in datepicker 'to'.
            Day, month, year - are integer values.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.DATE_OF_BIRTH_DATAPICKER_CSS)
        element.send_keys(year)
        element.send_keys(year)
        element.send_keys(year)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(month)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(day)




