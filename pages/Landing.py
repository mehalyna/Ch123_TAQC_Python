from pages.common.baseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement


class LandingPage(BaseWrapper):
    """
        Locators and methods for landing page.
    """

    SIGN_IN_UP_BTN_CSS = ".MuiButton-label"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_btn = ButtonElement(self.SIGN_IN_UP_BTN_CSS)
        self.find_event_btn = ButtonElement(self.FIND_EVENT_BTN_CSS)
        self.create_event_btn = ButtonElement(self.CREATE_EVENT_BTN_CSS)
        self.join_eventexpress_btn = ButtonElement(self.JOIN_EVENTEXPRESS_BTN_CSS)
        self.log_out_btn = ButtonElement(self.LOG_OUT_BTN_CSS)
