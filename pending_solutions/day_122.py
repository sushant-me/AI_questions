"""
Write a program demonstrating encapsulation.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Example usage
acc = BankAccount("John")
acc.deposit(100)
print(acc.get_balance())
acc.withdraw(50)
print(acc.get_balance())
acc.withdraw(60)
print(acc.get_balance())