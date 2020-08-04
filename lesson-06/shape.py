class Shape:

    @property
    def name(self):
        return self.__class__.__name__


class Triangle(Shape):
    pass


s = Shape()
t = Triangle()

print(s.name)
print(t.name)
