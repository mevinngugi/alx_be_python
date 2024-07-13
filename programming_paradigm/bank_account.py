class BankAccount:
    """A BankAccount class that encapsulates banking operations"""
    def __init__(self, account_balance = 0):
        try:
            self.account_balance = float(account_balance)
        except ValueError:
            print("Invalid account balance provided. Please provide an interger")


    def deposit(self, amount):
        """Adds specified ammount to account balance """
        try:
            self.account_balance += amount
            return self.account_balance
        except TypeError:
            return "Invalid amount"

    def withdraw(self, amount):
        """Deducts specified amount from account balance.
            If funds are sufficient return True else False
        """
        try:
            if amount > self.account_balance:
                return False
            self.account_balance -= amount
            return self.account_balance
        except TypeError:
            return "Invalid amount"

    def display_balance(self):
        """Displays the account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")
