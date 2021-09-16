from pages.common.baseContext import BaseContext
from selenium.webdriver.common.keys import Keys


class DatePicker(BaseContext):
    """
        Class for send DatePickers by css selector.
    """
    def __init__(self, selector, driver):
        super().__init__(driver)
        self.css_selector = selector

    def write_date_to_datepicker(self, day, month, year):
        """
            Method for write date on a datepicker by css selector.
            Day, month, year - are integer values.
        """
        element = self.find_element_by_css(self.css_selector)
        element.send_keys(year)
        element.send_keys(year)
        element.send_keys(year)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(month)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(day)

