


# import random

from random import randint




def quizzer():

    cont = True

    while cont:

        num1 = randint(1, 11)
        num2 = randint(1, 11)


        prod = num1 * num2
        ans = int(input(f'What is the result of {num1} x {num2}? '))

        if ans == prod:
            print("Good job! That's Correct!")
        else:
            print("Better luck next time! That's Incorrect.")

        temp = input("Would you like to continue, type 'y' for yes or 'n' for no: ")

        if temp == 'y':
            pass
        else:
            cont = False

quizzer()