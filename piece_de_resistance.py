import math
from object_triangle import Triangle

class Circle:
    def __init__(self, r):
        # Different classes of object may have different attributes
        self.r = r

    def __str__(self):
        return "a circle with radius {}".format(self.r)

    def area(self):
        return 2 * math.pi * self.r ** 2


if __name__ == '__main__':
    # Here's a compelling, if more advanced, idea. If each class implements the
    # 'same' method, we can call that method and the correct version will be
    # selected depending upon the object's class.

    shapes = [Triangle(3, 4, 5), Circle(6), Triangle(5, 12, 13)]

    for s in shapes:
        # The syntax here is the same as with the pure triangle approach.
        # This idea has a funky name (polymorphism) but it's one of the bonuses you
        # get from object-orientation over and above the encapsulation of
        # instance data.
        print(s, "has area", s.area())