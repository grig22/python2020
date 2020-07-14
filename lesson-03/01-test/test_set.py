import pytest


# 1
def test_isdisjoint():
    se1 = {1, 2, 3}
    se2 = {7, 8, 9}
    assert se1.isdisjoint(se2)


# 2
def test_issubset():
    smol = {10, 20, 30}
    huge = {350, 10, 450, 20, 550, 30}
    assert smol.issubset(huge)


# 3
def test_issuperset():
    huge = {100, 200, 300, 400, 500, 600}
    smol = {600}
    assert huge.issuperset(smol)


# 4
def test_union():
    se1 = {11, 22, 33}
    se2 = {777, 999}
    assert se1.union(se2) == {11, 777, 22, 999, 33}


# 5
@pytest.mark.parametrize("other, result", [({11, 22}, {22}), ({11, 22, 33}, {22, 33}), ({44}, {44})])
def test_intersection(other, result):
    se = {22, 33, 44, 55}
    assert se.intersection(other) == result
