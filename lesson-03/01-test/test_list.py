import pytest


# 1
def test_append():
    ls = [1, 2, 3]
    a = 4
    ls.append(a)
    assert ls == [1, 2, 3, 4]


# 2
def test_extend():
    ls1 = [1, 2, 3]
    ls2 = [4, 5, 6]
    ls1.extend(ls2)
    assert ls1 == [1, 2, 3, 4, 5, 6]


# 3
def test_insert():
    ls = ['a', 'b', 'd']
    ls.insert(2, 'c')
    assert ls == ['a', 'b', 'c', 'd']


# 4
def test_remove():
    ls = [111, 222, 333, 444, 555]
    ls.remove(444)
    assert ls == [111, 222, 333, 555]


# 5
@pytest.mark.parametrize("pos, exp", [(1, 911), (2, 922), (3, 933)])
def test_pop(pos, exp):
    ls = [900, 911, 922, 933]
    val = ls.pop(pos)
    assert val == exp
