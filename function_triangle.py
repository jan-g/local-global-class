import math


def describe_triangle(a, b, c):
    return "a triangle with sides of {}, {} and {}".format(a, b, c)


def area_triangle(a, b, c):
    # Heron's formula
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == '__main__':

    # The function version is easy to use with multiple sets of data

    triangles = [(3, 4, 5), (5, 12, 13), (2, 2, 2)]

    for (x, y, z) in triangles:
        print(describe_triangle(x, y, z), "has area", area_triangle(x, y, z))