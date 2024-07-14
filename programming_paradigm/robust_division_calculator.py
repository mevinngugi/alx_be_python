def safe_divide(numerator, denominator):
    """A division calculator that robustly handles errors like
    division by zero and non-numeric inputs"""
    try:
        return f"The result of the division is {int(numerator) / int(denominator)}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    #except TypeError:
    #    return "Error: Please enter numeric values only."
