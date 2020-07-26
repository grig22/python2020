import pytest
import requests


def test_random_image():
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    assert res.json()["status"] == "success"


def breeds():
    res = requests.get("https://dog.ceo/api/breeds/list/all")
    res_json = res.json()
    assert res_json["status"] == "success"
    return res_json["message"].keys()


@pytest.mark.parametrize("breed", breeds())
def test_by_breed(breed):
    print(breed)

