from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.elements.datepickers import DatePicker
from pages.elements.buttonElement import ButtonElement


class ProfilePage:
    """
       Locators and methods for Profile Page.
    """
    EDIT_PROFILE_BTN_CSS = "a:nth-child(1) > button"
    #Expansion panel Locators
    EXPANSION_PANEL_CSS = '.MuiExpansionPanel-root:nth-child({})'
    EXPANSION_PANEL_AVATAR_CHANGE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)"
    EXPANSION_PANEL_USERNAME_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)"
    EXPANSION_PANEL_GENDER_BTN_CSS = ".MuiExpansionPanel-root:nth-child(3)"
    EXPANSION_PANEL_DATE_OF_BIRTH_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)"
    EXPANSION_PANEL_FAVORITE_CATEGORIES_BTN_CSS = ".MuiExpansionPanel-root:nth-child(5)"
    EXPANSION_PANEL_MANAGE_NOTIFICATION_BTN_CSS = ".MuiExpansionPanel-root:nth-child(6)"
    EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS = ".MuiExpansionPanel-root:nth-child(7)"
    EXPANSION_PANEL_CHANGE_PASSWORD_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)"
    #Locators for action inside expansion panels manage notification
    MANAGE_NOTIFICATION_SAVE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(6)  button[type = 'submit']"
    #Locators for action inside expansion panels Username
    USERNAME_INP_CSS = "input[name^='userName']"
    USERNAME_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)  button[type= 'button'] "
    USERNAME_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(2)  button[type= 'submit'] "
    #Locators for action inside expansion panels Change Avatar
    CHANGE_AVATAR_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)  button[type= 'button']"
    CHANGE_AVATAR_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(1)  button[type= 'submit']"
    CHANGE_AVATAR_CROP_BTN_CSS = ".ImageResizer  button[type= 'button'] "
    CHANGE_AVATAR_UPLOAD_NEW_PICTURE = "#panel1bh-content > div > p > form > div:nth-child(1) > div > div > div"
    #Locators for action inside expansion panels Gender
    GENDER_DROPDOWN_CSS = ".MuiExpansionPanel-root:nth-child(3)  form > div:nth-child(1) > div"
    GENDER_OPT_CSS = "div > select"
    GENDER_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(3)  button[type= 'submit']"
    #Locators for action inside expansion panels Date of Birth
    DATE_OF_BIRTH_DATAPICKER_CSS = "input[type ='date']"
    DATE_OF_BIRTH_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)  button[type= 'button']"
    DATE_OF_BIRTH_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(4)  button[type= 'submit']"
    #Locators for action inside expansion panels Favorite Categories
    FAVORITE_CATEGORIES_SELECT_CATEGORIES_FORM_CSS = ".MuiExpansionPanel-root:nth-child(5)  form"
    FAVORITE_CATEGORIES_CATEGORIES_LIST = "#rw_1_listbox li"
    FAVORITE_CATEGORIES_SAVE_BTN_CSS = ".MuiExpansionPanel-root:nth-child(5)  button[type= 'submit']"
    #Locators for action inside expansion panels Linked Accounts
    LINKED_ACCOUNTS_GOOGLE_BTN_CSS = ".btnGoogle > i"
    LINKED_ACCOUNTS_MAIL_BTN_CSS = ".btnGoogle > svg"
    LINKED_ACCOUNTS_FACEBOOK_BTN_CSS = ".btnFacebook"
    #Locators for action inside expansion panels Change Password
    CHANGE_PASSWORD_CURRENT_PASSWORD_INP_CSS = "input[name^='oldPassword']"
    CHANGE_PASSWORD_NEW_PASSWORD_INP_CSS = "input[name^='newPassword']"
    CHANGE_PASSWORD_REPEAT_NEW_PASSWORD_INP_CSS = "input[name^='repeatPassword']"
    CHANGE_PASSWORD_CLEAR_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)  button[type= 'button']"
    CHANGE_PASSWORD_SUBMIT_BTN_CSS = ".MuiExpansionPanel-root:nth-child(8)  button[type= 'submit']"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.expansion_panel_date_of_birth_dtp = DatePicker(self.DATE_OF_BIRTH_DATAPICKER_CSS)
        self.username_clear_btn = ButtonElement(self.USERNAME_CLEAR_BTN_CSS)
        self.username_submit_btn = ButtonElement(self.USERNAME_SUBMIT_BTN_CSS)
        self.favorite_categories_save_btn = ButtonElement(self.FAVORITE_CATEGORIES_SAVE_BTN_CSS)
        self.password_submit_btn = ButtonElement(self.CHANGE_PASSWORD_SUBMIT_BTN_CSS)
        self.password_clear_btn = ButtonElement(self.CHANGE_PASSWORD_CLEAR_BTN_CSS)
        self.date_of_birth_clear_btn = ButtonElement(self.DATE_OF_BIRTH_CLEAR_BTN_CSS)
        self.date_of_birth_submit_btn = ButtonElement(self.DATE_OF_BIRTH_SUBMIT_BTN_CSS)

    def click_edit_your_profile_btn(self):
        """
            Method for opening edit profile page
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EDIT_PROFILE_BTN_CSS)
        element.click()

    def click_expansion_panel(self, expansion_panel_number):
        """
            Method for click on a needed expansion panel button
            int expansion_panel_number:
            1 = Change Avatar
            2 = Username
            3 = Gender
            4 = Date of Birth
            5 = Favorite Categories
            6 = Manage Notification
            7 = Linked Accounts
            8 = Change password
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_CSS.format(expansion_panel_number))
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


    def input_new_username(self, new_name):
        """
            Method to input new username
            string new name of a user
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_USERNAME_BTN_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        element1 = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_INP_CSS)
        element1.send_keys(new_name)


    def change_gender_option(self, option):
        """
           Method for changing gender
           string param opti: Male, Female, other
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_GENDER_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_DROPDOWN_CSS)
        element.click()
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, self.GENDER_OPT_CSS))
        dropdown.select_by_visible_text(option)
        element = self.driver.find_element(By.CSS_SELECTOR, self.GENDER_SUBMIT_BTN_CSS)
        element.click()

    def choose_favorite_categories(self, categories):
        """
           Method for choosing favorite categories
           string categories : Fishing, Football, Gaming, Golf, Meeting, Mount, Sea, Sport, Summer
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_FAVORITE_CATEGORIES_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.FAVORITE_CATEGORIES_SELECT_CATEGORIES_FORM_CSS)
        element.click()
        self.driver.implicitly_wait(10)
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.FAVORITE_CATEGORIES_CATEGORIES_LIST)
        self.driver.implicitly_wait(10)
        for el in elements:
            if el.text == categories:
                self.driver.implicitly_wait(10)
                el.click()

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

    def click_linked_account_google_btn(self):
        """
           Method to connect google account to your profile
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.LINKED_ACCOUNTS_GOOGLE_BTN_CSS)
        element.click()

    def click_linked_account_facebook_btn(self):
        """
           Method to connect facebook account to your profile
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.LINKED_ACCOUNTS_FACEBOOK_BTN_CSS)
        element.click()

    def click_linked_account_mail_btn(self):
        """
           Method to connect mail to your profile
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.EXPANSION_PANEL_LINKED_ACCOUNTS_BTN_CSS)
        element.click()
        element = self.driver.find_element(By.CSS_SELECTOR, self.LINKED_ACCOUNTS_MAIL_BTN_CSS)
        element.click()




