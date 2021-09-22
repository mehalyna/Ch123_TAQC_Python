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


def test_landing_login(app):
    """
        Testing the issue filtering using DatePicker`s and check result.
    """
    expected_result = "Admin"
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    app.landing.find_event_btn.click_btn_by_css()
    assert expected_result == app.navigation.get_user_name(), \
        "username results doesn`t same as expected"


def test_landing_registration(app):
    expected_result = "Your register was successfull. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    #app.modal.registration()
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message doesn`t same as expected"
