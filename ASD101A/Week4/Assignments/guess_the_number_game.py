# create a program that allows the user to play "guess the number game"

# import the art module
from art import *

# import random module
import random

# import sys module
import sys


# define main function
def guessing_game ():

    # create a while loop to allow the user to play the game multiple times
    while True:

        # print the art
        tprint("GAME!", font = "block", chr_ignore = True)

        # Border
        border_length = 100
        border_char = "*"

        # Print border
        print(border_char * border_length)
  
        # print a welcome message to the user
        greeting = "Welcome to the Guess the Number Game!"
        centered_greeting = greeting.center(100)
        print(centered_greeting)

        # instructions
        print("Instructions:\n" 
                "1. The computer will randomly generate a number between 1 and 100.\n"
                "2. You will have 10 guesses to guess the number.\n"
                "3. If you guess the number correctly, you win!\n"
                "4. If you do not guess the number correctly, you lose!\n"
                "5. If you do not guess the number correctly after 10 guesses, you lose!\n"
                "6. Good luck!\n")
        
        # Print border
        print(border_char * border_length)

        # define a variable to store the random number
        random_number = random.randint(1, 100)

        # define a variable to store the max guesses
        MAX_GUESSES = 10

        while True:
            
            # define a variable to store the user's guess
            user_guess = 0

            # define a variable to store the number of guesses
            number_of_guesses = 0

            # create a while loop to allow the user to guess the number
            while number_of_guesses < MAX_GUESSES:  

                
                # create a try/except block to handle the user's input
                try: 
                    user_guess = int(input("Enter a number between 1 and 100 : "))
                except ValueError:
                    print("Invalid input. Please enter a valid number between 1 and 100! ")
                    continue  

                if user_guess < 1 or user_guess > 100:
                    print("Plesae enter a valid number between 1 and 100! ")
                    continue        
                                        
                # print border
                print(border_char * border_length)

                # print the user's guess
                print(f'The number you inputted is : {user_guess}')

                # print border
                print(border_char * border_length)
                
                # increment the number of guesses
                number_of_guesses += 1
                
                # create an if statement to check if the user's guess accurately matches the random number
                if user_guess == random_number:
                    # print a message to the user
                    print("You are a genius!\n"
                        "You guessed correctly!\n")
                    print(f'The random number was : {random_number}')
                    # print border
                    print(border_char * border_length)
                    print(f'It took you : {number_of_guesses} guesses to get it right!')
                    print("Thank you for playing!\n" 
                        "Goodbye!")
                    sys.exit()
            
                # create an elif statement to check if the user's guess is higher than the random number
                elif user_guess > random_number:

                    # print a message to the user
                    print("Too high")

                    # print border
                    print(border_char * border_length)
                    print(f'You are at {number_of_guesses} number of guesses.')
                    print("Try again.")

                    # print border                
                    print(border_char * border_length)               
                                        
                # create an elif statement to check if the user's guess is lower than the random number    
                elif user_guess < random_number:

                    # print a message to the user
                    print("Too low")
                
                    # print border
                    print(border_char * border_length)
                    print(f'You are at {number_of_guesses} number of guesses.')
                    print("Try again.")

                    # print border
                    print(border_char * border_length)  

            # create an if statement to check if the user has reached the maximum number of guesses
            if number_of_guesses == MAX_GUESSES:
                # print border
                print(border_char * border_length)
                print("You have reached the maximum number of guesses = 10")
                print(f'The random number was : {random_number}\n'
                    f'You are at {number_of_guesses} number of guesses.')
                break
            break
        # Ask if the player wants to play again
        # print border
        print(border_char * border_length)
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!\n"
                  "Goodbye!") 
            sys.exit()   
            break
        else:
            # print border
            print(border_char * border_length)
            continue     

# Start the game
guessing_game()