import pretty_errors


class Calculator:

    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    def __init__(self):
        self.x = int(input('Enter a number : \n'))
        self.y = int(input('Enter another number : \n'))
        # self.x = x
        # self.y = y

    def changeValues(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
    
    def multiplication(self):
        return self.x*self.y
    
    def division(self):
        try:
            return self.x/self.y
        except:
            print('Division by zero is not allowed')

    def subtraction(self):
        return self.x - self.y
    
    def printValues(self):
        print(f'Your two values were {self.x} and {self.y}.')


mathObj = Calculator()
mathObj = Calculator(2, 3)
add = mathObj.addition()
sub = mathObj.subtraction()
mult = mathObj.multiplication()
div = mathObj.division()
print(f'Addition: {add}')
print(f'Subtraction: {sub}')
print(f'Multiplication: {mult}')
print(f'Division: {div}')
mathObj.printValues()
mathObj.changeValues(5, 10)
div = mathObj.division()
print(f'Division: {div}')
mathObj.printValues()
print(mathObj.x)
print(mathObj.y)
