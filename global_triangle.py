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