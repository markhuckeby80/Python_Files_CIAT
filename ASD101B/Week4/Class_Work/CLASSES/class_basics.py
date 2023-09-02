from random import randint

# First step is to create a class with all its corresponding attributes (variables) and methods (functions)
class Coin:

    def __init__(self):             # This is the constructor - initializing method
        self.sideup = 'Heads'

    def toss(self):
        if randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup
    
myObj = Coin()                      # Instantiate the class

flip = myObj.get_sideup()           # Use dot notation to link the object to the method (function) to run
print(flip)
for i in range(10):
    myObj.toss()
    flip = myObj.get_sideup()
    print(flip)

print('--------------------------------')
print(myObj.sideup)                 # This is the same as the above

