from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    def name(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def angles(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_square(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Надо 'Shape', а это '{}'".format(type(other).__name__))
        return self.area + other.area


class Triangle(Shape):
    pass


class Rectangle(Shape):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def angles(self):
        return 4

    @property
    def perimeter(self):
        return (self.side1 + self.side2) * 2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


class Circle(Shape):
    pass


s = Square(5)
print(s)
print(s.area)
print(s.angles)
print(s.perimeter)

r = Rectangle(10, 20)
print(r)
print(r.area)
print(r.angles)
print(r.perimeter)

print("-------- add")
a = s.add_square(r)
print(a)
