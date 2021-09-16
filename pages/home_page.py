from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.elements.datepickers import DatePicker


class HomePage:
    """
        Locators for Home page.
    """
    HOME_PAGE_CARD_TO_EVENTS_LINK_CSS = "div:nth-child({}) > div > div.MuiCardMedia-root"
    HOME_PAGE_NUMBER_OF_PAGE_BTN_CSS = "ul > div > div > button:nth-child({})"
    HOME_PAGE_KEYWORD_INP_CSS = "form > div:nth-child(1) > div > div > input"
    HOME_PAGE_MORE_FILTERS_BTN_CSS = "div:nth-child(2) > button > span.MuiButton-label"
    HOME_PAGE_RESET_FAVORITE_SEARCH_BTN_CSS = "div.d-flex > button > span.MuiButton-label"
    """
        Locators for More filters menu.
    """
    MORE_FILTERS_MENU_DATE_FROM_INP_CSS = "form > div:nth-child(2) > div > div > input"
    MORE_FILTERS_MENU_DATE_TO_INP_CSS = "form > div:nth-child(3) > div > div > input"
    MORE_FILTERS_MENU_HASHTAGS_INP_CSS = "div:nth-child(4) > div > div > div > input"
    MORE_FILTERS_MENU_CHECK_CSS = "div.checkbox > label"
    MORE_FILTERS_MENU_FILTER_BY_LOCATION_BTN_CSS = "div:nth-child(6) > div > button > span.MuiButton-label"
    MORE_FILTERS_MENU_LESS_BTN_CSS = "div:nth-child(8) > button > span.MuiButton-label"
    """ 
        Methods for Home page and More filters menu.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.send_date_from_input = DatePicker(self.MORE_FILTERS_MENU_DATE_FROM_INP_CSS)
        self.send_date_to_input = DatePicker(self.MORE_FILTERS_MENU_DATE_TO_INP_CSS)

    def click_to_event_link(self, index):
        """
            Method for click card to event.
            Index must contains integer value.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.HOME_PAGE_CARD_TO_EVENTS_LINK_CSS.format(index)).click()

    def click_number_of_page_btn(self, index):
        """
            Method for click number of page.
            Index must contains integer value.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.HOME_PAGE_NUMBER_OF_PAGE_BTN_CSS.format(index)).click()

    def send_keyword_input(self, string):
        """
            Method for input text in 'keyword' field.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.HOME_PAGE_KEYWORD_INP_CSS).send_keys(string)

    def click_more_filters_btn(self):
        """
            Method for open 'more filters menu'.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.HOME_PAGE_MORE_FILTERS_BTN_CSS).click()

    def send_date_from_input(self, date):
        """
            Method for input date in 'date from' field.
            Date must contains format like this 'dd-mm-yyyy'.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.MORE_FILTERS_MENU_DATE_FROM_INP_CSS).send_keys(date)

    def send_date_to_input(self, date):
        """
            Method for input date in 'date to' field.
            Date must contains format like this 'dd-mm-yyyy'.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.MORE_FILTERS_MENU_DATE_TO_INP_CSS).send_keys(date)

    def send_hashtags_input(self, string):
        """
            Method for input text in 'hashtags' field.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.MORE_FILTERS_MENU_HASHTAGS_INP_CSS).send_keys(string)

    def click_filter_checkbox(self, filter):
        """
            Method for click checkboxes in 'More filters' menu depending on text value.
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

    def click_filter_by_location_btn(self):
        """
            Method for click 'filter by location' button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.MORE_FILTERS_MENU_FILTER_BY_LOCATION_BTN_CSS).click()

    def click_less_btn(self):
        """
            Method for click 'less' button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.MORE_FILTERS_MENU_LESS_BTN_CSS).click()

    def click_reset_favourite_search_btn(self, reset_favorite_search):
        """
            Method for click buttons depending on text value.
                Available buttons:
                    'RESET'
                    'FAVOURITE'
                    'SEARCH'
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.HOME_PAGE_RESET_FAVORITE_SEARCH_BTN_CSS)
        for element in elements:
            if reset_favorite_search in element.text:
                element.click()
                return
