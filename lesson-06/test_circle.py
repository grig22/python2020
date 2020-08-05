import pytest
from shape import Circle
from math import pi


circles = [1, 100, 0.0000000000087654765, 546589987909547658, 25, 868897.0000000000876585]


@pytest.mark.parametrize("data", circles)
def test_name(data):
    c = Circle(data)
    assert c.name == "Circle"


@pytest.mark.parametrize("data", circles)
def test_area(data):
    c = Circle(data)
    assert c.area == pi * data * data


@pytest.mark.parametrize("data", circles)
def test_angles(data):
    c = Circle(data)
    assert c.angles == 0


@pytest.mark.parametrize("data", circles)
def test_perimeter(data):
    c = Circle(data)
    assert c.perimeter == 2 * pi * data
