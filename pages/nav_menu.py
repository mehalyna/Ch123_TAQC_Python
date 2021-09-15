from pages.basePage import BasePage
from pages.elements.buttonElement import ButtonElement


class NavigationPage(BasePage):
    """
        Locators and methods for navigation menu.
    """
    NAV_PAGE_TITLE_CSS = "span.nav-item-text"
    NAV_EDIT_PROFILE_CSS = "a:nth-child(1) > button"
    NAV_LOGOUT_CSS = "a:nth-child(2) > button"

    def __init__(self):
        super().__init__()
        self.navigation_edit_profile_btn = ButtonElement(self.NAV_EDIT_PROFILE_CSS)
        self.log_out_btn = ButtonElement(self.NAV_LOGOUT_CSS)

    def go_to_page(self, page_title):
        """
            Method for click on page depending on page_title value.
            page_title values for admin:
                'Home' - Home page
                'Comuna' - Comuna page
                'Admin' - Admin page
                'Issues' - Issues page
            page_title for user:
                'Home' - Home page
                'Profile' - Profile page
                'Draft' - Drafts page
                'Search Users' - Search/users page
                'Recurrent Events' - eventSchedules page
                'Contact us' - contactAdmin page
                'Comuna' Comuna page
        """

        elements = self.find_elements(self.NAV_PAGE_TITLE_CSS)
        for element in elements:
            if page_title in element.text:
                element.click()
                return

