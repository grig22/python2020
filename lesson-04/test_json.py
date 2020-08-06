import pytest
import requests
from jsonschema import validate
# import json


g_post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    }
}

g_userid_schema = {
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
        "items": g_post_schema
    }
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    res_json = res.json()
    validate(instance=res_json, schema=schema)


def userids():
    schema = {
        "type": "array",
        "minItems": 10,
        "maxItems": 10,
        "items": g_userid_schema
    }
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    res_json = res.json()
    validate(instance=res_json, schema=schema)
    ids = set()
    for user in res_json:
        ids.add(user["id"])
    return ids


@pytest.mark.parametrize("userid", userids())
def test_create(userid):
    body = {
        "title": "foo",
        "body": "bar",
        "userId": userid
    }
    res = requests.post("https://jsonplaceholder.typicode.com/posts", json=body)
    res_json = res.json()
    assert body.items() <= res_json.items()
    assert res_json["id"] == 101

