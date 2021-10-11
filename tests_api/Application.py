import requests
import config


class App:
    """
        Wrapper class for API tests
    """
    def __init__(self):
        self.header = None
        self.base_url = config.BASE_URL

    def login(self, mail, password):
        """
            Method POST for creating a header with 'login' URL and get authorize token.
        """
        payload = {
            'email': mail,
            'password': password
        }
        url = self.base_url + config.URL_LOGIN['login']
        res = requests.post(url=url, json=payload)
        h = res.json()
        auth = h['token']
        self.header = {
            "Authorization": "Bearer " + auth,
            "Content-Type": "application/json"}

    def get_category(self):
        """
            Method GET for getting category request.
            Return response with results of request.
        """
        url = self.base_url + config.URL_CATEGORY['get_all']
        res = requests.get(url=url, headers=self.header)
        return res

    def create_category(self, payload):
        """
            Method POST for creating new category request by payload.
            Return response with results of request.
        """
        url = self.base_url + config.URL_CATEGORY['create']
        res = requests.post(url=url, headers=self.header, json=payload)
        return res

    def edit_category(self, payload):
        """
             Method POST for edit category name by payload.
             Return response with results of request.
        """
        url = self.base_url + config.URL_CATEGORY['edit']
        res = requests.post(url=url, headers=self.header, json=payload)
        return res

    def delete_category(self, payload):
        """
             Method POST for delete category name by payload.
             Return response with results of request.
        """
        url = self.base_url + config.URL_CATEGORY['delete'] + payload
        res = requests.post(url=url, headers=self.header)
        return res

    def get_profile_info(self):
        """
             Method GET for get profile info.
             Return response with results of request.
        """
        url = self.base_url + config.URL_USER['getUserInfo']
        res = requests.get(url=url, headers=self.header)
        return res

    def get_profile_user_categories(self):
        """
             Method GET for get profile user info about categories.
             Return response with results of request.
        """
        url = self.base_url + config.URL_USER['getCategories']
        res = requests.get(url=url, headers=self.header)
        return res

    def edit_username(self, payload):
        """
             Method POST for edit username in profile info by payload.
             Return response with results of request.
        """
        url = self.base_url + config.URL_USER['editUsername']
        res = requests.post(url=url, headers=self.header, json=payload)
        return res

    def edit_birthday(self, payload):
        """
             Method POST for edit birthday date in profile info by payload.
             Return response with results of request.
        """
        url = self.base_url + config.URL_USER['editBirthday']
        res = requests.post(url=url, headers=self.header, json=payload)
        return res

    def edit_gender(self, payload):
        """
             Method POST for edit gender in profile info by payload.
             Return response with results of request.
        """
        url = self.base_url + config.URL_USER['editGender']
        res = requests.post(url=url, headers=self.header, json=payload)
        return res

    def edit_user_category(self, payload):
        """
             Method POST for edit favorite categories in profile info by payload.
             Return response with results of request.
        """
        url = self.base_url + config.URL_USER['editUserCategory']
        res = requests.post(url=url, headers=self.header, json=payload)
        return res
