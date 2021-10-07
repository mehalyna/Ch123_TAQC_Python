import requests
import config
import json



class App:

    def __init__(self, base_url):
        self.header = None
        self.base_url = base_url


    def login(self):
        payload = {
            'email': config.ADMIN_EMAIL,
            'password': config.ADMIN_PASS
        }
        res = requests.post("https://eventsexpress-test.azurewebsites.net/api/Authentication/Login", json=payload)
        # s.headers.update({'authorization': json.loads(res.content)['token']})
        j = res.json()
        self.header = {
            'Authorization': 'Bearer ' + j['token'],
            'Content-Type': 'application/json'
        }

    def get_header_login_admin(self, mail, password):
        payload = {
            'email': mail,
            'password': password
        }
        url = self.base_url + config.URL_LOGIN['login']
        res = requests.post(url=url,json=payload)
        h = res.json()
        auth = h['token']
        self.header = {
            "Authorization": "Bearer " + auth,
            "Content-Type": "application/json"}

        #return header
    def edit_category(self, payload):
        res = requests.post(url=config.URL_CATEGORY['edit'],headers=self.header, json=payload)

    def get_id_for_category(self):
        res = requests.get(config.URL_CATEGORY['get_all'],)

    def get_category_id(self, category_name):
        responce = requests.get(config.URL_CATEGORY['get_all'])
        categories = responce.json()
        # categories_name = [category['name'] for category in categories]
        for category in categories:
            if category['name'] == category_name:
                idd = category['id']
                return idd
            else:
                return

    def get_category_payload(self):
        responce = requests.get(config.URL_CATEGORY['get_all'],headers=self.header)
        return responce




