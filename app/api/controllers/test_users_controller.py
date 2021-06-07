import requests
import json

url = "http://localhost:8000"


def test_get_users():
    response = requests.get(url + "/api/users")
    assert response.status_code == 200


def test_create_user():
    body = {
        "name": "test",
        "email": "test@gmail.com"
    }
    response = requests.post(url + "/api/users",
                             data=json.dumps(body)
                             )
    assert response.status_code == 200
    assert type(response.json()['name']) is str
    assert response.json()['name'] == "test"
    assert type(response.json()['email']) is str
    assert response.json()['email'] == "test@gmail.com"
