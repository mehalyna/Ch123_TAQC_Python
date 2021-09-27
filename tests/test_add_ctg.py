import config

#Testing the 'Categories' page

CTG_PAGE = "Categories"
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASS = "1qaz1qaz"
name_of_ctg = "fun"


def test_ctg_add(app):
    """
        Verify that admin have ability add new category
    """
    expected_result = not None
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page(CTG_PAGE)
    app.categories.add_ctg_btn.click_btn_by_css()
    app.categories.ctg_name_inp.send_data(name_of_ctg)
    app.categories.submit_btn.click_btn_by_css()
    assert expected_result == app.categories.row_index.find_element_in_row(name_of_ctg), \
        "category {} wasn't added".format(name_of_ctg)


def test_edit_ctg(app):
    """
        Verify that admin have ability to edit exist category
    """
    expected_result = "funny"
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page(CTG_PAGE)
    idx = app.categories.row_index.find_element_in_row("fun")
    app.categories.edit_ctg_btn.click_btn_by_index_css(idx)
    app.categories.ctg_name_inp.send_data("funny")
    app.categories.submit_btn.click_btn_by_css()
    assert expected_result == app.categories.ctg_name.get_element_text_by_index(idx), \
        "category wasn't edited"

def test_cancel_changes(app):
    expected_result = "funny"
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page(CTG_PAGE)
    idx = app.categories.row_index.find_element_in_row("funny")
    app.categories.edit_ctg_btn.click_btn_by_index_css(idx)
    app.categories.ctg_name_inp.send_data("funny_new")
    app.categories.cancel_ctg_btn.click_btn_by_index_css(idx)
    assert  expected_result == app.categories.ctg_name.get_element_text_by_index(idx),\
        "category was changed"

def test_delete_ctg(app):
    expected_result = None
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page(CTG_PAGE)
    idx = app.categories.row_index.find_element_in_row("funny")
    app.categories.delete_ctg_btn.click_btn_by_index_css(idx)
    assert expected_result == app.categories.row_index.find_element_in_row("funny"),\
        "category wasn't deleted"


