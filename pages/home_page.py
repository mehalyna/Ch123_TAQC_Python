from pages.elements.buttonElement import ButtonElement
from pages.elements.buttons import ButtonElements
from pages.elements.datepickers import DatePicker
from pages.elements.InputElement import InputElement
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    """
        Locators and methods for Home page.
    """
    HOME_PAGE_CARD_TO_EVENTS_LINK_CSS = "div:nth-child({}) > div > .MuiCardMedia-root"
    HOME_PAGE_NUMBER_OF_PAGE_BTN_CSS = "button.btn-primary:nth-child({})"
    HOME_PAGE_KEYWORD_INP_CSS = "input[name='keyWord']"
    HOME_PAGE_MORE_FILTERS_BTN_CSS = "button.MuiButton-textSecondary"
    HOME_PAGE_RESET_FAVORITE_SEARCH_BTN_CSS = "div.d-flex span.MuiButton-label"
    # Locators for 'More filters' menu.
    MORE_FILTERS_MENU_DATE_FROM_INP_CSS = ".form-group:nth-child(2) input"
    MORE_FILTERS_MENU_DATE_TO_INP_CSS = ".form-group:nth-child(3) input"
    MORE_FILTERS_MENU_HASHTAGS_INP_CSS = "input.rw-input-reset"
    MORE_FILTERS_MENU_CHECK_CSS = "div.checkbox > label"
    MORE_FILTERS_MENU_FILTER_BY_LOCATION_BTN_CSS = "button.MuiButton-outlined"
    MORE_FILTERS_MENU_LESS_BTN_CSS = "button.MuiButton-textSecondary"

    def __init__(self):
        """
            Method for class fields declaration.
        """
        self.driver = webdriver.Chrome()
        self.date_from_input = DatePicker(self.MORE_FILTERS_MENU_DATE_FROM_INP_CSS)
        self.date_to_input = DatePicker(self.MORE_FILTERS_MENU_DATE_TO_INP_CSS)
        self.more_filters_btn = ButtonElement(self.HOME_PAGE_MORE_FILTERS_BTN_CSS)
        self.reset_favourite_search_btn = ButtonElements(self.HOME_PAGE_RESET_FAVORITE_SEARCH_BTN_CSS)
        self.less_btn = ButtonElement(self.MORE_FILTERS_MENU_LESS_BTN_CSS)
        self.filter_by_location_btn = ButtonElement(self.MORE_FILTERS_MENU_FILTER_BY_LOCATION_BTN_CSS)
        self.event_link = ButtonElement(self.HOME_PAGE_CARD_TO_EVENTS_LINK_CSS)
        self.number_of_page_btn = ButtonElement(self.HOME_PAGE_NUMBER_OF_PAGE_BTN_CSS)
        self.keyword_input = InputElement(self.HOME_PAGE_KEYWORD_INP_CSS)
        self.hashtags_input = InputElement(self.MORE_FILTERS_MENU_HASHTAGS_INP_CSS)

    def click_filter_checkbox(self, filter):
        """
            Method for click checkboxes in 'More filters' menu depending on text value.
            :param filter: It's parameter to select needed checkbox.
                Available checkboxes:
                    'Active'
                    'Blocked'
                    'Canceled'
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.MORE_FILTERS_MENU_CHECK_CSS)
        for element in elements:
            if filter in element.text:
                element.click()
                return
