# Write a program that asks the user to enter a series of single-digit numbers with \
# nothing separating them. The program should display the sum of all the single digit \
# numbers in the string. For example, if the user enters 2514, the method should return \
# 12, which is the sum of 2, 5, 1, and 4.

# I will create a function to do perform this task
def sumOfSingleDigitNumbers(userInput):

    # Create a while loop to verify the user input with an exception handler
    while True:

        try:

            # Get the user input
            userInput = input("Enter a series of single-digit numbers with nothing separating them : \n")

            # Check if the input consists of only single-digit numbers
            if not userInput.isdigit():
                raise ValueError("Invalid input.")


            # Initialize the sum
            sum = 0

            # Loop through the user input
            for i in userInput:
                # Add the current number to the sum
                sum += int(i)

            # Display the sum
            print("The sum of all the single digit numbers in the string is", sum)

            # Break out of the loop if the input is valid
            break

        except ValueError as error:
            print(error)


if __name__ == '__main__':
    sumOfSingleDigitNumbers(userInput = "")
