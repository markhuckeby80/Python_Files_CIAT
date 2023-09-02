


# After the user is finished with their first round of the quiz, 
# they will be asked if they want to play again.

# If they answer yes, the quizzer function will be called again.
def play_again():
    answer = input("Would you like to play again? (y/n) : ")
    if answer == "y":
        return True
    else:
        return False
