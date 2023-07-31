import sys

# Create a while loop where the user enters two numbers and displays the sum, ask to perform again or exit
def sum_two_num():  

    # Create a while loop to ask the user to enter two numbers
    while True:
        try:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            break
        except ValueError:
            print('Please enter a valid number.')
            continue

    # Calculate the sum of the two numbers
    sum = num1 + num2

    # Display the sum of the two numbers
    print(f'The sum of {num1} and {num2} is {sum}.')

    # Ask the user if they want to perform the operation again or exit
    def perform_operation_again():

        while True:
            try:
                again = input('Would you like to perform the operation again? (y/n): ')
                if again == 'y':
                    sum_two_num()
                elif again == 'n':
                    sys.exit()
                else:
                    print('Please enter y or n.')
                continue
            except ValueError:
                print('Please enter y or n.')
            continue

    # Call the function
    perform_operation_again()     

# Call the function
sum_two_num()