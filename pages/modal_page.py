from selenium import webdriver
from selenium.webdriver.common.by import By


class ModalPage:
    """
        Locators and methods for Modal page.
    """
    MODAL_DIALOG_XPATH = "//div[@class='MuiDialog-root'][2]"
    FORM_PAGE_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = '{{}}']"
    FORM_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='{{}}']"
    FORM_BTN_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = '{{}}']"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_page(self, page_title):
        """
            Method for click on page depending on text value.
        """
        element = self.driver.find_element(By.XPATH, self.FORM_PAGE_XPATH.format(page_title))
        element.click()

    def send_data_input(self, name_input, string):
        """
            Method for send data to input depending on text value.
        """
        element = self.driver.find_element(By.XPATH, self.FORM_INP_XPATH.format(name_input))
        element.send_keys(string)

    def click_button(self, name_button):
        """
            Method for click on button depending on text value.
        """
        element = self.driver.find_element(By.XPATH, self.FORM_BTN_XPATH.format(name_button))
        element.click()
