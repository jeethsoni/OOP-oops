"""
Encapsulation
"""


class BankAccount:
    """BankAccount class to control deposits and withdraws"""

    # initializing the attribute
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self.account_holder = account_holder

    # deposit method to deposit the money
    def deposit(self, amount):
        """depositing money into the account"""

        total = self.__balance + amount
        return total

    # withdraw method to withdraw money
    def withdraw(self, amount):
        """withdrawing money from the account"""

        if self.__balance >= amount:
            total = self.__balance - amount
            return total
        else:
            print("insufficient balance")
