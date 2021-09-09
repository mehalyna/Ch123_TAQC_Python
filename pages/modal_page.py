from selenium import webdriver
from selenium.webdriver.common.by import By


class ModalPage:
    """
    Locators and methods for Modal page.
    """
    MODAL_DIALOG_XPATH = "//div[@class='MuiDialog-root'][2]"
    FORM_LOGIN_PAGE_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = 'Login']"
    FORM_EMAIL_INPUT_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='email']"
    FORM_PASSWORD_INPUT_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='password']"
    FORM_SIGN_IN_BUTTON_XPATH = f"{MODAL_DIALOG_XPATH}//button[@value='Login']"
    FORM_FORGOT_BUTTON_XPATH = f"{MODAL_DIALOG_XPATH}//span[contains(text(),'Forgot password')]"
    FORM_CLEAR_BUTTON_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = 'CLEAR']"
    FORM_CANCEL_BUTTON_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = 'Cancel']"
    FORM_REGISTER_PAGE_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = 'Register']"
    FORM_REGISTER_PASSWORD_REPEAT_INPUT_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='RepeatPassword']"
    FORM_REGISTER_SIGN_UP_BUTTON_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = 'Sign Up']"

    """Methods"""
    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_log_in_page(self):
        element = self.driver.find_element(By.XPATH, self.FORM_LOGIN_PAGE_XPATH)
        element.click()

    def send_email_input(self, string):
        element = self.driver.find_element(By.XPATH, self.FORM_EMAIL_INPUT_XPATH)
        element.send_keys(string)

    def send_password_input(self, string):
        element = self.driver.find_element(By.XPATH, self.FORM_PASSWORD_INPUT_XPATH)
        element.send_keys(string)

    def click_sign_in(self):
        element = self.driver.find_element(By.XPATH, self.FORM_SIGN_IN_BUTTON_XPATH)
        element.click()

    def click_forgot(self):
        element = self.driver.find_element(By.XPATH, self.FORM_FORGOT_BUTTON_XPATH)
        element.click()

    def click_clear(self):
        element = self.driver.find_element(By.XPATH, self.FORM_CLEAR_BUTTON_XPATH)
        element.click()

    def click_cancel(self):
        element = self.driver.find_element(By.XPATH, self.FORM_CANCEL_BUTTON_XPATH)
        element.click()

    def click_regiser_page(self):
        element = self.driver.find_element(By.XPATH, self.FORM_REGISTER_PAGE_XPATH)
        element.click()

    def send_password_repeat_input(self, string):
        element = self.driver.find_element(By.XPATH, self.FORM_REGISTER_PASSWORD_REPEAT_INPUT_XPATH)
        element.send_keys(string)

    def click_sign_up(self):
        element = self.driver.find_element(By.XPATH, self.FORM_REGISTER_SIGN_UP_BUTTON_XPATH)
        element.click()
