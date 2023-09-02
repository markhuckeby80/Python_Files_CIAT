


# Create a answer function that will accept the result from 
# the quizzer function and return the appropriate message.

def answer(result):
    if result == True:
        print("Good Job! That is correct. You are a math genius.")
    else:
        print("Better luck next time.")