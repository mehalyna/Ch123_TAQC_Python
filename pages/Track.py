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


class TrackPage:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def info_track_btn(self, track_index):
        """Click track information button."""
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, INFO_BTN_TRACK_CSS.format(track_index)).click()

    def entity_name_field_track(self, search_text):
        """Entity name input method."""
        self.driver.find_element(By.CSS_SELECTOR, ENTYTY_NAME_FIELD_TRACK_CSS).send_keys(search_text)

    def undefined_status_track(self):
        """Enable 'undefined' status checkbox."""
        self.driver.find_element(By.CSS_SELECTOR, UNDEFINED_BOX_TRACK_CSS).click()

    def modified_status_track(self):
        """Enable 'modified' status checkbox."""
        self.driver.find_element(By.CSS_SELECTOR, MODIFIED_BOX_TRACK_CSS).click()

    def created_status_track(self):
        """Enable 'created' status checkbox."""
        self.driver.find_element(By.CSS_SELECTOR, CREATED_BOX_TRACK_CSS).click()

    def deleted_status_track(self):
        """Enable 'deleted' status checkbox."""
        self.driver.find_element(By.CSS_SELECTOR, DELETED_BOX_TRACK_CSS).click()

    def from_date_track(self, date):
        """Method for input date 'from' creating."""
        self.driver.find_element(By.CSS_SELECTOR, FROM_DATE_FIELD_TRACK_CSS).send_keys(date)

    def to_date_track(self, date):
        """Method for input date 'to' creating."""
        self.driver.find_element(By.CSS_SELECTOR, TO_DATE_FIELD_TRACK_CSS).send_keys(date)

    def search_track(self):
        """Method for clicking search search button."""
        self.driver.find_element(By.CSS_SELECTOR, SEARCH_BTN_TRACK_CSS).click()

    def reset_track(self):
        """Method for clicking reset button."""
        self.driver.find_element(By.CSS_SELECTOR, RESET_BTN_TRACK_CSS).click()