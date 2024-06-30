number = int(input("Enter a number to see its multiplication table:"))
for iteration in range(1,11):
    ans = number * iteration
    print(f"{number} * {iteration} = {ans}")