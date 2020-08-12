import pytest
import requests
from jsonschema import validate


def brew_schema():
    brewery = {
        "type": "object",
        "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": "string"},
                "latitude": {"type": "string"},
                "phone": {"type": "string"},
                "website_url": {"type": "string"},
                "updated_at": {"type": "string"},
        },
        "required": [],
        "additionalProperties": False
    }
    brewery["required"] = list(brewery["properties"].keys())
    schema = {
        "type": "array",
        "items": brewery
    }
    return schema


@pytest.fixture(scope="session")
def fetch_breweries():
    res = requests.get("https://api.openbrewerydb.org/breweries")
    return res.json()


def test_schema(fetch_breweries):
    validate(instance=fetch_breweries, schema=brew_schema())
