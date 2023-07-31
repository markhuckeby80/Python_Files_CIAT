


# Create an infinite loop with a counter that will never reach the condition
# This will run forever
counter = 1
while counter < 10:
    print("In the loop")
    counter = counter 
    break  