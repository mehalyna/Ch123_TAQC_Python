"""
Testing the 'Categories' page
"""
import allure
from allure_commons.types import Severity


ADMIN_PANEL = "Admin"
CATEGORY_PAGE = "Categories"


@allure.title("Test add category:")
@allure.severity(Severity.NORMAL)
def test_category_add(admin_setup):
    """
        Verify that the admin has the ability to add a new category.
    """
    NAME_OF_CTG = "fun"
    with allure.step("Click find event button and go to admin panel and go categories page "):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(ADMIN_PANEL)
    with allure.step("Add new category"):
        admin_setup.categories.add_ctg_btn.click_btn_by_css()
        admin_setup.categories.ctg_name_inp.send_data_by_css(NAME_OF_CTG)
        admin_setup.categories.submit_btn.click_btn_by_css()
    with allure.step("Check for a new category in the list"):
        assert admin_setup.categories.row_index.find_element_in_row(NAME_OF_CTG) is not None, \
            f"category {NAME_OF_CTG} wasn't added"
    with allure.step("TearDown"):
        ctg_row_index = admin_setup.categories.row_index.find_element_in_row(NAME_OF_CTG) + 2
        admin_setup.categories.delete_ctg_btn.click_btn_by_index_css(ctg_row_index)


@allure.title("Test edit category:")
@allure.severity(Severity.NORMAL)
def test_edit_category(admin_setup):
    """
        Verify that admin has the ability to edit existing category
    """
    NAME_OF_CTG = "fun"
    NAME_FOR_EDIT = "funny"
    expected_result = NAME_FOR_EDIT
    with allure.step("Click find event button and go to admin panel and go categories page "):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(ADMIN_PANEL)
    with allure.step("SetUp"):
        admin_setup.categories.add_ctg_btn.click_btn_by_css()
        admin_setup.categories.ctg_name_inp.send_data_by_css(NAME_OF_CTG)
        admin_setup.categories.submit_btn.click_btn_by_css()
    with allure.step("Edit category name"):
        ctg_row_index = admin_setup.categories.row_index.find_element_in_row(NAME_OF_CTG) + 2
        admin_setup.categories.edit_ctg_btn.click_btn_by_index_css(ctg_row_index)
        admin_setup.categories.ctg_name_inp.clear_field_by_css()
        admin_setup.categories.ctg_name_inp.send_data_by_css(NAME_FOR_EDIT)
        admin_setup.categories.submit_btn.click_btn_by_css()
    with allure.step("Check result of editing"):
        assert expected_result == admin_setup.categories.ctg_name.get_element_text_by_index(ctg_row_index), \
            "category wasn't edited"
    with allure.step("TearDown"):
        admin_setup.categories.delete_ctg_btn.click_btn_by_index_css(ctg_row_index)


@allure.title("Test cancel edit category:")
@allure.severity(Severity.NORMAL)
def test_cancel_changes(admin_setup):
    """
        Verify that admin has the ability to cancel a changes
    """
    NAME_OF_CTG = "fun"
    NAME_FOR_EDIT = "funny"
    expected_result = NAME_OF_CTG
    with allure.step("Click find event button and go to admin panel and go categories page "):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(ADMIN_PANEL)
    with allure.step("SetUp"):
        admin_setup.categories.add_ctg_btn.click_btn_by_css()
        admin_setup.categories.ctg_name_inp.send_data_by_css(NAME_OF_CTG)
        admin_setup.categories.submit_btn.click_btn_by_css()
    with allure.step("Edit and cancel category"):
        ctg_row_index = admin_setup.categories.row_index.find_element_in_row(NAME_OF_CTG) + 2
        admin_setup.categories.edit_ctg_btn.click_btn_by_index_css(ctg_row_index)
        admin_setup.categories.ctg_name_inp.clear_field_by_css()
        admin_setup.categories.ctg_name_inp.send_data_by_css(NAME_FOR_EDIT)
        admin_setup.categories.cancel_ctg_btn.click_btn_by_index_css(ctg_row_index)
    with allure.step("Check that name wasn't changed"):
        assert expected_result == admin_setup.categories.ctg_name.get_element_text_by_index(ctg_row_index),\
            "category was changed"
    with allure.step("TearDown"):
        admin_setup.categories.delete_ctg_btn.click_btn_by_index_css(ctg_row_index)


@allure.title("Test delete category:")
@allure.severity(Severity.NORMAL)
def test_delete_category(admin_setup):
    """
        Verify that admin has the ability to delete category
    """
    NAME_OF_CTG = "fun"
    with allure.step("Click find event button and go to admin panel and go categories page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.go_to_page(ADMIN_PANEL)
    with allure.step("SetUp"):
        admin_setup.categories.add_ctg_btn.click_btn_by_css()
        admin_setup.categories.ctg_name_inp.send_data_by_css(NAME_OF_CTG)
        admin_setup.categories.submit_btn.click_btn_by_css()
    with allure.step("Delete existing category"):
        ctg_row_index = admin_setup.categories.row_index.find_element_in_row(NAME_OF_CTG) + 2
        admin_setup.categories.delete_ctg_btn.click_btn_by_index_css(ctg_row_index)
    assert None == admin_setup.categories.row_index.find_element_in_row(NAME_OF_CTG), \
        "category wasn't deleted"

