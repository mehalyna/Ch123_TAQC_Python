import config
from pages.common.baseWrapper import BaseWrapper


class ModalPage(BaseWrapper):
    """
        Locators and methods for Modal page.
    """
    MODAL_DIALOG_XPATH = "//div[@class='MuiDialog-root'][2]"
    FORM_PAGE_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = '{{}}']"
    FORM_EMAIL_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='email']"
    FORM_PASSWORD_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='password']"
    FORM_REGISTER_PASSWORD_REPEAT_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='RepeatPassword']"
    FORM_BTN_XPATH = f"{MODAL_DIALOG_XPATH}//span[text() = '{{}}']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_page(self, page_title):
        """
            Method for click on page depending on page_title value.
        """
        element = self.find_element_by_xpath(self.FORM_PAGE_XPATH.format(page_title))
        element.click()

    def send_email_input(self, string):
        element = self.find_element_by_xpath(self.FORM_EMAIL_INP_XPATH)
        element.send_keys(string)

    def send_password_input(self, string):
        element = self.find_element_by_xpath(self.FORM_PASSWORD_INP_XPATH)
        element.send_keys(string)

    def send_password_repeat_input(self, string):
        element = self.find_element_by_xpath(self.FORM_REGISTER_PASSWORD_REPEAT_INP_XPATH)
        element.send_keys(string)

    def click_button(self, name_button):
        """
            Method for click on page depending on name_button value.
        """
        element = self.find_element_by_xpath(self.FORM_BTN_XPATH.format(name_button))
        element.click()

    def login(self, username, password):
        """
        Sign in method as a scenario
        actor - is a person with own permissions (admin or user).
        Method of precondition for testing
        :param username: username
        :param password: pass phrase
        """
        self.send_email_input(username)
        self.send_password_input(password)
        self.click_button(config.landing_sign_in_button)
