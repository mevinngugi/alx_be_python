def perform_operation(num1, num2, operation):
    """
    Parameters: 
        num1 (float),
        num2 (float),
        and operation (string). 
        The operation parameter accepts four possible values:
            'add', 'subtract', 'multiply', or 'divide'.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Sorry. You can't divide a number by zero."
        else:
            return num1 / num2
    else:
        return "Sorry our calculator only accepts 'add', 'subtract', 'multiply', or 'divide' at the moment"
