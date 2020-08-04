import pytest
from shape import Square


mysquares = [0, 1, 5, 25, 56.4879, 3190.88284641, 65498.156498465]


@pytest.mark.parametrize("data", mysquares)
def test_name(data):
    s = Square(data)
    assert s.name == "Square"


@pytest.mark.parametrize("data", mysquares)
def test_area(data):
    s = Square(data)
    assert s.area == data ** 2


@pytest.mark.parametrize("data", mysquares)
def test_angles(data):
    s = Square(data)
    assert s.angles == 4


@pytest.mark.parametrize("data", mysquares)
def test_perimeter(data):
    s = Square(data)
    assert s.perimeter == data * 4
