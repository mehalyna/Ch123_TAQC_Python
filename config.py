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
    'login': "https://eventsexpress-test.azurewebsites.net/api/Authentication/Login",
}

URL_CATEGORY = {
    'get_all': "api/Category/All",
    'create': "api/Category/Create",
    'edit': "api/Category/Edit",
    'delete': "https://eventsexpress-test.azurewebsites.net/api/Category/Delete",
}
URL_USER = {
    'changeUsername':"https://eventsexpress-test.azurewebsites.net/api/Users/EditUsername"
}
HEADER = {
    'header': {
        'Content-Type': 'application/json'}
}
LOGIN_PAYLOADS = {
    'payload_admin': {"Email": "admin@gmail.com", "Password": "1qaz1qaz"},
    'payload_user': {"Email": "mail", "Password": "password"}
}
CATEGORY_PAYLOAD= {
    'edit_category':{
        'id': None,
        'name': None
    }
}
