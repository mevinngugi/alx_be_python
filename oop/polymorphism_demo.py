"""
 In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle,
 each overriding the area() method to calculate their respective areas.

polymorphism_demo.py:
Base Class - Shape:

Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
Derived Class - Rectangle:

Inherits from Shape.
Attributes: length and width.
Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
Derived Class - Circle:

Inherits from Shape.
Attributes: radius.
Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).
"""
import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        #super().__init__()

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)
