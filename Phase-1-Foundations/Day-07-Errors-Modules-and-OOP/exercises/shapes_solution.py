"""
Exercise 3 — Shapes & Inheritance (solution).

Run:
    python shapes_solution.py
"""

import math


class Shape:                       # base class
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0                   # placeholder; subclasses override this


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")   # reuse parent setup (sets self.name)
        self.width = width
        self.height = height

    def area(self):                # override
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Rectangle):           # stretch: a Square IS-A Rectangle
    def __init__(self, side):
        super().__init__(side, side)    # a square is a rectangle with equal sides
        self.name = "Square"


# One list, many shape types — the loop doesn't care which is which (polymorphism):
shapes = [Rectangle(4, 5), Circle(3), Square(2)]
for shape in shapes:
    print(f"{shape.name:<10} area = {shape.area():.2f}")
