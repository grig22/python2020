import pytest


# 1
def test_split():
    st = "things falling apart"
    sp = st.split()
    assert sp[1] == "falling" and sp[2] == "apart"


# 2
def test_replace():
    st = "All the king's horses and all the king's men"
    sr = st.replace("king", "president")
    assert sr == "All the president's horses and all the president's men"


# 3
def test_partition():
    st = "collector@google.com"
    sp = st.partition("@")
    assert sp[0] == "collector"


# 4
def test_count():
    st = """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be nine green bottles hanging on the wall."""
    assert st.count("bottle") == 4


# 5
@pytest.mark.parametrize("addr", ["google.com", "yandex.ru", "whitehouse.gov"])
def test_endswith(addr):
    assert addr.endswith(("gov", "com", "ru"))
