from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminAddCategoryPage:
    """
        Locators and methods for Admin Edit category page
    """
    index_of_row = 0
    CTG_ADD_BTN_CSS = ".ml-0"
    CTG_INP_FIELD_CSS = "#save-form"
    CTG_SUBMIT_BTN_CSS = ".text-success"
    CTG_CANCEL_BTN_CSS = ".text-danger"
    CTG_EDIT_BTN_CSS = ".text-info"
    CTG_DELETE_BTN = "td:nth-child(5) button.text-danger"
    NUMBER_OF_USERS_VALUE_CSS = "td:nth-child(2)"
    NUMBER_OF_EVENTS_VALUE_CSS = "td:nth-child(3)"
    COLUMN_OF_TABLE_CSS = "tr > td:nth-child(1):not(td.align-middle)"
    CTG_ROW = "tr:nth-child({})"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def find_category_by_name(self, category_name, wait_time=10):
        """
            Search for a category row by name
        :param category_name: name of category which we want to find
        :return row index of category
        """
        elements = self.driver.find_elements_by_css_selector(self.COLUMN_OF_TABLE_CSS)
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.COLUMN_OF_TABLE_CSS)))
        for idx, element in enumerate(elements):
            if element.text == category_name:
                self.index_of_row = idx + 1
                return idx + 1

    def get_row(self):
        return self.driver.find_element_by_css_selector(self.CTG_ROW.format(self.index_of_row))

    def click_add_ctg_btn(self):
        """
            Method for pressing add category button
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_ADD_BTN_CSS)
        element.click()

    def click_submit_btn(self):
        """
            Method for pressing submit button
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_SUBMIT_BTN_CSS)
        element.click()

    def click_cancel_btn(self):
        """
            Method for pressing cansel button in some row
        """
        row = self.get_row()
        row.find_element(By.CSS_SELECTOR, self.CTG_SUBMIT_BTN_CSS).click()

    def input_data(self, string):
        """
            Method for entering some string into input field
        :param string: data, that we need to input
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.CTG_INP_FIELD_CSS)
        element.send_keys(string)

    def click_edit_ctg_btn(self):
        """
            Method for pressing edit category button
        """
        row = self.get_row()
        row.find_element(By.CSS_SELECTOR, self.CTG_EDIT_BTN_CSS).click()

    def click_delete_ctg_btn(self):
        """
            Method for pressing delete category button
        """
        row = self.get_row()
        row.find_element(By.CSS_SELECTOR, self.CTG_DELETE_BTN).click()




