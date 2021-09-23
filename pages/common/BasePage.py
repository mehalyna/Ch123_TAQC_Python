from pages.Issues import IssuesPage
from pages.Landing import LandingPage
from pages.ModalPage import ModalPage
from pages.NavigationPage import NavigationPage
from pages.common.baseWrapper import BaseWrapper
from pages.edit_categoty import AdminAddCategoryPage


class BasePage(BaseWrapper):

    def __init__(self, driver):
        """
            Page initialization.
        """
        super().__init__(driver)
        self.landing = LandingPage(driver)
        self.issues = IssuesPage(driver)
        self.modal = ModalPage(driver)
        self.navigation = NavigationPage(driver)
        self.categories = AdminAddCategoryPage(driver)
