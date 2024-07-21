"""
Objective: Solidify your understanding of class methods and
static methods in Python by implementing examples of each in a class,
demonstrating their usage and differences.
"""


class Calculator:
    """
    a class Calculator that includes both a class method and
        a static method to perform calculations
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {Calculator.calculation_type}")
        return a * b


print(Calculator.multiply(2, 5))
