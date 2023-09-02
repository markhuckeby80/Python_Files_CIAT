
# Imports of all the necessary functions and modules.

from art import tprint
from bmi_border_function import bmi_border as border
from bmi_calc_function import bmi_calculator
from bmi_result_function import bmi_result

# Main class that will call all the other functions.

class BMI_Main:

    def __init__(self):
        self.initial_screen()
        self.calculate_and_display_bmi()    

    # define a function for the initial screen
    def initial_screen(self):
            
        # print the art
        tprint("BMI=", font = "block", chr_ignore = True)    
                
        # Import the border function
        print(border())            
        
        # print a welcome message to the user
        greeting = "Welcome to the BMI Calculator!"
        centered_greeting = greeting.center(100)
        print(centered_greeting)
    
        # import the border function
        print(border())
    
        # print("Description of the program")
        description = "A simple BMI calculator."
        centered_description = description.center(100)
        print(centered_description)
    
        # import the border function
        print(border())
    
        # print("Instructions")
        print("Instructions :\n"
            "\tFirst, you will enter your weight in kilograms.\n"
            "\tSecond, you will enter your height in meters.\n"
            "\tLastly, the BMI calculator will show your BMI.")  
                
        # import the border function
        print(border())

    def calculate_and_display_bmi(self):    # Calling the function to calculate the BMI.
        calculated_bmi = bmi_calculator()
        print(border())
        bmi_result(calculated_bmi)
        print(border())
    
# Calling the class to run the program.
if __name__ == "__main__":
    BMI_Main()
  