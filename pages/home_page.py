from pages.common.baseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement
from pages.elements.ButtonElements import ButtonElements
from pages.elements.DatePicker import DatePicker
from pages.elements.InputElement import InputElement


class HomePage(BaseWrapper):
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
    # Locators for test.
    RESULTS_CSS = ".h1"
    EVENT_TITLE_CSS = ".text-block > .title"

    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        super().__init__(driver)
        self.date_from_input = DatePicker(self.MORE_FILTERS_MENU_DATE_FROM_INP_CSS, driver)
        self.date_to_input = DatePicker(self.MORE_FILTERS_MENU_DATE_TO_INP_CSS, driver)
        self.more_filters_btn = ButtonElement(self.HOME_PAGE_MORE_FILTERS_BTN_CSS, driver)
        self.reset_favourite_search_btn = ButtonElements(self.HOME_PAGE_RESET_FAVORITE_SEARCH_BTN_CSS, driver)
        self.less_btn = ButtonElement(self.MORE_FILTERS_MENU_LESS_BTN_CSS, driver)
        self.filter_by_location_btn = ButtonElement(self.MORE_FILTERS_MENU_FILTER_BY_LOCATION_BTN_CSS, driver)
        self.event_link = ButtonElement(self.HOME_PAGE_CARD_TO_EVENTS_LINK_CSS, driver)
        self.number_of_page_btn = ButtonElement(self.HOME_PAGE_NUMBER_OF_PAGE_BTN_CSS, driver)
        self.keyword_input = InputElement(self.HOME_PAGE_KEYWORD_INP_CSS, driver)
        self.hashtags_input = InputElement(self.MORE_FILTERS_MENU_HASHTAGS_INP_CSS, driver)

    def click_filter_checkbox(self, filter):
        """
            Method for click checkboxes in 'More filters' menu depending on text value.
            :param filter: It's parameter to select needed checkbox.
                Available checkboxes:
                    'Active'
                    'Blocked'
                    'Canceled'
        """
        elements = self.find_elements(self.MORE_FILTERS_MENU_CHECK_CSS)
        for element in elements:
            if filter in element.text:
                element.click()
                return

    def is_results_present(self):
        """
            Returns True if the results is displayed.
        """
        return self.find_element_by_css(self.RESULTS_CSS).is_displayed()

    def get_url(self):
        """
            Method for get URL.
        """
        return self.driver.current_url

    def is_title_displayed(self):
        """
            Returns True if the title is displayed.
        """
        return self.find_element_by_css(self.EVENT_TITLE_CSS).is_displayed()
