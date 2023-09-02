


# Create a function that generates a random number between 1 and 100 and ask the user
# How many attempts they would like to have to guess the number. 
# If the user guesses the number within the number of attempts they win, otherwise they lose.


import random

def guessing_game():
    maxNum = 100
    randNum = random.randint(1, maxNum+1)

    print("Welcome to the guessing game! \n" +
          "You will be asked to input a number from 1 to 100.")

    while True:
        guesses = (input("How many guesses would you like to have? \n"))
        if guesses.isdigit():
            guesses = int(guesses)
            break
        else:
            print("You did not enter a number, please try again.")
            return

    counter = 0

    while counter < guesses:
        userguess = int(input("Guess a number between 1 and 100: "))

        if userguess == randNum:
            print("Congrats! You won. ")
            break
        elif userguess > randNum:
            print("Your guess is too high.")
        elif userguess < randNum:
            print("Your guess is too low.")
        else:
            print("You did not enter a number, please try again.")

        counter += 1
        if counter == guesses:
            print("Sorry, you ran out of attempts.")


if __name__ == "__main__":
    guessing_game()