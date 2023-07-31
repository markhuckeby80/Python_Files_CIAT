


# Design a program using loop to print the following pattern for 5 lines (use nested loop)

lines = 5

for i in range(1, lines + 1):
    
    print(" " * (lines - i), end = "")

    print("*  " * i)
 
