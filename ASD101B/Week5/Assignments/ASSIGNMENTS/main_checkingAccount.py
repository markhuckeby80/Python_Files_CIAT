from border_function import border
import checkingAccount

def main():

    print(border())

    # Display the program's introduction.
    print('Welcome to ACME Bank! ')

    # Display the border
    print(border())

    # Get the starting balance.
    start_bal = float(input('Enter your starting balance in dollars : \n'))
    
    # Create a BankAccount object.
    checking = checkingAccount.CheckingAccount(start_bal)

    print(border())

    # Set the interest rate based on market choice
    checking.set_interest_rate()
    print(f"Interest rate set to {checking.get_interest_rate()}%")

    print(border())

    # Deposit the user's paycheck.
    pay = float(input('How much were you paid this week? \n Enter amount in dollars : \n'))
    print(f'${pay} will be deposited into your account.')
    checking.deposit(pay)

    print(border())

    # Display the balance without interest.
    print(f'Your account balance is ${checking.get_balance():,.2f}')
    
    # Display the balance with interest.
    checking.apply_interest()
    print(f'Your account balance with interest is ${checking.get_balance():,.2f}')

    print(border())
    
    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? \n Enter amount in dollars : \n'))
    print(f'${cash} will be withdrawn from your account.')
    checking.withdraw(cash)

    print(border())

    # Display the balance without interest.
    print(f'Your account balance is ${checking.get_balance():,.2f}')
    
    # Display the balance with interest.
    checking.apply_interest()
    print(f'Your account balance with interest is ${checking.get_balance():,.2f}')

    print(border())

    # Thank the user for using the program.
    print('Thank you for using ACME bank.')

# Call the main function.
if __name__ == '__main__':
    main()
