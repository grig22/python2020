import pytest
from shape import Rectangle


rectangles = [[1, 2], [0.00087865, 876576487.76876], [55, 76587.22], [423423.000000000033, 34536345324532]]


@pytest.mark.parametrize("data", rectangles)
def test_name(data):
    r = Rectangle(data[0], data[1])
    assert r.name == "Rectangle"


@pytest.mark.parametrize("data", rectangles)
def test_area(data):
    r = Rectangle(data[0], data[1])
    assert r.area == data[0] * data[1]


@pytest.mark.parametrize("data", rectangles)
def test_angles(data):
    r = Rectangle(data[0], data[1])
    assert r.angles == 4


@pytest.mark.parametrize("data", rectangles)
def test_perimeter(data):
    r = Rectangle(data[0], data[1])
    assert r.perimeter == data[0] * 2 + data[1] * 2
