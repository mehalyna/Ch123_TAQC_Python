from pages.basePage import BasePage
from selenium.webdriver.common.keys import Keys


class DatePicker(BasePage):
    """
        Class for send DatePickers by css selector.
    """
    def __init__(self, selector):
        super().__init__()
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

