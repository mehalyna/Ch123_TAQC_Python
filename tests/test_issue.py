"""
    Testing the 'Issues' page
"""


def test_issue_filter(app):
    """
        Testing the issue filtering using DatePicker`s and check result.
    """
    expected_result = 2
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.send_email_input("admin@gmail.com")
    app.modal.send_password_input("1qaz1qaz")
    app.modal.click_button("Sign In")
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Issues")
    app.issues.date_from_dtp.write_date_to_datepicker(21, 6, 2021)
    app.issues.date_to_dtp.write_date_to_datepicker(15, 9, 2022)
    app.issues.status_btns.click_btn_by_name("SEARCH")
    assert expected_result == app.issues.get_amount_of_issue_results(), \
        "amount of issue results doesn`t same as expected"
