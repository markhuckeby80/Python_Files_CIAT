class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Accessor Method
    def get_balance(self):
        return self.balance

    # Mutator Method
    def deposit(self, amount):
        self.balance += amount


# Create a new BankAccount object
account = BankAccount(1000)

# Using Accessor Method
current_balance = account.get_balance()
print("Current Balance:", current_balance)

# Using Mutator Method
account.deposit(200)
print("New Balance:", account.get_balance())
