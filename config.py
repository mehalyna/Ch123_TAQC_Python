"""
    Test data for login as admin.
"""
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASS = "1qaz1qaz"
LANDING_SIGN_IN_BUTTON = "Sign In"
BASE_URL = "https://eventsexpress-test.azurewebsites.net/"
"""
    Test data for api testing.
"""
URL_LOGIN = {
    'login': "api/Authentication/Login",
}

URL_CATEGORY = {
    'get_all': "api/Category/All",
    'create': "api/Category/Create",
    'edit': "api/Category/Edit",
    'delete': "api/Category/Delete/",
}
URL_USER = {
    'getUserInfo': "/api/Users/GetUserInfo",
    'getCategories': "/api/Users/GetCategories",
    'editUsername': "api/Users/EditUsername",
    'editBirthday': "/api/Users/EditBirthday",
    'editGender': "api/Users/EditGender",
    'editUserCategory': "api/Users/EditUserCategory",
    'changeAvatar': "api/Users/ChangeAvatar/",
}
HEADER = {
    'header': {
        'Content-Type': 'application/json'}
}

