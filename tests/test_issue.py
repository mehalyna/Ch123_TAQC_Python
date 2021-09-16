from pages.Issues import IssuesPage
from pages.Landing import LandingPage
from pages.ModalPage import ModalPage
from pages.NavigationPage import NavigationPage


class TestsRefactor:
    """
        Test class
    """
    def test_issue_filter(self, browser):
        self.landing = LandingPage(browser)
        self.landing.go_to_site()
        self.landing.sign_up_btn.click_btn_by_css()
        self.modal = ModalPage(browser)
        self.modal.send_email_input("admin@gmail.com")
        self.modal.send_password_input("1qaz1qaz")
        self.modal.click_button("Sign In")
        self.landing.find_event_btn.click_btn_by_css()
        self.navigation = NavigationPage(browser)
        self.navigation.go_to_page("Issues")
        self.issues = IssuesPage(browser)
        self.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
        self.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
        self.issues.status_btns.click_btn_by_name("SEARCH")
        assert len(self.issues.get_amount_of_issue_results()) == 2, "amount of issue results doesn`t same as expected"
