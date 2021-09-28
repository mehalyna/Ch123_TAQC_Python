"""
    Testing the 'Issues' page
"""
import allure
from allure_commons.types import Severity

import config


ISSUES_PAGE_TEXT = "Issues"
SEARCH_BUTTON_TEXT = "SEARCH"
RESET_BUTTON_TEXT = "RESET"
CHECK_OPEN_TEXT = "Open"
CHECK_IN_PROGRESS_TEXT = "In progress"
CHECK_RESOLVE_TEXT = "Resolve"


@allure.title("Test datepickers:")
@allure.severity(Severity.NORMAL)
def test_issue_datepicker(admin_setup):
    """
        Verify that admin have ability filter issue using DatePicker`s and check result.
    """
    expected_result = 2
    admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Click find event button and go to issue page"):
        admin_setup.navigation.go_to_page(ISSUES_PAGE_TEXT)
    with allure.step("Filling datepickers"):
        admin_setup.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
        admin_setup.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
    with allure.step("Click search button"):
        admin_setup.issues.status_btns.click_btn_by_name_by_css(SEARCH_BUTTON_TEXT)
    with allure.step("Checking the amount of issues"):
        assert expected_result == admin_setup.issues.get_amount_of_issue_results(), \
            "amount of issue results doesn`t same as expected"


@allure.title("Test checkbox filters:")
@allure.severity(Severity.NORMAL)
def test_issue_filter(admin_setup):
    """
        Verify that the admin has the ability to filter issues using status CheckBox and check results.
    """
    expected_result = 3
    admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Click find event button and go to issue page"):
        admin_setup.navigation.go_to_page(ISSUES_PAGE_TEXT)
    with allure.step("Use checkbox filters"):
        admin_setup.issues.click_issue_status_filter(CHECK_OPEN_TEXT)
    with allure.step("Click 'Search' button"):
        admin_setup.issues.status_btns.click_btn_by_name_by_css(SEARCH_BUTTON_TEXT)
    assert expected_result == admin_setup.issues.get_amount_of_issue_results(), \
        "amount of issue results doesn`t same as expected"


@allure.title("Test 'Reset button':")
@allure.severity(Severity.NORMAL)
def test_issue_reset_btn(admin_setup):
    """
        Verify that admin have ability clear input fields clicking by button 'RESET'.
    """
    expected_result = ""
    admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Click find event button and go to issue page"):
        admin_setup.navigation.go_to_page(ISSUES_PAGE_TEXT)
    with allure.step("Use filters"):
        admin_setup.issues.click_issue_status_filter(CHECK_OPEN_TEXT)
        admin_setup.issues.click_issue_status_filter(CHECK_RESOLVE_TEXT)
        admin_setup.issues.click_issue_status_filter(CHECK_IN_PROGRESS_TEXT)
        admin_setup.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
        admin_setup.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
        admin_setup.issues.status_btns.click_btn_by_name_by_css(SEARCH_BUTTON_TEXT)
    with allure.step("Click 'Reset' button"):
        admin_setup.issues.status_btns.click_btn_by_name_by_css(RESET_BUTTON_TEXT)
    assert expected_result == admin_setup.issues.get_datepicker_text(), "input is not empty"
