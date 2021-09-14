from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DatePicker:
    """
        Class for send DatePickers by css selector.
    """
    def __init__(self, selector):
        self.driver = webdriver.Chrome()
        self.css_selector = selector

    def write_date_to_datepicker(self, day, month, year):
        """
            Method for write date on a datepicker by css selector.
            Day, month, year - are integer values.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector)
        element.send_keys(year)
        element.send_keys(year)
        element.send_keys(year)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(month)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(day)

