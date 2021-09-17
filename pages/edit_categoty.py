from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminAddCategoryPage:
    """
        Locators and methods for Admin Edit category page
    """
    index_of_row = 0
    CTG_ADD_BTN_CSS = "button.ml-0"
    CTG_ADD_INP_FIELD_CSS = "#save-form > div > div > div > input"
    CTG_ADD_SUBMIT_BTN_CSS = "tr:nth-child(1) > td > div > button.text-success"
    CTG_ADD_CANCEL_BTN_CSS = "tr:nth-child(1) > td > div > button.text-danger"
    TABLE_OF_CTG_CSS = "table.table.w-100.m-auto"
    CTG_EDIT_BTN_CSS = "tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-info"
    CTG_EDIT_NAME_INP_CSS = "tr:nth-child({index_of_row}) > td:nth-child(1) > form#save-form > input"
    CTG_SUBMIT_EDIT_BTN_CSS = "tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-success"
    CTG_CANCEL_EDIT_BTN_CSS = "tr:nth-child({index_of_row}) > td:nth-child(4) > div > button.text-danger"
    CTG_DELETE_BTN_CSS = "tr:nth-child({index_of_row}) > td:nth-child(5) > button"
    NUMBER_OF_USERS_VALUE_CSS = "tr:nth-child({index_of_row}) > td:nth-child(2)"
    NUMBER_OF_EVENTS_VALUE_CSS = "tr:nth-child({index_of_row}) > td:nth-child(3)"
    COLUMN_OF_TABLE_CSS = "tbody > tr"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def find_category_by_name(self, category_name):
        """
            Search for a category row by name
        :param category_name: name of category which we want to find
        """
        for idx, row in enumerate(self.TABLE_OF_CTG_CSS):
            if row.text == category_name:
                self.index_of_row = idx

    def click_add_ctg_btn(self):
        """
               Method for creating new category with pressing button
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_ADD_BTN_CSS)
        element.click()

    def enter_ctg_name(self, data_for_input):
        """
              Method for entering new category name.
        :param data_for_input: Variable data_for_input should contain text which
              we need to enter (name of new category)
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_ADD_INP_FIELD_CSS)
        element.send_keys(data_for_input)

    def click_cancel_ctg_creating_btn(self):
        """
             Method for canceling of creating new category by pressing CANCEL button
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_ADD_CANCEL_BTN_CSS)
        element.click()

    def click_submit_ctg_creating_btn(self):
        """
            Method for pressing submit button to save new category
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_ADD_SUBMIT_BTN_CSS)
        element.click()

    def edit_ctg_name(self):
        """
            Method for pressing edit category button
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_EDIT_BTN_CSS.format(index_of_row = self.index_of_row))
        element.click()

    def inp_new_ctg_name(self, input_data):
        """
            Method for clearing input field and entering new name of category
        :param input_data: new name of category
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_EDIT_NAME_INP_CSS.format(index_of_row = self.index_of_row))
        element.clear()
        element.send_keys(input_data)

    def click_submit_ctg_edit_btn(self):
        """
           Method for saving change of category name
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_SUBMIT_EDIT_BTN_CSS.format(index_of_row = self.index_of_row))
        element.click()

    def click_cancel_ctg_edit_btn(self):
        """
            Method for canceling change of category name
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_CANCEL_EDIT_BTN_CSS.format(index_of_row=self.index_of_row))
        element.click()

    def click_delete_ctg_btn(self):
        """
            Method for deleting existing category
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_DELETE_BTN_CSS.format(index_of_row=self.index_of_row))
        element.click()

