import pytest
import requests
from jsonschema import validate
# import json


class SCHEMA:
    POST = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId", "id", "title", "body"]
    }

    USERID = {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
            },
            "required": ["id"]
        }


def test_schema_posts():
    schema = {
        "type": "array",
        "minItems": 100,
        "maxItems": 100,
        "items": SCHEMA.POST
    }
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    res_json = res.json()
    validate(instance=res_json, schema=schema)


def userids():
    schema = {
        "type": "array",
        "minItems": 10,
        "maxItems": 10,
        "items": SCHEMA.USERID
    }
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    res_json = res.json()
    validate(instance=res_json, schema=schema)
    ids = set()
    for user in res_json:
        ids.add(user["id"])
    assert ids
    return ids


@pytest.mark.parametrize("userid", userids())
def test_create(userid):
    body = {
        "title": "Тестирование REST сервиса 3",
        "body": "Тесты должны успешно проходить.",
        "userId": userid
    }
    res = requests.post("https://jsonplaceholder.typicode.com/posts", json=body)
    res_json = res.json()
    assert body.items() <= res_json.items()
    assert res_json["id"] == 101

