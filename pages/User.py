from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


PAGE_NUM_CSS = 'ul > div > div > button:nth-child({})'
SEARCH_FIELD_CSS = '.MuiFormControl-root.MuiTextField-root.MuiFormControl-fullWidth > div > input'
ROLE_FIELD_CSS = ".MuiFormControl-root.jss550 > div > select"
PAGESIZE_FIELD_CSS = '.MuiFormControl-root.jss567 > div > select'
SEARCH_BTN_CSS = 'button > span.MuiButton-label'
USER_STATUS_BOX_CSS = 'div:nth-child(6)'
USER_EDIT_CSS = 'tr:nth-child({}) > td:nth-child(6) > button'
USER_BLOCK_CSS = 'tbody > tr:nth-child({}) > td:nth-child(7) > div'


class UsersPage:
    """
        Admin Users editing blocking and filtering.
    """

    def __init__(self):
        self.driver = webdriver.Chrome()

    def user_edit_click(self, user_index):
        """
            Method for clicking user edit button.
        """
        self.driver.find_element(By.CSS_SELECTOR, USER_EDIT_CSS.format(user_index)).click()

    def user_block_click(self, user_index):
        """
            Method for clicking user delete button for user with user_index number.
        """
        self.driver.find_element(By.CSS_SELECTOR, USER_BLOCK_CSS.format(user_index)).click()

    def user_search_field(self, user_name):
        """
            Method for searching user with search field.
        """
        self.driver.find_element(By.CSS_SELECTOR, SEARCH_FIELD_CSS).send_keys(user_name)

    def choose_user_role(self, status):
        """
            Method for declaring that we search user with role
                'Admin'
                'User'.
        """
        select = Select(self.driver.find_element(By.CSS_SELECTOR, ROLE_FIELD_CSS))
        if status in element.text:
            select.select_by_value(status)
            return

    def choose_page_size(self, page_size):
        """
            Method for displaying numbers of user in one page.
                Available input:
                "5" , "10" , "15"
        """
        elements = Select(self.driver.find_elements(By.CSS_SELECTOR, PAGESIZE_FIELD_CSS))
        for element in elements:
            if page_size in element.text:
                elements.select_by_value(page_size)
                return

    def choose_user_status(self, status):
        """
            Method for choosing check-box on page user
                Status available commands:
                    'Active' to choose all active users
                    'Blocked' to choose all blocked users
                    'All' to choose all users
        """
        elements = Select(self.driver.find_elements(By.CSS_SELECTOR, USER_STATUS_BOX_CSS))
        for element in elements:
            if status in element.text:
                elements.select_by_value(status)
                return

    def user_search(self):
        """
            Method for clicking search button.
        """
        self.driver.find_element(By.CSS_SELECTOR, SEARCH_BTN_CSS).click()

    def choose_user_page(self, page_number):
        """
            Method for clicking on specific page number.
            Input page_number for click specific number of page
        """
        self.driver.find_element(By.CSS_SELECTOR, PAGE_NUM_CSS.format(page_number)).click()
