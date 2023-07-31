

# What will the following program display?

def main():
    x = 1
    y = 3.4
    print(x, y)        # prints 1 3.4
    change_us(x, y)    # calls change_us with x and y as arguments
    print(x, y)        # prints 1 3.4

def change_us(a, b):   # a and b are parameters
    a = 0
    b = 0
    print(a, b)        # prints 0 0 because a and b are 0
    
main()                 # calls main
# It will print 1 3.4
# It will print 0 0
# It will print 1 3.4
# The program will display 1 3.4 0 0 1 3.4
# It will not change the values of x and y because the change_us function is local.