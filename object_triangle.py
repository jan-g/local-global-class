import math

class Triangle:
    # we've renamed init_triangle
    # __init__ is 'magically' called when we construct an instance

    def __init__(self, a, b, c):
        # the 'self' reference gives us access to a separate namespace from
        # local and global variables.
        # They don't clash because they're written differently!
        self.a = a
        self.b = b
        self.c = c

    # We've renamed describe_triangle
    # __str__ is 'magically' called when Python wants a string representation -
    # either implicitly (via print) or explicitly (via str(...))

    def __str__(self):
        return "a triangle with sides of {}, {} and {}".format(self.a, self.b, self.c)

    def area(self):
        # Heron's formula
        # Python uses this explicit "self." notation. Some other languages
        # (the ones that are statically compiled in particular) are
        # more cunning in their name resolution for identifiers
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


if __name__ == '__main__':
    # Note: if we don't guard this bit with the above if statement, then it'll
    # *also* be run when importing this module from piece_de_resistance.


    # The class-based version constructs multiple instances. Each instance has its
    # own set of attributes.

    triangles = [Triangle(3, 4, 5), Triangle(5, 12, 13), Triangle(2, 2, 2)]

    for t in triangles:
        # The syntax here is different. The variable t refers to the object as a whole.
        # We can call methods implicitly (such as when Python tries to form a string
        # representation of the object) or explicitly.
        print(t, "has area", t.area())