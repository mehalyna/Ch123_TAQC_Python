import allure
from allure_commons.types import Severity
import pytest
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
def test_landing_login(app):
    """
        Testing the issue filtering using DatePicker`s and check result.
    """
    expected_result = "Admin"
    with allure.step("open Eventexpress page"):
        app.landing.go_to_site()
    with allure.step("Open 'Login' Modal page"):
        app.landing.sign_up_btn.click_btn_by_css()
    with allure.step("Filling email, password and click 'sign in' button"):
        app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    with allure.step("Click find event button and go to home page"):
        app.landing.find_event_btn.click_btn_by_css()
    with allure.step("Checking excepted result"):
        assert expected_result == app.navigation.get_user_name(), \
            "username results doesn`t same as expected"


def test_landing_registration(app):
    expected_result = "Your register was successfull. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    #app.modal.registration()
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message doesn`t same as expected"
