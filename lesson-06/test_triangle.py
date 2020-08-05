import pytest
from shape import Triangle


triangles = [[3, 4, 5], [22, 22, 22], [0.0000017, 0.0000022, 0.0000034], [367345, 679454, 345732]]


@pytest.mark.parametrize("data", triangles)
def test_name(data):
    t = Triangle(data[0], data[1], data[2])
    assert t.name == "Triangle"


@pytest.mark.parametrize("data", triangles)
def test_area(data):
    p = data[0] + data[1] + data[2]
    p /= 2
    area = (p * (p - data[0]) * (p - data[1]) * (p - data[2])) ** 0.5
    t = Triangle(data[0], data[1], data[2])
    assert t.area == area


@pytest.mark.parametrize("data", triangles)
def test_angles(data):
    t = Triangle(data[0], data[1], data[2])
    assert t.angles == 3


@pytest.mark.parametrize("data", triangles)
def test_perimeter(data):
    t = Triangle(data[0], data[1], data[2])
    assert t.perimeter == data[0] + data[1] + data[2]
