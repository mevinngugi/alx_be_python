num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        ans = num1 + num2
        print(f"The result is {ans}.")
    case "-":
        ans = num1 - num2
        print(f"The result is {ans}.")
    case "*":
        ans = num1 * num2
        print(f"The result is {ans}.")
    case "/" if num2 == 0:
        print("Cannot divide by zero.")
    case "/" if num2 != 0:
        ans = num1 / num2
        print(f"The result is {ans}.")
        