# create a program that allows the user to play "guess the number game"

# import the art module
from art import *

# import random module
import random

# import sys module
import sys


def complete_game():     
          
    # Border variables
    border_length = 100 
    border_char = "*"

    # define a function for the initial screen
    def initial_screen():
        
        # print the art
        tprint("GAME!", font = "block", chr_ignore = True)

    
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
    
    # define a function to get the user's guess
    def get_user_guess():
        
        # create a while loop to allow the user to guess the number
        while True:

            # create a try/except block to handle the user's input
            try: 
                user_guess = int(input("Enter a number between 1 and 100 : "))
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 100! ")
                continue  

            if user_guess < 1 or user_guess > 100:
                print("Please enter a valid number between 1 and 100! ")
                continue        
                                    
            # print border
            print(border_char * border_length)

            # print the user's guess
            print(f'The number you inputted is : {user_guess}')

            # print border
            print(border_char * border_length)
            
            return user_guess
        
    # define a function to create a random number
    def created_generated_number():

        # define a variable to store the random number    
        generated_number = random.randint(1, 100)

        return generated_number
                    
    # define a function to check if the user's guess is correct
    def check_guess(user_guess, generated_number, number_of_guesses):
        
        # create an if statement to check if the user's guess accurately matches the random number
        if user_guess == generated_number:
            # print a message to the user
            print("You are a genius!\n"
                "You guessed correctly!\n")
            print(f'The random number was : {generated_number}')
            # print border
            print(border_char * border_length)
            print(f'It took you : {number_of_guesses} guesses to get it right!')
            print("Thank you for playing!\n" 
                "Goodbye!")
            sys.exit()
        
        # create an elif statement to check if the user's guess is higher than the random number
        elif user_guess > generated_number:

            # print a message to the user
            print("Too high")

            # print border
            print(border_char * border_length)
            print(f'You are at {number_of_guesses} number of guesses.')
            print("Try again.")

            # print border                
            print(border_char * border_length)               
                                
        # create an elif statement to check if the user's guess is lower than the random number    
        elif user_guess < generated_number:

            # print a message to the user
            print("Too low")
        
            # print border
            print(border_char * border_length)
            print(f'You are at {number_of_guesses} number of guesses.')
            print("Try again.")

            # print border
            print(border_char * border_length)

        return False
    
    # define a function to check if the user has reached the max number of guesses
    def check_max_guesses(number_of_guesses, MAX_GUESSES):
            
        # create an if statement to check if the user has reached the maximum number of guesses
            if number_of_guesses == MAX_GUESSES:
                # print border
                print(border_char * border_length)
                print("You have reached the maximum number of guesses = 10")
                print(f'The random number was : {generated_number}\n'
                    f'You are at {number_of_guesses} number of guesses.')         
        
    # define a function to ask the user if they want to play again
    def ask_play_again():

        # Ask if the player wants to play again
        # print border
        print(border_char * border_length)
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!\n"
                "Goodbye!") 
            sys.exit()
            
        else:
            # print border
            print(border_char * border_length)

            return True
    
    # Game loop to handle multiple rounds of the game
    while True:
        initial_screen()
        generated_number = created_generated_number()
        MAX_GUESSES = 10
        number_of_guesses = 0

        while number_of_guesses < MAX_GUESSES:
            user_guess = get_user_guess()
            number_of_guesses += 1

            if check_guess(user_guess, generated_number, number_of_guesses):
                break

        check_max_guesses(number_of_guesses, MAX_GUESSES)
        if not ask_play_again():
            break
            
    

# call the function
complete_game()