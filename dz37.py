from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def get_width_from_square(self, square):
        multipliers = [2, 3, 5, 7, 1]
        for multiplier in multipliers:
            if square % multiplier == 0:
                return multiplier

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_square = self.get_square() + other.get_square()
        new_width = self.get_width_from_square(new_square)
        new_height = new_square / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_width = self.width * sqrt(n)
        new_height = self.height * sqrt(n)
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4

assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("ok")