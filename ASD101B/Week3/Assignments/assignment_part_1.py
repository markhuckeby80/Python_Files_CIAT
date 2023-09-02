


# Write a function that accepts a string as an argument and displays the string backwards.
def reverseString(string):
    print(string[::-1])

# I wanted to allow the user to input the string to be reversed.
userInput = input('Enter a string to be reversed : \n')


if __name__ == '__main__':
    reverseString(userInput)
