
# Imports of all the necessary functions and modules.

from art import tprint
from math_border_function import math_border as border
from quizzer_function import quizzer as quiz
from answer_function import answer
from play_again_function import play_again as play

# Main class that will call all the other functions.

class MATH_Main:

    def __init__(self):
        self.initial_screen()
                  

    # define a function for the initial screen
    def initial_screen(self):
            
        # print the art
        tprint("QUIZ!", font = "block", chr_ignore = True)    
                
        # Import the border function
        print(border())            
        
        # print a welcome message to the user
        greeting = "Welcome to the MATH Multiplication Game!"
        centered_greeting = greeting.center(100)
        print(centered_greeting)
    
        # import the border function
        print(border())
    
        # print("Description of the program")
        description = "Sharpen your multiplication skills."
        centered_description = description.center(100)
        print(centered_description)
    
        # import the border function
        print(border())
    
        # print("Instructions")
        print("Instructions :\n\n"
              
            "\tYou will see a multiplication problem display on your screen.\n"
            "\tYou will be asked to enter the value of that problem.\n"
            "\tIf you answer correctly, you will be congratulated.\n")  
                
        # import the border function
        print(border())

    # Call the quizzer function
    def quiz(self):
        return quiz()

    # Call the answer function
    def answer(self, result):
        answer(result)

    # Call the play again function
    def play(self):
        return play()

    
# Calling the class to run the program.
if __name__ == "__main__":
   math_game = MATH_Main()
   while True:
       result = math_game.quiz()
       math_game.answer(result)
       if math_game.play() == False:
           print("Thanks for playing!")
           break
