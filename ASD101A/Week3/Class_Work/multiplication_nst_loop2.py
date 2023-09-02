# multiplication nested loop

ask_until_get_correct_data = True
mul_range = 0

while ask_until_get_correct_data:

    user_input = input("Enter a number: \n")

    # user input should not be empty
    # user input can be converted to integer

    if len(user_input) >0 and user_input.isdigit() and int(user_input) < 100 :
        mul_range = int(user_input)
        ask_until_get_correct_data = False

    else :
        print("Enter a valid number between 1 to 100 ")
        

for outer_loop_number in range (1, mul_range+1):

    for inner_loop_number in range (1, mul_range+1):

        print(f"{outer_loop_number} * {inner_loop_number} = {outer_loop_number * inner_loop_number}")

    print()