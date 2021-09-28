import allure
from allure_commons.types import Severity
import config

"""
    Testing the 'Landing' page
"""
ISSUES_PAGE_TEXT = "Issues"
SEARCH_BUTTON_TEXT = "SEARCH"
RESET_BUTTON_TEXT = "RESET"
CHECK_OPEN_TEXT = "Open"
CHECK_IN_PROGRESS_TEXT = "In progress"
CHECK_RESOLVE_TEXT = "Resolve"


@allure.title("Test login:")
@allure.severity(Severity.BLOCKER)
def test_landing_login(admin_setup):
    """
        Verify that user have ability log in as a Admin.
    """
    expected_result = "Admin"
    with allure.step("Click find event button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Checking excepted result"):
        assert expected_result == admin_setup.navigation.get_user_name(), \
            "username results doesn`t same as expected"


@allure.title("Test registration:")
@allure.severity(Severity.CRITICAL)
def test_landing_registration(app):
    """
        Verify that user have ability register new account.
    """
    expected_result = "Your register was successfull. Please confirm your email."
    with allure.step("Go to site and click sign up button"):
        app.landing.go_to_site()
        app.landing.sign_up_btn.click_btn_by_css()
    with allure.step("Go to 'Registration' page"):
        app.modal.registration(config.ADMIN_EMAIL, config.ADMIN_PASS)
    with allure.step("Checking excepted result"):
        assert expected_result == app.modal.get_success_register_text(), \
            "alert message doesn`t same as expected"
