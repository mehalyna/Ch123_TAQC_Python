"""
    Testing Home Page
"""
import config


def test_home_page_date(app):
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Home Page")
    app.home_page.more_filters_btn.click_btn_by_css()
    app.home_page.date_from_input.write_date_to_datepicker(5, 10, 2021)
    app.home_page.date_to_input.write_date_to_datepicker(9, 10, 2021)
    app.home_page.reset_favourite_search_btn.click_btn_by_name("SEARCH")
    assert app.home_page.check_results() == True

def test_home_page_number_of_page(app):
    page_index = 2
    expected_result = f"https://eventsexpress-test.azurewebsites.net/home/events?page={page_index}"
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Home Page")
    app.home_page.number_of_page_btn.click_btn_by_index_css(page_index)
    assert expected_result == app.home_page.get_url()

def test_home_page_event(app):
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Home Page")
    app.home_page.event_link.click_btn_by_index_css(1)
    assert app.home_page.is_title_exist() == True

def test_home_page_keyword(app):
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Home Page")
    app.home_page.keyword_input.send_data("ttt")
    app.home_page.reset_favourite_search_btn.click_btn_by_name("SEARCH")
    assert app.home_page.check_results() == True

def test_home_page_checkboxes(app):
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Home Page")
    app.home_page.more_filters_btn.click_btn_by_css()
    app.home_page.click_filter_checkbox("Blocked")
    app.home_page.reset_favourite_search_btn.click_btn_by_name("SEARCH")
    assert app.home_page.check_results() == True
