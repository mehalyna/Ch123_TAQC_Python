import allure
from allure_commons.types import Severity
import config
from http import HTTPStatus

TEST_NAME = "Test101"
TEST_NAME_REPLACE = "Test007"
ADMIN_NAME = "Admin"
BIRTHDAY_DATE = "2001-05-29"
TEST_ID_CATEGORIES_CI = "c13bae28-178c-4e80-3fbb-08d98a5f09b7"
TEST_NAME_CATEGORIES_CI = "Ci"


@allure.title("User has the ability to login in EventExpress site")
@allure.severity(Severity.NORMAL)
def test_login(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert HTTPStatus.OK == res.status_code


@allure.title("Admin has the ability to see all categories in EventExpress site")
@allure.severity(Severity.NORMAL)
def test_api_get_category(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert HTTPStatus.OK == res.status_code


@allure.title("Admin has the ability to create a new category")
@allure.severity(Severity.NORMAL)
def test_api_create_category(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK
    payload = {
        'name': TEST_NAME
    }
    res = api_app.create_category(payload=payload)
    assert HTTPStatus.OK == res.status_code


@allure.title("Admin has the ability to edit category")
@allure.severity(Severity.NORMAL)
def test_api_edit_category(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK
    categories = res.json()
    mount_category = [category for category in categories if category["name"] == TEST_NAME][0]
    id = mount_category['id']
    payload = {
        'id': id,
        'name': TEST_NAME_REPLACE
    }
    api_app.edit_category(payload=payload)
    res = api_app.get_category()
    mount_new = get_category_id_by_name(res, TEST_NAME_REPLACE)
    assert HTTPStatus.OK == res.status_code
    assert id == mount_new


@allure.title("Admin has the ability to delete category")
@allure.severity(Severity.NORMAL)
def test_api_delete_category(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_category()
    assert res.status_code == HTTPStatus.OK
    id = get_category_id_by_name(res, TEST_NAME_REPLACE)
    res = api_app.delete_category(payload=id)
    assert HTTPStatus.OK == res.status_code


@allure.title("Admin has the ability to get profile info")
@allure.severity(Severity.NORMAL)
def test_api_get_user_info(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_profile_info()
    assert HTTPStatus.OK == res.status_code


@allure.title("Admin has the ability to get profile info about user categories")
@allure.severity(Severity.NORMAL)
def test_api_get_user_categories(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    res = api_app.get_profile_user_categories()
    assert HTTPStatus.OK == res.status_code


@allure.title("Admin has the ability to edit username")
@allure.severity(Severity.NORMAL)
def test_api_edit_username(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        'name': ADMIN_NAME
    }
    res = api_app.edit_username(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_info().json()
    assert ADMIN_NAME == res["name"]


@allure.title("Admin has the ability to edit user birthday info")
@allure.severity(Severity.NORMAL)
def test_api_edit_birthday(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        'birthday': BIRTHDAY_DATE
    }
    res = api_app.edit_birthday(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_info().json()
    assert BIRTHDAY_DATE in res["birthday"]


@allure.title("Admin has the ability to edit user gender info")
@allure.severity(Severity.NORMAL)
def test_api_edit_gender(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        'gender': 2
    }
    res = api_app.edit_gender(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_info().json()
    assert 2 == res["gender"]


@allure.title("Admin has the ability to edit user categories info")
@allure.severity(Severity.NORMAL)
def test_api_edit_user_category(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        "categories": [{
            'id': TEST_ID_CATEGORIES_CI,
            'name': TEST_NAME_CATEGORIES_CI,
            'countOfUser': 0,
            'countOfEvents': 0
        }]
    }
    res = api_app.edit_user_category(payload=payload)
    assert res.status_code == HTTPStatus.OK
    categories = api_app.get_profile_user_categories().json()
    mount_category = [category for category in categories if category["name"] == TEST_NAME_CATEGORIES_CI][0]
    assert TEST_NAME_CATEGORIES_CI == mount_category['name']


@allure.title("Admin has the ability to clean user categories info")
@allure.severity(Severity.NORMAL)
def test_api_edit_user_category_clean(api_app):
    api_app.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    payload = {
        "categories": []
    }
    res = api_app.edit_user_category(payload=payload)
    assert res.status_code == HTTPStatus.OK
    res = api_app.get_profile_user_categories().json()
    assert 0 == len(res)


def get_category_id_by_name(res, name):

    """
        Method GET for get category id by name category.
        Return response with results of request.
    """
    categories = res.json()
    mount_category = [category for category in categories if category["name"] == name][0]
    id = mount_category['id']
    return id