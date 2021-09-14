from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminAddCategoryPage():
    """
        Locators and methods for Admin Edit category page
    """

    """
        Locators for unique elements
    """
    index_of_row = 1
    ADD_CTG_BTN_CSS = "button.ml-0"
    ADD_CTG_INP_FIELD_CSS = f"#save-form > div > div > div > input"
    ADD_CTG_SUBMIT_BTN_CSS = "tr:nth-child(1) > td > div > button.text-success"
    ADD_CTG_CANCEL_BTN_CSS = "tr:nth-child(1) > td > div > button.text-danger"
    TABLE_OF_CTG_CSS = "table.table.w-100.m-auto"
    """
        Browser initialization method
    """
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Driver/chromedriver.exe')
        self.driver.get('https://eventsexpress-test.azurewebsites.net/admin')
    """
        Search for a category row by name
    """
    def find_category_by_name(self, category_name):
        category_table = self.driver.find_element(By.CSS_SELECTOR, self.TABLE_OF_CATEGORY_CSS)
        row_counter = 1
        for row in category_table.find_elements_by_css_selector('tr > td:nth-child(1)'):
            row_counter = row_counter + 1
            if row.text == category_name:
                self.index_of_row = row_counter
    """
        Category-dependent locators
    """
    EDIT_CTG_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-info"
    EDIT_CTG_NAME_INP_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(1) > form#save-form > input"
    SUBMIT_EDIT_CTG_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-success"
    CANCEL_EDIT_CTG_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-danger"
    DELETE_CTG_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(5) > button"
    NUMBER_OF_USERS_VALUE_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(2)"
    NUMBER_OF_EVENTS_VALUE_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(3)"
    """
        Methods of interaction with page elements
    """
    """
        Methods related to adding and confirming a new category or canceling its creation
    """
    """
        Method of creating new category with pressing button
    """
    def click_add_category_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.ADD_CTG_BTN_CSS)
        element.click()
    """
        Method of entering new category name
    """
    def input_new_category_name(self, new_category):
        element=self.driver.find_element(By.CSS_SELECTOR, self.ADD_CTG_INP_FIELD_CSS)
        element.send_keys(new_category)
    """
        Method of saving new category
    """
    def submit_new_category_name(self):
        element=self.driver.find_element(By.CSS_SELECTOR, self.ADD_CTG_SUBMIT_BTN_CSS)
        element.click()
    """
        Method of canceling new category
    """
    def cancel_new_category_name(self):
        element=self.driver.find_element(By.CSS_SELECTOR, self.ADD_CTG_CANCEL_BTN_CSS)
        element.click()
    """
        Editing existing category methods
    """
    """
        Method of clicking edit button for chosen category
    """
    def click_edit_category_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EDIT_CTG_BTN_CSS)
        element.click()
    """
        Method of editing existing name
    """
    def input_category_name(self, category):
        element = self.driver.find_element(By.CSS_SELECTOR, self.EDIT_CTG_NAME_INP_CSS)
        element.send_keys(category)
    """
        Method of confirmation changes
    """
    def click_submit_editing(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.SUBMIT_EDIT_CTG_BTN_CSS)
        element.click()
    """
        Method of canceling changes
    """
    def click_cancel_editing(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.CANCEL_EDIT_CTG_BTN_CSS)
        element.click()
    """
        Method of deleting existing category
    """
    def click_delete_category(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.DELETE_CTG_BTN_CSS)
        element.click()



