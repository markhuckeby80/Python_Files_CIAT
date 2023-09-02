# This class represents a bank account
class CheckingAccount:

    def __init__(self, balance, interest_rate=0):
        self.__balance = balance
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds available")

    def set_interest_rate(self):
        print("Select a market for your interest rate : ")
        print("1. Low Risk Market (1%) ")
        print("2. Medium Risk Market (2%)")
        print("3. High Risk Market (3%)")
        choice = int(input("Enter your choice (1/2/3): "))
        if choice == 1:
            self.__interest_rate = 0.01
        elif choice == 2:
            self.__interest_rate = 0.02
        elif choice == 3:
            self.__interest_rate = 0.03
        else:
            print("Invalid choice. Defaulting to Low Risk Market (1%).")
            self.__interest_rate = 0.01

    def apply_interest(self):
        self.__balance *= (1 + self.__interest_rate)

    def get_balance(self):
        return self.__balance

    def get_interest_rate(self):
        return self.__interest_rate * 100
