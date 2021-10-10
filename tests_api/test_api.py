import allure
from allure_commons.types import Severity
import config
from http import HTTPStatus


@allure.title("User has the ability to login in EventExpress site")
@allure.severity(Severity.NORMAL)
def test_login(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK


@allure.title("Admin has the ability to see all categories in EventExpress site")
@allure.severity(Severity.NORMAL)
def test_api_get_category(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK


@allure.title("Admin has the ability to create a new category")
@allure.severity(Severity.NORMAL)
def test_api_create_category(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK
    payload = {
        'name': 'Test101'
    }
    res = api_app.create_category(payload=payload)
    assert res.status_code == HTTPStatus.OK


@allure.title("Admin has the ability to edit category")
@allure.severity(Severity.NORMAL)
def test_api_edit_category(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK
    categories = res.json()
    mount_category = [category for category in categories if category["name"] == "Test101"][0]
    id = mount_category['id']
    payload = {
        'id': id,
        'name': 'Test007'
    }
    api_app.edit_category(payload=payload)
    res = api_app.get_category()
    mount_new = api_app.get_category_id_by_name(res, "Test007")
    assert res.status_code == HTTPStatus.OK
    assert id == mount_new


@allure.title("Admin has the ability to delete category")
@allure.severity(Severity.NORMAL)
def test_api_delete_category(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK
    id = api_app.get_category_id_by_name(res, "Test007")
    res = api_app.delete_category(payload=id)
    assert res.status_code == HTTPStatus.OK


@allure.title("Admin has the ability to get profile info")
@allure.severity(Severity.NORMAL)
def test_api_get_user_info(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_profile_info()
    assert res.status_code == HTTPStatus.OK


@allure.title("Admin has the ability to get profile info about user categories")
@allure.severity(Severity.NORMAL)
def test_api_get_user_categories(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_profile_user_categories()
    assert res.status_code == HTTPStatus.OK


@allure.title("Admin has the ability to edit username")
@allure.severity(Severity.NORMAL)
def test_api_edit_username(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        'name': 'Admin'
    }
    res = api_app.edit_username(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_info().json()
    assert res["name"] == "Admin"


@allure.title("Admin has the ability to edit user birthday info")
@allure.severity(Severity.NORMAL)
def test_api_edit_birthday(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        'birthday': '2001-05-29'
    }
    res = api_app.edit_birthday(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_info().json()
    assert "2001-05-29" in res["birthday"]


@allure.title("Admin has the ability to edit user gender info")
@allure.severity(Severity.NORMAL)
def test_api_edit_gender(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        'gender': 2
    }
    res = api_app.edit_gender(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_info().json()
    assert res["gender"] == 2


@allure.title("Admin has the ability to edit user categories info")
@allure.severity(Severity.NORMAL)
def test_api_edit_user_category(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        "categories": [{
            'id': "c13bae28-178c-4e80-3fbb-08d98a5f09b7",
            'name': "Ci",
            'countOfUser': 0,
            'countOfEvents': 0
        }]
    }
    res = api_app.edit_user_category(payload=payload)
    assert res.status_code == HTTPStatus.OK
    categories = api_app.get_profile_user_categories().json()
    mount_category = [category for category in categories if category["name"] == "Ci"][0]
    assert mount_category['name'] == "Ci"


@allure.title("Admin has the ability to clean user categories info")
@allure.severity(Severity.NORMAL)
def test_api_edit_user_category_clean(api_app):
    api_app.get_header_login_admin(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        "categories": []
    }
    res = api_app.edit_user_category(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_user_categories().json()
    assert len(res) == 0
