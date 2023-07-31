import sys


# Create a program that will provide the user their fortune based on their favorite color.

def wheel_of_fortune():

    # Ask the user their name.
    user_name = input("Please enter your name : ")

    # Display a welcome message.
    print(f"Welcome {user_name}! Let's see what your fortune is today.")

    # Display their color options.
    print("These are your colors of fortune : red, blue, green, yellow, or purple.")

    # Ask the user to enter their favorite color.
    user_color = input("Please enter your favorite color : ")
    
    if user_color == "red":
        print(f"{user_name}, you will have an excellent day! You should play the lottery.")
    elif user_color == "blue":
        print(f"{user_name}, you will have a sad day! Don't worry, tomorrow will be better.")
    elif user_color == "green":
        print(f"{user_name}, you will have a day full of plants! Please water them, and sing to them.")
    elif user_color == "yellow":
        print(f"{user_name}, You will have a bad day! You should go back to bed.")
    elif user_color == "purple":
        print(f"{user_name}, You will have a terrible day! DO NOT PASS GO, DO NOT COLLECT $200.")
    else:
        print(f"Sorry, {user_name}, that color is not listed.")

    # Ask the user if they want to end or continue the program.
    user_choice = input(f"{user_name}, would you like to end the program? (y/n) : ")

    # If the user chooses to end the program, display a goodbye message.
    if user_choice == "y":
        print(f"Goodbye, {user_name}!")
        sys.exit()

    # If the user chooses to continue the program, ask the user what time of day it is.
    elif user_choice == "n":
        user_time = input(f"{user_name}, what time of day is it? (morning, afternoon, or evening) : ")
        
        # If the user answers morning, display a good morning message.
        if user_time == "morning":
            print(f"Good morning, {user_name}!")
            sys.exit()

        # If the user answers afternoon, display a good afternoon message.
        elif user_time == "afternoon":
            print(f"Good afternoon, {user_name}!")
            sys.exit()

        # If the user answers evening, display a good evening message.
        elif user_time == "evening":
            print(f"Good evening, {user_name}!")
            sys.exit()

        # If the user does not enter a valid time of day, display an error message.
        else:
            print(f"Sorry, {user_name}, that is not a valid time of day.")


# Call the function.
wheel_of_fortune()


