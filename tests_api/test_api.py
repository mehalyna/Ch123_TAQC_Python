from json import dumps
import json
import requests
from http import HTTPStatus
import config


def test_login():
    response = requests.post(config.URL_LOGIN['login'],
                             data=json.dumps(config.LOGIN_PAYLOADS['payload_admin']),
                             headers=config.HEADER['header'])
    assert response.status_code == 200


def test_api_create_category(header_admin):
    responce = requests.post(config.URL_CATEGORY['create'],
                             headers=header_admin,
                             json={'name': 'Cin'})
    print(responce.text)
    assert responce.status_code == 200


def test_api_edit_category(api_app):
    api_app.get_header_login_admin("admin@gmail.com",
            "1qaz1qaz")
    res = api_app.get_category_payload()
    assert res.status_code == 200
    categories = res.json()
    mount_categori = [category for category in categories if category["name"] == "Moun"][0]
    id = mount_categori['id']
    payload = {
        'id': id,
        'name': 'Mount'
    }
    response = api_app.edit_category(payload=payload)
    responce1 = api_app.get_category_payload()
    categories = res.json()
    mount_new = [category for category in categories if category["name"] == "Mount"][0]
    assert responce1.status_code == 200
    assert id == mount_new['id']
    #responce = requests.post(config.URL_CATEGORY['url_edit'], headers=header_admin, json={'name': 'Cin'})


def test_edit_username(header_admin):
    responce = requests.post(config.URL_USER['changeUsername'], headers=header_admin,json={'name':'Admin'})
    assert responce.status_code == 200

def test_all_categories(header_admin,category_payload):

    responce = requests.get(config.URL_CATEGORY['create'],headers=header_admin,json=category_payload )





