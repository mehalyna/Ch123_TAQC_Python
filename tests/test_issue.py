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


def test_issue_datepicker(app):
    """
        Testing the issue filtering using DatePicker`s and check result.
    """
    expected_result = 2
    # start test
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    app.landing.find_event_btn.click_btn_by_css()
    # go to home page
    app.navigation.go_to_page(ISSUES_PAGE_TEXT)
    # go to Issues page
    app.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
    app.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
    app.issues.status_btns.click_btn_by_name(SEARCH_BUTTON_TEXT)
    assert expected_result == app.issues.get_amount_of_issue_results(), \
        "amount of issue results doesn`t same as expected"


def test_issue_filter(app):
    """
        Testing the issue filtering using DatePicker`s and check result.
    """
    expected_result = 3
    # start test
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    app.landing.find_event_btn.click_btn_by_css()
    # go to home page
    app.navigation.go_to_page(ISSUES_PAGE_TEXT)
    # go to Issues page
    app.issues.click_issue_status_filter(CHECK_OPEN_TEXT)
    app.issues.status_btns.click_btn_by_name(SEARCH_BUTTON_TEXT)
    assert expected_result == app.issues.get_amount_of_issue_results(), \
        "amount of issue results doesn`t same as expected"


def test_issue_reset_btn(app):
    expected_result = 4
    # start test
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    app.landing.find_event_btn.click_btn_by_css()
    # go to home page
    app.navigation.go_to_page(ISSUES_PAGE_TEXT)
    # go to Issues page
    app.issues.click_issue_status_filter(CHECK_OPEN_TEXT)
    app.issues.click_issue_status_filter(CHECK_RESOLVE_TEXT)
    app.issues.click_issue_status_filter(CHECK_IN_PROGRESS_TEXT)
    app.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
    app.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
    app.issues.status_btns.click_btn_by_name(SEARCH_BUTTON_TEXT)
    app.issues.status_btns.click_btn_by_name(RESET_BUTTON_TEXT)
    assert expected_result == app.issues.get_amount_of_issue_results(), \
        "amount of issue results doesn`t same as expected"
