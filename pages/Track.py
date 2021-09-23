from selenium import webdriver
from selenium.webdriver.common.by import By

ENTYTY_NAME_FIELD_TRACK_CSS = 'div:nth-child(1) > div:nth-child(1)'
FROM_DATE_FIELD_TRACK_CSS = 'div:nth-child(1) > div:nth-child(3) > div > div > input'
TO_DATE_FIELD_TRACK_CSS = 'div:nth-child(1) > div:nth-child(4) > div > div > input'
INFO_BTN_TRACK_CSS = 'tr:nth-child({}) > td:nth-child(5) > div > button'
CHECK_BOX_TRACK_CSS = '.checkbox > label'
SEARCH_RESET_BTNS_CSS = ".form-group.d-flex"


class TrackPage:
    """
        Admin track page filtering.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()

    def info_track_btn(self, track_index):
        """
            Click track information button.
            Track_index used for input number of user we want to get info about.
        """
        self.driver.find_element(By.CSS_SELECTOR, INFO_BTN_TRACK_CSS.format(track_index)).click()

    def entity_name_field_track(self, search_text):
        """
            Entity name input method.
        """
        self.driver.find_element(By.CSS_SELECTOR, ENTYTY_NAME_FIELD_TRACK_CSS).send_keys(search_text)

    def checkbox_status_track(self, status_name):
        """
            Method for click checkbox status
                Available commands for status_name:
                    'Undefined'
                    'Modified'
                    'Created'
                    'Deleted'
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, CHECK_BOX_TRACK_CSS)
        for element in elements:
            if status_name in element.text:
                element.click()
                return

    def search_reset_btns_track(self, btn_name):
        """
            Method for click buttons:
                input "Search" for search button
                input "Reset" for reset button
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, SEARCH_RESET_BTNS_CSS)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return

    def from_date_track(self, date):
        """
            Method for input date 'from' creating.
        """
        self.driver.find_element(By.CSS_SELECTOR, FROM_DATE_FIELD_TRACK_CSS).send_keys(date)

    def to_date_track(self, date):
        """
            Method for input date 'to' creating.

        """
        self.driver.find_element(By.CSS_SELECTOR, TO_DATE_FIELD_TRACK_CSS).send_keys(date)
