from abc import ABC, abstractmethod
from math import sqrt, pi

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
    def __init__(self, side0, side1, side2):
        self.sides = [side0, side1, side2]
        for side in self.sides:
            assert side > 0
            other_sides = list(self.sides)
            other_sides.remove(side)
            assert side < sum(other_sides)

    @property
    def area(self):
        # используем Формулу Герона
        semiper = self.perimeter / 2
        p = semiper
        for side in self.sides:
            p *= (semiper - side)
        return sqrt(p)

    @property
    def angles(self):
        return 3

    @property
    def perimeter(self):
        return sum(self.sides)


class Rectangle(Shape):

    def __init__(self, side0, side1):
        self.sides = [side0, side1]
        for side in self.sides:
            assert side > 0

    @property
    def area(self):
        return self.sides[0] * self.sides[1]

    @property
    def angles(self):
        return 4

    @property
    def perimeter(self):
        return sum(self.sides) * 2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        assert self.radius > 0

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def angles(self):
        return 0

    @property
    def perimeter(self):
        return 2 * pi * self.radius
