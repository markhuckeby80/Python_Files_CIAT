import sys

# Create a program that user inputs a number, loop iterates 10 times and keep a running total
def sum_ten_num():
    # Initialize variables
    total = 0
    count = 0

    # Loop 10 times
    while count < 10:
        try:
            num = int(input('Enter a number: '))
            count += 1
        except ValueError:
            print('Please enter a valid number.')
            continue
            
        # Calculate the running total
        total += num

    # Display the running total
    print(f'The running total is {total}.')

    # Ask the user if they want to perform the operation again or exit
    def perform_operation_again():
        
        while True:
            try:
                again = input('Would you like to perform the operation again? (y/n): ')
                if again == 'y':
                    sum_ten_num()
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
sum_ten_num()