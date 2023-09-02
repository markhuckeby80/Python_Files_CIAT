# This program imports the simulation module and
# creates three instances of the Coin class.

import bankaccount

def main():
    # Creates three objects from the BankAccount class.
    start_bal = float(input('Enter your starting balance: '))
    account1 = bankaccount.BankAccount(start_bal)
    start_bal = float(input('Enter your starting balance: '))
    account2 = bankaccount.BankAccount(start_bal)
    start_bal = float(input('Enter your starting balance: '))
    account3 = bankaccount.BankAccount(start_bal)

    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    account1.deposit(pay)
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    account2.deposit(pay)
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    account3.deposit(pay)

    # Display the balance.
    print(f'Your account1 balance is ${account1.get_balance():,.2f}.')
    # Display the balance.
    print(f'Your account2 balance is ${account2.get_balance():,.2f}.')
    # Display the balance.
    print(f'Your account3 balance is ${account3.get_balance():,.2f}.')

    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    account1.withdraw(cash)
    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    account2.withdraw(cash)
    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    account3.withdraw(cash)

    # Display the balance.
    print(f'Your account1 balance is ${account1.get_balance():,.2f}.')
    print(f'Your account2 balance is ${account2.get_balance():,.2f}.')
    print(f'Your account3 balance is ${account3.get_balance():,.2f}.')


# Call the main function.
if __name__ == '__main__':
    main()