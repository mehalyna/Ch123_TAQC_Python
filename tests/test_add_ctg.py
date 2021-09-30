"""
Testing the 'Categories' page
"""

import config


NAME_OF_CTG = "fun"
NAME_FOR_EDIT = "funny"
NAME_FOR_CANCEL = "funny_new"


def test_ctg_add(app):
    """
        Verify that the admin has the ability to add a new category.
    """
    app.landing.go_to_site()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Categories")
    app.categories.add_ctg_btn.click_btn_by_css()
    app.categories.ctg_name_inp.send_data(NAME_OF_CTG)
    app.categories.submit_btn.click_btn_by_css()
    assert app.categories.row_index.find_element_in_row(NAME_OF_CTG) is not None, \
        f"category {NAME_OF_CTG} wasn't added"


def test_edit_ctg(app):
    """
        Verify that admin has the ability to edit existing category
    """
    expected_result = "funny"
    app.landing.go_to_site()
    app.modal.login(config., config.admin_pass)
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Categories")
    ctg_row_index = app.categories.row_index.find_element_in_row("fun")
    app.categories.edit_ctg_btn.click_btn_by_index_css(ctg_row_index)
    app.categories.ctg_name_inp.send_data(NAME_FOR_EDIT)
    app.categories.submit_btn.click_btn_by_css()
    assert expected_result == app.categories.ctg_name.get_element_text_by_index(ctg_row_index), \
        "category wasn't edited"


def test_cancel_changes(app):
    """
        Verify that admin has the ability to cancel a changes
    """
    expected_result = "funny"
    app.landing.go_to_site()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Categories")
    ctg_row_index = app.categories.row_index.find_element_in_row("funny")
    app.categories.edit_ctg_btn.click_btn_by_index_css(ctg_row_index)
    app.categories.ctg_name_inp.send_data("funny_new")
    app.categories.cancel_ctg_btn.click_btn_by_index_css(ctg_row_index)
    assert expected_result == app.categories.ctg_name.get_element_text_by_index(ctg_row_index), \
        "category was changed"


def test_delete_ctg(app):
    """
        Verify that admin has the ability to delete category
    """
    expected_result = None
    app.landing.go_to_site()
    app.modal.login(config.admin_email, config.admin_pass)
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Categories")
    ctg_row_index = app.categories.row_index.find_element_in_row("funny")
    app.categories.delete_ctg_btn.click_btn_by_index_css(ctg_row_index)
    assert expected_result == app.categories.row_index.find_element_in_row("funny"), \
        "category wasn't deleted"


