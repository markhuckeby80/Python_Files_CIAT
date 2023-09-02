
# import the randint and datetime modules
import random 
from datetime import datetime

# set the seed for the random number generator
random.seed(datetime.now().timestamp())

# Create the quizzer function that will be called from the main.py file.
def quizzer():

    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)            
    num2 = random.randint(1, 10)

    # Print the their multiplication problem on the screen.
    print(f'Here is your multiplication problem : {num1} X {num2}')

    # Ask the user to enter the answer to the problem.
    ans = int(input('Enter your answer : '))

    # Calculate the product of the two numbers.
    prod = num1 * num2
    
    # Compare the user's answer to the product of the two numbers.
    if ans == prod:
        return True
    else:
        return False
    