from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminAddCategoryPage():
    """
        Locators and methods for Admin Edit category page
    """
    index_of_row = 0
    CTG_ADD_BTN_CSS = "button.ml-0"
    CTG_ADD_INP_FIELD_CSS = f"#save-form > div > div > div > input"
    CTG_ADD_SUBMIT_BTN_CSS = "tr:nth-child(1) > td > div > button.text-success"
    CTG_ADD_CANCEL_BTN_CSS = "tr:nth-child(1) > td > div > button.text-danger"
    TABLE_OF_CTG_CSS = "table.table.w-100.m-auto"
    CTG_EDIT_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-info"
    CTG_EDIT_NAME_INP_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(1) > form#save-form > input"
    CTG_SUBMIT_EDIT_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-success"
    CTG_CANCEL_EDIT_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-danger"
    CTG_DELETE_BTN_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(5) > button"
    NUMBER_OF_USERS_VALUE_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(2)"
    NUMBER_OF_EVENTS_VALUE_CSS = f"tr:nth-child({index_of_row}) > td:nth-child(3)"


    def __init__(self):
        self.driver = webdriver.Chrome('C:/Driver/chromedriver.exe')


    def find_category_by_name(self, category_name):
        """
                Search for a category row by name
        """
        category_table = self.driver.find_element(By.CSS_SELECTOR, self.TABLE_OF_CTG_CSS)
        row_counter = 1
        for row in category_table.find_elements_by_css_selector('tr > td:nth-child(1)'):
            row_counter = row_counter + 1
            if row.text == category_name:
                self.index_of_row = row_counter


    def click_add_category_button(self, locator_of_element):
        """
               Method of creating new category with pressing button
        """
        element = self.driver.find_element(By.CSS_SELECTOR, locator_of_element.format(self.index_of_row))
        element.click()

    def input_data_into_field(self, locator_of_element, data_for_input):
        """
              Method of entering new category name
        """
        element=self.driver.find_element(By.CSS_SELECTOR, locator_of_element.format(self.index_of_row))
        element.send_keys(data_for_input)




