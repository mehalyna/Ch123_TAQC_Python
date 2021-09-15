from pages.basePage import BasePage
from pages.elements.buttons import ButtonElements
from pages.elements.datepickers import DatePicker


class IssuesPage(BasePage):
    """ Locators and methods for Issues page. """

    VIEW_BTN_CSS = "tr:nth-child({})  a > button"
    CHECK_CSS = ".checkbox > label"
    BTN_CSS = "form > div.d-flex > button"
    DATAPICKER_FROM_CSS = ".form-group:nth-child(1) .MuiInputBase-input.MuiInput-input"
    DATAPICKER_TO_CSS = ".form-group:nth-child(2) .MuiInputBase-input.MuiInput-input"

    def __init__(self):
        super().__init__()
        self.status_btns = ButtonElements(self.BTN_CSS)
        self.date_from_dtp = DatePicker(self.DATAPICKER_FROM_CSS)
        self.date_to_dtp = DatePicker(self.DATAPICKER_TO_CSS)

    def click_view(self, view_number):
        """
            Method for click on a needed view button.
        """
        element = self.find_element_by_css(self.VIEW_BTN_CSS.format(view_number + 1))
        element.click()

    def click_issue_status_filter(self, issue_status):
        """
            Method for click on issue status checkbox depending on text value.
        """
        elements = self.find_elements(self.CHECK_CSS)
        for element in elements:
            if issue_status in element.text:
                element.click()
                return
