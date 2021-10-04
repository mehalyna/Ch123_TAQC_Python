"""
    Testing Home Page
"""
import allure
from allure_commons.types import Severity


HOME_PAGE_TEXT = "Home Page"
SEARCH_BTN_TEXT = "SEARCH"
BLOCKED_BOX_TEXT = "Blocked"


@allure.title("Test date:")
@allure.severity(Severity.NORMAL)
def test_home_page_date(admin_setup):
    """
        Verify that admin has the ability to filter events using DatePicker fields.
    """
    with allure.step("Click 'find event' button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(HOME_PAGE_TEXT)
    with allure.step("Click 'more filters' button"):
        admin_setup.home_page.more_filters_btn.click_btn_by_css()
    with allure.step("Filling datepickers"):
        admin_setup.home_page.date_from_input.write_date_to_datepicker(5, 10, 2021)
        admin_setup.home_page.date_to_input.write_date_to_datepicker(9, 10, 2021)
    with allure.step("Click 'search' button"):
        admin_setup.home_page.reset_favourite_search_btn.click_btn_by_name(SEARCH_BTN_TEXT)
    with allure.step("Verify that results is present"):
        assert admin_setup.home_page.is_results_present()

@allure.title("Test number of page:")
@allure.severity(Severity.NORMAL)
def test_home_page_number_of_page(admin_setup):
    """
        Verify that admin has the ability to go to the desired page by clicking on it.
    """
    page_index = 2
    expected_result = f"https://eventsexpress-test.azurewebsites.net/home/events?page={page_index}"
    with allure.step("Click 'find event' button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(HOME_PAGE_TEXT)
    with allure.step("Click to the desired page"):
        admin_setup.home_page.number_of_page_btn.click_btn_by_index_css(page_index)
    with allure.step("Verify that it is desired page"):
        assert expected_result == admin_setup.home_page.get_url()

@allure.title("Test click on event:")
@allure.severity(Severity.NORMAL)
def test_home_page_event(admin_setup):
    """
        Verify that admin has the ability to go to the desired event by clicking on it.
    """
    with allure.step("Click 'find event' button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(HOME_PAGE_TEXT)
    with allure.step("Click to the desired page"):
        admin_setup.home_page.event_link.click_btn_by_index_css(1)
    with allure.step("Verify that it is desired event"):
        assert admin_setup.home_page.is_title_displayed()

@allure.title("Test 'keyword' field:")
@allure.severity(Severity.NORMAL)
def test_home_page_keyword(admin_setup):
    """
        Verify that admin has the ability to input data to 'keyword' field and to filter using 'keyword' field.
    """
    with allure.step("Click 'find event' button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(HOME_PAGE_TEXT)
    with allure.step("Input 'ttt' to the 'keyword' field"):
        admin_setup.home_page.keyword_input.send_data("ttt")
    with allure.step("Click 'search' button"):
        admin_setup.home_page.reset_favourite_search_btn.click_btn_by_name(SEARCH_BTN_TEXT)
    with allure.step("Verify that results is present"):
        assert admin_setup.home_page.is_results_present()

@allure.title("Test checkbox 'Blocked' filter:")
@allure.severity(Severity.NORMAL)
def test_home_page_checkboxes(admin_setup):
    """
        Verify that admin has the ability to filter using 'Blocked' checkbox.
    """
    with allure.step("Click 'find event' button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(HOME_PAGE_TEXT)
    with allure.step("Click 'more filters' button"):
        admin_setup.home_page.more_filters_btn.click_btn_by_css()
    with allure.step("Click 'Blocked' checkbox"):
        admin_setup.home_page.click_filter_checkbox(BLOCKED_BOX_TEXT)
    with allure.step("Click 'search' button"):
        admin_setup.home_page.reset_favourite_search_btn.click_btn_by_name(SEARCH_BTN_TEXT)
    with allure.step("Verify that results is present"):
        assert admin_setup.home_page.is_results_present()
