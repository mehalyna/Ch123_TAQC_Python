from selenium import webdriver
from selenium.webdriver.common.by import By

class AdminAddCategoryPage():

    '''Locators and methjods for Admin Edit category page'''

    ADD_CATEGORY_BUTTON_XPATH = "//button[contains(text(),'Add element')]"
    EDIT_CATEGORY_BUTTON_CSS = " tr:nth-child(3) > td:nth-child(4) "
    NAME_CATEGORY_INPUT_XPATH = "//table[@class='table w-100 m-auto']/tr[3]/td[1]/input"
    SUBMIT_EDIT_CATEGORY_XPATH = "//table[@class='table w-100 m-auto']/tr[3]/td[4]/button[@type='submit']"
    CANCEL_EDIT_CATEGORY_XPATH = "//table[@class='table w-100 m-auto']/tr[3]/td[4]/button[2]"
    DELETE_CATEGORY_XPATH = "//table[@class='table w-100 m-auto']/tr[3]/td[5]/button"

    def __init__(self):
        self.driver=webdriver.Chrome()

    def click_add_category_button(self):
        element=self.driver.find_element(By.XPATH, self.ADD_CATEGORY_BUTTON_XPATH)
        element.click()

    def click_edit_category_button(self):
        element=self.driver.find_element(By.XPATH, self.EDIT_CATEGORY_BUTTON_XPATH)
        element.click()

    def input_category_name(self, string):
        element=self.driver.find_element(By.XPATH, self.NAME_CATEGORY_INPUT_XPATH)
        element.send_keys(string)

    def click_submit_editing(self):
        element=self.driver.find_element(By.XPATH, self.SUBMIT_EDIT_CATEGORY_XPATH)
        element.click()

    def click_cancel_editing(self):
        element=self.driver.find_element(By.XPATH, self.CANCEL_EDIT_CATEGORY_XPATH)
        element.click()

    def click_delete_category(self):
        element=self.driver.find_element(By.XPATH, self.DELETE_CATEGORY_XPATH)
        element.click()
