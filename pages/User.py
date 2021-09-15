from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

PAGE_NUM_CSS = 'ul > div > div > button:nth-child({page_number})'
SEARCH_FIELD_CSS = 'div.MuiFormControl-root.MuiTextField-root.MuiFormControl-fullWidth > div > input'
ROLE_FIELD_CSS = "div.MuiFormControl-root.jss550 > div > select"
PAGESIZE_FIELD_CSS = 'div.MuiFormControl-root.jss567 > div > select'
BLOCKED_BTN_CSS = 'div:nth-child(6) > div > label:nth-child(1)'
ACTIVE_BTN_CSS = 'div:nth-child(6) > div > label:nth-child(2)'
ALL_BTN_CSS = 'div:nth-child(6) > div > label:nth-child(3)'
SEARCH_BTN_CSS = 'button > span.MuiButton-label'
USER_EDIT_CSS = 'tr:nth-child({user_index}) > td:nth-child(6) > button'
USER_BLOCK_CSS = 'tbody > tr:nth-child({user_index}) > td:nth-child(7) > div'
ADMIN = "Admin"
USER = "User"

class UsersPage:
    """
        Admin Users editing blocking and filtering.
    """
    def __init__(self):
        """
            Init method used for set up.
        """
        self.driver = webdriver.Chrome()

    def user_edit(self, user_index):
        """
            Method for clicking user edit button.
        """
        self.driver.find_element(By.CSS_SELECTOR, USER_EDIT_CSS.format(user_index)).click()

    def user_block(self, user_index):
        """
            Method for clicking user delete button.
        """
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, USER_BLOCK_CSS.format(user_index)).click()

    def user_search_field(self, need_user):
        """
            Method for searching user with search field.
        """
        self.driver.find_element(By.CSS_SELECTOR, SEARCH_FIELD_CSS).send_keys(need_user)

    def user_role_admin(self):
        """
            Method for declaring that we search user with role 'admin'.
        """
        select = Select(self.driver.find_element(By.CSS_SELECTOR, ROLE_FIELD_CSS))
        self.driver.implicitly_wait(5)
        select.select_by_value(ADMIN)

    def user_role_user(self):
        """
            Method for declaring that we search user with role 'user'.
        """
        select = Select(self.driver.find_element(By.CSS_SELECTOR, ROLE_FIELD_CSS))
        self.driver.implicitly_wait(5)
        select.select_by_value(USER)

    def user_page_size(self, page_size):
        """
            Method for displaying 5 or 10 or 15 numbers of user in one page.
        """
        select = Select(self.driver.find_element(By.CSS_SELECTOR, PAGESIZE_FIELD_CSS))
        self.driver.implicitly_wait(15)
        if int(page_size) == 5 or int(page_size) == 10 or int(page_size) == 15:
            select.select_by_value(page_size)
        else:
            print('error')

    def user_is_blocked(self):
        """
            Method for clicking on checkbox for checking if user is blocked.
        """
        self.driver.find_element(By.CSS_SELECTOR, BLOCKED_BTN_CSS).click()

    def user_is_active(self):
        """
            Method for clicking on checkbox for checking if user is active.
        """
        self.driver.find_element(By.CSS_SELECTOR, ACTIVE_BTN_CSS).click()

    def user_all(self):
        """
            Method for clicking on checkbox for displaying all user.
        """
        return self.driver.find_element(By.CSS_SELECTOR, ALL_BTN_CSS).click()

    def user_search(self):
        """
            Method for clicking search button.
        """
        return self.driver.find_element(By.CSS_SELECTOR, SEARCH_BTN_CSS).click()

    def user_page(self, page_number):
        """
            Method for clicking on specific page number.
        """
        self.driver.find_element(By.CSS_SELECTOR, PAGE_NUM_CSS.format(page_number)).click()
