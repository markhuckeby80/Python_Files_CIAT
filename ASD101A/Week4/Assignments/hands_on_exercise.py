import sys

# Create a program that shows the amount of calories burned on a treadmill after 10, 15, 20, 25, and 30 minutes.

# def function
def calories_burned():

    # Create a loop to calculate calories burned
    for minutes in range(10, 31, 5):

        # calculate calories burned
        calories = 4.2 * minutes

        # print results
        print(f"AMAZING! You have burned ", calories, "calories in", minutes, "minutes.")
        
    # print goodbye message
    print("Keep up the good work!\n" "Goodbye!")
    
# call function
calories_burned()

# system exit
sys.exit(0)
