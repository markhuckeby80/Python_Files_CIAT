# Day of the Week

# Create a variable list of the days of the week and their corresponding number
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


# Create a simple loop with a single alternative outcome
while True:

    user_input = int(input("Enter a number in the range of 1 through 7: "))
    if 1 <= user_input <= 7:
        day_of_week = days[user_input]
        print("Corresponding day of the week:", day_of_week)
    else:
        print("Error: Please enter a number between 1 and 7.")