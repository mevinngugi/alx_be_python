task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high" if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "high" if time_bound == "no":
        print(f"Reminder: '{task}' is a high priority task that requires attention later today!")
    case "medium" if time_bound == "yes":
        print(f"Please note: '{task}' is a medium priority task that requires attention later today!")
    case "medium" if time_bound == "no":
        print(f"Please note: '{task}' is a medium priority task that requires attention later today!")
    case "low" if time_bound == "yes":
        print(f"Note: '{task}' is a low priority task. Consider completing later today.")
    case "low" if time_bound == "no":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")