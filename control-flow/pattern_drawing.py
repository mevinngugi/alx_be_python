pattern_size = int(input("Enter the size of the pattern:"))
count = 0
while count < pattern_size:
    for x in range(pattern_size):  # Loop for columns within each row
        print("*", end="")
    print()
    count += 1
    