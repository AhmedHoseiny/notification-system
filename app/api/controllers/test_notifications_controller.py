import requests
from fastapi.encoders import jsonable_encoder
import json

url = "http://localhost:8000"


def test_get_notifications():
    response = requests.get(url + "/api/notifications")
    assert response.status_code == 200


def test_create_notification():
    body = {
        "providers": ["fcm", "sms", "email"],
        "body": "test notification body",
        "receivers": ["60676d092af73ae8d2df9e3b", "60663af8a10b6c3b7dd39582"]
    }
    response = requests.post(url + "/api/notifications",
                             data=json.dumps(body)
                             )
    print(response.json()['body'])
    assert response.status_code == 200
    assert type(response.json()['body']) is str
    assert response.json()['body'] == "test notification body"
