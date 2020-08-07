import pytest
import requests
from jsonschema import validate
from copy import deepcopy


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

    USER_ID = {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
            },
            "required": ["id"]
        }


def test_schema_posts():
    posts_in_feed = 100
    schema = {
        "type": "array",
        "minItems": posts_in_feed,
        "maxItems": posts_in_feed,
        "items": SCHEMA.POST
    }
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    res_json = res.json()
    validate(instance=res_json, schema=schema)


def fetch_user_ids():
    users_in_feed = 10
    schema = {
        "type": "array",
        "minItems": users_in_feed,
        "maxItems": users_in_feed,
        "items": SCHEMA.USER_ID
    }
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    res_json = res.json()
    validate(instance=res_json, schema=schema)
    # ids = list()
    # for user in res_json:
    #     ids.append(user["id"])
    ids = [user["id"] for user in res_json]
    assert ids
    return ids


@pytest.mark.parametrize("user_id", fetch_user_ids())
def test_create(user_id):
    body = {
        "title": "Тестирование REST сервиса 3",
        "body": "Тесты должны успешно проходить.",
        "userId": user_id
    }
    res = requests.post("https://jsonplaceholder.typicode.com/posts", json=body)
    res_json = res.json()
    assert body.items() <= res_json.items()
    new_post_id = 101
    assert res_json["id"] == new_post_id


def fetch_post_ids(user_id):
    res = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": user_id})
    ids = list()
    res_json = res.json()
    assert res_json
    for post in res_json:
        validate(instance=post, schema=SCHEMA.POST)
        ids.append(post["id"])
    assert ids
    return ids


some_bodies = ["Тесты должны успешно проходить.",
               "",
               """The C++ Programming Language, Fourth Edition, delivers meticulous,
richly explained, and integrated coverage of the entire language — its facilities,
abstraction mechanisms, standard libraries, and key design techniques.""",
               "HUGE TEXT " * 1024]


@pytest.mark.parametrize("body", some_bodies)
@pytest.mark.parametrize("post_id", fetch_post_ids(fetch_user_ids()[5])[0:2])
def test_patch(post_id, body):
    url = "https://jsonplaceholder.typicode.com/posts/{}".format(post_id)
    old = requests.get(url)
    old_json = old.json()
    validate(instance=old_json, schema=SCHEMA.POST)
    new_json = deepcopy(old_json)
    new_json["body"] = body
    res = requests.patch(url, json=new_json)
    res_json = res.json()
    validate(instance=res_json, schema=SCHEMA.POST)
    assert res_json == new_json


@pytest.mark.parametrize("comment", requests.get("https://jsonplaceholder.typicode.com/comments").json()[0:100:5])
def test_comments(comment):
    post_id = comment["postId"]
    assert comment in requests.get("https://jsonplaceholder.typicode.com/posts/{}/comments".format(post_id)).json()


@pytest.mark.parametrize("post_id", range(1, 121, 5))
def test_two_path(post_id):
    res1 = requests.get("https://jsonplaceholder.typicode.com/posts/{}/comments".format(post_id))
    json1 = res1.json()
    res2 = requests.get("https://jsonplaceholder.typicode.com/comments?postId={}".format(post_id))
    json2 = res2.json()
    assert json1 == json2
    print("POST ID = '{}', len(JSON) = '{}'".format(post_id, len(json2)))
