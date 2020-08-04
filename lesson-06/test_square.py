from shape import Square


def test_square_area():
    s = Square(10)
    assert s.area == 100


def test_square_add():
    s1 = Square(10)
    s2 = Square(5)
    assert s1.add_square(s2) == 125

