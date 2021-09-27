from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.elements.ButtonElement import ButtonElement
from pages.common.baseWrapper import BaseWrapper
from pages.elements.InputElement import InputElement
from pages.elements.TableElement import TableElement
from pages.elements.TextElement import TextElement


class AdminAddCategoryPage(BaseWrapper):
    """
        Locators and methods for Admin Edit category page
    """
    index_of_row = 0
    CTG_NAME_CSS = "tr:nth-child({}) td:nth-child(1)"
    CTG_ADD_BTN_CSS = ".ml-0"
    CTG_INP_FIELD_CSS = "#save-form"
    CTG_SUBMIT_BTN_CSS = ".text-success"
    CTG_CANCEL_BTN_CSS = "tr:nth-child({}) .text-danger"
    CTG_EDIT_BTN_CSS = "tr:nth-child({}) .text-info"
    CTG_DELETE_BTN = "tr:nth-child({}) td:nth-child(5) button.text-danger"
    NUMBER_OF_USERS_VALUE_CSS = "tr:nth-child({}) td:nth-child(2)"
    NUMBER_OF_EVENTS_VALUE_CSS = "tr:nth-child({}) td:nth-child(3)"
    COLUMN_OF_TABLE_CSS = "tr > td:nth-child(1):not(td.align-middle)"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = webdriver.Chrome()
        self.add_ctg_btn = ButtonElement(self.CTG_ADD_BTN_CSS, self.driver)
        self.submit_btn = ButtonElement(self.CTG_SUBMIT_BTN_CSS, self.driver)
        self.ctg_name_inp = InputElement(self.CTG_INP_FIELD_CSS, self.driver)
        self.row_index = TableElement(self.COLUMN_OF_TABLE_CSS, self.driver)
        self.edit_ctg_btn = ButtonElement(self.CTG_EDIT_BTN_CSS, self.driver)
        self.cancel_ctg_btn = ButtonElement(self.CTG_CANCEL_BTN_CSS, self.driver)
        self.delete_ctg_btn = ButtonElement(self.CTG_DELETE_BTN, self.driver)
        self.users_in_ctg = TextElement(self.NUMBER_OF_USERS_VALUE_CSS, self.driver)
        self.events_in_ctg = TextElement(self.NUMBER_OF_EVENTS_VALUE_CSS, self.driver)
        self.ctg_name = TextElement(self.CTG_NAME_CSS, self.driver)





