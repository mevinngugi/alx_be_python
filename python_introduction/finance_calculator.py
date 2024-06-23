'''
Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on
a user’s monthly savings and potential future savings without applying conditional statements.

Task Description:

You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings
based on inputted monthly income and expenses. It will then project these savings over a year,
assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

Instructions:

User Input for Financial Details:

1. Prompt the user for their monthly income: “Enter your monthly income: ”.
2. Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
3. Calculate Monthly Savings:
    Calculate the monthly savings by subtracting monthly expenses from the monthly income.
4. Project Annual Savings:
    Assume a simple annual interest rate of 5%.
    Calculate the projected savings after one year, incorporating the interest.
    Use the simplified formula for annual savings projection:
    (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).

Output Results:

Display the user’s monthly savings.
Display the projected annual savings after including interest.
Example Interaction:

Enter your monthly income: 5000
Enter your total monthly expenses: 4000
Your monthly savings are $1000.
Projected savings after one year, with interest, is: $12600.
'''
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income - monthly_expenses)
anual_savings = monthly_savings * 12
projected_savings = anual_savings + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

