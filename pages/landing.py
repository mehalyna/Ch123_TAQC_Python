from pages.elements.buttonElement import ButtonElement
from selenium import webdriver


class LandingPage:
    """
        Locators and methods for landing page.
    """

    SIGN_IN_UP_BTN_CSS = ".MuiButton-label"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.sign_up = ButtonElement(self.SIGN_IN_UP_BTN_CSS)
        self.find_event = ButtonElement(self.FIND_EVENT_BTN_CSS)
        self.create_event = ButtonElement(self.CREATE_EVENT_BTN_CSS)
        self.join_eventexpress = ButtonElement(self.JOIN_EVENTEXPRESS_BTN_CSS)
        self.log_out = ButtonElement(self.LOG_OUT_BTN_CSS)
