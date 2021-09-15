from selenium import webdriver
from selenium.webdriver.common.by import By

ENTYTY_NAME_FIELD_TRACK_CSS = 'div:nth-child(1) > div:nth-child(1)'
UNDEFINED_BOX_TRACK_CSS = 'div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1)'
MODIFIED_BOX_TRACK_CSS = 'div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) '
CREATED_BOX_TRACK_CSS = 'div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3)'
DELETED_BOX_TRACK_CSS = 'div:nth-child(1) > div:nth-child(2) > div > div:nth-child(4)'
FROM_DATE_FIELD_TRACK_CSS = 'div:nth-child(1) > div:nth-child(3) > div > div > input'
TO_DATE_FIELD_TRACK_CSS = 'div:nth-child(1) > div:nth-child(4) > div > div > input'
RESET_BTN_TRACK_CSS = 'div.form-group.d-flex > button:nth-child(1)'
SEARCH_BTN_TRACK_CSS = 'div.form-group.d-flex > button:nth-child(2)'
INFO_BTN_TRACK_CSS = 'tr:nth-child({track_index}) > td:nth-child(5) > div > button'
CHECK_BOX_TRACK_CSS = 'div.checkbox > label'
SEARCH_RESET_BTNS_CSS = "button > span.MuiButton-label"

class TrackPage:
    """
        Admin track page filtering.
    """
    def __init__(self):
        """
            Init method used for set up.
        """
        self.driver = webdriver.Chrome()

    def info_track_btn(self, track_index):
        """
            Click track information button.
        """
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, INFO_BTN_TRACK_CSS.format(track_index)).click()

    def entity_name_field_track(self, search_text):
        """
            Entity name input method.
        """
        self.driver.find_element(By.CSS_SELECTOR, ENTYTY_NAME_FIELD_TRACK_CSS).send_keys(search_text)

    def checkbox_status_track(self, status_name):
        """
            Method for click checkbox status
                Available commands:
                    'Undefined'
                    'Modified'
                    'Created'
                    'Deleted'
        """
        self.driver.find_element(By.CSS_SELECTOR, CHECK_BOX_TRACK_CSS)
        for element in elements:
            if status_name in element.text:
                element.click()
                return

    def search_reset_btns_track(self, btn_name):
        self.driver.find_element(By.CSS_SELECTOR, SEARCH_RESET_BTNS_CSS)
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

