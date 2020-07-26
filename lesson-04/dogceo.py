import pytest
import requests


def test_random_image():
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    res_json = res.json()
    assert res_json["status"] == "success"


def breeds():
    res = requests.get("https://dog.ceo/api/breeds/list/all")
    res_json = res.json()
    assert res_json["status"] == "success"
    msg = res_json["message"]
    assert type(msg) is dict
    assert msg
    return msg


def all_breeds():
    return breeds().keys()


def breeds_with_subs():
    res = []
    for key, val in breeds():
        if val:
            res.append(key)
    assert res
    return res


@pytest.mark.parametrize("breed", breeds())
def test_by_breed(breed):
    t = "111{}222".format("finnish")
    assert t == "111finnish222"
    addr = "https://dog.ceo/api/{}/hound/images".format("finnish")
    # res = requests.get("https://dog.ceo/api/{}/hound/images".format('finnish'))
    res = requests.get(addr)
    res_json = res.json()
    # assert res_json["status"] == "success"
    # msg = res_json["message"]
    # assert type(msg) is list
    # assert msg
