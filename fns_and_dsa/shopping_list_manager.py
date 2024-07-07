def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Please enter the name of the item you would like to add to the shopping list: ")
            shopping_list.append(add_item)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Please enter the name of the item you would like to remove from the shopping list: ")
            if remove_item not in shopping_list:
                print(f"Sorry. {remove_item} is not in the shopping list.")
            else:
                shopping_list.remove(remove_item)
        elif choice == '3':
            # Display the shopping list
            print("Your shopping list has: ")
            for item in shopping_list:
                print("\t" + item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()