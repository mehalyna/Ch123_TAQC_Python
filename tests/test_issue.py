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
def test_datepicker_on_issue_page(admin_setup):
    """
        Verify that admin has the ability to filter issues using DatePicker fields.
    """
    expected_result = 2
    with allure.step("Click find event button and go to issue page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(ISSUES_PAGE_TEXT)
    with allure.step("Filling datepickers"):
        admin_setup.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
        admin_setup.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
    with allure.step("Click search button"):
        admin_setup.issues.status_btns.click_btn_by_name_by_css(SEARCH_BUTTON_TEXT)
    with allure.step("Verify that amount of issues equals expected quantity"):
        assert expected_result == admin_setup.issues.get_amount_of_issue_results(), \
            "amount of issue results doesn`t same as expected"


@allure.title("Test checkbox filters:")
@allure.severity(Severity.NORMAL)
def test_issue_filter(admin_setup):
    """
        Verify that the admin has the ability to filter issues using status CheckBox.
    """
    expected_result = 3
    with allure.step("Click find event button and go to issue page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(ISSUES_PAGE_TEXT)
    with allure.step("Use checkbox filters"):
        admin_setup.issues.click_issue_status_filter(CHECK_OPEN_TEXT)
    with allure.step("Click 'Search' button"):
        admin_setup.issues.status_btns.click_btn_by_name_by_css(SEARCH_BUTTON_TEXT)
    with allure.step("Verify that amount of issues equals expected quantity"):
        assert expected_result == admin_setup.issues.get_amount_of_issue_results(), \
            "amount of issue results doesn`t same as expected"


@allure.title("Test 'Reset button':")
@allure.severity(Severity.NORMAL)
def test_issue_reset_btn(admin_setup):
    """
        Verify that admin has the ability clear input fields clicking by button 'RESET'.
    """
    expected_result = ""
    with allure.step("Click find event button and go to issue page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
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
    with allure.step("Verify that after clicking 'Reset' button fields are empty"):
        assert expected_result == admin_setup.issues.date_from_dtp.get_datepicker_text(), "input is not empty"
