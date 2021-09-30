from pages.common.BaseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement


class NavigationForAdmin(BaseWrapper):
    """
        Locators and methods for navigation menu on admin panel
    """
    ADMIN_MENU = "#sub-nav"


    def go_to_page(self, page_title):
        """
            Method for click on page depending on page_title value.
            Pages of Admin Panel:
                "Categories" - Edit_category
                "UnitsOfMeasuring" - Units_of_measuring
                "Users" - User
                "Notification Templates" - NotificationPage
                "Tracks" - Track
        """
        elements = self.find_elements(self.ADMIN_MENU)
        for element in elements:
            if page_title in element.text:
                element.click()
                return
