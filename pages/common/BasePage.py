from pages.Issues import IssuesPage
from pages.Landing import LandingPage
from pages.ModalPage import ModalPage
from pages.NavigationForAdmin import NavigationForAdminPanel
from pages.NavigationPage import NavigationPage
from pages.Edit_categoty import AdminAddCategoryPage
from pages.common.BaseWrapper import BaseWrapper
from pages.home_page import HomePage
from pages.common.baseWrapper import BaseWrapper



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
        self.admin_panel = NavigationForAdminPanel(driver)
        self.home_page = HomePage(driver)

