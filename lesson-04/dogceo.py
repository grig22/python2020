import pytest
import requests


def test_single_random_image():
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    res_json = res.json()
    assert res_json["status"] == "success"


@pytest.mark.parametrize("num", range(1, 51))
def test_multiple_random_images(num):
    res = requests.get("https://dog.ceo/api/breeds/image/random/{}".format(num))
    res_json = res.json()
    assert res_json["status"] == "success"
    assert len(res_json["message"]) == num


def breeds_dict():
    res = requests.get("https://dog.ceo/api/breeds/list/all")
    res_json = res.json()
    assert res_json["status"] == "success"
    msg = res_json["message"]
    assert type(msg) is dict
    assert msg
    return msg


def all_breeds():
    return breeds_dict().keys()


@pytest.mark.parametrize("breed", all_breeds())
def test_by_breed(breed):
    res = requests.get("https://dog.ceo/api/breed/{}/images".format(breed))
    res_json = res.json()
    assert res_json["status"] == "success"
    msg = res_json["message"]
    assert type(msg) is list
    assert msg


def breeds_with_subs():
    res = []
    for key, val in breeds_dict().items():
        if val:
            res.append(key)
    assert res
    return res


@pytest.fixture(scope="session")
def breeds_dict_fix():
    return breeds_dict()


@pytest.mark.parametrize("breed", breeds_with_subs())
def test_sub_breeds(breed, breeds_dict_fix):
    res = requests.get("https://dog.ceo/api/breed/{}/list".format(breed))
    res_json = res.json()
    assert res_json["status"] == "success"
    msg = res_json["message"]
    assert msg == breeds_dict_fix[breed]


def test_error():
    res = res = requests.get("https://dog.ceo/api/breed/bhairava/images")
    res_json = res.json()
    assert res_json["status"] == "error"
