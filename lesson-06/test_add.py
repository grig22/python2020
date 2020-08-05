import pytest
from shape import Square, Rectangle, Triangle, Circle


class BadShape:
    def __init__(self, a):
        self.a = a

    @property
    def area(self):
        return self.a


figure_set_one = [Square(58.095), Rectangle(0.000887799, 44), Triangle(22.00001, 22.001, 22.1), Circle(900000234)]
figure_set_two = [Square(1), Rectangle(999993242, 555), Triangle(78.956, 112.44, 96.928), Circle(5667.00938),
                  pytest.param(BadShape(4444), marks=pytest.mark.xfail)]


@pytest.mark.parametrize("f1", figure_set_one)
@pytest.mark.parametrize("f2", figure_set_two)
def test_add(f1, f2):
    a1 = f1.area
    a2 = f2.area
    assert f1.add_square(f2) == a1 + a2
