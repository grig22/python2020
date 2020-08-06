import pytest
import requests
from jsonschema import validate


def test_schema_posts():
    schema = {
        "type": "array",
        "minItems": 100,
        "maxItems": 100,
        "items": {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "body": {"type": "string"},
            }
        }
    }
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    res_json = res.json()
    validate(instance=res_json, schema=schema)
