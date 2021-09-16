from pages.basePage import BasePage
from pages.issues import IssuesPage
from pages.landing import LandingPage
from pages.modal_page import ModalPage
from pages.nav_menu import NavigationPage


class Tests:

    landing = LandingPage()
    modal = ModalPage()
    navigation = NavigationPage()
    issues = IssuesPage()

    def test_issue_filter(self):
        self.landing.go_to_site()
        self.landing.sign_up_btn.click_btn_by_css()
        self.modal.send_email_input("admin@gmail.com")
        self.modal.send_password_input("1qaz1qaz")
        self.modal.click_button("Sign In")
        self.landing.find_event_btn.click_btn_by_css()
        self.navigation.go_to_page("Issues")
        self.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
        self.issues.date_from_dtp.write_date_to_datepicker(15, 9, 2022)
        self.issues.status_btns.click_btn_by_name("Search")
