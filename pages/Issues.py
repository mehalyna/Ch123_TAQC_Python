from pages.common.basePage import BasePage
from pages.elements.ButtonElements import ButtonElements
from pages.elements.DatePicker import DatePicker


class IssuesPage(BasePage):
    """ Locators and methods for Issues page. """
    VIEW_BTN_CSS = "tr:nth-child({})  a > button"
    CHECK_CSS = ".checkbox > label"
    BTN_CSS = "form > div.d-flex > button"
    DATAPICKER_FROM_CSS = ".form-group:nth-child(1) .MuiInputBase-input.MuiInput-input"
    DATAPICKER_TO_CSS = ".form-group:nth-child(2) .MuiInputBase-input.MuiInput-input"
    ISSUE_RESULTS_CSS = ".table.w-100.m-auto tr:not(.bg-light)"

    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        super().__init__(driver)
        self.status_btns = ButtonElements(self.BTN_CSS, driver)
        self.date_from_dtp = DatePicker(self.DATAPICKER_FROM_CSS, driver)
        self.date_to_dtp = DatePicker(self.DATAPICKER_TO_CSS, driver)

    def click_view(self, view_number):
        """
            Method for click on a needed view button as a view_number.
         :param view_number integer. It's parameter to select needed view button.
            The view number must be specified in the view_number variable.
        """
        element = self.find_element_by_css(self.VIEW_BTN_CSS.format(view_number + 1))
        element.click()

    def click_issue_status_filter(self, issue_status):
        """
            Method for click on issue status checkbox depending on text value.
             :param issue_status string. It's parameter to select needed checkbox.
        """
        elements = self.find_elements(self.CHECK_CSS)
        for element in elements:
            if issue_status in element.text:
                element.click()
                return

    def get_amount_of_issue_results(self):
        """
            Method for get amount of issue.
        """
        return len(self.find_elements(self.ISSUE_RESULTS_CSS))
