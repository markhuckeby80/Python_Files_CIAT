
# Import the current year from the datetime module
from datetime import datetime

# Create a Happy Birthday function with one integer parameter for year and 
# one string parameter for name.  The function should print a birthday message.

def HappyBirthday(year, name):
    current_year = datetime.now().year
    age = current_year - year
        
    while True:
        try:
            year = int(input("What year were you born? "))
            if year < 1920:
                print("Error, need at least 1920 year value.")
                print("Please try again.")
            elif year > current_year:
                print("Error, year value cannot be in the future.")
                print("Please try again.")
            else:
                break
        except ValueError:
            print("Error, please enter a valid year.")
            print("Please try again.")
    
    suffix = "th"
    if age % 10 == 1 and age % 100 != 11:
        suffix = "st"
    elif age % 10 == 2 and age % 100 != 12:
        suffix = "nd"
    elif age % 10 == 3 and age % 100 != 13:
        suffix = "rd"
    print(f'Happy {age}{suffix} Birthday {name}!')
      
# Get the user name
name = input("What is your name? ")


# Call the function with the user input as parameters.
HappyBirthday(0, name)
