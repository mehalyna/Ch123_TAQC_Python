from pages.common.BaseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement
from pages.elements.InputElement import InputElement
from pages.elements.TableElement import TableElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AdminAddCategoryPage(BaseWrapper):
    """
        Locators and methods for Admin Edit category page
    """
    CTG_ROW = "tr:nth-child({})"
    CTG_NAME_CSS = f"{CTG_ROW} td:nth-child(1)"
    CTG_ADD_BTN_CSS = ".ml-0"
    CTG_INP_FIELD_CSS = ".MuiInputBase-input.MuiInput-input"
    CTG_SUBMIT_BTN_CSS = ".text-success"
    CTG_CANCEL_BTN_CSS = f"{CTG_ROW} .text-danger"
    CTG_EDIT_BTN_CSS = f"{CTG_ROW} .text-info"
    CTG_DELETE_BTN = f"{CTG_ROW} td:nth-child(5) button.text-danger"
    NUMBER_OF_USERS_VALUE_CSS = f"{CTG_ROW} td:nth-child(2)"
    NUMBER_OF_EVENTS_VALUE_CSS = f"{CTG_ROW} td:nth-child(3)"
    COLUMN_OF_TABLE_CSS = "tr > td:nth-child(1):not(td.align-middle)"

    def __init__(self, driver):
        super().__init__(driver)
        self.add_ctg_btn = ButtonElement(self.CTG_ADD_BTN_CSS, driver)
        self.submit_btn = ButtonElement(self.CTG_SUBMIT_BTN_CSS, driver)
        self.ctg_name_inp = InputElement(self.CTG_INP_FIELD_CSS, driver)
        self.row_index = TableElement(self.COLUMN_OF_TABLE_CSS, driver)
        self.edit_ctg_btn = ButtonElement(self.CTG_EDIT_BTN_CSS, driver)
        self.cancel_ctg_btn = ButtonElement(self.CTG_CANCEL_BTN_CSS, driver)
        self.delete_ctg_btn = ButtonElement(self.CTG_DELETE_BTN, driver)

    def get_element_text_by_index(self, index, selector, wait_time=10):
        """
            Method for getting text of element by index
        :index - index of element, which we need to enter
                into locator before getting text
        """
        element_selector = selector.format(index)
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
        return self.find_element_by_css(element_selector).text



