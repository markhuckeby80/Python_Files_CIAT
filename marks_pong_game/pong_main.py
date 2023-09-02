from art import tprint

from marks_pong_game.pong_game import main_pong_game as mpg

# PONG by Mark

class Main:
   
    # define a function for the initial screen    
    def initial_screen(self):
                
        # print the art
        tprint("PONG!", font = "block", chr_ignore = True)

        # Border variables
        border_length = 100
        border_char = "*"
    
        # print border
        print(border_char * border_length)
        
        # print a welcome message to the user
        greeting = "Welcome to Mark's PONG!"
        centered_greeting = greeting.center(100)
        print(centered_greeting)
    
        # print border
        print(border_char * border_length)
    
        # print("Description of the game")
        description = "A simple game of PONG made with Python and Turtle"
        centered_description = description.center(100)
        print(centered_description)
    
        # print border
        print(border_char * border_length)
    
        # print("Instructions")
        print("Instructions :\n"
              "\tPlayer A controls the left paddle with the 'W' and 'S' keys\n"
              "\tPlayer B controls the right paddle with the 'Up' and 'Down' keys\n"
              "\tThe first player to reach 3 points wins")
    
        # print border
        print(border_char * border_length)


    # define a function for starting the game   
    def start_game(self):

        while True:
    
            # print("Start the game")
            print("Start the game? (y/n) : ")
            start = input().strip().lower()

            if start == "y":
                print("Starting the game...")
                print("3")
                print("2")
                print("1")
                print("Start!")
                print("")
                mpg()



            elif start == "n":
                print("Ending the game...")
                print("")
                print("Thank you for playing!")
                print("Created by Mark")
                print("End of program")
                exit()

            else:
                print("Invalid input")
                print("Please enter 'y' or 'n' : ")
            

    # Ask the user if they want to play again
    def ask_play_again(self):
    
        while True:

            print("Do you want to play again? (y/n)")
            play_again = input().strip().lower()

            if play_again == "y":
                print("Starting the game...")
                print("3")
                print("2")
                print("1")
                print("Start!")
                print("")
                mpg()

            elif play_again == "n":
                print("Ending the game...")
                print("")
                print("Thank you for playing!")
                print("Created by Mark")
                print("End of program")
                exit()
            
            else:
                print("Invalid input")
                print("Please enter 'y' or 'n' : ")
            

    # call the functions
    initial_screen(self=None)
    start_game(self=None)
    ask_play_again(self=None)


if __name__ == '__main__':
    Main()
