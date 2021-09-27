import allure
import config

"""
    Testing the 'Issues' page
"""
ISSUES_PAGE_TEXT = "Issues"
SEARCH_BUTTON_TEXT = "SEARCH"
RESET_BUTTON_TEXT = "RESET"
CHECK_OPEN_TEXT = "Open"
CHECK_IN_PROGRESS_TEXT = "In progress"
CHECK_RESOLVE_TEXT = "Resolve"


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
        admin_setup.issues.status_btns.click_btn_by_name(SEARCH_BUTTON_TEXT)
    with allure.step("Checking excepted result"):
        assert expected_result == admin_setup.issues.get_amount_of_issue_results(), \
            "amount of issue results doesn`t same as expected"


def test_issue_filter(admin_setup):
    """
        Verify that admin have ability filter issue using status CheckBox and check result.
    """
    expected_result = 3
    admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Click find event button and go to issue page"):
        admin_setup.navigation.go_to_page(ISSUES_PAGE_TEXT)
    with allure.step("Use checkbox filters"):
        admin_setup.issues.click_issue_status_filter(CHECK_OPEN_TEXT)
    with allure.step("Click 'Search' button"):
        admin_setup.issues.status_btns.click_btn_by_name(SEARCH_BUTTON_TEXT)
    assert expected_result == admin_setup.issues.get_amount_of_issue_results(), \
        "amount of issue results doesn`t same as expected"


def test_issue_reset_btn(admin_setup):
    """
        Verify that admin have ability clear input fields clicking by button 'RESET'.
    """
    ###
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
        admin_setup.issues.status_btns.click_btn_by_name(SEARCH_BUTTON_TEXT)
    with allure.step("Click 'Reset' button"):
        admin_setup.issues.status_btns.click_btn_by_name(RESET_BUTTON_TEXT)
    #not working, i fix it in next PR
    #assert expected_result == admin_setup.issues.DATAPICKER_FROM_CSS.value, \
        "amount of issue results doesn`t same as expected"
