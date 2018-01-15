import math


def init_triangle(x, y, z):
    global a, b, c
    a = x
    b = y
    c = z


def describe_triangle():
    return "a triangle with sides of {}, {} and {}".format(a, b, c)


def area_triangle():
    # Heron's formula
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == '__main__':
    # The global version needs fewer parameters passing around, but using it with
    # multiple triangles is *really* ugly.

    triangles = [(3, 4, 5), (5, 12, 13), (2, 2, 2)]

    for (x, y, z) in triangles:
        # We need to remember to reset the globals every time we want to change triangles!
        # If we have more than one, this is basically a non-starter.
        init_triangle(x, y, z)
        print(describe_triangle(), "has area", area_triangle())

# This is worth editorialising over: when should you do this, and when not?
# If you ever find yourself writing a for loop that repeatedly resets global
# variables, that's a sign that you need a different approach.

# If you truly have a logical 'singleton' - that is, one instance of some idea
# is all you'll need and all parts of the program that refer to it should refer
# to the same copy, this is perhaps an acceptable approach.

# See, for instance, the Python 'logging' module. There is one copy of the
# global logging configuration, referred to by a module-level variable.
# Individual 'Logger' objects may be more than one in number, and thus are
# represented as distinct instances of a class (see the following example).
