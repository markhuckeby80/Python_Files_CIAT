


# Create a greeting with gender function with one string parameter for name
# and one for gender.  The function should print a greeting message.

def greeting_with_gender(name, gender):
   
    if gender.lower() == "male":
        print(f'Hello Mr. {name}! Welcome to Python Programming!')
    elif gender.lower() == "female":
        print(f'Hello Mrs. {name}! Welcome to Python Programming!')
    else:
        print(f'Hello {name}! Welcome to Python Programming!')

# Get the user name
name = input("What is your name? : \n")
gender = input("What is your preferred gender identity? : \n")


# Call the function with the user input as parameters.
greeting_with_gender(name, gender)
