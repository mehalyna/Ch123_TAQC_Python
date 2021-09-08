from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class ModalPage:
    """
    locators for Modal page
    """

    FORM_LOGIN_PAGE_XPATH = "//div[@class='MuiDialog-root'][2]//span[text() = 'Login']"
    FORM_EMAIL_INPUT_XPATH = "//div[@class='MuiDialog-root'][2]//input[@name='email']"
    FORM_PASSWORD_INPUT_XPATH = "//div[@class='MuiDialog-root'][2]//input[@name='password']"
    FORM_SIGN_IN_BUTTON_XPATH = "//div[@class='MuiDialog-root'][2]//button[@value='Login']"
    FORM_FORGOT_BUTTON_XPATH = "//div[@class='MuiDialog-root'][2]//span[contains(text(),'Forgot password')]"
    FORM_CLEAR_BUTTON_XPATH = "//div[@class='MuiDialog-root'][2]//span[text() = 'CLEAR']"
    FORM_CANCEL_BUTTON_XPATH = "//div[@class='MuiDialog-root'][2]//span[text() = 'Cancel']"
    FORM_REGISTER_PAGE_XPATH = "//div[@class='MuiDialog-root'][2]//span[text() = 'Register']"
    FORM_REGISTER_PASSWORD_REPEAT_INPUT_XPATH = "//div[@class='MuiDialog-root'][2]//input[@name='RepeatPassword']"
    FORM_REGISTER_SIGN_UP_BUTTON_XPATH = "//div[@class='MuiDialog-root'][2]//span[text() = 'Sign Up']"

    def click_log_in_page(self, FORM_LOGIN_PAGE_XPATH):
        element = driver.find_element(By.XPATH, FORM_LOGIN_PAGE_XPATH)
        element.click()

    def send_email_input(self, FORM_EMAIL_INPUT_XPATH, string):
        element = driver.find_element(By.XPATH, FORM_EMAIL_INPUT_XPATH)
        element.send_keys(string)

    def send_password_input(self, FORM_PASSWORD_INPUT_XPATH, string):
        element = driver.find_element(By.XPATH, FORM_PASSWORD_INPUT_XPATH)
        element.send_keys(string)

    def click_sign_in(self, FORM_SIGN_IN_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, FORM_SIGN_IN_BUTTON_XPATH)
        element.click()

    def click_forgot(self, FORM_FORGOT_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, FORM_FORGOT_BUTTON_XPATH)
        element.click()

    def click_clear(self, FORM_CLEAR_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, FORM_CLEAR_BUTTON_XPATH)
        element.click()

    def click_cancel(self, FORM_CANCEL_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, FORM_CANCEL_BUTTON_XPATH)
        element.click()

    def click_regiser_page(self, FORM_REGISTER_PAGE_XPATH):
        element = driver.find_element(By.XPATH, FORM_REGISTER_PAGE_XPATH)
        element.click()

    def send_password_repeat_input(self, FORM_REGISTER_PASSWORD_REPEAT_INPUT_XPATH, string):
        element = driver.find_element(By.XPATH, FORM_REGISTER_PASSWORD_REPEAT_INPUT_XPATH)
        element.send_keys(string)

    def click_sign_up(self, FORM_REGISTER_SIGN_UP_BUTTON_XPATH):
        element = driver.find_element(By.XPATH, FORM_REGISTER_SIGN_UP_BUTTON_XPATH)
        element.click()