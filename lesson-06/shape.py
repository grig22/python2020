class Shape:

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def area(self):
        return 33

    @property
    def angles(self):
        return 44

    @property
    def perimeter(self):
        return 55

    def add_square(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Надо 'Shape', а это '{}'".format(type(other).__name__))
        return self.area + other.area


class Triangle(Shape):
    pass


class Rectangle(Shape):
    pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2


class Circle(Shape):
    pass


s = Shape()
t = Triangle()

print(s.name)
print(s.area)

print(t.name)
print(t.area)

print(s.add_square(t))
# print(t.add_square([55,66,77,88]))
